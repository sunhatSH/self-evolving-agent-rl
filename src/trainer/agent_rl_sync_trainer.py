"""Self-evolving RL trainer: oversample + 淘汰 + 选组 (advantage-driven).

继承 recipe_custom 的 CustomPPOTrainerSync (custom_sync), 重写 _step_once:
  1. sample 取 S 组 (超生量 = train_batch_size, verl 一步处理 S 个 prompt)
  2. reward → balance → old_log_prob → ref_log_prob → advantage (全 S 组算)
  3. ★选组层★: 淘汰(后20%且<0.3 丢 query) → 从 R 组按组内 advantage 绝对值选 N 组
  4. _update_actor 只用选中的 N×n 条 (select_keys 构造子集 KVBatchMeta)

新范式核心: 推理超生 S×n, 训练只用 N×n (advantage 最强的 N 组). 多轮在跨 step 层,
不在 session 内 (harness 已回归单轮).

注册: @register_trainer("agent_rl_sync"); config 里 trainer.v1.trainer_mode = agent_rl_sync.
"""

from __future__ import annotations

import logging
from typing import Any

import numpy as np

# transfer_queue / KVBatchMeta / verl: 训练侧才有, off-cluster 降级
try:
    import transfer_queue as tq
    from transfer_queue import KVBatchMeta
except ImportError:  # off-cluster (CPU 单测环境)
    tq = None  # type: ignore[assignment]
    KVBatchMeta = None  # type: ignore[assignment]

try:
    from verl.trainer.ppo.v1.trainer_base import register_trainer
    from verl.utils.debug import marked_timer
    _HAS_VERL = True
except ImportError:
    _HAS_VERL = False
    # 降级 stubs, 让模块 off-cluster 可 import 可测
    def register_trainer(name):  # type: ignore[no-redef]
        def _wrap(cls):
            return cls
        return _wrap

    class _marked_timer:  # type: ignore[no-redef]
        def __init__(self, *a, **k):
            pass

        def __call__(self, fn):
            import functools

            @functools.wraps(fn)
            def wrapper(*args, **kwargs):
                return fn(*args, **kwargs)

            return wrapper

    marked_timer = _marked_timer()  # type: ignore[assignment]

# recipe_custom 的 SyncTrainer (custom_sync) — 延迟 import, off-cluster 可降级
try:
    from recipe_custom.trainer.v1.sync_trainer import CustomPPOTrainerSync
except Exception as exc:  # noqa: BLE001 -- recipe_custom absent off-cluster
    CustomPPOTrainerSync = None  # type: ignore[assignment]
    _IMPORT_ERR = exc
else:
    _IMPORT_ERR = None

logger = logging.getLogger(__name__)


def _group_keys_by_uid(keys: list[str]) -> dict[str, list[str]]:
    """把 batch.keys 按 uid 分组. key 格式: {uid}_{session_id}_{index}.

    同一 uid 的所有 session/index 归为一组 (GRPO 组). 返回 {uid: [key, ...]}.
    """
    groups: dict[str, list[str]] = {}
    for key in keys:
        parts = key.rsplit("_", 2)
        if len(parts) == 3:
            uid = parts[0]
        else:
            uid = key  # 退化: 无 session/index 的 key 自成一组
        groups.setdefault(uid, []).append(key)
    return groups


def _read_group_rewards(
    keys: list[str], partition_id: str
) -> dict[str, float]:
    """读每组的 reward (rm_scores). 返回 {uid: 组内最大 reward} (该组最优轨迹的得分).

    rm_scores 是 [B, R] 张量 (R = response_length), 每行一个轨迹. 组内取 max 作为
    "该组最优轨迹得分" (用于淘汰判断: 后20%且<0.3).
    """
    if tq is None:
        return {}
    fields = ["uid", "rm_scores"]
    data = tq.kv_batch_get(keys=keys, partition_id=partition_id, select_fields=fields)
    # uid: 每行对应的 uid (可能含 session/index 后缀, 需归并)
    uids_raw = data["uid"]
    if hasattr(uids_raw, "tolist"):
        uids = uids_raw.tolist()
    else:
        uids = list(uids_raw)
    rm = data["rm_scores"]  # nested tensor [B, R] 或 offsets
    # rm 可能是 NestedTensor; 取每行的 sum (一条轨迹的总 reward) 作为该轨迹得分
    try:
        # to_padded_tensor 后 [B, R], sum(dim=1) → [B]
        rm_padded = rm.to_padded_tensor(padding=0.0) if hasattr(rm, "to_padded_tensor") else rm
        scores = rm_padded.sum(dim=-1).float().tolist() if hasattr(rm_padded, "sum") else None
    except Exception:  # noqa: BLE001
        scores = None
    if scores is None:
        # 退化: 无法读 reward, 返回空 (调用方处理)
        return {}

    # 归并: uid → 组内最大 score
    group_best: dict[str, float] = {}
    for uid_full, score in zip(uids, scores, strict=False):
        # uid_full 可能是 {uid}_{session}_{index}, 取前缀
        uid = uid_full.rsplit("_", 2)[0] if isinstance(uid_full, str) and uid_full.count("_") >= 2 else str(uid_full)
        s = float(score)
        if uid not in group_best or s > group_best[uid]:
            group_best[uid] = s
    return group_best


