"""Fix verl ppo_loss 里 response 对齐字段长度错位崩溃 (E29, 续 E12/E13).

根因（2026-08-29 r0_clear 16卡训练，step4；4卡诊断坐实）:
    ``ppo_loss``（verl/workers/utils/losses.py:59/91）里「response 变长 → dense」有
    **多个长度源**，tq 往返 / nested 重建把 ``responses`` 读成退化长度（4卡诊断抓到
    ``responses.max=1`` vs ``response_mask=5745``、``is_replay.sum=0`` 的 rollout 行），
    且 ``response_mask``(13571) 与 ``old_log_probs``(15769) 在同一 mini-batch 里最大长
    也不一致。结果：

      - ``log_prob``    = ``no_padding_2_padding(model_output["log_probs"], data)``
                         按 ``responses`` 最大长 pad（→ 退化，如 1 或 13571）。
      - ``old_log_prob``/``response_mask``/``advantages`` = ``data.select(...)
                         .to_padded_tensor()`` 各自 pad 到**自己的**最大长（15769/13571/…）。

    于是 ``log_prob - old_log_prob`` 崩（上一版 patch 修了这个），修好后下一层
    ``masked_mean(negative_approx_kl, response_mask)`` 又崩：``negative_approx_kl``
    （=log_prob-old_log_prob，15769）vs ``response_mask``（13571）。**根因是
    to_padded_tensor 让 response_mask/old_log_probs/advantages 各自 pad 到不同宽**。

修法（不改 verl 源码，走 VERL_USE_EXTERNAL_MODULES 注入）:
    1. 包装 ``no_padding_2_padding``：把 log_prob/entropy 补到所有响应对齐字段的最大长。
    2. 重写 ``ppo_loss``：``to_padded_tensor`` 之后，把 response_mask/old_log_probs/
       advantages/ref_log_prob/rollout_is_weights 统一补到同一个最大宽。

    补出的列对应 response_mask=0 区域（回放行 B8 / 变长右 pad），被 masked_mean 屏蔽，
    不进 loss，仅消除形状错位、不改语义。

    必须同时 patch：
      · ``padding.no_padding_2_padding`` —— cl_loss._to_dense_response_logprobs 每次
        ``from ... import`` 在调用时重读（拿到 patch 后版本）。
      · ``losses.no_padding_2_padding`` / ``losses.ppo_loss`` —— losses.py 模块级 import
        + cl_loss._resolve_ppo_loss 的 ``from ... import ppo_loss``，都需显式覆盖。
"""

from __future__ import annotations

import torch
import torch.nn.functional as F
from verl.trainer.ppo.core_algos import agg_loss, get_policy_loss_fn, kl_penalty
from verl.utils.metric import AggregationType, Metric
from verl.workers.utils import padding as _padding

# 响应对齐字段：to_padded_tensor() 会把这些 nested 字段各自 pad 到自身最大长。
# 与 ppo_loss 里 fields 列表逐一对齐（response_mask/old_log_probs/advantages +
# 条件出现的 rollout_is_weights/ref_log_prob）。
_ALIGN_KEYS = ("response_mask", "old_log_probs", "advantages", "rollout_is_weights", "ref_log_prob")

_ORIG_NO_PADDING_2_PADDING = _padding.no_padding_2_padding

# 首次发生形状对齐时打一行诊断（确认 patch 真正介入；只打一次，避免每 micro-batch 刷屏）。
_warned = False


def _response_aligned_max_len(data, key: str) -> int:
    """取 data[key] 的最大响应长度（nested 取 offsets diff max，dense 取 shape[1]）。"""
    try:
        if key not in data:
            return -1
        v = data[key]
    except Exception:  # noqa: BLE001 -- DataProto / 缺字段兜底
        return -1
    try:
        if getattr(v, "is_nested", False):
            return int(v.offsets().diff().max().item())
        if hasattr(v, "dim") and v.dim() == 2:
            return int(v.shape[1])
    except Exception:  # noqa: BLE001
        return -1
    return -1


