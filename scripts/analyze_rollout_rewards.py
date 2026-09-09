#!/usr/bin/env python3
"""一次性分析：把 rollouts/training/<exp>/rollout_status-*.jsonl 里
每 step、每 query、每 8 个 rollout 的 reward 抽出来 → 导出 JSON + 画图。

用法:
    python scripts/analyze_rollout_rewards.py cl2r_clear
    python scripts/analyze_rollout_rewards.py cl2r_kl
输出:
    logs/experiments/figs/<exp>_rollout_rewards.json
    logs/experiments/figs/<exp>_reward_analysis.png
"""
import glob
import json
import os
import re
import sys
from statistics import mean, pstdev

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402


def load_exp(exp):
    files = sorted(
        glob.glob(f"rollouts/training/{exp}/rollout_status-*.jsonl"),
        key=lambda p: int(re.search(r"-(\d+)\.jsonl", p).group(1)),
    )
    steps = []
    for f in files:
        st = int(re.search(r"-(\d+)\.jsonl", f).group(1))
        queries = []
        for line in open(f):
            d = json.loads(line)
            rewards = [
                (r.get("reward") if r.get("status") == "success" else None)
                for r in d["rollouts"]
            ]
            queries.append(
                {
                    "task_id": d["task_id"],
                    "bucket": d["bucket"],
                    "n_success": d["n_success"],
                    "rewards": [None if x is None else round(x, 4) for x in rewards],
                    "subscores": [
                        {
                            "correctness": r.get("correctness"),
                            "trajectory": r.get("trajectory"),
                            "safety": r.get("safety"),
                        }
                        for r in d["rollouts"]
                    ],
                }
            )
        steps.append({"step": st, "queries": queries})
    return steps


def export_json(exp, steps):
    out = f"logs/experiments/figs/{exp}_rollout_rewards.json"
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w") as fh:
        json.dump({"experiment": exp, "steps": steps}, fh, ensure_ascii=False, indent=1)
    print(f"[json] {out}  ({len(steps)} steps)")
    return out


def _valid(vals):
    return [v for v in vals if v is not None]


