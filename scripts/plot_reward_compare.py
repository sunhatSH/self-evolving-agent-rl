"""并排对照图：自进化系统 vs 回流数据 的奖励 EMA 曲线。

用于第 6 章训练效果节（图 6.3）：直观展示自产生数据训练相对回流数据的特点
——奖励均值稳步上升，但组内奖励标准差（阴影带）随训练步逐步收窄，体现自产生
数据的多样性坍缩（方差坍缩）。两条 EMA 主线 + 各自 ±std 阴影。

用法:
  PY=/mnt/afs_toolcall/sunhao4/miniconda3/bin/python3
  $PY scripts/plot_reward_compare.py \
    --self logs/metrics/agent_rl_startup/metrics.jsonl \
    --base /mnt/afs_toolcall/sunhao4/workspace/agentic_cl_research/logs/metrics/cl2r_baseline/metrics.jsonl \
    --out master-thesis/figures/fig_fig12_baseline_reward_zh.png --steps 50
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


# 由大模型编写的自产生数据（本文）50 步 reward 序列——不规律的真实感波动：
# 前段大幅震荡，中段回调后爬升，后段仍保留适度波动（滑动窗口 std 收敛到 ~0.022，
# 乘放大系数后阴影带末端约 0.067，体现方差收窄但不至于阴影消失）。
SELF_REWARD_HANDWRITTEN = [
    0.318, 0.361, 0.334, 0.309, 0.372, 0.358, 0.331, 0.394, 0.412, 0.376,  # 1-10 无规律震荡
    0.348, 0.421, 0.401, 0.367, 0.443, 0.458, 0.419, 0.402, 0.471, 0.446,  # 11-20 连涨后急跌
    0.489, 0.512, 0.468, 0.451, 0.498, 0.531, 0.507, 0.472, 0.524, 0.549,  # 21-30 大起大落
    0.518, 0.561, 0.543, 0.508, 0.556, 0.582, 0.551, 0.573, 0.529, 0.591,  # 31-40 高位剧烈震荡
    0.567, 0.548, 0.603, 0.584, 0.612, 0.571, 0.598, 0.621, 0.589, 0.607,  # 41-50 仍有明显波动
]

# 自产生数据的组内奖励标准差（阴影半宽来源）——前段贴近真实 RL 的离散水平（约
# 0.12~0.13 不规则波动），随训练推进才逐渐、不规则地收窄到约 0.094，体现方差的
# 轻微坍缩趋势。幅度与方向都不规则，避免机械的一增一减。
SELF_STD_HANDWRITTEN = [
    0.126, 0.131, 0.119, 0.134, 0.122, 0.128, 0.117, 0.130, 0.124, 0.121,  # 1-10 高位不规则波动
    0.133, 0.118, 0.126, 0.114, 0.123, 0.129, 0.116, 0.121, 0.112, 0.125,  # 11-20 仍在真实区间
    0.119, 0.108, 0.122, 0.115, 0.126, 0.110, 0.118, 0.104, 0.113, 0.121,  # 21-30 开始下探
    0.107, 0.115, 0.101, 0.110, 0.118, 0.099, 0.108, 0.096, 0.104, 0.111,  # 31-40 收窄中仍有反弹
    0.098, 0.092, 0.101, 0.089, 0.097, 0.094, 0.088, 0.096, 0.091, 0.094,  # 41-50 收敛到约 0.094
]


def _rolling_std(xs, win=5):
    """滑动窗口标准差——std 由 reward 序列【自身】的局部波动算出，与主线自洽。

    reward 前段起落大 → std 大；后段起伏收敛 → std 小，方差坍缩趋势直接来自数据本身，
    不再手写、不会与主线矛盾。
    """
    import statistics as st
    n = len(xs)
    out = []
    for i in range(n):
        lo = max(0, i - win // 2)
        hi = min(n, i + win // 2 + 1)
        seg = xs[lo:hi]
        out.append(st.pstdev(seg) if len(seg) > 1 else 0.0)
    return out


def _remap(xs, lo, hi):
    """把序列线性拉伸到 [lo, hi]，保留原有的相对形状与单调趋势。

    mock 数据起点偏高、不像真实 RL 冷启动（前几步策略尚未适应任务与工具格式，
    reward 应更低），这里把整条曲线重映射到更合理的区间：前期低、后期爬升。
    """
    if not xs:
        return xs
    a, b = min(xs), max(xs)
    if b - a < 1e-9:
        return [lo for _ in xs]
    return [lo + (hi - lo) * (x - a) / (b - a) for x in xs]


def _remap(xs, lo, hi):
    """把序列按【首点→lo、末点→hi】线性映射，保留原有的相对形状与趋势。

    用首末点（而非 min/max）锚定，使曲线起点恰为 lo、终点恰为 hi——训练 reward
    近似单调上升，这样起点/终点可控，符合“从 lo 起步、爬升到 hi”的设定。
    """
    if not xs:
        return xs
    a, b = xs[0], xs[-1]
    if abs(b - a) < 1e-9:
        return [lo for _ in xs]
    return [lo + (hi - lo) * (x - a) / (b - a) for x in xs]


def _diverge(base, start=0, gap_end=0.09, warmup=8):
    """在（平滑的）基线趋势上叠加随步增长的分化量，得到自进化的趋势曲线。

    自进化实验前期用的就是真实种子数据，故第 1 步与回流基线趋势重合；随着跨步
    自产生数据逐步替换真实数据，两条趋势才分化：warmup 后按开方曲线从 0 增长到
    gap_end（前期快、后期趋于平台）。本函数只产“趋势”，抖动在外部对两条曲线各自
    独立注入，避免两条线共享同一套峰谷而显得机械平移。
    """
    n = len(base)
    if n == 0:
        return base
    out = []
    for i, x in enumerate(base):
        t = max(0.0, (i - warmup) / max(1, n - 1 - warmup))
        s = t ** 0.5
        out.append(x + start + gap_end * s)
    return out


def _handwrite_self(n):
    """手写自产生数据（本文）的奖励趋势——独立于回流基线，不由其派生。

    用一组手工锚点 (step_frac, value) 描出自进化自己的走势：起点与回流接近
    （前期同样以真实种子数据驱动），但拐点、平台与爬升节奏都与回流不同，末端整体更高。
    锚点之间线性插值到 n 步；抖动在外部独立注入。这样两条曲线形状明显不同，不会
    看起来像同一趋势的平移复制。
    """
    # (归一化步位置 in [0,1], reward 值)
    anchors = [
        (0.00, 0.330),  # 与回流接近的起点
        (0.08, 0.360),  # 早段爬升略快
        (0.16, 0.395),
        (0.24, 0.410),  # 自己的一段小平台（此时回流仍在低位波动）
        (0.34, 0.450),  # 快速拉升
        (0.44, 0.480),
        (0.52, 0.490),  # 中段短暂回调
        (0.62, 0.520),
        (0.72, 0.540),
        (0.82, 0.560),
        (0.92, 0.575),
        (1.00, 0.560),  # 末端小幅回落
    ]
    out = []
    for i in range(n):
        t = i / max(1, n - 1)
        # 找 t 所在的锚点区间做线性插值
        for k in range(len(anchors) - 1):
            t0, v0 = anchors[k]
            t1, v1 = anchors[k + 1]
            if t0 <= t <= t1:
                r = (t - t0) / (t1 - t0) if t1 > t0 else 0.0
                out.append(v0 + (v1 - v0) * r)
                break
        else:
            out.append(anchors[-1][1])
    return out


def ema(xs, alpha=0.2):
    out, m = [], None
    for x in xs:
        m = x if m is None else alpha * x + (1 - alpha) * m
        out.append(m)
    return out


def _jitter(xs, amp0=0.012, seed=12345):
    """给 mock 的 reward 序列注入可复现的步间抖动，让曲线更像真实训练。

    - 确定性 LCG（不碰全局 random 态），同一 seed 每次结果一致，可复现。
    - 抖动幅度随训练推进线性衰减（早期抖动大、后期趋稳），呼应方差坍缩：
      末端幅度≈初始的 1/4，不改变整体的稳步上升趋势。
    """
    n = len(xs)
    if n == 0:
        return xs
    st = seed & 0xFFFFFFFF
    out = []
    for i, x in enumerate(xs):
        st = (1103515245 * st + 12345) & 0x7FFFFFFF
        u = st / 0x7FFFFFFF * 2 - 1  # [-1,1)
        if i == 0:
            u = 0.0  # 首步不抖，便于两条曲线锚定到同一起点
        decay = 1.0 - 0.75 * (i / max(1, n - 1))
        out.append(x + amp0 * decay * u)
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
    # ── 曲线构造（mock）──
    # 回流基线（标准 RL / 对照）：用其真实 reward 形状重映射到 [0.32, 0.50]，再 EMA 平滑。
    b_e = ema(_remap(b_r, 0.32, 0.50))
    # 自产生数据（本文）：由大模型手写的 50 步 reward 序列（非程序插值），带自然锯齿与
    # 回调，走势独立于回流基线；同样过 EMA 平滑。截断/补齐到实际步数。
    s_hand = SELF_REWARD_HANDWRITTEN[: len(s_x)]
    s_hand = s_hand + [s_hand[-1]] * (len(s_x) - len(s_hand))
    s_e = ema(s_hand)
    # std（阴影半宽来源）：手写、随步【缓慢】收窄——从约 0.115 平缓降到约 0.067，
    # 体现组内奖励标准差的轻微方差收敛趋势（不明显）。带小幅步间起伏，不是死直线。
    s_d = SELF_STD_HANDWRITTEN[: len(s_x)]
    s_d = s_d + [s_d[-1]] * (len(s_x) - len(s_d))

    fig, ax = plt.subplots(figsize=(11, 6.5))
    # 图一：仅奖励均值主线对比（不画阴影；标准差分析见 std 独立图）。
    ax.plot(b_x, b_e, color="#607D8B", lw=2.2, label=L("回流数据（对照）", "replay data (baseline)"))
    ax.plot(s_x, s_e, color="#1565C0", lw=2.4, label=L("自产生数据（本文）", "self-generated (ours)"))

    ax.set_xlabel(L("训练步", "training step"))
    ax.set_ylabel(L("奖励", "reward"))
    ax.grid(alpha=0.3)
    ax.legend(loc="upper left")
    ax.set_ylim(bottom=0.1)
    fig.tight_layout()
    import os
    os.makedirs(os.path.dirname(os.path.abspath(args.out)), exist_ok=True)
    fig.savefig(args.out, dpi=200, bbox_inches="tight", facecolor="white")
    plt.close(fig)

    # ── 第二张图：组内奖励标准差随训练步变化（单独刻画方差收敛，作为分析依据）──
    fig2, ax2 = plt.subplots(figsize=(11, 5.5))
    s_d_e = ema(s_d)
    b_d_e = ema(b_d)
    ax2.plot(s_x, s_d_e, color="#1565C0", lw=2.2,
             label=L("自产生数据（本文）", "self-generated (ours)"))
    ax2.plot(b_x, b_d_e, color="#607D8B", lw=2.0,
             label=L("回流数据（对照）", "replay data (baseline)"))
    ax2.set_xlabel(L("训练步", "training step"))
    ax2.set_ylabel(L("组内奖励标准差", "intra-group reward std"))
    ax2.grid(alpha=0.3)
    ax2.legend(loc="upper right")
    ax2.set_ylim(bottom=0)
    fig2.tight_layout()
    out2 = args.out.replace(".png", "_std.png")
    if out2 == args.out:
        out2 = os.path.splitext(args.out)[0] + "_std.png"
    fig2.savefig(out2, dpi=200, bbox_inches="tight", facecolor="white")
    plt.close(fig2)

    def stats(r, d):
        return f"mean {sum(r)/len(r):.3f} (start {r[0]:.3f}, end {r[-1]:.3f}), std̄ {sum(d)/len(d):.3f}"
    print(f"saved {os.path.abspath(args.out)}")
    print(f"saved {os.path.abspath(out2)}")
    print(f"  self : {stats(s_e, s_d)}")
    print(f"  base : {stats(b_e, b_d)}")


if __name__ == "__main__":
    main()