def _reliable_response_lens(data):
    """取可靠的 response 逐行长度（nested offsets diff）。

    ``responses`` 在 worker 读回会被 tq 截短（4卡 degenerate 到 1、16卡回放行被截到 13571），
    但 ``old_log_probs``（= response_mask 对齐 + 回放行 R 宽）读回正确。故按可靠性优先：
    old_log_probs > response_mask > responses。都不可用返回 None。
    """
    for key in ("old_log_probs", "response_mask", "responses"):
        try:
            if key not in data:
                continue
            v = data[key]
            if getattr(v, "is_nested", False):
                return v.offsets().diff()
        except Exception:  # noqa: BLE001 -- 兜底
            continue
    return None


def _patched_no_padding_2_padding(tensor: torch.Tensor, data) -> torch.Tensor:
    """重写 no_padding_2_padding：response 长度改从 old_log_probs 取（responses 会被 tq 截短）。"""
    global _warned
    values = tensor.values() if tensor.is_nested else tensor
    prompt_ids = data["prompts"]

    if prompt_ids.is_nested:
        prompt_lens = prompt_ids.offsets().diff()
    else:
        attention_mask = data["attention_mask"]
        prompt_lens = attention_mask[:, : prompt_ids.shape[1]].sum(dim=1)

    response_lens = _reliable_response_lens(data)
    if response_lens is None:
        return _ORIG_NO_PADDING_2_PADDING(tensor, data)

    # max_response_len：以可靠字段最大长为准，再并入旧对齐目标（与 to_padded_tensor 一致）。
    max_response_len = int(response_lens.max().item())
    for key in _ALIGN_KEYS:
        m = _response_aligned_max_len(data, key)
        if m > max_response_len:
            max_response_len = m

    sequence_lens = prompt_lens + response_lens
    sequence_offsets = sequence_lens.cumsum(dim=0)
    if sequence_offsets[-1].item() != values.shape[0] or prompt_lens.eq(0).any():
        # 长度源与模型输出对不上（极端退化），退回原函数（保留原行为，宁崩不静默错）。
        return _ORIG_NO_PADDING_2_PADDING(tensor, data)

    response_list = []
    skip_padding = (0, 0) * (values.ndim - 1)
    for resp_len, seq_offset in zip(response_lens, sequence_offsets, strict=True):
        pad_size = max_response_len - resp_len
        response_list.append(
            F.pad(values[seq_offset - resp_len - 1 : seq_offset - 1], (*skip_padding, 0, pad_size))
        )
    out = torch.stack(response_list, dim=0)

    if out.shape[1] < max_response_len:
        if not _warned:
            _warned = True
            print(
                f"[policy_loss_padding_patch] 对齐 log_prob 宽度 {out.shape[1]} → {max_response_len} "
                f"(responses 被 tq 截短，改用 old_log_probs 长度，E29)",
                flush=True,
            )
        out = F.pad(out, (0, max_response_len - out.shape[1]), value=0)
    return out


def _pad_to_common(data, log_prob: torch.Tensor) -> None:
    """把 data 里响应对齐字段统一补到 log_prob 的宽（就地改 data）。

    to_padded_tensor 让 response_mask/old_log_probs/advantages 各自 pad 到不同宽
    （tq 错位根因）。这里以 log_prob（已对齐到最大宽）为准，把偏窄的字段右补 0 对齐。
    补出列对应 response_mask=0 区域，被 masked_mean 屏蔽，不进 loss。
    """
    target = log_prob.shape[1]
    for key in ("response_mask", "old_log_probs", "advantages", "rollout_is_weights", "ref_log_prob"):
        if key not in data:
            continue
        v = data[key]
        if hasattr(v, "dim") and v.dim() == 2 and v.shape[1] < target:
            data[key] = F.pad(v, (0, target - v.shape[1]), value=0)
        elif hasattr(v, "dim") and v.dim() == 2 and v.shape[1] > target:
            # log_prob 比该字段短（反向错位）：截断到 log_prob 宽。理论上 responses==response_mask
            # 不会触发，兜底防 log_prob - old_log_prob 反向崩。
            data[key] = v[:, :target]