def _read_group_advantages(
    keys: list[str], partition_id: str
) -> dict[str, float]:
    """读每组的 advantage. 返回 {uid: 组内 advantage 绝对值的均值} (该组的梯度强度代理).

    advantage 已由 _compute_advantage 写回 TQ. 组内取 |adv|.mean() 作为该组的学习信号强度.
    """
    if tq is None:
        return {}
    fields = ["uid", "advantages"]
    data = tq.kv_batch_get(keys=keys, partition_id=partition_id, select_fields=fields)
    uids_raw = data["uid"]
    uids = uids_raw.tolist() if hasattr(uids_raw, "tolist") else list(uids_raw)
    adv = data["advantages"]
    try:
        adv_padded = adv.to_padded_tensor(padding=0.0) if hasattr(adv, "to_padded_tensor") else adv
        # 每条轨迹的 advantage: 在 response_mask 区域取 |adv|.mean()
        adv_abs = adv_padded.abs().float()
        # [B, R] → 每行 mean (近似; 精确应 mask, 但作选组代理足够)
        per_row = adv_abs.mean(dim=-1).tolist() if hasattr(adv_abs, "mean") else None
    except Exception:  # noqa: BLE001
        per_row = None
    if per_row is None:
        return {}

    group_strength: dict[str, list[float]] = {}
    for uid_full, strength in zip(uids, per_row, strict=False):
        uid = uid_full.rsplit("_", 2)[0] if isinstance(uid_full, str) and uid_full.count("_") >= 2 else str(uid_full)
        group_strength.setdefault(uid, []).append(float(strength))
    # 组内取均值作为该组梯度强度
    return {uid: float(np.mean(vals)) for uid, vals in group_strength.items()}


def select_groups(
    batch: KVBatchMeta,
    *,
    n_select: int,
    group_size: int = 8,
    drop_bottom_pct: float = 0.2,
    drop_below: float = 0.5,
) -> tuple[KVBatchMeta, list[str]]:
    """选组层: 淘汰(S→R) + 选组(R→N). 返回 (训练子集, 存活组 uids R).

    两件独立的事:
    - 淘汰: S 组 → R 组. 丢烂组(该组最优 reward 同时满足 后 drop_bottom_pct% 且 < drop_below).
      同时满足才丢 → ≥80% 存活. R 是【下一轮的 S】(存活组做追问), 也是这一轮训练的候选池.
    - 选组: 从 R 组按组内 advantage 绝对值均值降序, 选梯度最优 N 组训练.

    返回:
      - 训练子集 KVBatchMeta (select_keys, batch_size = N × group_size)
      - 存活组 uids (R 个, 供 _step_once 存下, 下一轮对这些组追问)
    """
    all_groups = _group_keys_by_uid(list(batch.keys))
    # 只保留完整组(恰好 group_size 条). 残缺组丢弃(GRPO 要完整组).
    groups = {uid: keys for uid, keys in all_groups.items() if len(keys) == group_size}
    n_incomplete = len(all_groups) - len(groups)
    if n_incomplete:
        print(f"[select] dropped {n_incomplete} incomplete groups (<{group_size} sessions)", flush=True)

    # 读每组最优 reward
    group_best = _read_group_rewards(list(batch.keys), batch.partition_id)
    if not group_best:
        print("[select] cannot read rewards, skip selection", flush=True)
        all_keys = []
        for uid in groups:
            all_keys.extend(groups[uid])
        return (batch.select_keys(all_keys) if all_keys else batch), list(groups.keys())
    group_best = {uid: group_best[uid] for uid in groups if uid in group_best}

    # ── 淘汰: S → R (后 drop_bottom_pct% 且 < drop_below 同时满足才丢) ──
    best_scores = sorted(group_best.values())
    n = len(best_scores)
    if n > 0:
        threshold_rank = best_scores[min(int(np.ceil(n * drop_bottom_pct)), n - 1)]
        dropped_uids = {
            uid for uid, score in group_best.items()
            if score <= threshold_rank and score < drop_below
        }
    else:
        dropped_uids = set()
    survived_uids = [uid for uid in groups if uid not in dropped_uids]  # R 个
    print(
        f"[select] eliminate: S={len(groups)} dropped={len(dropped_uids)} "
        f"(bottom{drop_bottom_pct*100:.0f}% & <{drop_below}) → R={len(survived_uids)}",
        flush=True,
    )

    # ── 选组: 从 R 组按 advantage 选梯度最优 N 组训练 ──
    if len(survived_uids) <= n_select:
        # R <= N, 全部训练
        selected_uids = survived_uids
    else:
        group_adv = _read_group_advantages(list(batch.keys), batch.partition_id)
        if not group_adv:
            ranked = sorted(survived_uids, key=lambda u: -group_best.get(u, 0.0))
        else:
            ranked = sorted(survived_uids, key=lambda u: -group_adv.get(u, 0.0))
        selected_uids = ranked[:n_select]
    print(
        f"[select] train: R={len(survived_uids)} → N={len(selected_uids)} "
        f"({len(selected_uids) * group_size} rows)",
        flush=True,
    )

    # 构造训练子集: 选中 uid 的所有 keys
    selected_keys = []
    for uid in selected_uids:
        selected_keys.extend(groups[uid])
    train_batch = batch.select_keys(selected_keys) if selected_keys else batch
    return train_batch, survived_uids


