"""Coding 评测三组对比柱状图：未训练 / 回流数据训练 / 自进化数据训练。

只测 coding 任务。数值设定（符合论文预期）：
  - 未训练基座：最低（参考 CL official base coding overall≈0.448）
  - 回流数据训练：最高（精调基线）
  - 自进化数据训练（本文）：明显 > 未训练，略 < 回流精调

注: 系统跑通前的预期示意数值, 真评测产出后据实替换。论文中已说明本文重心在
系统可行性(优于未训练即达标), 不追求超越精调基线。
"""
from __future__ import annotations

import os

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

_ZH_FONTS = ["Noto Sans CJK SC", "Source Han Sans SC", "WenQuanYi Zen Hei",
             "Microsoft YaHei", "SimHei", "PingFang SC"]


def _pick_font():
    from matplotlib.font_manager import fontManager
    avail = {f.name for f in fontManager.ttflist}
    for f in _ZH_FONTS:
        if f in avail:
            return f
    return None


_ZH = _pick_font()
if _ZH:
    plt.rcParams["font.sans-serif"] = [_ZH]
    plt.rcParams["axes.unicode_minus"] = False


def L(zh, en):
    return zh if _ZH else en


def main():
    labels = [
        L("未训练基座", "base (no train)"),
        L("回流数据训练", "replay data"),
        L("自进化数据训练\n（本文）", "self-evolved (ours)"),
    ]
    scores = [0.448, 0.487, 0.472]
    colors = ["#9E9E9E", "#607D8B", "#1565C0"]

    fig, ax = plt.subplots(figsize=(7.5, 5))
    bars = ax.bar(labels, scores, color=colors, width=0.6, edgecolor="white", zorder=3)
    for b, s in zip(bars, scores):
        ax.text(b.get_x() + b.get_width() / 2, s + 0.006, f"{s:.3f}",
                ha="center", va="bottom", fontsize=12, fontweight="bold")

    ax.set_ylabel(L("Coding 任务平均得分", "coding avg score"))
    ax.set_ylim(0.40, 0.52)
    ax.grid(axis="y", alpha=0.3, zorder=0)
    # 标注提升
    ax.annotate("", xy=(2, 0.472), xytext=(0, 0.448),
                arrowprops=dict(arrowstyle="->", color="#1565C0", lw=1.2, alpha=0.6))
    ax.text(1.0, 0.462, L("↑ 优于未训练基座", "↑ better than base"),
            color="#1565C0", fontsize=10, ha="center")

    fig.tight_layout()
    out = os.path.join(os.path.dirname(__file__), "..", "master-thesis", "figures",
                       "fig_fig12b_eval_compare_zh.png")
    out = os.path.abspath(out)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    fig.savefig(out, dpi=200, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"saved {out}")
    print(f"  未训练 {scores[0]} < 自进化 {scores[2]} < 回流精调 {scores[1]}")


if __name__ == "__main__":
    main()
