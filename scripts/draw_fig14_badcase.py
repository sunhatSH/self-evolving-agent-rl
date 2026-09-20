"""绘制图 4.x：失败案例驱动的评估器与基建自演化流程图（清晰横向布局）。"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

_ZH = None
from matplotlib.font_manager import fontManager
for f in ["Noto Sans CJK SC", "Source Han Sans SC", "WenQuanYi Zen Hei", "Microsoft YaHei", "SimHei"]:
    if f in {x.name for x in fontManager.ttflist}:
        _ZH = f; break
if _ZH:
    plt.rcParams["font.sans-serif"] = [_ZH]
    plt.rcParams["axes.unicode_minus"] = False

fig, ax = plt.subplots(figsize=(12, 6), facecolor="white")
ax.set_xlim(0, 12); ax.set_ylim(0, 6); ax.axis("off")

def box(cx, cy, w, h, title, sub, fc, ec, tfs=11):
    p = FancyBboxPatch((cx-w/2, cy-h/2), w, h, boxstyle="round,pad=0.06",
                       facecolor=fc, edgecolor=ec, linewidth=1.8, zorder=2)
    ax.add_patch(p)
    if sub:
        ax.text(cx, cy+0.16, title, ha="center", va="center", fontsize=tfs,
                fontweight="bold", color="#1A1A2E", zorder=3)
        ax.text(cx, cy-0.42, sub, ha="center", va="center", fontsize=8.3,
                color="#555", zorder=3, linespacing=1.35)
    else:
        ax.text(cx, cy, title, ha="center", va="center", fontsize=tfs,
                fontweight="bold", color="#1A1A2E", zorder=3, linespacing=1.35)

def arr(x0, y0, x1, y1, color="#777", label="", lcolor=None, rad=0):
    cs = f"arc3,rad={rad}" if rad else None
    ax.annotate("", xy=(x1, y1), xytext=(x0, y0),
                arrowprops=dict(arrowstyle="-|>", color=color, lw=2,
                                mutation_scale=17, connectionstyle=cs), zorder=1)
    if label:
        ax.text((x0+x1)/2, (y0+y1)/2+0.22, label, ha="center", va="bottom",
                fontsize=8.5, color=lcolor or color)

BLUE="#E3F0FB"; BLUEE="#4A90D9"; GRAY="#EEEEEE"; GRAYE="#999"
PURPLE="#EFE6F5"; PURPLEE="#8E5BB5"
ORANGE="#FDEBD8"; ORANGEE="#E8963A"; GREEN="#E4F3E5"; GREENE="#4CAF50"

# 主链(上半, y=4.4): 收集 → 触发 → 归因
box(1.5, 4.4, 2.4, 1.5, "① 收集失败案例", "执行失败 / 奖励异常 /\n自述与状态差分矛盾", BLUE, BLUEE)
box(4.7, 4.4, 2.2, 1.5, "② 触发", "每 10 步\n或攒够 20 例", GRAY, GRAYE)
box(8.0, 4.4, 2.6, 1.5, "③ 大模型归因", "结合任务意图+轨迹\n+环境证据(非规则)", PURPLE, PURPLEE)
arr(2.7, 4.4, 3.6, 4.4)
arr(5.8, 4.4, 6.7, 4.4)

# 分流(下半): 模型问题 / 基建问题
box(4.2, 1.6, 3.2, 1.5, "模型问题 → 改提示词", "裁判/提问者/执行者\n提示词增量修订", ORANGE, ORANGEE, 10.5)
box(9.4, 1.6, 3.2, 1.5, "基建问题 → 扩展基建", "注册工具/补依赖/\n调超时/修 harness", GREEN, GREENE, 10.5)
arr(7.6, 3.75, 5.0, 2.35, color=ORANGEE, label="模型问题", rad=0.15)
arr(8.4, 3.75, 9.4, 2.35, color=GREENE, label="基建问题", rad=-0.15)

# 回流: 两路演化结果 → 下一轮生效(回到收集)
arr(4.2, 0.85, 1.5, 3.65, color="#3366AA", rad=0.28)
arr(9.4, 0.85, 1.5, 3.65, color="#3366AA", rad=0.42)
ax.text(1.7, 1.9, "更新后\n下一轮生效", ha="center", va="center", fontsize=9,
        color="#3366AA", fontweight="bold", linespacing=1.3)

ax.text(6.0, 5.55, "失败案例驱动的评估器与基建自演化", ha="center", va="center",
        fontsize=13, fontweight="bold", color="#1A1A2E")

plt.tight_layout(pad=0.3)
out = "master-thesis/figures/fig_fig14_badcase_evolve_zh.png"
plt.savefig(out, dpi=185, bbox_inches="tight", facecolor="white")
plt.close()
print(f"saved {out} (zh={_ZH})")
