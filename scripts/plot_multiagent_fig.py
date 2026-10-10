"""重绘图 4.6：多智能体协作机制（三智能体 + 裁判评估模块）。

本文系统含执行者／观察者／提问者三个协同智能体；裁判为独立于三者的外部评估模块，
不计入智能体，故图中只对三个智能体编号。本脚本以 matplotlib 确定性重绘：
  ① 执行者（蓝，被训练策略）→ ② 观察者（绿，确定性取证）
                            ├→ 裁判（青，冻结评估模块，据差分评分 → 奖励）
                            └→ ③ 提问者（橙，人设驱动 → 下一轮任务，回灌执行者）

产出: master-thesis/figures/fig_fig16_multiagent_zh.png
"""
import os

import matplotlib

matplotlib.use("Agg")
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
from matplotlib.font_manager import fontManager
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

_ZH = None
for f in ["Noto Sans CJK SC", "Source Han Sans SC", "WenQuanYi Zen Hei", "SimHei", "Arial Unicode MS"]:
    if f in {x.name for x in fontManager.ttflist}:
        _ZH = f
        break
if _ZH:
    plt.rcParams["font.sans-serif"] = [_ZH]
    plt.rcParams["axes.unicode_minus"] = False

# 配色：执行者=蓝 观察者=绿 提问者=橙 裁判/评估=青 沙箱=浅灰
BLUE, BLUE_L = "#1565C0", "#E3F2FD"
GREEN, GREEN_L = "#2E7D32", "#E8F5E9"
ORANGE, ORANGE_L = "#E65100", "#FFF3E0"
TEAL, TEAL_L = "#00695C", "#E0F2F1"
GRAY, GRAY_L = "#78909C", "#F5F5F5"
INK = "#263238"

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
OUT = os.path.join(ROOT, "master-thesis", "figures", "fig_fig16_multiagent_zh.png")

fig, ax = plt.subplots(figsize=(13.2, 7.4))
ax.set_xlim(0, 132)
ax.set_ylim(0, 74)
ax.axis("off")


def box(x, y, w, h, fc, ec, lw=1.6, r=1.6, z=2, ls="-"):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle=f"round,pad=0,rounding_size={r}",
                                facecolor=fc, edgecolor=ec, linewidth=lw, zorder=z,
                                linestyle=ls))


def txt(x, y, s, size=10, color=INK, weight="normal", ha="center", va="center", z=5):
    ax.text(x, y, s, fontsize=size, color=color, fontweight=weight,
            ha=ha, va=va, zorder=z)


def arrow(x1, y1, x2, y2, color=GRAY, lw=1.8, style="-|>", rad=0.0, z=3, ls="-"):
    ax.add_patch(FancyArrowPatch((x1, y1), (x2, y2),
                                 connectionstyle=f"arc3,rad={rad}",
                                 arrowstyle=style, mutation_scale=15,
                                 color=color, linewidth=lw, zorder=z, linestyle=ls))


# ════════ 沙箱外框（含执行者）════════
box(3, 20, 38, 46, GRAY_L, GRAY, lw=1.8, r=2)
txt(22, 63.2, "代码沙箱（隔离执行环境）", 10.5, GRAY, "bold")

# 执行者
box(6, 36, 32, 24, BLUE_L, BLUE, lw=1.8)
txt(22, 57.2, "① 执行者 Actor", 11.5, BLUE, "bold")
txt(22, 54.0, "被训练策略 $\\pi_\\theta$（唯一参与 GRPO 更新）", 8.8, BLUE)

# ReAct 循环三步
for i, (lbl, dx) in enumerate([("思考", 0), ("调用工具", 10.6), ("观察", 21.2)]):
    box(8.2 + dx, 44.5, 9.2, 5.6, "white", BLUE, lw=1.2, r=1.0)
    txt(12.8 + dx, 47.3, lbl, 9.2, BLUE)
    if i < 2:
        arrow(17.4 + dx, 47.3, 18.6 + dx, 47.3, BLUE, 1.3, "-|>")
# 回环箭头
arrow(29.4, 43.9, 12.8, 43.9, BLUE, 1.2, "-|>", rad=0.38)
txt(21, 40.3, "ReAct 多步循环", 8.5, BLUE)

# 可用工具
box(6, 23, 32, 10, "white", GRAY, lw=1.2, r=1.0)
txt(22, 30.6, "可用工具", 8.8, GRAY, "bold")
for lbl, dx in [("终端", 0), ("Python", 10.6), ("文件操作", 21.2)]:
    box(8.2 + dx, 24.4, 9.2, 4.4, GRAY_L, GRAY, lw=1.0, r=0.8)
    txt(12.8 + dx, 26.6, lbl, 8.5, INK)

# 执行者 → 观察者
arrow(41.3, 48, 50.2, 48, GRAY, 2.0)
txt(45.7, 50.4, "交互轨迹 $\\tau$", 9.2, INK)

