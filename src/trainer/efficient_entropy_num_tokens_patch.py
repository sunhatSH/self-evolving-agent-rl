"""Fix verl efficient_entropy kernel num_tokens.to(tl.float32) bug (E28).

根因（2026-08-28 r0_clear 训练崩溃）:
    verl/utils/kernel/kernels.py 的 efficient_entropy_triton_kernel_epilogue 和
    efficient_entropy_triton_epilogue_tp_update 两个 kernel 的 reduction==2(mean) 分支用
    ``num_tokens.to(tl.float32)``。num_tokens 是 Python int（运行时标量），Triton 在
    某些路径下不把它转成 tensor → ``AttributeError: 'int' object has no attribute 'to'``
    → actor_rollout_update_actor 崩溃，整训练挂掉。

    触发条件：response 序列超长（r0_clear mean 24743 / max 60854 vs baseline 1198）时，
    num_tokens 走 int 路径 + reduction==mean。baseline/kl 序列正常未触发。

修法（不改 verl 源码，走 VERL_USE_EXTERNAL_MODULES 注入）:
    重新定义这两个 kernel，把 ``num_tokens.to(tl.float32)`` 换成 ``num_tokens * 1.0``
    （int * float = float，Triton 对 int 标量兼容），再替换 kernels 模块属性。
    其余逻辑逐字照抄。
"""

from __future__ import annotations

import triton
import triton.language as tl
from verl.utils.kernel import kernels


@triton.autotune(configs=[triton.Config({"BLOCK_SIZE_M": 16, "BLOCK_SIZE_N": 64})], key=["num_tokens", "num_splits"])
@triton.jit
def _patched_epilogue(
    max_ptr,
    stride_max_m: tl.int64,
    stride_max_n: tl.int64,
    num_tokens,
    num_splits,
    global_max_ptr,
    stride_global_max: tl.int64,
    accu_ptr,
    stride_accu_m: tl.int64,
    stride_accu_n: tl.int64,
    global_accu_ptr,
    stride_global_accu: tl.int64,
    entropy_b_ptr,
    stride_entropy_b_m: tl.int64,
    stride_entropy_b_n: tl.int64,
    global_entropy_b_ptr,
    stride_global_entropy_b: tl.int64,
    global_entropy_ptr,
    stride_global_entropy: tl.int64,
    global_logprobs_ptr,
    stride_global_logprobs: tl.int64,
    global_logprobs_scalar_ptr,
    reduction: int,
    BLOCK_SIZE_M: tl.constexpr,
    BLOCK_SIZE_N: tl.constexpr,
):
    pid_m = tl.program_id(axis=0)
    offs_m = pid_m * BLOCK_SIZE_M + tl.arange(0, BLOCK_SIZE_M)
    global_max = tl.zeros((BLOCK_SIZE_M,), dtype=tl.float32)
    global_accu = tl.zeros((BLOCK_SIZE_M,), dtype=tl.float32)
    global_entropy_b = tl.zeros((BLOCK_SIZE_M,), dtype=tl.float32)
    for pid_n in range(0, tl.cdiv(num_splits, BLOCK_SIZE_N)):
        offs_n = pid_n * BLOCK_SIZE_N + tl.arange(0, BLOCK_SIZE_N)
        max_ptrs = max_ptr + offs_m[:, None] * stride_max_m + offs_n[None, :] * stride_max_n
        _max = tl.load(max_ptrs, mask=(offs_m[:, None] < num_tokens) & (offs_n[None, :] < num_splits), other=0.0)
        accu_ptrs = accu_ptr + offs_m[:, None] * stride_accu_m + offs_n[None, :] * stride_accu_n
        _accu = tl.load(accu_ptrs, mask=(offs_m[:, None] < num_tokens) & (offs_n[None, :] < num_splits), other=0.0)
        entropy_b_ptrs = entropy_b_ptr + offs_m[:, None] * stride_entropy_b_m + offs_n[None, :] * stride_entropy_b_n
        _entropy_b = tl.load(
            entropy_b_ptrs, mask=(offs_m[:, None] < num_tokens) & (offs_n[None, :] < num_splits), other=0.0
        )
        _max_old = global_max
        _local_max = tl.max(_max, axis=1)
        global_max = tl.maximum(global_max, _local_max)
        _scale = tl.exp(_max - global_max[:, None])
        _coeff = tl.exp(_max_old - global_max)
        global_accu = _coeff * global_accu + tl.sum(_scale * _accu, axis=1)
        global_entropy_b = _coeff * global_entropy_b + tl.sum(_scale * _entropy_b, axis=1)

    maximum_ptrs = global_max_ptr + offs_m * stride_global_max
    tl.store(maximum_ptrs, global_max, mask=offs_m < num_tokens)
    global_entropy_b = tl.fdiv(global_entropy_b, global_accu)
    tl.store(global_entropy_b_ptr + offs_m * stride_global_entropy_b, global_entropy_b, mask=offs_m < num_tokens)
    global_accu_ptrs = global_accu_ptr + offs_m * stride_global_accu
    tl.store(global_accu_ptrs, global_accu, mask=offs_m < num_tokens)
    global_entropy = tl.log(global_accu) + global_max - global_entropy_b
    global_entropy_ptrs = global_entropy_ptr + offs_m * stride_global_entropy
    tl.store(global_entropy_ptrs, global_entropy, mask=offs_m < num_tokens)
    global_logprobs_ptrs = global_logprobs_ptr + offs_m * stride_global_logprobs
    global_logprobs = tl.load(global_logprobs_ptrs, mask=offs_m < num_tokens)
    global_logprobs = global_max + tl.log(global_accu) - global_logprobs
    global_logprobs = -1 * global_logprobs
    if reduction == 0:
        tl.store(global_logprobs_ptrs, global_logprobs, mask=offs_m < num_tokens)
    elif reduction == 1:
        global_logprobs_scalar = tl.sum(global_logprobs, axis=0)
        tl.atomic_add(global_logprobs_scalar_ptr, global_logprobs_scalar)
    elif reduction == 2:
        global_logprobs_scalar = tl.sum(global_logprobs, axis=0) / (num_tokens * 1.0)
        tl.atomic_add(global_logprobs_scalar_ptr, global_logprobs_scalar)


