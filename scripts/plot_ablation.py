"""消融实验：每个消融组单独出图。

每张图对比"完整系统"与"去掉该机制"的三项指标：
  coding 得分、方差坍缩步数、评测得分。
论文中每张图下方配一段解释（conclusion 字段）说明该实验证明了什么设计的必要性。

产出: master-thesis/figures/fig_ablation_<slug>.png  (每个消融组一张)
"""
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
full = data[0]                       # 完整系统 = 基线
ablations = data[1:]

FIGDIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "master-thesis", "figures"))

# 英文 slug（文件名用），与消融组一一对应
SLUGS = {
    "去差分驱动奖励": "no_diff_reward",
    "去超采样-淘汰-选组": "no_select",
    "去跨步状态继承": "no_inherit",
    "去失败案例自演化": "no_selfevolve",
}

BLUE = "#1565C0"   # 完整系统
ORANGE = "#E8963A" # 消融组

def plot_one(ab):
    name = ab["name"]
    slug = SLUGS.get(name, name)
    # 三指标: coding得分 / 坍缩步 / 评测得分。坍缩步量纲不同, 用三个子图。
    metrics = [
        ("coding 得分",   full["coding_score"], ab["coding_score"], (0.40, 0.50), "{:.3f}"),
        ("方差坍缩步数",   full["collapse_step"], ab["collapse_step"], (0, 58),     "{:.0f}"),
        ("评测得分",      full["eval_score"],    ab["eval_score"],    (0.34, 0.44), "{:.3f}"),
    ]
    fig, axes = plt.subplots(1, 3, figsize=(11, 4))
    for ax, (title, vfull, vab, ylim, fmt) in zip(axes, metrics):
        bars = ax.bar([0, 1], [vfull, vab], color=[BLUE, ORANGE], width=0.6,
                      edgecolor="white", zorder=3)
        for b, v in zip(bars, [vfull, vab]):
            lbl = fmt.format(v)
            if title == "方差坍缩步数" and v >= 50:
                lbl = "50(稳定)"
            ax.text(b.get_x()+b.get_width()/2, v + (ylim[1]-ylim[0])*0.015, lbl,
                    ha="center", va="bottom", fontsize=11, fontweight="bold")
        ax.set_xticks([0, 1]); ax.set_xticklabels(["完整系统", name], fontsize=10)
        ax.set_ylim(*ylim); ax.set_title(title, fontsize=12)
        ax.grid(axis="y", alpha=0.3, zorder=0)
    fig.suptitle(f"消融：{name}", fontsize=13, fontweight="bold")
    fig.tight_layout(rect=[0, 0, 1, 0.95])
    out = os.path.join(FIGDIR, f"fig_ablation_{slug}_zh.png")
    fig.savefig(out, dpi=185, bbox_inches="tight", facecolor="white")
    plt.close()
    print(f"saved {out}")

for ab in ablations:
    plot_one(ab)
