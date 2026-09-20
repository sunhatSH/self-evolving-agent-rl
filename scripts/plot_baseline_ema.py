"""从 baseline metrics.jsonl 重绘前 50 步的奖励 EMA 曲线（对照实验图）。

用作论文对照组：不使用本文自进化系统的普通 RL 训练（固定任务集 + KL 约束 GRPO）
的奖励随步变化。去掉 CL 实验名标签，中文标签，仅取前 50 步。

用法:
  PY=/mnt/afs_toolcall/sunhao4/miniconda3/bin/python3
  $PY scripts/plot_baseline_ema.py \
    --src /mnt/afs_toolcall/sunhao4/workspace/agentic_cl_research/logs/metrics/cl2r_baseline/metrics.jsonl \
    --out master-thesis/figures/fig_fig12_baseline_reward_zh.png --steps 50
"""
from __future__ import annotations

import argparse
import json
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


def ema(xs, alpha=0.3):
    out, m = [], None
    for x in xs:
        m = x if m is None else alpha * x + (1 - alpha) * m
        out.append(m)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--src", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--steps", type=int, default=50)
    ap.add_argument("--reward-key", default="cl/reward_mean")
    ap.add_argument("--std-key", default="cl/reward_std")
    args = ap.parse_args()

    steps, reward, std = [], [], []
    with open(args.src, encoding="utf-8") as f:
        for line in f:
            d = json.loads(line)
            s = d["step"]
            if s > args.steps:
                continue
            data = d.get("data", {})
            if args.reward_key in data:
                steps.append(s)
                reward.append(data[args.reward_key])
                std.append(data.get(args.std_key, 0.0))

    if not steps:
        raise SystemExit(f"no data with key {args.reward_key} in first {args.steps} steps")

    reward_ema = ema(reward, alpha=0.3)

    fig, ax = plt.subplots(figsize=(8, 5))
    # 原始奖励均值(淡) + EMA(实线) + ±std 带
    ax.plot(steps, reward, color="#90CAF9", lw=1, alpha=0.7,
            label=L("奖励均值(原始)", "reward mean (raw)"))
    ax.plot(steps, reward_ema, color="#1565C0", lw=2.2,
            label=L("奖励均值(EMA)", "reward mean (EMA)"))
    lo = [r - s for r, s in zip(reward, std)]
    hi = [r + s for r, s in zip(reward, std)]
    ax.fill_between(steps, lo, hi, color="#1565C0", alpha=0.12,
                    label=L("±组间标准差", "±reward std"))

    ax.set_xlabel(L("训练步", "training step"))
    ax.set_ylabel(L("奖励", "reward"))
    ax.grid(alpha=0.3)
    ax.legend(loc="best")
    ax.set_ylim(bottom=0.3)
    fig.tight_layout()
    os.makedirs(os.path.dirname(os.path.abspath(args.out)), exist_ok=True)
    fig.savefig(args.out, dpi=200, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"saved {os.path.abspath(args.out)}  ({len(steps)} steps, zh={_ZH or 'EN'})")


if __name__ == "__main__":
    main()
