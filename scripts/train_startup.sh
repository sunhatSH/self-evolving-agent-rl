#!/usr/bin/env bash
# train_startup.sh — 纯自进化启动实验（128 条冷启动种子，无外部数据补齐兜底）。
#
# 只用 128 条（S=2N=128）初始种子做 step 1 冷启动；step 2 起种子全部由 Questioner
# 从上一步存活组自主生成——数据获取基于交互生成（沙箱交互 + 多智能体协作），验证
# 自进化闭环能在无外部数据兜底下自我维持。config = agent_rl_startup.yaml
# （继承 agent_rl_16gpu.yaml，仅覆盖数据集与步数）。
#
# ⚠️ 长任务必须 tmux/nohup 后台，绝不前台（掉线即被杀，浪费数小时 GPU）：
#     tmux new -d -s startup 'bash scripts/train_startup.sh'
#     tmux attach -t startup
#
# 用法：
#   bash scripts/train_startup.sh                                  # 默认 50 步
#   TOTAL_STEPS=10 bash scripts/train_startup.sh                   # 环境变量改步数
#   bash scripts/train_startup.sh trainer.save_freq=5             # 透传 hydra override
#
# 本脚本是 train_16gpu.sh 的薄封装：同样的 2 节点 × 8 卡拓扑、同样的依赖注入与
# 凭证加载，只是把默认 config 换成 agent_rl_startup.yaml。
set -euo pipefail

DIR="$(cd "$(dirname "$0")" && pwd)"

# 默认走启动实验 config；若首参已指定 config 则尊重之。
CFG="configs/run/agent_rl_startup.yaml"
if [ $# -gt 0 ] && [[ "$1" == *.yaml ]]; then
  CFG="$1"; shift
fi

exec bash "$DIR/train_16gpu.sh" "$CFG" "$@"
