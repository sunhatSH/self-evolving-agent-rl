"""从训练 console 日志解析指标，绘制论文实验图（fig9/10/11）。

训练跑通后用法:
  PY=/mnt/afs_toolcall/sunhao4/miniconda3/bin/python3
  $PY scripts/plot_train_figures.py logs/smoke_4gpu.log --out master-thesis/figures

产出（覆盖占位框对应的三张图）:
  fig_fig9_training_curves_zh.png   训练指标 2x2 + 终止判据竖线
  fig_fig10_S_shrink_zh.png         超采样量 S 随步收缩
  fig_fig11_difficulty_evolve_zh.png 任务难度(响应长度/轮数)随步演化

解析的日志行:
  verl 每步指标块:  "<key> : <value>"  (key 含 critic/rewards/mean, actor/pg_loss,
                    actor/ppo_kl, response_length/mean, sys/reward_std, sys/advantage_std,
                    sys/group_reward_std, sys/num_groups, training/global_step)
  自定义行:  "[select] eliminate: S=32 dropped=3 (...) → R=29"
            "[monitor] step N: reward_std=.. adv_std=.. group_std=.."
            "[cross-step] step N: generated M seeds"

设计取舍: 只用 stdlib + matplotlib(AFS python 有), 不依赖 pandas/tensorboard。
日志缺某指标时该子图跳过并在图上标注, 不编造数据。中文字体缺失时自动退英文标签。
"""
from __future__ import annotations

import argparse
import os
import re
import sys

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ── 中文字体探测: 有则用中文标签, 无则退英文(避免豆腐块) ──────────────────────
_ZH_FONTS = ["Noto Sans CJK SC", "Source Han Sans SC", "WenQuanYi Zen Hei",
             "Microsoft YaHei", "SimHei", "PingFang SC"]


def _pick_font() -> str | None:
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


def L(zh: str, en: str) -> str:
    """按字体可用性返回中/英标签。"""
    return zh if _ZH else en


# ── 日志解析 ─────────────────────────────────────────────────────────────────
# verl 指标行:  很多空格分隔的  "key : value"
_METRIC_RE = re.compile(r"([A-Za-z][\w/]+)\s*:\s*(-?[\d.eE+]+|nan|inf|-inf)\s*$")
_STEP_RE = re.compile(r"training/global_step\s*:\s*(\d+)")
_ELIM_RE = re.compile(r"\[select\]\s*eliminate:\s*S=(\d+).*?→\s*R=(\d+)")
_ELIM_RE2 = re.compile(r"\[select\]\s*groups=(\d+)\s+dropped=\d+.*?remaining=(\d+)")

_WANT = {
    "critic/rewards/mean", "cl/reward_mean", "sys/reward_mean",
    "actor/pg_loss", "actor/ppo_kl",
    "sys/reward_std", "sys/advantage_std", "sys/group_reward_std",
    "sys/num_groups", "response_length/mean", "training/num_turns/mean",
}


def parse_log(path: str) -> list[dict]:
    """返回按步聚合的 [{step, metric:value, ...}]。以 training/global_step 划分步边界。"""
    steps: list[dict] = []
    cur: dict = {}
    with open(path, encoding="utf-8", errors="ignore") as f:
        for raw in f:
            line = raw.rstrip("\n")
            # 去掉 ray 前缀色码/pid 装饰
            line_clean = re.sub(r"\x1b\[[0-9;]*m", "", line)

            m_step = _STEP_RE.search(line_clean)
            if m_step:
                cur["step"] = int(m_step.group(1))

            m_elim = _ELIM_RE.search(line_clean) or _ELIM_RE2.search(line_clean)
            if m_elim:
                cur["S"] = int(m_elim.group(1))
                cur["R"] = int(m_elim.group(2))

            m = _METRIC_RE.search(line_clean)
            if m:
                key, val = m.group(1), m.group(2)
                if key in _WANT:
                    try:
                        cur[key] = float(val)
                    except ValueError:
                        cur[key] = float("nan")

            # 一个指标块以 timing_s/step 或 training/global_step 结束 → flush
            if "timing_s/step" in line_clean and cur:
                steps.append(cur)
                cur = {}
    if cur.get("step") is not None or len(cur) > 1:
        steps.append(cur)
    # 去重: 同 step 合并
    merged: dict[int, dict] = {}
    for i, s in enumerate(steps):
        k = s.get("step", i)
        merged.setdefault(k, {}).update(s)
    return [merged[k] for k in sorted(merged)]


def _series(rows: list[dict], key: str) -> tuple[list, list]:
    xs, ys = [], []
    for r in rows:
        if key in r and r.get("step") is not None:
            xs.append(r["step"]); ys.append(r[key])
    return xs, ys


def _reward_key(rows: list[dict]) -> str:
    for k in ("critic/rewards/mean", "cl/reward_mean", "sys/reward_mean"):
        if any(k in r for r in rows):
            return k
    return "critic/rewards/mean"


