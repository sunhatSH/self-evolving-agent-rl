#!/usr/bin/env bash
# ─────────────────────────────────────────────────────────────────────────────
# Hermes 迁移版 ClawEval 评测（Hermes agent + 官方 grader + 可选 mock_services）
#
# 跟 eval_official.sh 的区别：
#   eval_official.sh  — 完全官方（官方 agent loop + mock_services + 官方 grader）
#   eval_hermes.sh    — Hermes 迁移版（Hermes agent loop + 官方 grader；
#                       --with-mock-services 时恢复 audit_data + 真实 tool dispatch）
#
# 评测对象（依次）：
#   1. base（Qwen3.5-9B 基座）
#   2. baseline_step200（ckpts_archive 里的旧数据 ckpt，已 merge）
#   3. kl_step200（同上）
#
# judge/user_agent = gpt-5.6-luna @ tokenhub（跟 eval_official.sh 同口径）
#
# 两种 runner 模式：
#   --offline-messages <jsonl>  离线转换（把已采集的 Hermes message_history 转官方 trace）
#                               —— 本机可跑（无 GPU/沙箱），但需有 message_history JSONL
#   --e2b                       实时跑 Hermes（腾讯沙箱，集群 + GPU + 凭证）
#
# 用法：
#   # 离线（推荐，本机可跑）：评 base，用冷启动轨迹
#   bash scripts/eval_hermes.sh base --offline \\
#     /mnt/afs_toolcall/sunhao4/workspace/agentic_cl_research/rollouts/cold_start/grpo_hermes.jsonl
#
#   # 离线 + 恢复 audit_data（T 系列任务 safety 不再漏判）
#   bash scripts/eval_hermes.sh base --offline <jsonl> --with-mock-services
#
#   # 实时（集群）
#   bash scripts/eval_hermes.sh base --e2b
#
#   # 评多个模型
#   bash scripts/eval_hermes.sh base baseline kl --offline <jsonl>
#
# 输出：eval/results/hermes/<model>/{score_summary.json, score_summary.txt}
# ─────────────────────────────────────────────────────────────────────────────
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
HARNESS_DIR="${HARNESS_DIR:-/mnt/afs_toolcall/sunhao4/workspace/claw-eval-hermes}"
LIGHTLLM_DIR="/mnt/afs_toolcall/sunhao4/workspace/LightLLM"
RESULTS_DIR="$ROOT_DIR/eval/results/hermes"

# 模型路径（跟 eval_official.sh 同）
declare -A MODEL_PATHS=(
  ["base"]="/mnt/afs_toolcall/sunhao4/models/Qwen3.5-9B"
  ["baseline"]="$ROOT_DIR/eval/.tmp/merged_baseline"
  ["kl"]="$ROOT_DIR/eval/.tmp/merged_kl"
)

# ── 解析参数 ──────────────────────────────────────────────────────────────
MODELS=()
RUNNER_FLAGS=()
OFFLINE_FILE=""
RUNNER_MODE=""

while [ $# -gt 0 ]; do
  case "$1" in
    --offline)
      RUNNER_MODE="offline"
      shift
      OFFLINE_FILE="${1:?--offline requires a jsonl path}"
      shift
      ;;
    --e2b)
      RUNNER_MODE="e2b"
      shift
      ;;
    --with-mock-services)
      RUNNER_FLAGS+=("--with-mock-services")
      shift
      ;;
    base|baseline|kl)
      MODELS+=("$1")
      shift
      ;;
    *)
      echo "❌ 未知参数: $1" >&2
      exit 1
      ;;
  esac
done

