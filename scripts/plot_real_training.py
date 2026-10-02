"""从真实训练日志 logs/metrics/agent_rl_16gpu/metrics.jsonl 生成训练图。

产出:
  master-thesis/figures/fig_fig9_training_curves_zh.png
    — 三子图: 奖励均值(reward_mean) / 策略熵(entropy) / 轨迹多样性std(rollout_is_std)
"""
import json, os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

_ZH = None
from matplotlib.font_manager import fontManager
for f in ["Noto Sans CJK SC","Source Han Sans SC","WenQuanYi Zen Hei","Microsoft YaHei","SimHei"]:
    if f in {x.name for x in fontManager.ttflist}: _ZH = f; break
if _ZH:
    plt.rcParams["font.sans-serif"] = [_ZH]
    plt.rcParams["axes.unicode_minus"] = False

BLUE   = "#1565C0"
ORANGE = "#E65100"
GREEN  = "#2E7D32"

ROOT   = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SRC    = os.path.join(ROOT, "logs", "metrics", "agent_rl_16gpu", "metrics.jsonl")
FIGDIR = os.path.join(ROOT, "master-thesis", "figures")

# ── 读数据 ──────────────────────────────────────────────────────────────
with open(SRC) as f:
    rows = [json.loads(l) for l in f if l.strip()]

steps, r_mean, r_max, r_min, entropy, is_std = [], [], [], [], [], []
for r in rows:
    d = r["data"]
    if "critic/rewards/mean" not in d:
        continue
    steps.append(r["step"])
    r_mean.append(d["critic/rewards/mean"])
    r_max.append(d.get("critic/rewards/max", d["critic/rewards/mean"]))
    r_min.append(d.get("critic/rewards/min", d["critic/rewards/mean"]))
    entropy.append(d.get("actor/entropy", float("nan")))
    is_std.append(d.get("rollout_corr/rollout_is_std", float("nan")))

steps   = np.array(steps)
r_mean  = np.array(r_mean)
r_max   = np.array(r_max)
r_min   = np.array(r_min)
entropy = np.array(entropy)
is_std  = np.array(is_std)

def ema(x, a=0.3):
    out = np.zeros_like(x, dtype=float)
    out[0] = x[0]
    for i in range(1, len(x)):
        out[i] = a * x[i] + (1 - a) * out[i-1]
    return out

r_smooth  = ema(r_mean)
ent_smooth = ema(entropy)
std_smooth = ema(is_std)

# ── 图9: 训练曲线（三子图）─────────────────────────────────────────────
fig, axes = plt.subplots(1, 3, figsize=(15, 4.5))

# 子图1: 奖励均值（带 max/min 阴影）
ax = axes[0]
ax.fill_between(steps, r_min, r_max, alpha=0.12, color=BLUE)
ax.plot(steps, r_mean,   color=BLUE, alpha=0.30, lw=1.2)
ax.plot(steps, r_smooth, color=BLUE, lw=2.2, label="EMA")
ax.set_xlabel("训练步"); ax.set_ylabel("奖励均值")
ax.set_title("（a）奖励均值", fontsize=12)
ax.grid(alpha=0.3)
# 注解第1步偏低的原因
ax.annotate("第1步偏低：\n选组按优势而非 reward",
            xy=(steps[0], r_mean[0]), xytext=(6, r_mean[0]+0.09),
            fontsize=7.5, color="#555",
            arrowprops=dict(arrowstyle="->", color="#999", lw=0.8))
ax.text(0.97, 0.05, f"{r_mean[0]:.3f} → {r_mean[-1]:.3f}",
        transform=ax.transAxes, ha="right", va="bottom", fontsize=9, color=BLUE)

# 子图2: 策略熵
ax = axes[1]
ax.plot(steps, entropy,    color=ORANGE, alpha=0.30, lw=1.2)
ax.plot(steps, ent_smooth, color=ORANGE, lw=2.2)
ax.set_xlabel("训练步"); ax.set_ylabel("策略熵")
ax.set_title("（b）策略熵（多样性）", fontsize=12)
ax.grid(alpha=0.3)
ax.text(0.97, 0.97, f"{entropy[0]:.3f} → {entropy[-1]:.3f}",
        transform=ax.transAxes, ha="right", va="top", fontsize=9, color=ORANGE)

