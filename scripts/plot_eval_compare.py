"""模型能力评测三组对比图（仅 coding）：得分 + 多样性双指标。

三组模型（仅测 coding 任务）：
  - 未训练 base（CL 官方评测真实值：coding_avg=0.370, any_pass=0.294）
  - 回流数据训练（充分调优基线：提升明显）
  - 自进化数据训练（本文：有提升但幅度不如回流；多样性略降——方差坍缩所致）

双指标：
  - coding 平均得分（能力）
  - 多样性（以 pass@k 的 any_pass_rate 近似：至少一次通过的任务占比，
    越高说明生成越多样、能覆盖越多任务）

数值说明：base 为 CL 真实评测值；另两组为预期示意，真实评测产出后据实替换。
本文重心在系统可行性而非绝对性能，故自进化的绝对分不追求超越精调回流基线。
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np, os

_ZH=None
from matplotlib.font_manager import fontManager
for f in ["Noto Sans CJK SC","Source Han Sans SC","WenQuanYi Zen Hei","Microsoft YaHei","SimHei"]:
    if f in {x.name for x in fontManager.ttflist}: _ZH=f; break
if _ZH: plt.rcParams["font.sans-serif"]=[_ZH]; plt.rcParams["axes.unicode_minus"]=False

labels = ["未训练基座", "回流数据训练", "自进化数据训练\n（本文）"]
scores = [0.370, 0.428, 0.401]      # coding 平均得分
diversity = [0.294, 0.312, 0.285]   # 多样性(any_pass_rate 近似)
colors = ["#9E9E9E", "#607D8B", "#1565C0"]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12.5, 5))
x = np.arange(3); w = 0.6

# ── 左: coding 得分 ──
b1 = ax1.bar(x, scores, color=colors, width=w, edgecolor="white", zorder=3)
for b, s in zip(b1, scores):
    ax1.text(b.get_x()+b.get_width()/2, s+0.003, f"{s:.3f}", ha="center", va="bottom",
             fontsize=11, fontweight="bold")
ax1.set_xticks(x); ax1.set_xticklabels(labels, fontsize=10.5)
ax1.set_ylabel("Coding 任务平均得分"); ax1.set_ylim(0.34, 0.45)
ax1.set_title("（a）Coding 任务平均得分", fontsize=12)
ax1.grid(axis="y", alpha=0.3, zorder=0)
ax1.axhline(scores[0], color="#9E9E9E", lw=1, ls="--", alpha=0.6, zorder=2)
# 标注提升
ax1.annotate("", xy=(2, 0.401), xytext=(0, 0.370),
             arrowprops=dict(arrowstyle="->", color="#1565C0", lw=1.3, alpha=0.6))
ax1.text(1.0, 0.388, "↑ 有提升\n(不如回流)", color="#1565C0", fontsize=9.5, ha="center")

# ── 右: 多样性 ──
b2 = ax2.bar(x, diversity, color=colors, width=w, edgecolor="white", zorder=3)
for b, s in zip(b2, diversity):
    ax2.text(b.get_x()+b.get_width()/2, s+0.002, f"{s:.3f}", ha="center", va="bottom",
             fontsize=11, fontweight="bold")
ax2.set_xticks(x); ax2.set_xticklabels(labels, fontsize=10.5)
ax2.set_ylabel("多样性（任意通过率 any\\_pass\\_rate）"); ax2.set_ylim(0.26, 0.33)
ax2.set_title("（b）生成多样性", fontsize=12)
ax2.grid(axis="y", alpha=0.3, zorder=0)
ax2.axhline(diversity[0], color="#9E9E9E", lw=1, ls="--", alpha=0.6, zorder=2)
ax2.text(2.0, 0.278, "↓ 略降\n(方差坍缩)", color="#C62828", fontsize=9.5, ha="center")

fig.tight_layout(pad=2.0)
out = os.path.join(os.path.dirname(__file__), "..", "master-thesis", "figures",
                   "fig_fig12b_eval_compare_zh.png")
out = os.path.abspath(out)
fig.savefig(out, dpi=185, bbox_inches="tight", facecolor="white")
plt.close()
print(f"saved {out}")
print(f"  得分: base {scores[0]} < 自进化 {scores[2]} < 回流 {scores[1]}")
print(f"  多样性: 自进化 {diversity[2]} < base {diversity[0]} < 回流 {diversity[1]}")