# ── 绘图 ─────────────────────────────────────────────────────────────────────
def plot_fig9(rows, out):
    """训练指标 2x2 + 终止判据。"""
    fig, axes = plt.subplots(2, 2, figsize=(11, 7))
    rk = _reward_key(rows)
    panels = [
        (axes[0, 0], rk, L("奖励均值", "reward mean"), "#2E7D32"),
        (axes[0, 1], "sys/reward_std", L("奖励标准差", "reward std"), "#1565C0"),
        (axes[1, 0], "actor/pg_loss", L("策略损失 pg_loss", "pg_loss"), "#C62828"),
        (axes[1, 1], "actor/ppo_kl", L("策略 KL 散度 ppo_kl", "ppo_kl"), "#6A1B9A"),
    ]
    for ax, key, title, col in panels:
        xs, ys = _series(rows, key)
        if xs:
            ax.plot(xs, ys, "-o", color=col, ms=3, lw=1.5)
        else:
            ax.text(0.5, 0.5, L("日志无此指标", "metric absent"),
                    ha="center", va="center", transform=ax.transAxes, color="#999")
        ax.set_title(title, fontsize=11)
        ax.set_xlabel(L("训练步", "step")); ax.grid(alpha=0.3)
    # 终止步竖线(最后一步)
    last = max((r["step"] for r in rows if r.get("step") is not None), default=None)
    if last is not None:
        for ax in axes.flat:
            ax.axvline(last, color="#D32F2F", ls="--", lw=1, alpha=0.6)
    fig.suptitle(L("训练指标与终止判据", "Training metrics & stop criterion"), fontsize=13)
    fig.tight_layout()
    fig.savefig(out, dpi=200, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"saved {out}")


def plot_fig10(rows, out):
    """超采样量 S 随步收缩 + N 参考线。"""
    xs, ys = _series(rows, "S")
    if not xs:  # 退化: 用 num_groups
        xs, ys = _series(rows, "sys/num_groups")
    fig, ax = plt.subplots(figsize=(8, 5))
    if xs:
        ax.step(xs, ys, where="mid", color="#1565C0", lw=2, label="S")
        ax.fill_between(xs, ys, step="mid", alpha=0.15, color="#1565C0")
    else:
        ax.text(0.5, 0.5, L("日志无 S/存活组数", "no S / num_groups in log"),
                ha="center", va="center", transform=ax.transAxes, color="#999")
    ax.set_xlabel(L("训练步", "step"))
    ax.set_ylabel(L("超采样量 S（存活组数）", "oversample size S (survived groups)"))
    ax.set_title(L("超采样量 S 随训练步收缩", "Oversample size S shrinks over steps"))
    ax.grid(alpha=0.3); ax.legend()
    fig.tight_layout()
    fig.savefig(out, dpi=200, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"saved {out}")


def plot_fig11(rows, out):
    """任务难度代理(响应长度 / 平均轮数)随步演化。"""
    fig, ax = plt.subplots(figsize=(8, 5))
    x1, y1 = _series(rows, "response_length/mean")
    x2, y2 = _series(rows, "training/num_turns/mean")
    plotted = False
    if x1:
        ax.plot(x1, y1, "-o", color="#E65100", ms=3, lw=1.5,
                label=L("平均响应长度", "mean response length"))
        plotted = True
    if x2:
        ax2 = ax.twinx()
        ax2.plot(x2, y2, "-s", color="#00695C", ms=3, lw=1.5,
                 label=L("平均轮数", "mean turns"))
        ax2.set_ylabel(L("平均轮数", "mean turns"), color="#00695C")
        plotted = True
    if not plotted:
        ax.text(0.5, 0.5, L("日志无难度代理指标", "no difficulty proxy in log"),
                ha="center", va="center", transform=ax.transAxes, color="#999")
    ax.set_xlabel(L("训练步", "step"))
    ax.set_ylabel(L("平均响应长度（token）", "mean response length (tokens)"), color="#E65100")
    ax.set_title(L("任务难度随自进化演化", "Task difficulty over self-evolution"))
    ax.grid(alpha=0.3)
    fig.tight_layout()
    fig.savefig(out, dpi=200, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"saved {out}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("log", help="训练 console 日志路径")
    ap.add_argument("--out", default="master-thesis/figures", help="图输出目录")
    args = ap.parse_args()

    if not os.path.isfile(args.log):
        sys.exit(f"log not found: {args.log}")
    rows = parse_log(args.log)
    n = sum(1 for r in rows if r.get("step") is not None)
    print(f"parsed {len(rows)} metric blocks, {n} with step index"
          f" (zh font: {_ZH or 'NONE → English labels'})")
    if n == 0:
        print("WARNING: 未解析到任何带 step 的指标块; 图将标注'无数据'。"
              "确认日志是训练 console 输出(含 training/global_step 行)。")

    os.makedirs(args.out, exist_ok=True)
    plot_fig9(rows, os.path.join(args.out, "fig_fig9_training_curves_zh.png"))
    plot_fig10(rows, os.path.join(args.out, "fig_fig10_S_shrink_zh.png"))
    plot_fig11(rows, os.path.join(args.out, "fig_fig11_difficulty_evolve_zh.png"))


if __name__ == "__main__":
    main()
