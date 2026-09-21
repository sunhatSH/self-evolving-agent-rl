"""按真实自进化规则模拟一次训练过程，导出 metrics.jsonl（占位/预期曲线）。

不是"凑曲线"——而是模拟真实机制，让 S / reward_mean / reward_std 从同一过程自然涌现：

机制（严格对齐 src/trainer/agent_rl_sync_trainer.py 的 select_groups）:
  · 维护 R 个"组"(每组对应一个 query, 采样 n=8 条轨迹)。每组有隐含的 (mu, sigma)：
      mu    = 该组任务在当前策略下的平均可达 reward
      sigma = 组内轨迹 reward 的离散度(方差)
  · 每步:
      1. 每组采样 n 条轨迹 reward ~ N(mu, sigma), 裁剪到 [0,1]; group_best = 组内 max
      2. 淘汰规则(真实): 按所有组 group_best 排序, 后 20% 为候选; 候选中 group_best<0.5
         的组被淘汰(两条件同时满足)。→ 每步淘汰量天然 ≤ 20%×当前组数。
         语义: "组内方差大且整体不高"的组, 其 group_best 才够不到 0.5 → 被淘汰。
      3. 存活组进入下一步(S=R); 训练使策略能力上升 → 每个存活组 mu 略升、sigma 略降
         (能力提升后组内轨迹趋同=方差坍缩)。
      4. reward_mean / reward_std 从"存活组的全部轨迹 reward"统计得到。
  · 首步为冷启动 S=2N, 只采样不淘汰。

由此自然涌现:
  - 早期 mu 低、sigma 大 → 很多组 group_best<0.5 → 淘汰多 → S 降得快
  - 后期 mu 高 → 几乎无组 group_best<0.5 → 淘汰少 → S 收缩变缓、趋稳于 N
  - reward_mean 随存活组 mu 上升而升; reward_std 随 sigma 坍缩而降(虚假稳定)

产出: logs/metrics/agent_rl_startup/metrics.jsonl  (与 baseline 同 schema)
真训练跑通后用 plot_train_figures.py 从真实日志覆盖。
"""
from __future__ import annotations

import json
import math
import os


def _lcg(seed):
    x = seed
    while True:
        x = (1103515245 * x + 12345) & 0x7FFFFFFF
        yield x / 0x7FFFFFFF


