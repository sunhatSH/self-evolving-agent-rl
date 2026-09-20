"""Training entry for the self-evolving agentic-RL system.

Resolves OmegaConf inheritance (``defaults: [../base]``), applies CLI overrides,
and drives a standard GRPO run over multi-agent sandbox rollouts via
``trainer.agent_rl_runner.run_agent_ppo``.

No experience-replay buffer and no custom continual-learning loss: training uses
verl's stock PPO/GRPO objective. The system's contribution is the multi-agent
sampling + sandbox environment + diff-driven reward.

Usage::

    python -m trainer.agent_rl_main --config configs/run/agent_rl_4gpu.yaml
    python -m trainer.agent_rl_main --config <cfg> data.train_files=/path.parquet
    python -m trainer.agent_rl_main --config <cfg> --resume-from ckpts/exp-step-50
"""

from __future__ import annotations

import argparse
import os
from pathlib import Path

from omegaconf import OmegaConf


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", type=str, required=True, help="Path to experiment yaml.")
    parser.add_argument("--resume-from", type=str, default=None, help="Optional checkpoint to resume.")
    parser.add_argument(
        "--lr",
        type=float,
        default=None,
        help="Override actor_rollout_ref.actor.optim.lr (e.g. --lr 1.5e-6).",
    )
    # Hydra-style key=value overrides, e.g. trainer.total_training_steps=4
    parser.add_argument(
        "overrides",
        nargs="*",
        default=[],
        help="Config overrides in key=value format (e.g. data.train_files=/path.parquet).",
    )
    return parser.parse_args()


def _apply_overrides(cfg, overrides: list[str]):
    for ov in overrides:
        if "=" not in ov:
            print(f"[agent-rl] WARNING: skipping malformed override '{ov}' (missing '=')")
            continue
        key, _, value = ov.partition("=")
        v = value.strip()
        if v.lower() == "true":
            v = True
        elif v.lower() == "false":
            v = False
        else:
            try:
                v = int(v)
            except ValueError:
                try:
                    v = float(v)
                except ValueError:
                    v = value  # keep as string
        OmegaConf.update(cfg, key.strip(), v, force_add=True)
        print(f"[agent-rl] override: {key.strip()}={v!r}")


def load_config(config_path: str):
    """Resolve OmegaConf inheritance (``defaults: [../base]``).

    Recurses into a base that itself declares ``defaults`` (e.g. a run config that
    inherits another run config), so nested inheritance resolves fully. The
    ``defaults`` key is always stripped from the returned config so verl never
    sees an unknown top-level key.
    """
    cfg_path = Path(config_path).resolve()
    cfg = OmegaConf.load(cfg_path)

    defaults = cfg.pop("defaults", None)
    if defaults:
        merged = OmegaConf.create({})
        for entry in defaults:
            ref = str(entry).strip()
            if ref.startswith("/"):
                base_path = Path(f"{ref}.yaml") if not ref.endswith(".yaml") else Path(ref)
            else:  # both "../x" and "x" resolve relative to this file's dir
                base_path = (cfg_path.parent / f"{ref}.yaml").resolve()
            # Recurse so a base with its own `defaults` resolves fully.
            base_cfg = load_config(str(base_path))
            merged = OmegaConf.merge(merged, base_cfg)
        cfg = OmegaConf.merge(merged, cfg)

    cfg.pop("defaults", None)  # never leak `defaults` into verl

    # If CKPT_DIR is set (train.sh), write checkpoints there.
    ckpt_dir = os.environ.get("CKPT_DIR")
    if ckpt_dir:
        OmegaConf.update(cfg, "trainer.default_local_dir", ckpt_dir, force_add=True)
    return cfg


def main():
    args = parse_args()
    cfg = load_config(args.config)
    _apply_overrides(cfg, args.overrides)
    if args.lr is not None:
        OmegaConf.update(cfg, "actor_rollout_ref.actor.optim.lr", args.lr, force_add=True)
        print(f"[agent-rl] --lr override: actor_rollout_ref.actor.optim.lr={args.lr}", flush=True)

    from trainer.agent_rl_runner import run_agent_ppo

    run_agent_ppo(cfg, resume_from=args.resume_from)


if __name__ == "__main__":
    main()
