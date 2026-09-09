"""verl RayPPOTrainer construction for the self-evolving agentic-RL system.

Wraps ``verl.trainer.main_ppo.TaskRunner`` to run standard GRPO over multi-agent
sandbox rollouts. Rollout is verl's native agent_loop (recipe_custom
``RayPPOTrainerV1`` when available; standard ``RayPPOTrainer`` off-cluster), so
the actor gets logprobs, tool-output truncation, and rollout correction for
free. Reward is grounded on the Observer's diff-driven ``ObservationReport`` via
the ``observer`` reward manager.

This runner deliberately does NOT install any experience-replay buffer or custom
continual-learning loss -- training uses verl's stock PPO/GRPO objective. The
system's contribution is the multi-agent sampling + sandbox environment +
diff-driven reward, validated by a plain GRPO run.
"""

from __future__ import annotations

from typing import Any

from omegaconf import OmegaConf


def merge_verl_config(cfg: Any) -> Any:
    """Ensure the OmegaConf object is compatible with verl RayPPOTrainer.

    verl expects a full Hydra-style config. Experiment yamls inherit
    ``configs/base.yaml``; additional verl fields are supplied via experiment
    overrides or a verl defaults yaml on the cluster.
    """
    if not OmegaConf.is_config(cfg):
        cfg = OmegaConf.create(cfg)
    OmegaConf.set_struct(cfg, False)
    return cfg


def compute_std_metrics(batch: Any) -> dict[str, float]:
    """Dispersion metrics verl's ``compute_data_metrics`` does NOT emit.

    verl logs reward/advantage mean/max/min but no std, and no GRPO group-level
    spread. Those are exactly what we watch to catch a collapsing policy
    (advantage std -> 0) or degenerate groups (all trajectories in a prompt's
    group scoring identically -> 0 learning signal). Emitted under the ``sys/``
    namespace so they never collide with verl's native keys.

    Computed from the RL batch AFTER ``compute_advantage`` (verl fit runs it
    before ``_update_actor``), so ``token_level_rewards`` / ``advantages`` /
    ``response_mask`` are present, and ``non_tensor_batch["uid"]`` identifies the
    GRPO group. Returns ``{}`` when torch or the required fields are absent
    (off-cluster / unexpected layout) rather than raising.

    Keys:
      - sys/reward_std          : std of per-sequence reward (sum over tokens)
      - sys/reward_mean         : mean of per-sequence reward (cross-check vs verl)
      - sys/advantage_std       : std of valid (masked) advantages
      - sys/group_reward_std    : mean over groups of the within-group reward std
                                  (GRPO "group std" -- 0 => degenerate groups)
      - sys/group_reward_std_max: worst (largest) within-group reward std
      - sys/num_groups          : number of distinct uids in the batch
    """
    try:
        import torch
    except ImportError:
        return {}
    bb = getattr(batch, "batch", None)
    if bb is None:
        return {}
    try:
        tlr = bb.get("token_level_rewards")
        resp_mask = bb.get("response_mask")
        adv = bb.get("advantages")
    except Exception:  # noqa: BLE001 -- TensorDict access variability
        tlr = resp_mask = adv = None
    if tlr is None:
        return {}

    out: dict[str, float] = {}
    seq_reward = tlr.sum(dim=-1).float()  # [B]
    if seq_reward.numel() > 0:
        out["sys/reward_std"] = float(seq_reward.std(unbiased=False).item())
        out["sys/reward_mean"] = float(seq_reward.mean().item())

    if adv is not None and resp_mask is not None:
        valid = torch.masked_select(adv, resp_mask.bool())
        if valid.numel() > 0:
            out["sys/advantage_std"] = float(valid.std(unbiased=False).item())

    # GRPO group spread: std of per-sequence reward within each uid group.
    uids = None
    nt = getattr(batch, "non_tensor_batch", None)
    if isinstance(nt, dict):
        uids = nt.get("uid")
    if uids is not None and seq_reward.numel() == len(uids):
        groups: dict[Any, list[float]] = {}
        for u, r in zip(list(uids), seq_reward.tolist(), strict=False):
            groups.setdefault(u, []).append(r)
        stds = []
        for vals in groups.values():
            if len(vals) > 1:
                t = torch.tensor(vals)
                stds.append(float(t.std(unbiased=False).item()))
            else:
                stds.append(0.0)
        if stds:
            out["sys/group_reward_std"] = float(sum(stds) / len(stds))
            out["sys/group_reward_std_max"] = float(max(stds))
        out["sys/num_groups"] = float(len(groups))
    return out


