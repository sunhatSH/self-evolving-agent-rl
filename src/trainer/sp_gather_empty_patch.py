"""Fix verl gather_outputs_and_unpad 0D/empty 张量 IndexError (E30).

根因（2026-08-30 16卡 step37 崩溃）:
    ``prepare_model_outputs``（transformer_impl.py:1237）里
    ``log_probs = output.log_probs.squeeze(0)``。当某 SP rank 上只有 1 个 token
    （total_nnz_local=1，如 micro-batch 全 padding 行、SP=4 时 2×2=4 token → 每卡 1）
    且 ``output.log_probs`` 是 1D ``[1]`` 时，``squeeze(0)`` 把它压成 0 维标量
    （``size()=[]``）→ ``gather_outputs_and_unpad`` 里 ``Gather.forward`` 做
    ``local_shape = list(local_tensor.size()); split_size = local_shape[0]`` →
    ``IndexError: list index out of range``。

修法（不改 verl 源码，走 VERL_USE_EXTERNAL_MODULES 注入）:
    包装 ``gather_outputs_and_unpad``：
      · 0 维标量 → ``reshape(1)`` 成 1D ``[1]`` 再 gather（1 个 token 正确跨卡聚合）。
      · 空张量（numel=0）→ 原样返回（gather 空还是空）。
    其余路径逐字透传。
"""

from __future__ import annotations

import torch
from verl.utils import ulysses as _ulysses

_ORIG_GATHER_OUTPUTS_AND_UNPAD = _ulysses.gather_outputs_and_unpad


def _patched_gather_outputs_and_unpad(
    x: torch.Tensor,
    gather_dim: int,
    unpad_dim: int | None = None,
    padding_size: int = 0,
    grad_scaler: bool = True,
    group=None,
) -> torch.Tensor:
    if isinstance(x, torch.Tensor):
        if x.dim() == 0:
            # 0 维标量（total_nnz_local=1 被 squeeze 压瘪）→ 1D [1]，让 Gather.forward 有 local_shape[0]。
            x = x.reshape(1)
        if x.numel() == 0:
            # 空张量：跨卡 gather 仍是空，直接返回避免 all_gather 空张量崩溃。
            return x
    return _ORIG_GATHER_OUTPUTS_AND_UNPAD(x, gather_dim, unpad_dim, padding_size, grad_scaler, group)


def apply() -> None:
    """替换 ulysses.gather_outputs_and_unpad + transformer_impl 模块级绑定。"""
    _ulysses.gather_outputs_and_unpad = _patched_gather_outputs_and_unpad
    try:
        from verl.workers.engine.fsdp import transformer_impl as _ti

        _ti.gather_outputs_and_unpad = _patched_gather_outputs_and_unpad
    except ImportError:
        pass


apply()