if CustomPPOTrainerSync is not None:

    @register_trainer("agent_rl_sync")
    class AgentRLSyncTrainer(CustomPPOTrainerSync):
        """自进化 RL trainer: 超生 + 淘汰 + 选组 (advantage-driven) + 跨 step 追问.

        与 custom_sync 的区别:
        1. _step_once 在 _compute_advantage 之后、_update_actor 之前插入 select_groups.
        2. _step_once 末尾存跨 step seeds(最优轨迹+observer_report).
        3. _add_batch_to_generate: step 1 从 dataloader, step 2+ 用 Questioner 产的新 query.
        """

        def __init__(self, config):
            super().__init__(config)
            self._cross_step_seeds: list = []  # 跨 step seeds(Questioner 产的新 query)
            self._should_stop: bool = False  # 训练终止标志(坍缩/崩溃触发)

        def _check_collapse(self, metrics: dict) -> None:
            """检测训练坍缩/崩溃, 触发则设 _should_stop=True.

            自进化系统无人值守, 需在以下任一条件触发时终止:
            - 奖励标准差 → 0 (策略多样性坍缩)
            - 优势标准差 → 0 (无梯度信号)
            - pg_loss 出现 NaN/Inf
            - ppo_kl 超阈值 (策略偏离过远)
            - 存活组数 < 训练组数 (超生池耗尽)
            """
            import math

            reward_std = metrics.get("sys/reward_std")
            adv_std = metrics.get("sys/advantage_std")
            pg_loss = metrics.get("actor/pg_loss")
            ppo_kl = metrics.get("actor/ppo_kl")
            num_groups = metrics.get("sys/num_groups")
            n_select = self.config.data.get("gen_batch_size", 0)

            reasons: list[str] = []

            if reward_std is not None and reward_std < 1e-6:
                reasons.append(f"reward_std={reward_std:.2e} → 0 (策略多样性坍缩)")
            if adv_std is not None and adv_std < 1e-6:
                reasons.append(f"advantage_std={adv_std:.2e} → 0 (无梯度信号)")
            if pg_loss is not None and (math.isnan(pg_loss) or math.isinf(pg_loss)):
                reasons.append(f"pg_loss={pg_loss} (NaN/Inf)")
            if ppo_kl is not None and abs(ppo_kl) > 10.0:
                reasons.append(f"ppo_kl={ppo_kl:.4f} > 10.0 (策略偏离过远)")
            if num_groups is not None and n_select > 0 and num_groups < n_select:
                reasons.append(f"num_groups={num_groups} < n_select={n_select} (超生池耗尽)")

            if reasons:
                self._should_stop = True
                print(
                    f"[monitor] step {self.global_steps}: TRAINING STOP — {'; '.join(reasons)}",
                    flush=True,
                )
                metrics["sys/should_stop"] = 1.0

        def _add_batch_to_generate(self):
            """跨 step: step 1 从 dataloader, step 2+ 用 Questioner 产的新 query + dataloader 补齐.

            verl 约束: num_prompts 必须是 gen_batch_size 的整数倍.
            故补齐数向上取整到 gen_batch_size 的倍数.
            """
            train_batch_size = self.config.data.train_batch_size
            gen_batch_size = self.config.data.get("gen_batch_size", None) or train_batch_size
            if self._cross_step_seeds:
                # step 2+: 用跨 step seeds(Questioner 产的新 query)构造 batch
                try:
                    from agents.cross_step import build_cross_step_batch
                    from verl.utils import tensordict_utils as tu
                    n_cross = len(self._cross_step_seeds)
                    print(f"[cross-step] step {self.global_steps}: {n_cross} cross-step seeds", flush=True)

                    # cross-step seeds 不够 train_batch_size → 用 dataloader 补齐
                    if n_cross < train_batch_size:
                        n_need = train_batch_size - n_cross
                        # 向上取整到 gen_batch_size 的倍数 (verl 约束)
                        n_need = ((n_need + gen_batch_size - 1) // gen_batch_size) * gen_batch_size
                        print(f"[cross-step] supplementing {n_need} from dataloader (cross-step {n_cross} < train_batch {train_batch_size}, rounded to gen_batch {gen_batch_size})", flush=True)
                        # 先取 dataloader 的补齐部分
                        supplement_batch = self._next_train_batch(num_prompts=n_need)
                        # 再取 cross-step seeds 部分
                        cross_batch_dict = build_cross_step_batch(self._cross_step_seeds)
                        if cross_batch_dict is not None:
                            cross_batch = tu.get_tensordict(cross_batch_dict)
                            tu.assign_non_tensor_data(cross_batch, "global_steps", self.global_steps)
                            # 合并: cross-step + dataloader
                            batch = tu.concat_tensordict([cross_batch, supplement_batch])
                            _, rollout_metrics = self._submit_batch_to_rollout(batch)
                            print(f"[cross-step] step {self.global_steps}: submitted {n_cross} cross-step + {n_need} dataloader = {n_cross + n_need}", flush=True)
                            return rollout_metrics
                    else:
                        # cross-step seeds 够, 直接用(取前 train_batch_size 个)
                        cross_batch_dict = build_cross_step_batch(self._cross_step_seeds[:train_batch_size])
                        if cross_batch_dict is not None:
                            batch = tu.get_tensordict(cross_batch_dict)
                            tu.assign_non_tensor_data(batch, "global_steps", self.global_steps)
                            _, rollout_metrics = self._submit_batch_to_rollout(batch)
                            print(f"[cross-step] step {self.global_steps}: submitted {train_batch_size} cross-step seeds", flush=True)
                            return rollout_metrics
                except Exception as exc:  # noqa: BLE001 -- fallback to dataloader
                    print(f"[cross-step] cross-step batch failed ({exc}), fallback to dataloader", flush=True)

            # step 1 or fallback: 从 dataloader 取
            batch = self._next_train_batch()
            _, rollout_metrics = self._submit_batch_to_rollout(batch)
            return rollout_metrics

        def _step_once(
            self,
            metrics: dict,
            timing_raw: dict,
            sample_batch_size: int,
            batch: KVBatchMeta | None = None,
        ) -> KVBatchMeta:
            with marked_timer("gen", timing_raw, color="red"):
                self.on_sample_begin()
                if batch is None:
                    batch, off_policy_metrics = self.replay_buffer.sample(
                        global_steps=self.global_steps,
                        partition_id="train",
                        batch_size=sample_batch_size,
                    )
                    metrics.update(off_policy_metrics)
                batch.extra_info["temperature"] = self.config.actor_rollout_ref.rollout.temperature
                self.on_sample_end()

            if self.reward_loop_manager.reward_loop_worker_handles is None:
                with marked_timer("reward", timing_raw, color="yellow"):
                    batch = self._compute_reward_colocate(batch, metrics=metrics)
            batch = self._balance_batch(batch, metrics=metrics)

            with marked_timer("old_log_prob", timing_raw, color="blue"):
                batch = self._compute_old_log_prob(batch, metrics=metrics)
            if self.use_reference_policy:
                with marked_timer("ref", timing_raw, color="olive"):
                    batch = self._compute_ref_log_prob(batch, metrics=metrics)
            if self.use_critic:
                with marked_timer("values", timing_raw, color="cyan"):
                    batch = self._compute_values(batch, metrics=metrics)
            with marked_timer("adv", timing_raw, color="brown"):
                batch = self._compute_advantage(batch, metrics=metrics)

            # ★ 训练监控: 计算坍缩指标写入 metrics ★
            try:
                from trainer.agent_rl_runner import compute_std_metrics
                std_metrics = compute_std_metrics(batch)
                if std_metrics:
                    metrics.update(std_metrics)
                    print(
                        f"[monitor] step {self.global_steps}: "
                        f"reward_std={std_metrics.get('sys/reward_std', -1):.4f} "
                        f"adv_std={std_metrics.get('sys/advantage_std', -1):.4f} "
                        f"group_std={std_metrics.get('sys/group_reward_std', -1):.4f}",
                        flush=True,
                    )
            except Exception as exc:  # noqa: BLE001
                print(f"[monitor] std metrics failed: {exc}", flush=True)

            # ★ 选组层: 淘汰(S→R) + 选组(R→N) ★
            # 返回训练子集 + 存活组 uids(R). R 组存下 → 下一轮对这些组追问(S=R).
            n_select = self.config.data.get("gen_batch_size", sample_batch_size)
            group_size = self.config.actor_rollout_ref.rollout.n
            full_batch_keys = list(batch.keys)  # 淘汰前的全 S 组 keys(cross-step 取快照用)
            full_partition = batch.partition_id
            with marked_timer("select", timing_raw, color="magenta"):
                batch, survived_uids = select_groups(
                    batch,
                    n_select=n_select,
                    group_size=group_size,
                    drop_bottom_pct=0.2,
                    drop_below=0.5,
                )
            self._survived_uids = survived_uids  # R 组: 下一轮追问对象

            # 兜底: 选组后 batch 太小(< 1 组) → skip 该 step, 不进 update_actor
            if len(batch.keys) < group_size:
                print(
                    f"[select] after selection: {len(batch.keys)} rows < {group_size} "
                    f"(1 group), skip training update at global_steps={self.global_steps}",
                    flush=True,
                )
                metrics["rollout/selection_skip_step"] = 1.0
                metrics["rollout/skipped_step"] = 1.0
                # 抛 _EmptyBatchSkip 让 empty_batch_skip_patch 的 step() 包装捕获
                try:
                    from trainer.empty_batch_skip_patch import _EmptyBatchSkip
                    raise _EmptyBatchSkip(
                        f"selection skip: {len(batch.keys)} rows at step {self.global_steps}"
                    )
                except ImportError:
                    return None  # fallback if patch not loaded

            if self.use_critic:
                with marked_timer("update_critic", timing_raw, color="pink"):
                    batch = self._update_critic(batch, metrics=metrics)
            if self.config.trainer.critic_warmup <= self.global_steps:
                with marked_timer("update_actor", timing_raw, color="red"):
                    batch = self._update_actor(batch, metrics=metrics)

            # ★ 训练监控: 检测坍缩/崩溃, 触发则终止自进化 ★
            self._check_collapse(metrics)

            # 若坍缩/崩溃触发, 跳过跨步种子生成, 让 fit() 循环检测到 _should_stop 后终止
            if self._should_stop:
                print(
                    f"[monitor] step {self.global_steps}: collapse detected, "
                    f"skipping cross-step seed generation, training will stop",
                    flush=True,
                )
                return batch

            # ★ 跨 step: 对存活的 R 组(淘汰后)每组产新 seed → 下一轮 S=R ★
            # 用淘汰前的全 keys(full_batch_keys), 限定到存活 uids(survived_uids).
            # 每个存活组: 取最优轨迹 → observer LLM 概括 + 沙箱快照 → Questioner 产新 query.
            try:
                from agents.cross_step import generate_cross_step_seeds
                survived = getattr(self, "_survived_uids", [])
                print(
                    f"[cross-step] step {self.global_steps}: generating seeds for R={len(survived)} survived groups...",
                    flush=True,
                )
                self._cross_step_seeds = generate_cross_step_seeds(
                    full_batch_keys,
                    full_partition,
                    group_size,
                    survived_uids=survived,
                )
                print(
                    f"[cross-step] step {self.global_steps}: generated {len(self._cross_step_seeds)} seeds (next S)",
                    flush=True,
                )
            except Exception as exc:  # noqa: BLE001 -- best-effort, don't crash training
                print(f"[cross-step] seed generation failed: {exc}", flush=True)
                self._cross_step_seeds = []

            return batch

else:  # off-cluster: 占位, import 不报错
    class AgentRLSyncTrainer:  # type: ignore[no-redef]
        """Off-cluster placeholder (recipe_custom absent)."""

        def __init__(self, *args, **kwargs):
            raise RuntimeError(
                f"AgentRLSyncTrainer requires recipe_custom (got import error: {_IMPORT_ERR})"
            )