# ════════ 观察者 ════════
box(50.5, 24, 30, 42, GREEN_L, GREEN, lw=1.8, r=2)
txt(65.5, 63.2, "② 观察者 Observer", 11.5, GREEN, "bold")
txt(65.5, 60.2, "权重冻结，仅采信环境证据", 8.8, GREEN)

# 前后快照
box(52.5, 51, 12.6, 6.2, "white", GREEN, lw=1.2, r=1.0)
txt(58.8, 54.1, "执行前快照", 9.0, INK)
box(66.4, 51, 12.6, 6.2, "white", GREEN, lw=1.2, r=1.0)
txt(72.7, 54.1, "执行后快照", 9.0, INK)
arrow(58.8, 50.4, 63.6, 46.6, GREEN, 1.3)
arrow(72.7, 50.4, 67.9, 46.6, GREEN, 1.3)

# 差分
box(52.5, 37.4, 26.5, 8.6, "white", GREEN, lw=1.5, r=1.0)
txt(65.7, 43.4, "确定性状态差分", 10.0, GREEN, "bold")
txt(65.7, 40.1, "文件系统变更（含内容）+ 系统状态变更", 8.3, INK)

# 客观状态报告
box(52.5, 27, 26.5, 7.4, "white", GREEN, lw=1.5, r=1.0, ls="--")
txt(65.7, 30.7, "客观状态报告", 9.8, GREEN, "bold")

arrow(65.7, 37.0, 65.7, 34.8, GREEN, 1.5)

# ════════ 裁判（评估模块，非智能体）════════
box(89, 42, 39, 24, TEAL_L, TEAL, lw=1.8, r=2, ls="--")
txt(108.5, 63.2, "裁判 Reward Judge", 11.5, TEAL, "bold")
txt(108.5, 60.2, "外部冻结评估模块（不计入智能体），独立于被训练策略", 8.3, TEAL)

box(91, 50.6, 35, 7.4, "white", TEAL, lw=1.3, r=1.0)
txt(108.5, 56.2, "以状态差分为评分证据", 9.5, TEAL, "bold")
txt(108.5, 52.9, "自述仅作交叉核对，矛盾时以差分为准", 8.2, INK)

box(91, 44, 35, 5.4, TEAL, TEAL, lw=0, r=1.0)
txt(108.5, 46.7, "奖励 $r$ → GRPO 策略更新", 9.8, "white", "bold")

# 差分 → 裁判
arrow(79.3, 43.5, 88.7, 50.5, TEAL, 2.0, rad=-0.12)
txt(84.6, 48.9, "差分证据", 8.8, TEAL)

# ════════ 提问者 ════════
box(89, 12, 39, 24, ORANGE_L, ORANGE, lw=1.8, r=2)
txt(108.5, 33.2, "③ 提问者 Questioner", 11.5, ORANGE, "bold")
txt(108.5, 30.2, "人设驱动的模拟用户（42 个人设随机抽取）", 8.5, ORANGE)

box(91, 21.4, 35, 6.6, "white", ORANGE, lw=1.3, r=1.0)
txt(108.5, 24.7, "读取客观状态报告 + 执行概括", 9.3, INK)

box(91, 14.2, 35, 5.4, ORANGE, ORANGE, lw=0, r=1.0)
txt(108.5, 16.9, "生成下一轮追问任务", 9.8, "white", "bold")

# 报告 → 提问者
arrow(79.3, 30.2, 88.7, 25.2, ORANGE, 2.0, rad=0.12)
txt(84.3, 29.3, "追问依据", 8.8, ORANGE)

# ════════ 回灌执行者 ════════
arrow(95, 13.6, 22, 19.4, ORANGE, 2.0, rad=0.16)
txt(58, 8.6, "作为下一轮任务输入（沙箱状态跨步继承）", 9.5, ORANGE, "bold")

# ════════ 图例 ════════
leg = [mpatches.Patch(facecolor=BLUE_L, edgecolor=BLUE, label="执行者（训练对象）"),
       mpatches.Patch(facecolor=GREEN_L, edgecolor=GREEN, label="观察者（取证）"),
       mpatches.Patch(facecolor=TEAL_L, edgecolor=TEAL, label="裁判（评估模块）"),
       mpatches.Patch(facecolor=ORANGE_L, edgecolor=ORANGE, label="提问者（追问）")]
ax.legend(handles=leg, loc="lower left", bbox_to_anchor=(0.005, 0.005),
          fontsize=8.8, ncol=1, framealpha=0.95, edgecolor="#CCC")

txt(66, 70.6, "一次采样的完整回路：提问 → 求解 → 取证 → 评分 → 再提问", 12, INK, "bold")

fig.tight_layout(pad=0.4)
fig.savefig(OUT, dpi=200, bbox_inches="tight", facecolor="white")
plt.close(fig)
print(f"saved {OUT}")
