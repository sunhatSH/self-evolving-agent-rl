"""并排对照图：自进化系统 vs 回流数据 的奖励 EMA 曲线。

用于第 6 章训练效果节：直观展示自产生数据训练相对回流数据的特点
——均值稍高、波动更大（阴影带更宽）。两条 EMA 主线 + 各自 ±std 阴影。

用法:
  PY=/mnt/afs_toolcall/sunhao4/miniconda3/bin/python3
  $PY scripts/plot_reward_compare.py \
    --self logs/metrics/agent_rl_startup/metrics.jsonl \
    --base /mnt/afs_toolcall/sunhao4/workspace/agentic_cl_research/logs/metrics/cl2r_baseline/metrics.jsonl \
    --out master-thesis/figures/fig_fig12_reward_compare_zh.png --steps 50
"""
from __future__ import annotations

import argparse
import json

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


def load(path, steps, rkey="cl/reward_mean", skey="cl/group_reward_std"):
    S, R, D = [], [], []
    with open(path, encoding="utf-8") as f:
        for line in f:
            d = json.loads(line)
            s = d["step"]
            if s > steps:
                continue
            data = d.get("data", {})
            if rkey in data:
                S.append(s); R.append(data[rkey]); D.append(data.get(skey, 0.0))
    return S, R, D


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--self", dest="self_", required=True)
    ap.add_argument("--base", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--steps", type=int, default=50)
    args = ap.parse_args()

    s_x, s_r, s_d = load(args.self_, args.steps)
    b_x, b_r, b_d = load(args.base, args.steps)
    s_e, b_e = ema(s_r), ema(b_r)

    fig, ax = plt.subplots(figsize=(9, 5.5))
    band = 0.5  # 阴影半宽系数: 画 ±0.5·std, 避免带宽过大盖住主线
    # 回流(对照) — 灰蓝
    ax.plot(b_x, b_e, color="#607D8B", lw=2.2, label=L("回流数据（对照）", "replay data (baseline)"))
    ax.fill_between(b_x, [m - band * d for m, d in zip(b_e, b_d)],
                    [m + band * d for m, d in zip(b_e, b_d)],
                    color="#607D8B", alpha=0.12)
    # 自进化(本文) — 蓝
    ax.plot(s_x, s_e, color="#1565C0", lw=2.4, label=L("自产生数据（本文）", "self-generated (ours)"))
    ax.fill_between(s_x, [m - band * d for m, d in zip(s_e, s_d)],
                    [m + band * d for m, d in zip(s_e, s_d)],
                    color="#1565C0", alpha=0.16)

    ax.set_xlabel(L("训练步", "training step"))
    ax.set_ylabel(L("奖励", "reward"))
    ax.grid(alpha=0.3)
    ax.legend(loc="upper left")
    ax.set_ylim(bottom=0.3)
    fig.tight_layout()
    import os
    os.makedirs(os.path.dirname(os.path.abspath(args.out)), exist_ok=True)
    fig.savefig(args.out, dpi=200, bbox_inches="tight", facecolor="white")
    plt.close(fig)

    def stats(r, d):
        return f"mean {sum(r)/len(r):.3f} (end {r[-1]:.3f}), std̄ {sum(d)/len(d):.3f}"
    print(f"saved {os.path.abspath(args.out)}")
    print(f"  self : {stats(s_r, s_d)}")
    print(f"  base : {stats(b_r, b_d)}")


if __name__ == "__main__":
    main()
