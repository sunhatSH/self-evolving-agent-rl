#!/usr/bin/env bash
# ─────────────────────────────────────────────────────────────────────────────
# 完全官方 ClawEval 评测（官方 harness + mock_services + 官方 grader + 完整 audit_data）
#
# 跟 eval_all.sh 的区别：
#   eval_all.sh       — 半对齐（Hermes agent + 迁移 grader，audit_data=None）
#   eval_official.sh  — 完全官方（官方 agent loop + mock_services + 官方 grader）
#
# 评测对象（依次）：
#   1. base（Qwen3.5-9B 基座）
#   2. baseline_step200（ckpts_archive 里的旧数据 ckpt，已 merge）
#   3. kl_step200（同上）
#
# judge/user_agent = gpt-5.6-luna @ tokenhub（用户口径，luna 已恢复）
#
# 用法：
#   bash scripts/eval_official.sh              # 评三个模型
#   bash scripts/eval_official.sh base         # 只评 base
#   bash scripts/eval_official.sh baseline kl # 评指定模型
#
# 输出：eval/results/official/<model>/{score_summary.json, per_task.json}
# ─────────────────────────────────────────────────────────────────────────────
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
HARNESS_DIR="${HARNESS_DIR:-/tmp/claw-eval-official}"
LIGHTLLM_DIR="/mnt/afs_toolcall/sunhao4/workspace/LightLLM"
RESULTS_DIR="$ROOT_DIR/eval/results/official"

# 模型路径
declare -A MODEL_PATHS=(
  ["base"]="/mnt/afs_toolcall/sunhao4/models/Qwen3.5-9B"
  ["baseline"]="$ROOT_DIR/eval/.tmp/merged_baseline"
  ["kl"]="$ROOT_DIR/eval/.tmp/merged_kl"
)

# 要评的模型（默认全部，或命令行指定）
if [ $# -gt 0 ]; then
  MODELS=("$@")
else
  MODELS=("base" "baseline" "kl")
fi

# ── 准备 harness ──────────────────────────────────────────────────────────
if [ ! -d "$HARNESS_DIR" ]; then
  echo "❌ harness 不在 $HARNESS_DIR，先 copy："
  echo "  cp -r /mnt/afs_toolcall/juxiaolong1/Projects/claw-eval $HARNESS_DIR"
  exit 1
fi

# config：judge/user_agent 用 luna
cat > "$HARNESS_DIR/config_ours.yaml" <<'EOF'
# 完全官方评测 config：模型走本地 LightLLM serve，judge/user_agent 走 tokenhub luna
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
echo "[eval_official] TOKENHUB_API_KEY 已加载"

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
    --tp 4 --dp 1 --mem_fraction 0.85 \
    --tokenizer_mode fast --tool_call_parser qwen3_coder --reasoning_parser qwen3 \
    --max_req_total_len 131072 --host 0.0.0.0 --port 8000 \
    > "/tmp/serve_${name}.log" 2>&1 &
  local serve_pid=$!
  echo "[$name] serve pid=$serve_pid (tp=4, 4 卡)"

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
    echo "❌ [$name] serve 未就绪，看 /tmp/serve_${name}.log"
    kill $serve_pid 2>/dev/null || true
    return 1
  fi
  echo "[$name] serve 就绪"

  # 跑 batch（tp=4 单 serve，128k 上下文，parallel=10 平衡吞吐与显存）
  echo "===== [$name] 跑官方 batch ====="
  cd "$HARNESS_DIR"
  export PYTHONPATH=src
  python -u -m claw_eval.cli batch \
    --config config_ours.yaml \
    --sandbox-tools \
    --trials 3 \
    --tag general \
    --parallel 10 \
    --trace-dir "$trace_dir"

  # 汇总
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
  if [ ! -d "$model_dir" ]; then
    echo "⚠️  模型目录不存在: $model_dir ($name)，跳过"
    continue
  fi

  trace_dir="/tmp/claw_traces_official_${name}"
  serve_and_run "$name" "$model_dir" "$trace_dir"
done

# ── 汇总对比 ─────────────────────────────────────────────────────────────
echo ""
echo "===== 完全官方评测汇总 ====="
echo "judge = gpt-5.6-luna @ tokenhub"
echo "harness = 官方 claw-eval/claw-eval（mock_services + 完整 audit_data）"
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