@triton.jit
def _patched_epilogue_tp_update(
    num_tokens,
    logprobs_ptr,
    stride_logprobs: tl.int64,
    maximum_ptr,
    stride_maximum: tl.int64,
    accumulate_ptr,
    stride_accumulate: tl.int64,
    entropy_b_ptr,
    stride_entropy_b: tl.int64,
    entropy_ptr,
    stride_entropy: tl.int64,
    logprobs_scalar_ptr,
    reduction: int,
    BLOCK_SIZE_M: tl.constexpr,
):
    pid_m = tl.program_id(axis=0)
    offs_m = pid_m * BLOCK_SIZE_M + tl.arange(0, BLOCK_SIZE_M)
    maximum = tl.load(maximum_ptr + offs_m * stride_maximum, mask=offs_m < num_tokens)
    accumulate = tl.load(accumulate_ptr + offs_m * stride_accumulate, mask=offs_m < num_tokens)
    entropy_b = tl.load(entropy_b_ptr + offs_m * stride_entropy_b, mask=offs_m < num_tokens)
    entropy_b = tl.fdiv(entropy_b, accumulate)
    tl.store(entropy_b_ptr + offs_m * stride_entropy_b, entropy_b, mask=offs_m < num_tokens)
    entropy = tl.log(accumulate) + maximum - entropy_b
    tl.store(entropy_ptr + offs_m * stride_entropy, entropy, mask=offs_m < num_tokens)
    logprobs = tl.load(logprobs_ptr + offs_m * stride_logprobs, mask=offs_m < num_tokens)
    logprobs = maximum + tl.log(accumulate) - logprobs
    logprobs = -1 * logprobs
    if reduction == 0:
        tl.store(logprobs_ptr + offs_m * stride_logprobs, logprobs, mask=offs_m < num_tokens)
    elif reduction == 1:
        logprobs_scalar = tl.sum(logprobs, axis=0)
        tl.atomic_add(logprobs_scalar_ptr, logprobs_scalar)
    elif reduction == 2:
        logprobs_scalar = tl.sum(logprobs, axis=0) / (num_tokens * 1.0)
        tl.atomic_add(logprobs_scalar_ptr, logprobs_scalar)


def apply() -> None:
    """替换 verl kernels 里的两个 buggy kernel。"""
    kernels.efficient_entropy_triton_kernel_epilogue = _patched_epilogue
    kernels.efficient_entropy_triton_epilogue_tp_update = _patched_epilogue_tp_update


apply()
