"""绘制图 4.4：超采样—淘汰—选组机制（中文标签）。

不写死具体组数（S/R/N 随卡数/拓扑而变，如 16 卡与 64 卡不同）：
每阶段用符号 S/R/N 标注，柱阵在组与组之间插入省略号 ⋯，表示"中间省略若干组"。
"""
import os

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.font_manager import FontProperties, fontManager  # noqa: E402

# 中文字体：优先用仓库自带 simhei.ttf
_ZH = None
_REPO = os.path.join(os.path.dirname(__file__), "..")
_TTF = os.path.join(_REPO, "master-thesis", "simhei.ttf")
if os.path.exists(_TTF):
    fontManager.addfont(_TTF)
    _ZH = FontProperties(fname=_TTF).get_name()
if _ZH:
    plt.rcParams["font.sans-serif"] = [_ZH]
plt.rcParams["axes.unicode_minus"] = False

BLUE = "#4A90D9"
GREEN = "#4CAF50"
GRAY_X = "#C0C0C0"   # 被淘汰的组
ARROW = "#777777"
S1_BG = "#EBF3FB"
S2_BG = "#EBF3FB"
S3_BG = "#EDF7EE"
BORDER = "#AAAAAA"
DARK = "#1A1A2E"
MID = "#44445A"

fig, ax = plt.subplots(figsize=(15, 7.5), facecolor="white")
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis("off")


def rbox(ax, x, y, w, h, fc, ec=BORDER, lw=1.5, ls="-", zorder=1):
    from matplotlib.patches import FancyBboxPatch
    p = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.015",
                       facecolor=fc, edgecolor=ec, linewidth=lw, linestyle=ls, zorder=zorder)
    ax.add_patch(p)


def draw_bars(ax, cx, cy, cols, rows, bw, bh, gx, gy, color, elim=None, ellipsis_row=None):
    """画 rows×cols 柱阵，每个柱=一个组。

    ellipsis_row: 指定某一行不画柱子，改在该行整行位置画横排省略号 ⋯，
    表示"这里省略了若干组"（省略号位于上下两批组之间）。
    """
    for r in range(rows):
        y = cy + r * (bh + gy)
        if r == ellipsis_row:
            # 该行不画组，改画横排省略号（用散点画三个圆点，避免字体缺 ⋯ 字形），
            # 位于上下两批组之间，表示"这里省略了若干组"。
            span_x0 = cx
            span_x1 = cx + (cols - 1) * (bw + gx) + bw
            xc = (span_x0 + span_x1) / 2
            yc = y + bh / 2
            dot_dx = bw * 0.5
            for off in (-dot_dx, 0.0, dot_dx):
                ax.plot(xc + off, yc, marker="o", markersize=5,
                        color="#8899AA", zorder=3)
            continue
        for c in range(cols):
            idx = r * cols + c
            x = cx + c * (bw + gx)
            fc = GRAY_X if (elim and idx in elim) else color
            rect = plt.Rectangle((x, y), bw, bh, facecolor=fc,
                                  edgecolor="white", linewidth=0.5, zorder=3)
            ax.add_patch(rect)
            if elim and idx in elim:
                ax.plot([x + 0.003, x + bw - 0.003], [y + 0.003, y + bh - 0.003],
                        color="#888", lw=0.9, zorder=4)
                ax.plot([x + 0.003, x + bw - 0.003], [y + bh - 0.003, y + 0.003],
                        color="#888", lw=0.9, zorder=4)


def arrow(ax, x0, y0, x1, y1):
    ax.annotate("", xy=(x1, y1), xytext=(x0, y0),
                arrowprops=dict(arrowstyle="-|>", color=ARROW, lw=2.0, mutation_scale=18))


# ── 阶段1：超采样 ───────────────────────────────────────────────────────────
rbox(ax, 0.01, 0.06, 0.30, 0.87, S1_BG, lw=2, ls="--")
ax.text(0.16, 0.91, "① 超采样", ha="center", va="top",
        fontsize=16, fontweight="bold", color=DARK)
ax.text(0.16, 0.855, "S 个查询组\n（每组 n 条轨迹）", ha="center", va="top",
        fontsize=11, color=MID, linespacing=1.6)
# 5 行，第 2 行(索引2)为省略号：上下各若干组，中间省略
draw_bars(ax, cx=0.025, cy=0.09, cols=4, rows=5,
          bw=0.056, bh=0.058, gx=0.009, gy=0.006, color=BLUE, ellipsis_row=2)

arrow(ax, 0.32, 0.495, 0.355, 0.495)

# ── 阶段2：淘汰 ─────────────────────────────────────────────────────────────
rbox(ax, 0.36, 0.09, 0.29, 0.84, S2_BG, lw=2)
ax.text(0.505, 0.91, "② 淘汰", ha="center", va="top",
        fontsize=16, fontweight="bold", color=DARK)
ax.text(0.505, 0.855, "S → R 组", ha="center", va="top",
        fontsize=12, fontweight="bold", color=DARK)
ax.text(0.505, 0.81,
        "丢弃组内最优奖励\n同时满足「后 20%」\n且「低于 0.5」的组",
        ha="center", va="top", fontsize=10, color=MID, linespacing=1.6)
draw_bars(ax, cx=0.375, cy=0.09, cols=4, rows=5,
          bw=0.054, bh=0.054, gx=0.010, gy=0.007,
          color=BLUE, elim={12, 3}, ellipsis_row=2)

arrow(ax, 0.66, 0.495, 0.695, 0.495)

# ── 阶段3：选组 ─────────────────────────────────────────────────────────────
rbox(ax, 0.70, 0.13, 0.255, 0.76, S3_BG, lw=2, ec="#5DAF62")
ax.text(0.8275, 0.87, "③ 选组", ha="center", va="top",
        fontsize=16, fontweight="bold", color="#2E7D32")
ax.text(0.8275, 0.815, "R → N 组", ha="center", va="top",
        fontsize=12, fontweight="bold", color="#2E7D32")
ax.text(0.8275, 0.77,
        "按组内优势绝对值\n均值取前 N 组\n→ 送入 GRPO 训练",
        ha="center", va="top", fontsize=10, color=MID, linespacing=1.6)
# 3 行，中间行(索引1)省略号
draw_bars(ax, cx=0.716, cy=0.15, cols=4, rows=3,
          bw=0.047, bh=0.062, gx=0.011, gy=0.014, color=GREEN, ellipsis_row=1)

# ── 侧注 ────────────────────────────────────────────────────────────────────
ax.annotate(
    "每步满足 S ≥ R ≥ N；\n具体组数随 GPU\n拓扑而变",
    xy=(0.962, 0.49), ha="right", va="center", fontsize=9.5, color="#555566",
    fontproperties=FontProperties(fname=_TTF) if _ZH else None,
    bbox=dict(boxstyle="round,pad=0.3", facecolor="#F0F4FF", edgecolor="#AAAACC", lw=1.0))

plt.tight_layout(pad=0.2)
out = os.path.join(_REPO, "master-thesis/figures/fig_fig3_oversample_select_zh.png")
plt.savefig(out, dpi=200, bbox_inches="tight", facecolor="white")
plt.close()
print(f"saved {out}")
