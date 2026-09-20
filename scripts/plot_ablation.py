"""消融实验双指标对比图：coding 得分 + 方差坍缩步数。"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import json, os, numpy as np

_ZH = None
from matplotlib.font_manager import fontManager
for f in ["Noto Sans CJK SC","Source Han Sans SC","WenQuanYi Zen Hei","Microsoft YaHei","SimHei"]:
    if f in {x.name for x in fontManager.ttflist}: _ZH=f; break
if _ZH: plt.rcParams["font.sans-serif"]=[_ZH]; plt.rcParams["axes.unicode_minus"]=False

src = os.path.join(os.path.dirname(__file__), "..", "logs", "metrics", "ablation_results.json")
data = json.load(open(os.path.abspath(src)))

names    = [d["name"] for d in data]
scores   = [d["coding_score"] for d in data]
colsteps = [d["collapse_step"] for d in data]

BLUE="#1565C0"; GRAY="#90A4AE"; RED="#C62828"; ORANGE="#E65100"
colors = [BLUE] + [GRAY]*5 + [RED]  # 完整系统=蓝，去监控=红，其余=灰

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5.5))

x = np.arange(len(names))
w = 0.6

# ── 左: coding 得分 ──
bars = ax1.bar(x, scores, color=colors, width=w, edgecolor="white", zorder=3)
for b, s in zip(bars, scores):
    ax1.text(b.get_x()+b.get_width()/2, s+0.002, f"{s:.3f}",
             ha="center", va="bottom", fontsize=9, fontweight="bold")
ax1.set_xticks(x); ax1.set_xticklabels(names, rotation=25, ha="right", fontsize=9.5)
ax1.set_ylabel("Coding 任务平均得分"); ax1.set_ylim(0.40, 0.50)
ax1.set_title("（a）各消融组 Coding 得分", fontsize=12)
ax1.grid(axis="y", alpha=0.3, zorder=0)
ax1.axhline(scores[0], color=BLUE, lw=1.2, ls="--", alpha=0.5, zorder=2)

# ── 右: 坍缩步数 ──
bars2 = ax2.bar(x, colsteps, color=colors, width=w, edgecolor="white", zorder=3)
for b, s in zip(bars2, colsteps):
    label = str(s) if s < 50 else "50(稳定)"
    ax2.text(b.get_x()+b.get_width()/2, s+0.5, label,
             ha="center", va="bottom", fontsize=9, fontweight="bold")
ax2.set_xticks(x); ax2.set_xticklabels(names, rotation=25, ha="right", fontsize=9.5)
ax2.set_ylabel("方差坍缩步数（首次触及阈值，50=未触发）")
ax2.set_ylim(0, 58)
ax2.set_title("（b）各消融组方差坍缩步数", fontsize=12)
ax2.grid(axis="y", alpha=0.3, zorder=0)
ax2.axhline(50, color=BLUE, lw=1.2, ls="--", alpha=0.5, zorder=2)

fig.tight_layout(pad=2.0)
out = os.path.join(os.path.dirname(__file__), "..", "master-thesis", "figures",
                   "fig_fig15_ablation_zh.png")
out = os.path.abspath(out)
fig.savefig(out, dpi=185, bbox_inches="tight", facecolor="white")
plt.close()
print(f"saved {out}")
