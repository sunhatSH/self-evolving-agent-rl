"""Draw fig 4.3: Oversample–Eliminate–Select mechanism (English labels, no legend row)."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

BLUE   = "#4A90D9"
GREEN  = "#4CAF50"
GRAY_X = "#C0C0C0"   # eliminated groups
ARROW  = "#777777"
S1_BG  = "#EBF3FB"
S2_BG  = "#EBF3FB"
S3_BG  = "#EDF7EE"
BORDER = "#AAAAAA"
DARK   = "#1A1A2E"
MID    = "#44445A"

fig, ax = plt.subplots(figsize=(15, 7.5), facecolor="white")
ax.set_xlim(0, 1); ax.set_ylim(0, 1)
ax.axis("off")

def rbox(ax, x, y, w, h, fc, ec=BORDER, lw=1.5, ls="-", zorder=1):
    from matplotlib.patches import FancyBboxPatch
    p = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.015",
                       facecolor=fc, edgecolor=ec, linewidth=lw, linestyle=ls, zorder=zorder)
    ax.add_patch(p)

def draw_bars(ax, cx, cy, cols, rows, bw, bh, gx, gy, color, elim=None):
    for r in range(rows):
        for c in range(cols):
            idx = r * cols + c
            x = cx + c * (bw + gx)
            y = cy + r * (bh + gy)
            fc = GRAY_X if (elim and idx in elim) else color
            rect = plt.Rectangle((x, y), bw, bh, facecolor=fc,
                                  edgecolor="white", linewidth=0.5, zorder=3)
            ax.add_patch(rect)
            if elim and idx in elim:
                ax.plot([x+0.003, x+bw-0.003], [y+0.003, y+bh-0.003],
                        color="#888", lw=0.9, zorder=4)
                ax.plot([x+0.003, x+bw-0.003], [y+bh-0.003, y+0.003],
                        color="#888", lw=0.9, zorder=4)

def arrow(ax, x0, y0, x1, y1):
    ax.annotate("", xy=(x1, y1), xytext=(x0, y0),
                arrowprops=dict(arrowstyle="-|>", color=ARROW, lw=2.0,
                                mutation_scale=18))

# ── Stage 1: OVERSAMPLE ────────────────────────────────────────────────────
rbox(ax, 0.01, 0.06, 0.30, 0.87, S1_BG, lw=2, ls="--")
ax.text(0.16, 0.91, "1.  OVERSAMPLE", ha="center", va="top",
        fontsize=15, fontweight="bold", color=DARK)
ax.text(0.16, 0.86, "S = 32 query groups\n(8 trajectories each)", ha="center", va="top",
        fontsize=10.5, color=MID, linespacing=1.5)

draw_bars(ax, cx=0.025, cy=0.09, cols=4, rows=8,
          bw=0.056, bh=0.058, gx=0.009, gy=0.005, color=BLUE)

# ── Arrow 1→2 ─────────────────────────────────────────────────────────────
arrow(ax, 0.32, 0.495, 0.355, 0.495)

# ── Stage 2: ELIMINATE ────────────────────────────────────────────────────
rbox(ax, 0.36, 0.09, 0.29, 0.84, S2_BG, lw=2)
ax.text(0.505, 0.91, "2.  ELIMINATE", ha="center", va="top",
        fontsize=15, fontweight="bold", color=DARK)
ax.text(0.505, 0.865, "R = 30 groups", ha="center", va="top",
        fontsize=11.5, fontweight="bold", color=DARK)
ax.text(0.505, 0.82,
        "Drop groups where\nmax reward < 0.5\nAND in bottom 20%",
        ha="center", va="top", fontsize=9.5, color=MID, linespacing=1.55)

draw_bars(ax, cx=0.375, cy=0.09, cols=4, rows=8,
          bw=0.054, bh=0.054, gx=0.010, gy=0.006,
          color=BLUE, elim={28, 30})

# ── Arrow 2→3 ─────────────────────────────────────────────────────────────
arrow(ax, 0.66, 0.495, 0.695, 0.495)

# ── Stage 3: SELECT ───────────────────────────────────────────────────────
rbox(ax, 0.70, 0.13, 0.255, 0.76, S3_BG, lw=2, ec="#5DAF62")
ax.text(0.8275, 0.87, "3.  SELECT", ha="center", va="top",
        fontsize=15, fontweight="bold", color="#2E7D32")
ax.text(0.8275, 0.82, "N = 16 groups", ha="center", va="top",
        fontsize=11.5, fontweight="bold", color="#2E7D32")
ax.text(0.8275, 0.775,
        "Top N by |advantage|\nmean → GRPO training",
        ha="center", va="top", fontsize=9.5, color=MID, linespacing=1.55)

draw_bars(ax, cx=0.716, cy=0.14, cols=4, rows=4,
          bw=0.047, bh=0.068, gx=0.011, gy=0.011, color=GREEN)

# ── Side note ─────────────────────────────────────────────────────────────
ax.annotate(
    "S shrinks each step:\n32 → 30 → 27 → 26",
    xy=(0.962, 0.49), ha="right", va="center", fontsize=9, color="#555566",
    bbox=dict(boxstyle="round,pad=0.3", facecolor="#F0F4FF",
              edgecolor="#AAAACC", lw=1.0))

plt.tight_layout(pad=0.2)
out = "master-thesis/figures/fig_fig3_oversample_select_zh.png"
plt.savefig(out, dpi=200, bbox_inches="tight", facecolor="white")
plt.close()
print(f"saved {out}")