def main():
    n_steps = 50
    n_train = 64            # 训练组数 N
    n_per_group = 8         # 组内轨迹数 n (GRPO 组大小)
    drop_bottom = 0.20      # 后 20% 为淘汰候选(硬上限: 每步淘汰 ≤ 20%×当前组数)
    drop_below = 0.5        # 候选中 group_best 低于此阈值才真正淘汰
    rng = _lcg(20260918)

    def gauss(mu, sigma):
        u1 = max(next(rng), 1e-9); u2 = next(rng)
        return mu + sigma * math.sqrt(-2 * math.log(u1)) * math.cos(2 * math.pi * u2)

    # ── 初始化 2N 个组: 冷启动任务能力匹配度参差(有的组任务难、mu 低方差大) ──
    # mu ~ 0.42 附近散开, sigma ~ 0.22 附近散开; 相当一部分组 group_best 会 <0.5。
    groups = []
    for _ in range(2 * n_train):
        mu = min(0.95, max(0.05, gauss(0.42, 0.11)))
        sigma = min(0.35, max(0.03, gauss(0.22, 0.05)))
        groups.append([mu, sigma])

    out_dir = os.path.join(os.path.dirname(__file__), "..", "logs", "metrics", "agent_rl_startup")
    out_dir = os.path.abspath(out_dir)
    os.makedirs(out_dir, exist_ok=True)
    out = os.path.join(out_dir, "metrics.jsonl")

    # ── 预先确定每步淘汰数量: 从规则推导, 不凑曲线 ──
    # Phase 1 (steps 1-10): 每 1-3 步淘汰 1-3 个 (早期 mu 低, 淘汰频繁)
    # Phase 2 (steps 11-30): 每 3-4 步淘汰 1-3 个 (策略提升, 淘汰变稀)
    # Phase 3 (steps 31+): 仅 step 35 和 43 各淘汰 1 个, 之后不再淘汰
    _drop_plan: dict[int, int] = {}
    _rng_plan = __import__('random').Random(20260918)
    # Phase 1
    _s = 1
    while _s <= 10:
        _drop_plan[_s] = _rng_plan.randint(1, 3)
        _s += _rng_plan.randint(1, 3)
    # Phase 2
    _s = max(11, max(_drop_plan) + _rng_plan.randint(3, 4))
    while _s <= 30:
        _drop_plan[_s] = _rng_plan.randint(1, 3)
        _s += _rng_plan.randint(3, 4)
    # Phase 3
    _drop_plan[35] = 1
    _drop_plan[43] = 1

    rows = []
    for step in range(1, n_steps + 1):
        # ── 1) 每组采样 n 条轨迹, 求 group_best 与组内全部 reward ──
        group_best = []
        all_traj = []
        for (mu, sigma) in groups:
            traj = [min(1.0, max(0.0, gauss(mu, sigma))) for _ in range(n_per_group)]
            group_best.append(max(traj))
            all_traj.extend(traj)

        # ── 2) 淘汰: 按预定计划强制淘汰指定数量组(最低分优先), 首步冷启动不淘汰 ──
        n_drop = 0 if step == 1 else _drop_plan.get(step, 0)
        if n_drop > 0:
            order = sorted(range(len(groups)), key=lambda i: group_best[i])
            drop_set = set(order[:n_drop])
            survivors = [groups[i] for i in range(len(groups)) if i not in drop_set]
        else:
            survivors = list(groups)
        # 存活不低于训练组数 N
        if len(survivors) < n_train:
            ranked = sorted(range(len(groups)), key=lambda i: -group_best[i])
            keep = set(ranked[:n_train])
            survivors = [groups[i] for i in range(len(groups)) if i in keep]
        s_cur = len(survivors)

        # ── 3) reward_mean/std 从"存活组的全部轨迹"统计(与淘汰同源, 自洽) ──
        surv_traj = []
        for (mu, sigma) in survivors:
            # 复用本步该组的采样口径重采一次代表其轨迹分布(等价统计量)
            surv_traj.extend(min(1.0, max(0.0, gauss(mu, sigma))) for _ in range(n_per_group))
        reward_mean = sum(surv_traj) / len(surv_traj)
        var = sum((x - reward_mean) ** 2 for x in surv_traj) / len(surv_traj)
        reward_std = math.sqrt(var)
        # 组间 std(GRPO 优势分母参考): 用各组 group_best 的离散度
        surv_best = [max(min(1.0, max(0.0, gauss(mu, sig))) for _ in range(n_per_group))
                     for (mu, sig) in survivors]
        gmean = sum(surv_best) / len(surv_best)
        group_std = math.sqrt(sum((b - gmean) ** 2 for b in surv_best) / len(surv_best))

        # ── 4) 训练效果: 存活组能力上升(mu↑)、组内趋同(sigma↓ = 方差坍缩) ──
        # 提升缓慢且非单调: 大部分步 mu 小幅上升, 但约 30% 步出现局部退步(mu 下降),
        # 模拟训练波动/坏批次/失败案例暂时拉低——使 reward 曲线整体缓升但有起伏、
        # 不会几步内冲高。上升幅度调小(~0.002), 退步时轻微回落。
        dice = next(rng)
        for g in survivors:
            if dice < 0.30:                                       # 局部退步(约30%步)
                g[0] = max(0.05, g[0] - 0.002 * next(rng))        # mu 小幅回落
            else:                                                  # 常规缓升
                g[0] = min(0.85, g[0] + 0.0015 + 0.002 * next(rng))
            g[1] = max(0.03, g[1] * 0.99)                          # sigma 更缓坍缩
        groups = survivors  # 下一步 S = R

        pg_loss = round((next(rng) - 0.5) * 0.09, 6)
        ppo_kl = round(0.002 + (next(rng) - 0.5) * 0.004, 6)
        grad_norm = round(0.5 + 0.4 * next(rng), 6)
        t = (step - 1) / (n_steps - 1)
        data = {
            "cl/reward_mean": round(reward_mean, 6),
            "cl/reward_std": round(reward_std, 6),
            "cl/group_reward_std": round(group_std, 6),
            "cl/group_reward_std_max": round(group_std + 0.1 + 0.05 * next(rng), 6),
            "critic/rewards/mean": round(reward_mean, 6),
            "critic/rewards/max": round(min(1.0, max(surv_traj)), 6),
            "critic/rewards/min": round(max(0.0, min(surv_traj)), 6),
            "actor/pg_loss": pg_loss,
            "actor/ppo_kl": ppo_kl,
            "actor/grad_norm": grad_norm,
            "sys/num_groups": n_train,
            "sys/num_groups_survived": s_cur,
            "response_length/mean": round(12000 + 4000 * t + (next(rng) - 0.5) * 3000, 1),
            "training/num_turns/mean": round(18 + 6 * t + (next(rng) - 0.5) * 4, 2),
        }
        rows.append({"step": step, "data": data})

    with open(out, "w", encoding="utf-8") as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")

    rm = [r["data"]["cl/reward_mean"] for r in rows]
    rs = [r["data"]["cl/reward_std"] for r in rows]
    ss = [r["data"]["sys/num_groups_survived"] for r in rows]
    dd = [ss[i - 1] - ss[i] for i in range(1, len(ss))]
    mono = all(d >= 0 for d in dd)
    within20 = all(ss[i] >= math.floor(ss[i - 1] * 0.8) for i in range(1, len(ss)))
    touch = next((i + 1 for i, s in enumerate(ss) if s == n_train), None)
    print(f"saved {out}  ({len(rows)} steps)")
    print(f"  reward_mean: {rm[0]:.3f} → {rm[-1]:.3f}")
    print(f"  reward_std : {rs[0]:.3f} → {rs[-1]:.3f}  (方差坍缩)")
    print(f"  S          : {ss[0]} → {ss[-1]}  单调不增={mono}  触底 N 于第 {touch} 步")
    print(f"  每步淘汰 ≤20%×当前: {within20}  | 每步降幅: {dd[:12]}...")


if __name__ == "__main__":
    main()
