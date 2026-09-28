"""论文矢量配图公共工具：中文字体 + 简约学术风格的 box / arrow 辅助。

参考 example.png 的风格：细线、直角箭头、圆角矩形、克制配色、文字精确。
所有 draw_*.py 复用本模块，保证全书图风格统一。
"""
from __future__ import annotations

import os

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.font_manager import FontProperties, fontManager  # noqa: E402
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch  # noqa: E402

# ── 中文字体：优先用仓库自带 simhei.ttf ──────────────────────────────
_REPO = os.path.join(os.path.dirname(__file__), "..")
_FONT_CANDIDATES = [
    os.path.join(_REPO, "master-thesis", "simhei.ttf"),
    os.path.join(_REPO, "master-thesis", "simsun.ttc"),
]
ZH = None
for _tp in _FONT_CANDIDATES:
    if os.path.exists(_tp):
        fontManager.addfont(_tp)
        ZH = FontProperties(fname=_tp).get_name()
        break
if ZH:
    plt.rcParams["font.sans-serif"] = [ZH]
plt.rcParams["axes.unicode_minus"] = False

# ── 配色（柔和学术风，填充浅、描边深）────────────────────────────────
INK = "#1A1A2E"          # 主文字
SUB = "#555555"          # 次要文字
LINE = "#777777"         # 箭头/连线
PALE = "#DDDDDD"         # 浅边框

# Agent 固定色：Actor=蓝 Observer=绿 Questioner=橙 sandbox=灰 judge=紫 评估器/基建=青
BLUE, BLUE_E = "#E3F0FB", "#4A90D9"
GREEN, GREEN_E = "#E4F3E5", "#4CAF50"
ORANGE, ORANGE_E = "#FDEBD8", "#E8963A"
GRAY, GRAY_E = "#EFEFEF", "#999999"
PURPLE, PURPLE_E = "#EFE6F5", "#8E5BB5"
TEAL, TEAL_E = "#DEF3F1", "#2FA79B"   # 评估器与基建（第四维）


def new_ax(w=12.0, h=6.0, xlim=12.0, ylim=6.0):
    """建一张白底无坐标轴的画布。"""
    fig, ax = plt.subplots(figsize=(w, h), facecolor="white")
    ax.set_xlim(0, xlim)
    ax.set_ylim(0, ylim)
    ax.axis("off")
    return fig, ax


def box(ax, cx, cy, w, h, title, sub="", fc="white", ec=INK,
        tfs=11, sfs=8.3, lw=1.6, bold=True):
    """圆角矩形 + 居中标题（可选副标题）。"""
    p = FancyBboxPatch((cx - w / 2, cy - h / 2), w, h,
                       boxstyle="round,pad=0.04,rounding_size=0.12",
                       facecolor=fc, edgecolor=ec, linewidth=lw, zorder=2)
    ax.add_patch(p)
    fw = "bold" if bold else "normal"
    if sub:
        ax.text(cx, cy + h * 0.16, title, ha="center", va="center",
                fontsize=tfs, fontweight=fw, color=INK, zorder=3)
        ax.text(cx, cy - h * 0.22, sub, ha="center", va="center",
                fontsize=sfs, color=SUB, zorder=3, linespacing=1.3)
    else:
        ax.text(cx, cy, title, ha="center", va="center", fontsize=tfs,
                fontweight=fw, color=INK, zorder=3, linespacing=1.3)
    return p


def arrow(ax, x0, y0, x1, y1, color=LINE, lw=1.8, label="", lcolor=None,
          rad=0.0, dashed=False, lfs=8.5, ldy=0.2):
    """直角/弧线箭头，可带标签。rad!=0 走弧线；dashed 虚线。"""
    style = "arc3,rad=%.2f" % rad
    ap = FancyArrowPatch((x0, y0), (x1, y1), connectionstyle=style,
                         arrowstyle="-|>", mutation_scale=16, lw=lw,
                         color=color, zorder=1,
                         linestyle="--" if dashed else "-")
    ax.add_patch(ap)
    if label:
        ax.text((x0 + x1) / 2, (y0 + y1) / 2 + ldy, label, ha="center",
                va="bottom", fontsize=lfs, color=lcolor or color, zorder=3)


def save(fig, name, dpi=200):
    """存到 assets/ 与 master-thesis/figures/ 两处。"""
    for d in [os.path.join(_REPO, "assets"),
              os.path.join(_REPO, "master-thesis", "figures")]:
        os.makedirs(d, exist_ok=True)
        fig.savefig(os.path.join(d, name), dpi=dpi, bbox_inches="tight",
                    facecolor="white")
    plt.close(fig)
    print("saved", name)
