# configs/run/ — runnable configs

Top layer of the config inheritance chain. A `run/*.yaml` composes the shared
base with the fields needed to actually launch a job.

## Inheritance

```
base.yaml         # shared defaults (model, rollout, reward=LLM judge, agent_rl.rollout)
cluster.yaml      # cluster engine overlay (lightllm/FSDP/Ray, 64-GPU scale, data paths)
run/*.yaml        # runnable config: `defaults` list + job-specific overrides
```

`base.yaml` and `cluster.yaml` are overlays, not complete verl configs. A runnable
config lists the layers it needs under `defaults` (resolved by
`src/trainer/agent_rl_main.py::load_config`, which does `OmegaConf.merge` in
`defaults` order, then merges the file body on top).

## Current files

| File | Purpose |
|------|---------|
| [`agent_rl_4gpu.yaml`](agent_rl_4gpu.yaml) | 4-GPU debug smoke config. Inherits `base.yaml`, shrinks batch/steps/GPUs. Validates the rollout+GRPO train loop on 4×H800 — not for real results. |

Launch:

```bash
bash scripts/train.sh 4gpu --config configs/run/agent_rl_4gpu.yaml
```

The 4-GPU debug config uses a small model (Qwen3.5-9B) via `${oc.env:MODEL_PATH,...}`
and a `local` sandbox backend (no cluster sandbox creds). The launch script exports
`MODEL_PATH` / `TRAIN_FILES` / `VAL_FILES`.

For a full cluster run, create a new `run/*.yaml` that also pulls in `cluster.yaml`
(and `_generated_ppo_trainer.yaml` for the full verl defaults) under `defaults`,
then override the job-specific fields.
