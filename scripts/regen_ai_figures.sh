#!/usr/bin/env bash
# 用新模型(sunburst/openai_L)重生 13 张 AI 概念示意图。
# 严禁碰的图(matplotlib 真数据/矢量, 不在此列):
#   fig3, fig9, fig10, fig11, fig12, fig12b, fig14, ablation_*
set -uo pipefail
cd "$(dirname "${BASH_SOURCE[0]}")/.."   # repo root
PY=/mnt/afs_toolcall/sunhao4/miniconda3/bin/python3
set -a; source .env; set +a

# 英文源图: 需 gen 英文 → translate 汉化
EN_KEYS="fig1_architecture fig4_self_evolve_loop fig5_diff_reward fig6_sandbox_inherit \
fig7_sequence fig8_react_loop fig16_multiagent fig17_stability fig18_sandbox_env \
fig19_async_schedule fig20_decouple fig21_data_pipeline"

# 中文直生图: 只 gen(已在试片生成, 用 --force 确保是新风格)
ZH_KEYS="fig2_dataflow_zh fig_state4_zh"

echo "########## STEP 1: 生成英文源图 ##########"
$PY scripts/gen_thesis_figures.py --force --only $EN_KEYS 2>&1

echo "########## STEP 2: 生成中文直生图 ##########"
$PY scripts/gen_thesis_figures.py --force --only $ZH_KEYS 2>&1

echo "########## STEP 3: 汉化英文源图 ##########"
TR_ARGS=""
for k in $EN_KEYS; do TR_ARGS="$TR_ARGS fig_${k}.png"; done
$PY scripts/translate_figures_zh.py --force --only $TR_ARGS 2>&1

echo "########## STEP 4: 拷贝 _zh 到 master-thesis/figures/ ##########"
n=0
for k in $EN_KEYS $ZH_KEYS; do
  # 英文源汉化后是 fig_<k>_zh.png; 中文直生本身就是 fig_<k>.png(已含_zh)
  src="assets/fig_${k}_zh.png"
  [[ "$k" == *_zh ]] && src="assets/fig_${k}.png"
  if [[ -s "$src" ]]; then
    cp "$src" master-thesis/figures/ && { echo "  copied $(basename $src)"; ((n++)); }
  else
    echo "  !! MISSING $src"
  fi
done
echo "########## ALL DONE: copied $n figures ##########"