# 默认评全部模型
if [ ${#MODELS[@]} -eq 0 ]; then
  MODELS=("base" "baseline" "kl")
fi

if [ -z "$RUNNER_MODE" ]; then
  echo "❌ 必须指定 --offline <jsonl> 或 --e2b"
  echo "   离线: bash scripts/eval_hermes.sh base --offline <jsonl> [--with-mock-services]"
  echo "   实时: bash scripts/eval_hermes.sh base --e2b [--with-mock-services]"
  exit 1
fi

# ── 准备 harness ──────────────────────────────────────────────────────────
if [ ! -d "$HARNESS_DIR" ]; then
  echo "❌ harness 不在 $HARNESS_DIR"
  exit 1
fi

# config：跟 eval_official.sh 同口径（模型 LightLLM serve，judge/user_agent luna）
cat > "$HARNESS_DIR/config_ours.yaml" <<'EOF'
# Hermes 迁移版评测 config：模型走本地 LightLLM serve，judge/user_agent 走 tokenhub luna
model:
  api_key: dummy
  base_url: http://127.0.0.1:8000/v1
  model_id: Qwen3.5-9B
  context_window: 32768
  api_mode: openai

judge:
  api_key: ${TOKENHUB_API_KEY}
  base_url: https://tokenhub.sensetime.com/v1
  model_id: gpt-5.6-luna
  enabled: true

user_agent_model:
  api_key: ${TOKENHUB_API_KEY}
  base_url: https://tokenhub.sensetime.com/v1
  model_id: gpt-5.6-luna

defaults:
  trace_dir: traces
  tasks_dir: tasks
EOF

# 凭证
export TOKENHUB_API_KEY=$(grep -oE 'TOKENHUB_API_KEY=.*' "$ROOT_DIR/.env" 2>/dev/null | cut -d= -f2- | tr -d '"' | tr -d "'")
if [ -z "$TOKENHUB_API_KEY" ]; then
  echo "❌ TOKENHUB_API_KEY 未找到（.env 里没有）"
  exit 1
fi
echo "[eval_hermes] TOKENHUB_API_KEY 已加载"

# ── serve + batch 函数 ────────────────────────────────────────────────────
serve_and_run() {
  local name=$1 model_dir=$2 trace_dir=$3

  echo ""
  echo "===== [$name] 起 serve: $model_dir ====="

  # 杀残留 serve
  pkill -f "lightllm.server.api_server" 2>/dev/null || true
  sleep 3

  export PATH=/mnt/afs_toolcall/sunhao4/.local/bin:/opt/conda/bin:$PATH
  export PYTHONPATH="$LIGHTLLM_DIR:/mnt/afs_toolcall/sunhao4/dependencies/verl:$ROOT_DIR/src:$ROOT_DIR"
  export VLLM_GDN_PREFILL_BACKEND=triton
  export NCCL_CUMEM_ENABLE=0
  export TEXT_MODEL_ONLY=1

  python -m lightllm.server.api_server \
    --model_dir "$model_dir" \
    --tp 2 --dp 1 --mem_fraction 0.75 \
    --tokenizer_mode fast --tool_call_parser qwen3_coder --reasoning_parser qwen3 \
    --max_req_total_len 32768 --host 0.0.0.0 --port 8000 \
    > "/tmp/serve_hermes_${name}.log" 2>&1 &
  local serve_pid=$!
  echo "[$name] serve pid=$serve_pid"

  # 等 serve 就绪（最多 10 分钟）
  echo "[$name] 等 serve 就绪..."
  local ready=0
  for i in $(seq 1 120); do
    if curl -s -m 2 http://127.0.0.1:8000/v1/models >/dev/null 2>&1; then
      ready=1
      break
    fi
    sleep 5
  done
  if [ "$ready" != "1" ]; then
    echo "❌ [$name] serve 未就绪，看 /tmp/serve_hermes_${name}.log"
    kill $serve_pid 2>/dev/null || true
    return 1
  fi
  echo "[$name] serve 就绪"

  # 跑 Hermes batch
  echo "===== [$name] 跑 Hermes batch (runner=$RUNNER_MODE) ====="
  cd "$HARNESS_DIR"
  export PYTHONPATH="src:/mnt/afs_toolcall/sunhao4/dependencies/verl:$ROOT_DIR/src:$ROOT_DIR"

  local batch_args=(
    --config config_ours.yaml
    --tasks-dir tasks
    --tag general
    --trials 3
    --parallel 8
    --trace-dir "$trace_dir"
  )

  if [ "$RUNNER_MODE" = "offline" ]; then
    batch_args+=(--offline-messages "$OFFLINE_FILE")
  else
    batch_args+=(--e2b)
    batch_args+=(--e2b-hermes-config /mnt/afs_toolcall/sunhao4/dependencies/verl/recipe_custom/scripts/e2b_agent/hermes.config.yaml)
    batch_args+=(--e2b-template node-python-hermes-26-7-1)
    batch_args+=(--model-base-url http://127.0.0.1:8000/v1)
    # 腾讯沙箱凭证
    source "$ROOT_DIR/scripts/env/load_tencent_env.sh" 2>/dev/null || true
  fi

  batch_args+=("${RUNNER_FLAGS[@]}")

  python -u run_hermes_batch.py "${batch_args[@]}"

  # 汇总（官方 score_summary.py，不改一行）
  python score_summary.py "$trace_dir" > "$trace_dir.score_summary.txt" 2>&1 || true
  echo "----- [$name] score -----"
  cat "$trace_dir.score_summary.txt" 2>/dev/null || echo "(汇总失败)"

  # 存结果
  mkdir -p "$RESULTS_DIR/$name"
  cp "$trace_dir/score_summary.json" "$RESULTS_DIR/$name/score_summary.json" 2>/dev/null || true
  cp "$trace_dir.score_summary.txt" "$RESULTS_DIR/$name/score_summary.txt" 2>/dev/null || true

  # 杀 serve
  kill $serve_pid 2>/dev/null || true
  sleep 5
  pkill -f "lightllm.server.api_server" 2>/dev/null || true
  echo "===== [$name] 完成 ====="
}

# ── 依次评测 ─────────────────────────────────────────────────────────────
mkdir -p "$RESULTS_DIR"

for name in "${MODELS[@]}"; do
  model_dir="${MODEL_PATHS[$name]:-}"
  if [ -z "$model_dir" ]; then
    echo "⚠️  未知模型: $name，跳过"
    continue
  fi
  if [ "$RUNNER_MODE" = "e2b" ] && [ ! -d "$model_dir" ]; then
    echo "⚠️  模型目录不存在: $model_dir ($name)，跳过"
    continue
  fi

  trace_dir="/tmp/claw_traces_hermes_${name}"
  serve_and_run "$name" "$model_dir" "$trace_dir"
done

# ── 汇总对比 ─────────────────────────────────────────────────────────────
echo ""
echo "===== Hermes 迁移版评测汇总 ====="
echo "judge = gpt-5.6-luna @ tokenhub"
echo "harness = Hermes (claw-eval-hermes) + 官方 grader"
if printf '%s\n' "${RUNNER_FLAGS[@]}" | grep -q -- '--with-mock-services'; then
  echo "audit_data = 真实 (mock_services /audit)"
else
  echo "audit_data = None (无 --with-mock-services)"
fi
echo ""
printf "%-15s %10s %10s %10s %10s\n" "model" "AvgScore" "AvgPass" "AnyPass" "AllPass"
printf "%-15s %10s %10s %10s %10s\n" "-----" "---------" "--------" "-------" "-------"
for name in "${MODELS[@]}"; do
  f="$RESULTS_DIR/$name/score_summary.json"
  [ -f "$f" ] || continue
  python3 -c "
import json
d=json.load(open('$f'))
for m in d:
    print(f'${name:<15s} {m.get(\"overall_avg_score\",0):>10.3f} {str(m.get(\"n_avg_pass\",\"-\"))+\"/\"+str(m.get(\"n_tasks\",\"-\")):>10s} {m.get(\"n_any_pass\",\"-\"):>10s} {m.get(\"n_all_pass\",\"-\"):>10s}')
" 2>/dev/null || echo "$name (读取失败)"
done
echo ""
echo "✅ 全部完成。结果在 $RESULTS_DIR/"
echo "   对照官方: eval/results/official/<model>/ (eval_official.sh 产出)"