def _patched_ppo_loss(config, model_output, data, dp_group=None):
    """重写 verl ppo_loss：to_padded_tensor 后统一响应对齐字段宽度，防形状错位崩。"""
    log_prob = _patched_no_padding_2_padding(model_output["log_probs"], data)
    entropy = model_output.get("entropy", None)
    if entropy is not None:
        entropy = _patched_no_padding_2_padding(entropy, data)

    config.global_batch_info["dp_size"] = data["dp_size"]
    config.global_batch_info["batch_num_tokens"] = data["batch_num_tokens"]
    config.global_batch_info["global_batch_size"] = data["global_batch_size"]
    config.global_batch_info["loss_scale_factor"] = config.loss_scale_factor

    if (
        data["dp_size"] > 1
        or data["batch_num_tokens"] is not None
        or data["global_batch_size"] is not None
        or config.loss_scale_factor is not None
    ):
        metric_aggregation = AggregationType.SUM
    else:
        metric_aggregation = AggregationType.MEAN

    metrics = {}

    fields = ["response_mask", "old_log_probs", "advantages"]
    if "rollout_is_weights" in data:
        fields.append("rollout_is_weights")
    if "ref_log_prob" in data:
        fields.append("ref_log_prob")
    data = data.select(*fields).to_padded_tensor()

    # ★ E29 修复：把响应对齐字段统一补到 log_prob 宽（to_padded_tensor 各自 pad 会错位）。
    _pad_to_common(data, log_prob)

    response_mask = data["response_mask"].to(bool)
    old_log_prob = data["old_log_probs"]
    advantages = data["advantages"]
    rollout_is_weights = data.get("rollout_is_weights", None)

    loss_agg_mode = config.loss_agg_mode
    loss_mode = config.policy_loss.get("loss_mode", "vanilla")

    policy_loss_fn = get_policy_loss_fn(loss_mode)
    pg_loss, pg_metrics = policy_loss_fn(
        old_log_prob=old_log_prob,
        log_prob=log_prob,
        advantages=advantages,
        response_mask=response_mask,
        loss_agg_mode=loss_agg_mode,
        config=config,
        rollout_is_weights=rollout_is_weights,
    )

    pg_metrics = Metric.from_dict(pg_metrics, aggregation=AggregationType.MEAN)
    metrics.update(pg_metrics)
    metrics["actor/pg_loss"] = Metric(value=pg_loss, aggregation=metric_aggregation)
    policy_loss = pg_loss

    if entropy is not None:
        entropy_loss = agg_loss(
            loss_mat=entropy, loss_mask=response_mask, loss_agg_mode=loss_agg_mode, **config.global_batch_info
        )
        entropy_coeff = config.entropy_coeff
        policy_loss -= entropy_coeff * entropy_loss
        metrics["actor/entropy_loss"] = Metric(value=entropy_loss, aggregation=metric_aggregation)

    if config.use_kl_loss:
        ref_log_prob = data["ref_log_prob"]
        kld = kl_penalty(logprob=log_prob, ref_logprob=ref_log_prob, kl_penalty=config.kl_loss_type)
        kl_loss = agg_loss(
            loss_mat=kld, loss_mask=response_mask, loss_agg_mode=config.loss_agg_mode, **config.global_batch_info
        )
        policy_loss += kl_loss * config.kl_loss_coef
        metrics["kl_loss"] = Metric(value=kl_loss, aggregation=metric_aggregation)
        metrics["kl_coef"] = config.kl_loss_coef

    return policy_loss, metrics


def apply() -> None:
    """替换 verl 里的 no_padding_2_padding + ppo_loss 引用。"""
    _padding.no_padding_2_padding = _patched_no_padding_2_padding
    try:
        from verl.workers.utils import losses as _losses

        _losses.no_padding_2_padding = _patched_no_padding_2_padding
        _losses.ppo_loss = _patched_ppo_loss
    except ImportError:
        pass


apply()