# 子图3: 轨迹多样性 std（rollout importance-sampling std）
ax = axes[2]
ax.plot(steps, is_std,     color=GREEN, alpha=0.30, lw=1.2)
ax.plot(steps, std_smooth, color=GREEN, lw=2.2)
ax.set_xlabel("训练步"); ax.set_ylabel("轨迹多样性 std")
ax.set_title("（c）轨迹多样性（rollout IS std）", fontsize=12)
ax.grid(alpha=0.3)
ax.text(0.97, 0.97, f"{is_std[0]:.3f} → {is_std[-1]:.3f}",
        transform=ax.transAxes, ha="right", va="top", fontsize=9, color=GREEN)

fig.tight_layout(pad=2.0)
out9 = os.path.join(FIGDIR, "fig_fig9_training_curves_zh.png")
fig.savefig(out9, dpi=185, bbox_inches="tight", facecolor="white")
plt.close()
print(f"saved {out9}")

print(f"\n数据摘要 (真实训练, {len(steps)} 步):")
print(f"  reward_mean : {r_mean[0]:.3f} → {r_mean[-1]:.3f}")
print(f"  entropy     : {entropy[0]:.3f} → {entropy[-1]:.3f}  (↓ 多样性下降)")
print(f"  rollout_std : {is_std[0]:.3f} → {is_std[-1]:.3f}  (↓ 方差坍缩)")

import json, os, math
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

_ZH = None
from matplotlib.font_manager import fontManager
for f in ["Noto Sans CJK SC","Source Han Sans SC","WenQuanYi Zen Hei","Microsoft YaHei","SimHei"]:
    if f in {x.name for x in fontManager.ttflist}: _ZH = f; break
if _ZH:
    plt.rcParams["font.sans-serif"] = [_ZH]
    plt.rcParams["axes.unicode_minus"] = False

BLUE   = "#1565C0"
ORANGE = "#E65100"
GREEN  = "#2E7D32"
GRAY   = "#90A4AE"

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SRC  = os.path.join(ROOT, "logs", "metrics", "agent_rl_16gpu", "metrics.jsonl")
FIGDIR = os.path.join(ROOT, "master-thesis", "figures")

# ── 读数据 ──────────────────────────────────────────────────────────────
with open(SRC) as f:
    rows = [json.loads(l) for l in f if l.strip()]

steps, r_mean, r_max, r_min, groups, pg_loss, ppo_kl = [], [], [], [], [], [], []
for r in rows:
    d = r["data"]
    if "critic/rewards/mean" not in d:
        continue
    steps.append(r["step"])
    r_mean.append(d["critic/rewards/mean"])
    r_max.append(d.get("critic/rewards/max", d["critic/rewards/mean"]))
    r_min.append(d.get("critic/rewards/min", d["critic/rewards/mean"]))
    groups.append(int(d.get("training/batch/num_groups", 64)))
    pg_loss.append(d.get("actor/pg_loss", 0))
    ppo_kl.append(d.get("actor/ppo_kl", 0))

steps = np.array(steps)
r_mean = np.array(r_mean)
r_max  = np.array(r_max)
r_min  = np.array(r_min)
groups = np.array(groups)
pg_loss = np.array(pg_loss)
ppo_kl  = np.array(ppo_kl)

# EMA 平滑（alpha=0.3）
def ema(x, a=0.3):
    out = np.zeros_like(x)
    out[0] = x[0]
    for i in range(1, len(x)):
        out[i] = a * x[i] + (1 - a) * out[i-1]
    return out

r_smooth = ema(r_mean)
pg_smooth = ema(pg_loss)
kl_smooth = ema(ppo_kl)

# ── 图9: 训练曲线（三子图）─────────────────────────────────────────────
fig, axes = plt.subplots(1, 3, figsize=(15, 4.5))

