#!/usr/bin/env bash
# train_4gpu.sh — 4-GPU debug smoke launcher for the self-evolving agent-RL loop.
#
# ⚠️ This is a 4-step smoke to validate the training loop end-to-end (rollout →
#    reward → PPO update → checkpoint), NOT for producing results. Use the small
#    debug config (configs/run/agent_rl_4gpu.yaml: small model, local sandbox,
#    total_training_steps=4, 16-query batch).
#
# Per project rule, real / long runs must NOT run in the foreground (a dropped
# session kills them). Even this smoke should go in tmux or nohup, e.g.:
#     tmux new -d -s smoke 'bash scripts/train_4gpu.sh'
#     tmux attach -t smoke
#
# Usage:
#   bash scripts/train_4gpu.sh                                        # default config
#   bash scripts/train_4gpu.sh configs/run/agent_rl_4gpu.yaml         # explicit config
#   bash scripts/train_4gpu.sh configs/run/agent_rl_4gpu.yaml trainer.total_training_steps=2
#
# Env overrides (all optional, sane debug defaults applied if unset):
#   MODEL_PATH   — small local model (default: /mnt/afs_toolcall/sunhao4/models/Qwen3.5-9B)
#   TRAIN_FILES  — train parquet   (left to config default unless exported)
#   VAL_FILES    — val parquet     (left to config default unless exported)
#   VERL_DIR     — verl checkout   (default: /mnt/afs_toolcall/sunhao4/dependencies/verl)
#   LIGHTLLM_DIR — LightLLM checkout (default: /mnt/afs_toolcall/sunhao4/workspace/LightLLM)
set -euo pipefail

DIR="$(cd "$(dirname "$0")" && pwd)"
ROOT="$(cd "$DIR/.." && pwd)"

# ── config (first positional arg, defaults to the 4-GPU debug config) ─────────
CFG="${1:-configs/run/agent_rl_4gpu.yaml}"
if [ $# -gt 0 ]; then shift; fi   # rest of "$@" = pass-through hydra overrides

# ── GPUs: 4 cards unless the caller already pinned CUDA_VISIBLE_DEVICES ───────
export CUDA_VISIBLE_DEVICES="${CUDA_VISIBLE_DEVICES:-0,1,2,3}"

# ── debug defaults (only set if unset) ───────────────────────────────────────
# Small local model. The config reads it via env ${oc.env:MODEL_PATH}.
export MODEL_PATH="${MODEL_PATH:-/mnt/afs_toolcall/sunhao4/models/Qwen3.5-9B}"
# TRAIN_FILES / VAL_FILES intentionally left to the config default unless the
# caller exports them — no small debug parquet is hardcoded here.

# ── training python + dependency checkouts (verl/lightllm are NOT pip-installed;
#    they live as source trees injected via PYTHONPATH, same as _train_impl.sh) ─
PY="/opt/conda/bin/python3"
VERL_DIR="${VERL_DIR:-/mnt/afs_toolcall/sunhao4/dependencies/verl}"
LIGHTLLM_DIR="${LIGHTLLM_DIR:-/mnt/afs_toolcall/sunhao4/workspace/LightLLM}"
export PYTHONPATH="$LIGHTLLM_DIR:$VERL_DIR:$ROOT/src:$ROOT${PYTHONPATH:+:$PYTHONPATH}"

cd "$ROOT"

# Register our verl external modules (rollout manager FQN + stability patches)
# the same way the full trainer does. Best-effort: harmless if absent.
if [ -f "$DIR/env/verl_external_modules.sh" ]; then
  # shellcheck disable=SC1090
  source "$DIR/env/verl_external_modules.sh" || true
fi

# ── resolved command (printed before running) ───────────────────────────────
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "[train_4gpu] 4-step smoke (validate loop, NOT for results)"
echo "[train_4gpu] CUDA_VISIBLE_DEVICES=$CUDA_VISIBLE_DEVICES"
echo "[train_4gpu] MODEL_PATH=$MODEL_PATH"
echo "[train_4gpu] VERL_DIR=$VERL_DIR  LIGHTLLM_DIR=$LIGHTLLM_DIR"
echo "[train_4gpu] PYTHONPATH=$PYTHONPATH"
echo "[train_4gpu] cwd=$ROOT  config=$CFG"
echo "[train_4gpu] cmd: $PY -m trainer.agent_rl_main --config $CFG $*"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

exec "$PY" -m trainer.agent_rl_main --config "$CFG" "$@"