def make_plots(exp, steps):
    # 逐 step 聚合
    step_ids, glob_mean, within_std_mean, across_std = [], [], [], []
    frac_dead_groups = []  # 组内全相同(std≈0) 的比例 → GRPO 没梯度
    all_rewards_flat = []
    for s in steps:
        step_ids.append(s["step"])
        per_query_means, per_query_within_std = [], []
        dead = 0
        for q in s["queries"]:
            vs = _valid(q["rewards"])
            all_rewards_flat.extend(vs)
            if not vs:
                continue
            per_query_means.append(mean(vs))
            wstd = pstdev(vs) if len(vs) > 1 else 0.0
            per_query_within_std.append(wstd)
            if wstd < 0.02:  # 组内几乎无分化
                dead += 1
        glob_mean.append(mean(per_query_means) if per_query_means else np.nan)
        within_std_mean.append(mean(per_query_within_std) if per_query_within_std else np.nan)
        across_std.append(pstdev(per_query_means) if len(per_query_means) > 1 else 0.0)
        frac_dead_groups.append(dead / max(1, len(s["queries"])))

    # reward 子分量逐 step 均值
    comp_keys = ["correctness", "trajectory", "safety"]
    comp_series = {k: [] for k in comp_keys}
    for s in steps:
        acc = {k: [] for k in comp_keys}
        for q in s["queries"]:
            for i, sub in enumerate(q["subscores"]):
                if q["rewards"][i] is None:
                    continue
                for k in comp_keys:
                    if sub.get(k) is not None:
                        acc[k].append(sub[k])
        for k in comp_keys:
            comp_series[k].append(mean(acc[k]) if acc[k] else np.nan)

    fig, axes = plt.subplots(2, 2, figsize=(15, 10))

    # (1) reward mean + within-group / across-query std band
    ax = axes[0, 0]
    gm = np.array(glob_mean)
    ws = np.array(within_std_mean)
    ax.plot(step_ids, gm, "-o", ms=3, color="C0", label="reward mean (per-step)")
    ax.fill_between(step_ids, gm - ws, gm + ws, alpha=0.2, color="C0",
                    label="+/- within-group std (GRPO signal)")
    ax.plot(step_ids, across_std, "-", color="C3", label="across-query std (difficulty)")
    ax.set_title(f"{exp}: reward mean & dispersion")
    ax.set_xlabel("step")
    ax.set_ylabel("reward")
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3)

    # (2) reward subcomponents per step
    ax = axes[0, 1]
    for k, c in zip(comp_keys, ["C0", "C1", "C2", "C3"]):
        ax.plot(step_ids, comp_series[k], "-o", ms=2, color=c, label=k)
    ax.set_title(f"{exp}: reward subcomponents (per-step mean)")
    ax.set_xlabel("step")
    ax.set_ylabel("score")
    ax.set_ylim(0, 1.05)
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3)

    # (3) within-group std (GRPO advantage denominator)
    ax = axes[1, 0]
    ax.plot(step_ids, within_std_mean, "-o", ms=3, color="C2")
    ax.axhline(0.15, ls="--", color="gray", label="~0.15 observed mean")
    ax.set_title(f"{exp}: within-group reward std (GRPO adv denominator)")
    ax.set_xlabel("step")
    ax.set_ylabel("within-group std")
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3)

    # (4) all-rollout reward histogram
    ax = axes[1, 1]
    ax.hist(all_rewards_flat, bins=40, color="C4", alpha=0.8)
    ax.axvline(mean(all_rewards_flat), color="k", ls="--",
               label=f"mean={mean(all_rewards_flat):.3f}")
    ax.set_title(f"{exp}: all-rollout reward distribution (n={len(all_rewards_flat)})")
    ax.set_xlabel("reward")
    ax.set_ylabel("count")
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3)

    fig.tight_layout()
    out = f"logs/experiments/figs/{exp}_reward_analysis.png"
    fig.savefig(out, dpi=110)
    print(f"[fig ] {out}")

    # 附：per-step per-query 的 8-rollout 热力(取前 20 step × 前 32 query 的均值矩阵)
    fig2, ax2 = plt.subplots(figsize=(14, 6))
    mat = []
    for s in steps:
        row = [mean(_valid(q["rewards"])) if _valid(q["rewards"]) else np.nan for q in s["queries"]]
        mat.append(row)
    maxq = max(len(r) for r in mat)
    mat = [r + [np.nan] * (maxq - len(r)) for r in mat]
    arr = np.array(mat)
    im = ax2.imshow(arr, aspect="auto", cmap="viridis", vmin=0, vmax=1)
    ax2.set_title(f"{exp}: per step x query mean reward (over 8 rollouts)")
    ax2.set_xlabel("query idx (within step)")
    ax2.set_ylabel("step")
    fig2.colorbar(im, ax=ax2, label="mean reward")
    fig2.tight_layout()
    out2 = f"logs/experiments/figs/{exp}_reward_heatmap.png"
    fig2.savefig(out2, dpi=110)
    print(f"[fig ] {out2}")

    return {
        "reward_mean_overall": round(mean(all_rewards_flat), 4),
        "within_group_std_mean": round(mean(_valid(within_std_mean)), 4),
        "across_query_std_mean": round(mean(_valid(across_std)), 4),
        "dead_group_pct_mean": round(mean(frac_dead_groups) * 100, 2),
        "n_rollouts_total": len(all_rewards_flat),
    }


if __name__ == "__main__":
    exp = sys.argv[1] if len(sys.argv) > 1 else "cl2r_clear"
    steps = load_exp(exp)
    export_json(exp, steps)
    summ = make_plots(exp, steps)
    print("\n=== summary ===")
    print(json.dumps(summ, indent=2))
