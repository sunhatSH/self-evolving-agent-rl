# configs/ — training configuration

OmegaConf/YAML configs for the self-evolving multi-agent RL system. Configs are
layered overlays merged in `defaults` order by
`src/trainer/agent_rl_main.py::load_config`; each layer overrides the previous,
and a file's own body overrides its `defaults`.

## Layers

```
base.yaml                 # shared defaults: model (Qwen3.5-9B base), rollout,
                          #   reward = external LLM judge, algorithm = GRPO, and the
                          #   custom `agent_rl.rollout` section (sessions_per_step)
cluster.yaml              # cluster engine overlay (lightllm/FSDP/Ray, 64-GPU scale,
                          #   data paths, v1 custom_sync trainer)
_generated_ppo_trainer.yaml  # full verl ppo_trainer defaults (Hydra base for cluster)
run/*.yaml                # runnable configs; pick the layers you need via `defaults`
```

The `agent_rl:` top-level section is our own custom rollout config, read only by
`trainer/agent_rollout_manager.py` (verl ignores it). It holds
`rollout.sessions_per_step` (and optional `max_single_gen_tokens`).

## Key files

| File | Purpose |
|------|---------|
| `base.yaml` | Shared defaults, not run directly. |
| `cluster.yaml` | 64-GPU cluster engine overlay. |
| `run/agent_rl_4gpu.yaml` | 4-GPU debug smoke config (inherits `base.yaml`). See `run/README.md`. |
| `run/agent_rl_16gpu.yaml` | 16-GPU (2-node) formal training config (Qwen3.5-9B). |
| `agents.yaml` | Multi-agent (observer / questioner / judge) settings. |
| `exps/` | verl agent-loop + hermes config (credentials via `${oc.env}`). |
| `templates/` | Reference layered-config templates (hardware × experiment); not wired into the launch scripts. |
| `sandbox_*.json` | Sandbox tool / runtime env definitions. |

## Model paths

- Base model in `base.yaml` = Qwen3.5-9B (`/mnt/afs_toolcall/sunhao4/models/Qwen3.5-9B`,
  override `actor_rollout_ref.model.path` or env `MODEL_PATH`). Both the 4-GPU
  debug config and the 16-GPU formal config use the 9B model.
- Data paths use `${oc.env:TRAIN_FILES,...}` / `${oc.env:VAL_FILES,...}`; the launch
  script exports them.

## Usage

```bash
# 4-GPU debug smoke
bash scripts/train_4gpu.sh configs/run/agent_rl_4gpu.yaml

# 16-GPU formal training (in tmux)
tmux new -d -s train 'bash scripts/train_16gpu.sh configs/run/agent_rl_16gpu.yaml'

# entry point also callable directly
python -m trainer.agent_rl_main --config configs/run/agent_rl_4gpu.yaml
```