class AgentRLTaskRunner:
    """``verl.trainer.main_ppo.TaskRunner`` variant for multi-agent GRPO.

    Same worker wiring as verl's stock TaskRunner; the only differences are:
      1. rollout uses recipe_custom's native agent_loop when on-cluster;
      2. the ``observer`` reward manager is imported so reward is grounded on the
         Observer diff report;
      3. NO buffer / NO custom CL loss -- stock PPO/GRPO objective.

    Usage::

        run_agent_ppo(cfg)  # ray.init + remote AgentRLTaskRunner.run
    """

    def __init__(self):
        self.role_worker_mapping = {}
        self.mapping = {}

    # ---- Worker registration delegated to verl TaskRunner helpers ---------
    def add_actor_rollout_worker(self, config):
        from verl.trainer.main_ppo import TaskRunner

        return TaskRunner.add_actor_rollout_worker(self, config)

    def add_critic_worker(self, config):
        from verl.trainer.main_ppo import TaskRunner

        TaskRunner.add_critic_worker(self, config)

    def init_resource_pool_mgr(self, config):
        from verl.trainer.main_ppo import TaskRunner

        return TaskRunner.init_resource_pool_mgr(self, config)

    def add_reward_model_resource_pool(self, config):
        from verl.trainer.main_ppo import TaskRunner

        TaskRunner.add_reward_model_resource_pool(self, config)

    def add_teacher_model_resource_pool(self, config):
        from verl.trainer.main_ppo import TaskRunner

        TaskRunner.add_teacher_model_resource_pool(self, config)

    def add_ref_policy_worker(self, config, ref_policy_cls):
        from verl.trainer.main_ppo import TaskRunner

        return TaskRunner.add_ref_policy_worker(self, config, ref_policy_cls)

    # ---- Main entry -------------------------------------------------------
    def run(self, config, resume_from: str | None = None) -> None:
        """Mirror ``TaskRunner.run`` with stock GRPO (no buffer, no CL loss)."""
        import os
        import socket
        from pprint import pprint

        from verl.trainer.main_ppo import create_rl_dataset, create_rl_sampler
        from verl.trainer.ppo.ray_trainer import RayPPOTrainer
        from verl.trainer.ppo.utils import need_critic, need_reference_policy
        from verl.utils import hf_processor, hf_tokenizer
        from verl.utils.config import validate_config
        from verl.utils.dataset.rl_dataset import collate_fn
        from verl.utils.fs import copy_to_local

        config = merge_verl_config(config)
        print(f"AgentRLTaskRunner hostname: {socket.gethostname()}")
        pprint(OmegaConf.to_container(config, resolve=True))
        # Rebuild config from a plain container so list-valued nodes (e.g.
        # trainer.logger = ['console','swanlab']) become native lists instead of
        # ListConfig nodes. OmegaConf 2.3 resolve() rejects ListConfig as a
        # "non-primitive" value; recreating from container sidesteps that.
        config = OmegaConf.create(OmegaConf.to_container(config, resolve=False))
        OmegaConf.resolve(config)

        # Import the custom reward manager so its @register("observer") fires
        # BEFORE RayPPOTrainer resolves reward.reward_manager.name. It folds the
        # per-row observer diff (non_tensor "observer_report") into extra_info so
        # the training judge grounds completion on real state. No-op when verl's
        # reward-loop registry is unavailable (off-cluster).
        try:
            import trainer.observer_reward_manager  # noqa: F401
        except Exception as exc:  # noqa: BLE001 -- registry absent off-cluster
            print(
                f"[agent-rl] observer reward manager not registered ({exc}); "
                "using configured manager",
                flush=True,
            )

        actor_rollout_cls, ray_worker_group_cls = self.add_actor_rollout_worker(config)
        self.add_critic_worker(config)
        self.add_reward_model_resource_pool(config)
        self.add_teacher_model_resource_pool(config)
        self.add_ref_policy_worker(config, actor_rollout_cls)

        validate_config(
            config=config,
            use_reference_policy=need_reference_policy(config),
            use_critic=need_critic(config),
        )

        local_path = copy_to_local(
            config.actor_rollout_ref.model.path,
            use_shm=config.actor_rollout_ref.model.get("use_shm", False),
        )
        trust_remote_code = config.data.get("trust_remote_code", False)
        tokenizer = hf_tokenizer(local_path, trust_remote_code=trust_remote_code)
        processor = hf_processor(local_path, trust_remote_code=trust_remote_code, use_fast=True)

        resource_pool_manager = self.init_resource_pool_mgr(config)

        # verl HARD-REQUIRES a non-empty val dataloader: RayPPOTrainer._create_dataloader
        # always builds val from config.data.val_files and asserts len>=1
        # regardless of test_freq/val_before_train. We evaluate offline after
        # training (test_freq=-1), so alias val_files -> train_files whenever val
        # is EMPTY or points at a missing file (verl's create_rl_dataset dies on
        # None/missing). Set it ON config.data so verl's internal re-build sees it.
        val_files = config.data.get("val_files", None)
        _val_missing = bool(val_files) and isinstance(val_files, str) and not os.path.exists(val_files)
        if not val_files or _val_missing:
            reason = "empty" if not val_files else f"missing file ({val_files})"
            OmegaConf.update(config, "data.val_files", config.data.train_files, force_add=True)
            print(
                f"[agent-rl] data.val_files {reason} -> aliasing to train_files "
                "(verl requires a loadable val dataloader; in-loop validation is "
                "disabled, so this placeholder is never used to validate).",
                flush=True,
            )

        train_dataset = create_rl_dataset(
            config.data.train_files,
            config.data,
            tokenizer,
            processor,
            is_train=True,
            max_samples=config.data.get("train_max_samples", -1),
        )
        val_dataset = create_rl_dataset(
            config.data.val_files,
            config.data,
            tokenizer,
            processor,
            is_train=False,
            max_samples=config.data.get("val_max_samples", -1),
        )
        train_sampler = create_rl_sampler(config.data, train_dataset)

        # Use recipe_custom's RayPPOTrainerV1 (subclass of RayPPOTrainer, same
        # ctor signature). In init_workers it swaps rollout for recipe_custom's
        # native agent_loop RolloutManager -> rollout gets logprobs, tool-output
        # truncation, rollout_correction, Qwen3.5 GDN variable-length packing for
        # free. Fall back to stock RayPPOTrainer off-cluster so import stays sane.
        _TrainerCls = RayPPOTrainer
        try:
            from recipe_custom.ray_trainer_v1 import RayPPOTrainerV1

            _TrainerCls = RayPPOTrainerV1
            print("[agent-rl] using recipe_custom.RayPPOTrainerV1 (native agent_loop rollout)", flush=True)
        except Exception as exc:  # noqa: BLE001 -- recipe_custom absent off-cluster
            print(
                f"[agent-rl] recipe_custom unavailable ({exc}); falling back to stock RayPPOTrainer",
                flush=True,
            )

        trainer = _TrainerCls(
            config=config,
            tokenizer=tokenizer,
            processor=processor,
            role_worker_mapping=self.role_worker_mapping,
            resource_pool_manager=resource_pool_manager,
            ray_worker_group_cls=ray_worker_group_cls,
            train_dataset=train_dataset,
            val_dataset=val_dataset,
            collate_fn=collate_fn,
            train_sampler=train_sampler,
        )
        trainer.init_workers()
        # NOTE: no set_loss_fn / no buffer hooks -- stock PPO/GRPO objective.

        # Resume: verl's fit() -> _load_checkpoint() does this natively. Drive it
        # via resume_mode rather than calling any private loader here.
        if resume_from:
            OmegaConf.update(config, "trainer.resume_mode", "resume_path", force_add=True)
            OmegaConf.update(config, "trainer.resume_from_path", str(resume_from), force_add=True)
        trainer.fit()


def run_agent_ppo(cfg: Any, resume_from: str | None = None) -> None:
    """Ray entry: init Ray and drive a remote ``AgentRLTaskRunner.run``.

    Mirrors verl's ``main_ppo`` bootstrap but with our task runner. Kept thin so
    it can be called from ``agent_rl_main`` or a smoke test.
    """
    import ray

    if not ray.is_initialized():
        runtime_env = {
            "env_vars": {
                "TOKENIZERS_PARALLELISM": "true",
                "NCCL_DEBUG": "WARN",
                "VLLM_LOGGING_LEVEL": "WARN",
            }
        }
        ray.init(runtime_env=runtime_env)

    runner = ray.remote(num_cpus=1)(AgentRLTaskRunner).remote()
    ray.get(runner.run.remote(cfg, resume_from))
