"""Patch qwen3_5 forward: skip dummy visual call when no image (pure-text training).

根因:recipe_custom/models/transformers/qwen3_5.py:338-344 在无图时仍构造 dummy
pixel_values 调 self.visual() (加 0.0* 保持梯度)。纯文本训练下,visual 塔
(多模态视觉塔)的并行度校验 product(parallel_sizes)==world_size 在 4 卡
TP=2+SP=2 下失败 → ValueError。

本 patch:无图时直接跳过 self.visual(),不保持那个 0.0* 的梯度连接(纯文本
训练不需要视觉梯度)。有图时行为不变(走原 visual 分支)。

挂载:monkey-patch Qwen3_5Model.forward / Qwen3_5MoeModel.forward,覆盖
recipe_custom 挂的 patch_qwen3_5_model_forward_for_linear_attention。走
VERL_USE_EXTERNAL_MODULES 注入,不改 verl/recipe_custom 源码。
"""

from __future__ import annotations

import logging

_PATCHED = False
logger = logging.getLogger(__name__)


def install() -> None:
    """Monkey-patch qwen3_5 model forward to skip dummy visual call. Idempotent."""
    global _PATCHED
    if _PATCHED:
        return

    try:
        from recipe_custom.models.transformers import qwen3_5 as _qwen
        from transformers.models.qwen3_5.modeling_qwen3_5 import (
            Qwen3_5Model,
        )
    except Exception as exc:  # noqa: BLE001 -- off-cluster / no recipe_custom
        print(f"[agent-rl] qwen3_5 visual-skip patch skipped ({exc})", flush=True)
        return

    try:
        from transformers.models.qwen3_5_moe.modeling_qwen3_5_moe import Qwen3_5MoeModel
    except Exception:  # noqa: BLE001 -- moe variant absent
        Qwen3_5MoeModel = None  # type: ignore[assignment]

    _orig_forward = _qwen.patch_qwen3_5_model_forward_for_linear_attention

    def _forward_no_dummy_visual(
        self,
        input_ids=None,
        attention_mask=None,
        position_ids=None,
        past_key_values=None,
        inputs_embeds=None,
        pixel_values=None,
        pixel_values_videos=None,
        image_grid_thw=None,
        video_grid_thw=None,
        mm_token_type_ids=None,
        **kwargs,
    ):
        """Pure-text forward: skip the dummy self.visual() call when no image.

        有图(pixel_values/pixel_values_videos 非 None)→ 走原 forward(含 visual)。
        无图 → 跳过 dummy visual,直接走 embedding + position_ids。
        """
        if pixel_values is None and pixel_values_videos is None:
            # 无图: 跳过 visual, 直接算 embedding + position
            if inputs_embeds is None:
                inputs_embeds = self.get_input_embeddings()(input_ids)

            # position_ids 由原 forward 的后续逻辑算(compute_3d_position_ids 等),
            # 但原 forward 在无图时依赖 image_grid_thw (dummy)。这里给个默认
            # 让后续 position 计算不崩: image_grid_thw=None 时走纯文本 position。
            if position_ids is None:
                # 纯文本 position_ids: 用 attention_mask cumsum
                if attention_mask is None:
                    position_ids = torch.arange(
                        inputs_embeds.shape[1],
                        device=inputs_embeds.device,
                    ).unsqueeze(0)
                else:
                    position_ids = attention_mask.long().cumsum(-1) - 1
                    position_ids.masked_fill_(attention_mask == 0, 1)

            # 调原 forward 的剩余部分(跳过 338-344 的 dummy visual):
            # 原函数在 346+ 行算 position_ids + 走 model layers。我们直接调
            # 原函数但把 pixel_values 设成一个 sentinel 让它跳过 visual 分支——
            # 不行,原函数无图时强制走 dummy。故这里手动走 model layers。
            # 简化:直接调原 forward,但 patch 掉 self.visual 让它返回零张量。
            return _orig_forward(
                self,
                input_ids=input_ids,
                attention_mask=attention_mask,
                position_ids=position_ids,
                past_key_values=past_key_values,
                inputs_embeds=inputs_embeds,
                pixel_values=pixel_values,
                pixel_values_videos=pixel_values_videos,
                image_grid_thw=image_grid_thw,
                video_grid_thw=video_grid_thw,
                mm_token_type_ids=mm_token_type_ids,
                **kwargs,
            )

        # 有图: 走原 forward (含 visual)
        return _orig_forward(
            self,
            input_ids=input_ids,
            attention_mask=attention_mask,
            position_ids=position_ids,
            past_key_values=past_key_values,
            inputs_embeds=inputs_embeds,
            pixel_values=pixel_values,
            pixel_values_videos=pixel_values_videos,
            image_grid_thw=image_grid_thw,
            video_grid_thw=video_grid_thw,
            mm_token_type_ids=mm_token_type_ids,
            **kwargs,
        )

    # 更稳的解法: patch self.visual 让 dummy 调用返回零, 而非跳过整个 forward
    # (原 forward 后续 position_ids 计算依赖 image_grid_thw, 跳过会崩)
    def _forward_with_visual_stub(
        self,
        input_ids=None,
        attention_mask=None,
        position_ids=None,
        past_key_values=None,
        inputs_embeds=None,
        pixel_values=None,
        pixel_values_videos=None,
        image_grid_thw=None,
        video_grid_thw=None,
        mm_token_type_ids=None,
        **kwargs,
    ):
        """无图时把 self.visual 替换成返回零的 stub, 避开并行度校验."""
        if pixel_values is None and pixel_values_videos is None:
            _orig_visual = getattr(self, "visual", None)

            class _VisualStub:
                """Stub visual: returns object with .pooler_output = zero tensor."""
                def __call__(self, pv, grid_thw=None, **kw):
                    class _Out:
                        pass
                    out = _Out()
                    # pooler_output shape 不重要, 后续 0.0 * .mean() 会消掉
                    out.pooler_output = torch.zeros(
                        (1, 1), dtype=inputs_embeds.dtype, device=inputs_embeds.device
                    ) if inputs_embeds is not None else torch.zeros((1, 1))
                    return out
            try:
                self.visual = _VisualStub()  # type: ignore[assignment]
            except Exception:  # noqa: BLE001 -- frozen dataclass etc
                pass
            try:
                return _orig_forward(
                    self,
                    input_ids=input_ids,
                    attention_mask=attention_mask,
                    position_ids=position_ids,
                    past_key_values=past_key_values,
                    inputs_embeds=inputs_embeds,
                    pixel_values=pixel_values,
                    pixel_values_videos=pixel_values_videos,
                    image_grid_thw=image_grid_thw,
                    video_grid_thw=video_grid_thw,
                    mm_token_type_ids=mm_token_type_ids,
                    **kwargs,
                )
            finally:
                if _orig_visual is not None:
                    try:
                        self.visual = _orig_visual
                    except Exception:  # noqa: BLE001
                        pass
        # 有图: 走原 forward
        return _orig_forward(
            self,
            input_ids=input_ids,
            attention_mask=attention_mask,
            position_ids=position_ids,
            past_key_values=past_key_values,
            inputs_embeds=inputs_embeds,
            pixel_values=pixel_values,
            pixel_values_videos=pixel_values_videos,
            image_grid_thw=image_grid_thw,
            video_grid_thw=video_grid_thw,
            mm_token_type_ids=mm_token_type_ids,
            **kwargs,
        )

    # 用 visual stub 方案(更稳, 不破坏原 forward 的 position 计算逻辑)
    Qwen3_5Model.forward = _forward_with_visual_stub
    if Qwen3_5MoeModel is not None:
        Qwen3_5MoeModel.forward = _forward_with_visual_stub
    _PATCHED = True
    print(
        "[agent-rl] qwen3_5 visual-skip patch installed "
        "(dummy self.visual() stubbed to zero when no image, avoids parallel-size assert)",
        flush=True,
    )


# import torch (needed for the stub's zeros)
try:
    import torch  # noqa: F401
except ImportError:
    pass

install()
