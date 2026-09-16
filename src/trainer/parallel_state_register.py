"""Patch FSDPEngine.__init__ to call init_parallel_state (veomni).

问题: FSDPEngine.__init__ 没调 veomni 的 init_parallel_state, 导致后续
flash_attention_forward → get_parallel_state() 返回未初始化默认值 →
ParallelState() 构造时 product≠world_size 崩. VeOmniEngine.__init__ 有调,
但 fsdp2 + custom_language_model 走的是 CustomFSDPEngineWithLMHead(继承
FSDPEngine), 没走 VeOmniEngine, 故漏了.

解法: monkey-patch FSDPEngine.__init__, 在原 __init__ 之后补调
init_parallel_state(对齐 VeOmniEngine.__init__ 的做法). 在 WorkerDict 进程
(GPU worker)里执行, 那里有 torch.distributed process group.

触发: VERL_USE_EXTERNAL_MODULES 里加 trainer.parallel_state_register,
import 即安装 patch. 幂等.
"""

from __future__ import annotations

import logging

logger = logging.getLogger(__name__)
_PATCHED = False


def install() -> None:
    """Monkey-patch FSDPEngine.__init__ to init veomni parallel state. Idempotent."""
    global _PATCHED
    if _PATCHED:
        return

    try:
        from verl.workers.engine.fsdp.transformer_impl import FSDPEngine
    except Exception as exc:  # noqa: BLE001 -- verl absent off-cluster
        print(f"[agent-rl] parallel_state_register skipped (verl absent: {exc})", flush=True)
        return

    try:
        from veomni.distributed import parallel_state
    except Exception as exc:  # noqa: BLE001 -- veomni absent
        print(f"[agent-rl] parallel_state_register skipped (veomni absent: {exc})", flush=True)
        return

    import torch.distributed as dist

    _orig_init = FSDPEngine.__init__

    def _patched_init(self, model_config, engine_config, optimizer_config, checkpoint_config):
        _orig_init(self, model_config, engine_config, optimizer_config, checkpoint_config)

        # 只在 SP>1 且 process group 已初始化时调 (WorkerDict 进程)
        sp_size = engine_config.ulysses_sequence_parallel_size
        if sp_size <= 1:
            return
        if not dist.is_initialized():
            return

        world_size = dist.get_world_size()
        dp_size = world_size // sp_size
        if dp_size < 1:
            return

        try:
            parallel_state.init_parallel_state(
                dp_size=dp_size,
                ulysses_size=sp_size,
                dp_mode="fsdp2",
            )
            print(
                f"[agent-rl] FSDPEngine patched: init_parallel_state "
                f"world_size={world_size} sp={sp_size} dp={dp_size}",
                flush=True,
            )
        except Exception as exc:  # noqa: BLE001 -- best-effort, don't crash init
            print(
                f"[agent-rl] FSDPEngine patched: init_parallel_state failed ({exc})",
                flush=True,
            )

    FSDPEngine.__init__ = _patched_init
    _PATCHED = True
    print("[agent-rl] parallel_state_register installed (FSDPEngine.__init__ patched)", flush=True)


# import 即安装 (与 observer_hook_register / harness_register 同模式)
install()
