#!/usr/bin/env bash
# train_16gpu.sh — 16-GPU (2-node × 8) 20-step self-evolving RL training launcher.
#
# Runs the full self-evolving agent-RL loop on 16×H800: verl V1 agent_loop rollout
# (RemoteAgentLoopManager + e2b sandbox) → diff-driven external judge reward →
# GRPO update. 20 steps (from config), Qwen3.5-9B base.
#
# ⚠️ Per project rule, training MUST run in tmux/nohup, never foreground
#    (a dropped session kills the job and wastes hours of GPU time):
#     tmux new -d -s train 'bash scripts/train_16gpu.sh'
#     tmux attach -t train
#
# Training python = /opt/conda/bin/python3 (has torch/verl).
# verl = source checkout at /mnt/afs_toolcall/sunhao4/dependencies/verl (PYTHONPATH, not pip).
# LightLLM = source checkout at /mnt/afs_toolcall/sunhao4/workspace/LightLLM (PYTHONPATH).
#
# This is a thin wrapper around scripts/_train_impl.sh, which handles:
#   - multi-node Ray head/worker startup (2-node barrier sync via torch.distributed)
#   - jemalloc LD_PRELOAD (anti GatewayActor OOM on long runs)
#   - model prewarming to node-local /dev/shm (anti 16-GPU lightllm startup hang)
#   - metrics archiving + auto-resume from checkpoint
#   - log redirection to logs/experiments/<exp>/train.log
#
# Usage:
#   bash scripts/train_16gpu.sh                                       # default config
#   bash scripts/train_16gpu.sh configs/run/agent_rl_16gpu.yaml       # explicit config
#   bash scripts/train_16gpu.sh configs/run/agent_rl_16gpu.yaml trainer.save_freq=5
#
# Env overrides (all optional, sane defaults applied if unset):
#   MODEL_PATH     — base model (default: /mnt/afs_toolcall/sunhao4/models/Qwen3.5-9B)
#   TRAIN_FILES    — train parquet   (left to config default unless exported)
#   VERL_DIR       — verl checkout   (default: /mnt/afs_toolcall/sunhao4/dependencies/verl)
#   LIGHTLLM_DIR   — LightLLM checkout (default: /mnt/afs_toolcall/sunhao4/workspace/LightLLM)
set -euo pipefail

DIR="$(cd "$(dirname "$0")" && pwd)"
ROOT="$(cd "$DIR/.." && pwd)"

# ── config (first positional arg, defaults to the 16-GPU config) ─────────────
CFG="${1:-configs/run/agent_rl_16gpu.yaml}"
if [ $# -gt 0 ]; then shift; fi   # rest of "$@" = pass-through hydra overrides

# ── training python + dependency checkouts (verl/lightllm are NOT pip-installed;
#    they live as source trees injected via PYTHONPATH, same as train_4gpu.sh) ─
PY="/opt/conda/bin/python3"
VERL_DIR="${VERL_DIR:-/mnt/afs_toolcall/sunhao4/dependencies/verl}"
LIGHTLLM_DIR="${LIGHTLLM_DIR:-/mnt/afs_toolcall/sunhao4/workspace/LightLLM}"
export PYTHONPATH="$LIGHTLLM_DIR:$VERL_DIR:$ROOT/src:$ROOT${PYTHONPATH:+:$PYTHONPATH}"

# Model path (config reads it via ${oc.env:MODEL_PATH,...})
export MODEL_PATH="${MODEL_PATH:-/mnt/afs_toolcall/sunhao4/models/Qwen3.5-9B}"

cd "$ROOT"

# ── credentials: e2b sandbox (tencent.env) + judge/swanlab (.env) ────────────
# The V1 rollout drives the e2b hermes sandbox; the omni reward calls the LLM
# judge. Both read creds from env. Source the same loaders _train_impl.sh uses.
# `set -a` so sourced KEY=VALUE lines are exported to the Python process.
if [ -f "$DIR/env/load_tencent_env.sh" ]; then
  set -a; # shellcheck disable=SC1090
  source "$DIR/env/load_tencent_env.sh" || true
  set +a
fi
if [ -f "$DIR/env/load_training_env.sh" ]; then
  set -a; # shellcheck disable=SC1090
  source "$DIR/env/load_training_env.sh" || true
  set +a
fi

# ── verl external modules (rollout patches + FQN hook factory) ───────────────
# Registers our rollout patches (e2b_http1, observer_hook, pause_generation,
# dataproto_tensordict, empty_batch_skip, etc.) via VERL_USE_EXTERNAL_MODULES.
# _train_impl.sh re-sources this too; the script is idempotent (dedup loop).
if [ -f "$DIR/env/verl_external_modules.sh" ]; then
  # shellcheck disable=SC1090
  source "$DIR/env/verl_external_modules.sh" || true
fi

# ── env flags (same as train_4gpu.sh) ─────────────────────────────────────────
# e2b: tencent AGS uses an ark_ key -> skip the e2b_ prefix check.
export E2B_VALIDATE_API_KEY="${E2B_VALIDATE_API_KEY:-false}"
# NCCL cuMem off (lightllm torch_memory_saver vs NCCL cuMem P2P deadlock guard).
export NCCL_CUMEM_ENABLE="${NCCL_CUMEM_ENABLE:-0}"

# ── resolved command (printed before running) ───────────────────────────────
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "[train_16gpu] 16-GPU 20-step self-evolving RL training"
echo "[train_16gpu] MODEL_PATH=$MODEL_PATH"
echo "[train_16gpu] VERL_DIR=$VERL_DIR  LIGHTLLM_DIR=$LIGHTLLM_DIR"
echo "[train_16gpu] E2B_DOMAIN=${E2B_DOMAIN:-<unset>}  E2B_API_KEY=${E2B_API_KEY:+<set>}"
echo "[train_16gpu] TOKENHUB_API_KEY=${TOKENHUB_API_KEY:+<set>}"
echo "[train_16gpu] PYTHONPATH=$PYTHONPATH"
echo "[train_16gpu] cwd=$ROOT  config=$CFG"
echo "[train_16gpu] cmd: bash $DIR/_train_impl.sh --config $CFG --nnodes 2 --gpus-per-node 8 $*"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

# ── delegate to _train_impl.sh ───────────────────────────────────────────────
# _train_impl.sh handles all heavy lifting:
#   - multi-node Ray head/worker (2-node barrier sync, --num-cpus from nproc)
#   - jemalloc LD_PRELOAD (anti GatewayActor OOM)
#   - model prewarming to /dev/shm (anti 16-GPU lightllm startup hang)
#   - flash_attn shim detection
#   - metrics archiving + auto-resume from checkpoint
#   - log redirection to logs/experiments/<exp>/train.log
#   - NCCL_CUMEM_ENABLE, E2B_VALIDATE_API_KEY (re-exported internally, harmless)
# Topology (nnodes=2, gpus-per-node=8) matches configs/run/agent_rl_16gpu.yaml.
exec bash "$DIR/_train_impl.sh" \
  --config "$CFG" \
  --nnodes 2 \
  --gpus-per-node 8 \
  "$@"
