# baseline vs kl 训练统一数据表(2026-09-09)

两个训练各 100 步(4 卡→16 卡语义,step1-100),数据取自 `logs/metrics/cl2r_{baseline,kl}/metrics.jsonl`。
reward 对比图:`eval/results/reward_baseline_vs_kl.png`(左=每步原始;右=10 步滑动平均)。

## 统一数据表(全程 100 步聚合)

| 指标 | baseline (无 CL) | kl (reverse-KL) |
|------|------|------|
| reward_mean | mean 0.513 / min 0.351 / max 0.676 | mean 0.444 / min 0.358 / max 0.519 |
| reward_std(batch) | 0.160 | 0.169 |
| group_reward_std | 0.114 | 0.127 |
| grad_norm | mean 0.211 / max 0.544 | mean 0.182 / max 0.389 |
| total_loss | 0.025 | 0.021 |
| pg_loss | 0.025 | 0.021 |
| entropy | 0.267 | 0.274 |
| ppo_kl | -0.0003 | -0.0004 |
| kl_loss | 无 | 0.0024 |
| replay_loss | 0(不开 buffer) | 0(不开 buffer) |

## 收敛区(最后 20 步)reward_mean

- baseline **0.638**(末步 step100 = 0.631)
- kl **0.497**(末步 step100 = 0.492)

## 关键结论

1. **baseline reward 明显更高**(收敛 0.638 vs 0.497)。kl 项(coef=0.05)把策略拉向 π_ref、限制 reward 上涨——kl_loss 恒 0.0024 极小,但持续约束累积压低收敛 reward ~0.14。
2. **两训练都健康稳定**:grad_norm 0.11-0.54 正常(对比 replay 未修时爆到 185),entropy 0.27 无坍缩,ppo_kl≈0。
3. **kl 的 grad_norm 略低**(0.182 vs 0.211)——kl 正则平滑了梯度,代价是 reward。
4. **replay_loss 两者皆 0** —— baseline/kl 都不开 buffer(replay 是 r 系列才开)。

## 评测

base + cl2r_baseline/global_step_100 + cl2r_kl/global_step_100,均 Pass^3,`scripts/eval_all.sh`。
kl_step100 已加进 MODELS 列表(2026-09-09)。