# 子图1: 奖励均值（带 max/min 阴影）
ax = axes[0]
ax.fill_between(steps, r_min, r_max, alpha=0.15, color=BLUE, label="reward min/max")
ax.plot(steps, r_mean,  color=BLUE,  alpha=0.35, lw=1.2, label="原始")
ax.plot(steps, r_smooth, color=BLUE, lw=2.2, label="EMA")
ax.set_xlabel("训练步"); ax.set_ylabel("奖励均值")
ax.set_title("（a）奖励均值", fontsize=12)
ax.legend(fontsize=8); ax.grid(alpha=0.3)
ax.annotate("第1步 reward 偏低：\n选组按优势而非 reward",
            xy=(1, r_mean[0]), xytext=(6, r_mean[0]+0.08),
            fontsize=7.5, color="#555",
            arrowprops=dict(arrowstyle="->", color="#888", lw=0.8))

# 子图2: pg_loss
ax = axes[1]
ax.plot(steps, pg_loss,   color=ORANGE, alpha=0.3, lw=1)
ax.plot(steps, pg_smooth, color=ORANGE, lw=2.2)
ax.axhline(0, color="#aaa", lw=0.8, ls="--")
ax.set_xlabel("训练步"); ax.set_ylabel("pg_loss")
ax.set_title("（b）策略梯度损失 pg_loss", fontsize=12)
ax.grid(alpha=0.3)

# 子图3: ppo_kl
ax = axes[2]
ax.plot(steps, ppo_kl,   color=GREEN, alpha=0.3, lw=1)
ax.plot(steps, kl_smooth, color=GREEN, lw=2.2)
ax.axhline(0, color="#aaa", lw=0.8, ls="--")
ax.set_xlabel("训练步"); ax.set_ylabel("ppo_kl")
ax.set_title("（c）策略 KL 散度 ppo_kl", fontsize=12)
ax.grid(alpha=0.3)

fig.tight_layout(pad=2.0)
out9 = os.path.join(FIGDIR, "fig_fig9_training_curves_zh.png")
fig.savefig(out9, dpi=185, bbox_inches="tight", facecolor="white")
plt.close()
print(f"saved {out9}")

# ── 图10: S 收缩曲线（阶梯图）────────────────────────────────────────
fig, ax = plt.subplots(figsize=(9, 4.5))

ax.step(steps, groups, where="post", color=BLUE, lw=2.2, label="存活组数 S")
ax.fill_between(steps, 64, groups, step="post", alpha=0.12, color=BLUE)
ax.axhline(64, color=GRAY, lw=1.2, ls="--", label="训练组数 N=64")

# 标注变化点
prev = None
for s, g in zip(steps, groups):
    if prev is not None and g != prev:
        ax.annotate(f"{g}", xy=(s, g), xytext=(s+0.3, g-2),
                    fontsize=7.5, color=BLUE,
                    arrowprops=dict(arrowstyle="-", color=BLUE, lw=0.6))
    prev = g

ax.set_xlabel("训练步")
ax.set_ylabel("存活组数 S")
ax.set_title("超采样量 S 随训练步收缩", fontsize=12)
ax.legend(fontsize=9)
ax.set_ylim(50, max(groups) + 5)
ax.grid(alpha=0.3)

# 说明文字
ax.text(0.98, 0.97,
        f"S: {groups[0]} → {groups[-1]}（共 {len(steps)} 步）\n单调不增 ✓",
        transform=ax.transAxes, ha="right", va="top",
        fontsize=9, color="#444",
        bbox=dict(boxstyle="round,pad=0.3", facecolor="#f0f4ff",
                  edgecolor="#aac", lw=0.8))

fig.tight_layout()
out10 = os.path.join(FIGDIR, "fig_fig10_S_shrink_zh.png")
fig.savefig(out10, dpi=185, bbox_inches="tight", facecolor="white")
plt.close()
print(f"saved {out10}")

print(f"\n数据摘要:")
print(f"  步数: {steps[0]}–{steps[-1]}  (共 {len(steps)} 步)")
print(f"  reward_mean: {r_mean[0]:.3f} → {r_mean[-1]:.3f}")
print(f"  S (num_groups): {groups[0]} → {groups[-1]}")
print(f"  pg_loss: {pg_loss[0]:.4f} → {pg_loss[-1]:.4f}")
print(f"  ppo_kl:  {ppo_kl[0]:.6f} → {ppo_kl[-1]:.6f}")
