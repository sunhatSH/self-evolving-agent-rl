"""图3.x 四类状态在训练轮次间的传递（矢量绘制，参考 example.png 简约风格）。"""
from fig_common import (BLUE, BLUE_E, GRAY, GRAY_E, INK, ORANGE, ORANGE_E,
                        SUB, TEAL, TEAL_E, arrow, box, new_ax, save)

fig, ax = new_ax(w=11, h=6.2, xlim=11, ylim=6.2)

# 两列虚线框：第 t 步 / 第 t+1 步
import matplotlib.patches as mp

for x0, label in [(0.5, "第 $t$ 步"), (7.7, "第 $t{+}1$ 步")]:
    ax.add_patch(mp.FancyBboxPatch((x0, 0.7), 2.8, 4.9,
                 boxstyle="round,pad=0.02,rounding_size=0.1",
                 facecolor="#FAFAFA", edgecolor="#CCCCCC",
                 linewidth=1.2, linestyle="--", zorder=0))
    ax.text(x0 + 1.4, 5.85, label, ha="center", va="center",
            fontsize=12, fontweight="bold", color=INK)

# 四类状态行： (y, 名称, 符号t, 符号t+1, 填充, 描边, 箭头标签)
rows = [
    (4.9, "策略状态", r"$\theta_t$", r"$\theta_{t+1}$", BLUE, BLUE_E, "GRPO 更新"),
    (3.7, "沙箱状态", r"$s_t$", r"$s_{t+1}$", GRAY, GRAY_E, "最优轨迹快照继承"),
    (2.5, "任务状态", r"$Q_t$", r"$Q_{t+1}$", ORANGE, ORANGE_E,
     "提问者再生成（仅 $Q_0$ 为人工种子）"),
    (1.3, "评估器与基建", r"$\Phi_t$", r"$\Phi_{t+1}$", TEAL, TEAL_E,
     "失败案例 $\\mathcal{B}_t$ 归因后演化：模型侧改提示词 / 基建侧补能力"),
]
for y, name, symt, symt1, fc, ec, lab in rows:
    box(ax, 1.9, y, 2.3, 0.85, f"{name}", symt, fc=fc, ec=ec, tfs=10, sfs=11)
    box(ax, 9.1, y, 2.3, 0.85, f"{name}", symt1, fc=fc, ec=ec, tfs=10, sfs=11)
    arrow(ax, 3.15, y, 7.9, y, color=ec, lw=2.0, label=lab, lcolor=SUB, ldy=0.16)

# 第四维强调：底部总结
ax.text(5.5, 0.35,
        "传统强化学习仅演化策略 $\\theta$；本文扩展为 "
        "任务·策略·评估器·基建 四维协同自进化",
        ha="center", va="center", fontsize=9.5, color=TEAL_E, fontweight="bold")

save(fig, "fig_fig_state4_zh.png")
