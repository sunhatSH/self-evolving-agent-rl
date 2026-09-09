#!/usr/bin/env bash
# ─────────────────────────────────────────────────────────────────────────────
# 统一评测脚本：对一组模型跑 ClawEval 195 题 + 聚合，结果按 <模型名>-<时间> 分目录。
#
# 用法：
#   bash scripts/eval_all.sh
#   GPU_MODE=4gpu bash scripts/eval_all.sh          # 4 卡评测（本机 debug）
#   NUM_RUNS=1 bash scripts/eval_all.sh             # Pass^1（快，debug 用）
#   MODELS_OVERRIDE="base,cl2r_baseline_step75" bash scripts/eval_all.sh  # 只评子集
#
# ★ 开头 MODELS 数组定义要评的模型。每项格式：
#   "<output_name>|<model_path>"
#   - output_name: 结果目录名（eval/results/<output_name>-<时间>/），也是对比图标签
#   - model_path:  HF 格式模型路径。若是 FSDP ckpt（ckpts/.../global_step_N/actor），
#                  脚本会先 merge 成 HF 再评（merge 到 /tmp/merged_hf_<output_name>）
#
# GPU 规模（env）：
#   GPU_MODE=4gpu（本机 debug，默认）/ 16gpu（集群）
#
# 输出：eval/results/<output_name>-<时间戳>/
#   per_task.json  — 每题四维打分
#   scores.json    — 聚合：pass@N / 均分 / 按桶 / 与 base 对比
# 评测结束后在 eval/results/ 生成 comparison.json + comparison_reward.png（多模型对比）。
# ─────────────────────────────────────────────────────────────────────────────
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT_DIR"

# ── ★ 要评测的模型列表（格式：<输出名>|<模型路径>）──────────────────────────
# FSDP ckpt 会自动 merge；HF 目录直接用。
MODELS=(
  "base|/mnt/afs_toolcall/sunhao4/models/Qwen3.5-9B"
  "cl2r_baseline_step100|ckpts/cl2r_baseline/global_step_100/actor"
  "cl2r_kl_step100|ckpts/cl2r_kl/global_step_100/actor"
)
# ─────────────────────────────────────────────────────────────────────────────

# 允许 env 覆盖（逗号分隔的 output_name 子集）
if [ -n "${MODELS_OVERRIDE:-}" ]; then
  IFS=',' read -ra _filt <<< "$MODELS_OVERRIDE"
  _filtered=()
  for entry in "${MODELS[@]}"; do
    _name="${entry%%|*}"
    for f in "${_filt[@]}"; do
      if [ "$_name" = "$f" ]; then _filtered+=("$entry"); break; fi
    done
  done
  MODELS=("${_filtered[@]}")
fi

NUM_RUNS="${NUM_RUNS:-3}"
GPU_MODE="${GPU_MODE:-4gpu}"   # 本机 debug 默认 4 卡；集群设 GPU_MODE=16gpu
PY="/opt/conda/bin/python"

# 时间戳（YYYYMMDD-HHMMSS），所有模型共用同一时间戳便于横向对比
STAMP="$(date +%Y%m%d-%H%M%S)"

echo "=== eval_all: ${#MODELS[@]} 个模型, GPU_MODE=$GPU_MODE, Pass^$NUM_RUNS, stamp=$STAMP ==="
for m in "${MODELS[@]}"; do echo "  - $m"; done
echo

# 逐个评测
declare -a OUT_NAMES=()
for entry in "${MODELS[@]}"; do
  out_name="${entry%%|*}"
  model_path="${entry#*|}"
  out_dir_name="${out_name}-${STAMP}"
  OUT_NAMES+=("$out_dir_name")

  # FSDP ckpt → 先 merge 成 HF
  if [ -d "$model_path" ] && ls "$model_path"/extra_state_world_size_*.pt >/dev/null 2>&1; then
    merged="/tmp/merged_hf_${out_name}"
    echo "=== [$out_name] merge FSDP → HF: $model_path → $merged ==="
    rm -rf "$merged"
    VERL_DIR="/mnt/afs_toolcall/sunhao4/dependencies/verl"
    PYTHONPATH="$VERL_DIR" "$PY" -m verl.model_merger merge \
      --backend fsdp --local_dir "$model_path" --target_dir "$merged"
    model_path="$merged"
  fi

  echo "=== [$out_name] 评测: $model_path → eval/results/$out_dir_name ==="
  GPU_MODE="$GPU_MODE" bash scripts/eval_model.sh "$model_path" "$out_dir_name" "$NUM_RUNS"
  echo
done

# ── 多模型对比图 ────────────────────────────────────────────────────────────
echo "=== 生成对比图 ==="
NAMES_STR="${OUT_NAMES[*]}"
"$PY" - "$NAMES_STR" <<'PYEOF'
import json, os, sys
from pathlib import Path

results_dir = Path("eval/results")
names = sys.argv[1].split()

data = {}
for n in names:
    sf = results_dir / n / "scores.json"
    if sf.exists():
        with open(sf) as f:
            d = json.load(f)
        data[n] = d

# 写对比 JSON
out = results_dir / "comparison.json"
with open(out, "w") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
print(f"  对比 JSON: {out}")

# 画图（总分 + 按桶）
try:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    import numpy as np

    labels = list(data.keys())

    # 总分对比
    fig, ax = plt.subplots(figsize=(10, 5))
    means = []
    for n in labels:
        d = data[n]
        m = d.get("mean_reward")
        if m is None:
            m = d.get("overall", {}).get("mean_reward", 0)
        means.append(m)
    ax.bar(labels, means)
    ax.set_ylabel("mean reward")
    ax.set_title("ClawEval mean reward comparison")
    plt.xticks(rotation=20, ha="right")
    plt.tight_layout()
    pf = results_dir / "comparison_reward.png"
    plt.savefig(pf, dpi=120)
    print(f"  对比图: {pf}")
    plt.close()

    # 按桶对比（如有 per-bucket 数据）
    buckets = set()
    for n in labels:
        buckets.update(data[n].get("per_bucket", {}).get("buckets", {}).keys())
    if buckets:
        fig, ax = plt.subplots(figsize=(12, 5))
        x = np.arange(len(buckets))
        w = 0.8 / max(len(labels), 1)
        for i, n in enumerate(labels):
            pb = data[n].get("per_bucket", {}).get("buckets", {})
            vals = [pb.get(b, {}).get("mean_reward", 0) for b in sorted(buckets)]
            ax.bar(x + i * w, vals, w, label=n)
        ax.set_xticks(x + w * (len(labels) - 1) / 2)
        ax.set_xticklabels(sorted(buckets), rotation=30, ha="right")
        ax.set_ylabel("mean reward")
        ax.set_title("ClawEval per-bucket reward")
        ax.legend()
        plt.tight_layout()
        pf2 = results_dir / "comparison_per_bucket.png"
        plt.savefig(pf2, dpi=120)
        print(f"  按桶图: {pf2}")
        plt.close()
except Exception as e:
    print(f"  画图跳过: {e}")
PYEOF

echo
echo "✅ 全部评测完成。结果: eval/results/<model_name>-${STAMP}/"
echo "   对比: eval/results/comparison.json + comparison_reward.png"
