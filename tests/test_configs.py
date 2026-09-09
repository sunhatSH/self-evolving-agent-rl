"""Validate the runnable configs load and follow the verl Hydra schema.

These checks are framework-agnostic (no verl import): they assert that our
overlay yamls (a) inherit base.yaml cleanly via ``defaults``, (b) place
actor/model/rollout fields under verl's canonical key paths, (c) contain no
dead ``cl_grpo`` loss_mode, and (d) expose the new agent_rl rollout schema
(``agent_rl.rollout.sessions_per_step``) with no CL/buffer/weighting leftovers.
"""

from __future__ import annotations

from pathlib import Path

import pytest
from omegaconf import OmegaConf

from trainer.agent_rl_main import load_config

CONFIG_ROOT = Path(__file__).resolve().parents[1] / "configs"

# Runnable overlay configs under configs/run/ (inherit base.yaml). The CL phase
# rosters (phase1..6 / _legacy_phases) were removed with the CL code.
RUN_CONFIGS = sorted(CONFIG_ROOT.glob("run/*.yaml"))


def test_found_run_configs():
    assert RUN_CONFIGS, "expected at least one runnable config under configs/run/"


def test_base_config_loads():
    cfg = OmegaConf.load(CONFIG_ROOT / "base.yaml")
    # No dead CL sections should remain in base.
    assert "cl" not in cfg
    assert "buffer" not in cfg
    assert "weighting" not in cfg
    # New agent_rl rollout schema present.
    assert "agent_rl" in cfg and "rollout" in cfg.agent_rl
    assert "sessions_per_step" in cfg.agent_rl.rollout


@pytest.mark.parametrize("cfg_path", RUN_CONFIGS, ids=lambda p: p.stem)
def test_config_loads_and_matches_verl_schema(cfg_path):
    cfg = load_config(str(cfg_path))

    # (a) No top-level `actor:` -- actor config must live under actor_rollout_ref.
    assert "actor" not in cfg, f"{cfg_path.name}: top-level 'actor' should be actor_rollout_ref.actor"

    # (b) Actor knobs sit on verl's canonical path.
    aro = cfg.get("actor_rollout_ref")
    assert aro is not None and "actor" in aro, f"{cfg_path.name}: missing actor_rollout_ref.actor"
    assert "use_kl_loss" in aro.actor

    # (c) rollout.n = traj/query (GRPO group size) must be a positive int.
    assert int(aro.rollout.n) >= 1, f"{cfg_path.name}: rollout.n must be >= 1"

    # (d) No dead cl_grpo loss_mode anywhere.
    dumped = OmegaConf.to_yaml(cfg)
    assert "cl_grpo" not in dumped, f"{cfg_path.name}: dead cl_grpo loss_mode present"

    # (e) Model path lives under actor_rollout_ref.model.path.
    assert "model" in aro and "path" in aro.model

    # (f) agent_rl rollout schema present; no CL/buffer/weighting leftovers.
    assert "cl" not in cfg, f"{cfg_path.name}: dead cl section present"
    assert "agent_rl" in cfg and "rollout" in cfg.agent_rl
    assert "sessions_per_step" in cfg.agent_rl.rollout
