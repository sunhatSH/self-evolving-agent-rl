"""verl V1 TaskRunner for the self-evolving agentic-RL system.

This verl build (``/mnt/afs_toolcall/sunhao4/dependencies/verl``) is a V1 /
TransferQueue fork: training goes through ``verl.trainer.main_ppo.run_ppo`` ->
``TaskRunnerV1.run`` (``get_trainer_cls(trainer_mode)`` -> ``tq.init`` ->
``init_agent_loop_manager`` -> ``trainer.fit(manager)``), NOT the stock upstream
``RayPPOTrainer`` + ``create_rl_dataset`` API. Rollout is verl's native V1
agent_loop: ``recipe_custom``'s ``RemoteAgentLoopManager`` drives the sandbox
harness, so the actor gets logprobs, tool-output truncation and rollout
correction for free. Reward is grounded on the Observer's diff-driven
``ObservationReport`` via the ``omni``/``observer`` reward manager + the
``ObserverDiffHook``.

We do NOT fork verl -- we use its official recipe hook: ``run_ppo`` accepts a
``task_runner_class`` (main_ppo.py "For recipe to change TaskRunner"). Our
``AgentRLTaskRunnerV1`` replicates the stock ``TaskRunnerV1.run`` three steps
WITHOUT any experience-replay buffer or custom continual-learning loss -- stock
PPO/GRPO objective. The system's contribution is the multi-agent sampling +
sandbox environment + diff-driven reward, validated by a plain GRPO run.
"""

from __future__ import annotations

from typing import Any

from omegaconf import OmegaConf


def merge_verl_config(cfg: Any) -> Any:
    """Ensure the OmegaConf object is compatible with verl.

    verl expects a full Hydra-style config. Experiment yamls inherit
    ``configs/base.yaml`` (+ ``_generated_ppo_trainer`` on the cluster); struct
    mode is disabled so runtime aliases (e.g. val_files) can be added.
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


def _make_agent_rl_task_runner_v1():
    """Build the ``@ray.remote`` ``AgentRLTaskRunnerV1`` class (ray import deferred).

    Replicates verl ``TaskRunnerV1.run`` verbatim (get_trainer_cls -> tq.init ->
    trainer.init -> init_agent_loop_manager -> fit) with two additions and ZERO
    CL injection:
      1. import the observer/omni reward manager so its ``@register`` fires before
         the trainer resolves ``reward.reward_manager.name``;
      2. import ``observer_hook_register`` so the harness ``hooks:`` FQNs
         (``trainer.observer_hook.ObserverDiffHook`` etc.) resolve without editing
         verl source.
    verl ``TaskRunnerV1`` is itself an ``@ray.remote`` actor (can't be subclassed
    then re-decorated), so we replicate rather than subclass. Defined inside a
    function so importing this module off-cluster never requires ray.
    """
    import ray

    @ray.remote
    class AgentRLTaskRunnerV1:
        """V1 TaskRunner: verl-native V1 flow, stock PPO/GRPO, no buffer/CL loss."""

        def __init__(self):
            self.config = None
            self.trainer = None
            self.agent_loop_manager = None

        def init_agent_loop_manager(self):
            # Mirror verl TaskRunnerV1.init_agent_loop_manager: pick the manager by
            # rollout.agent.agent_loop_manager_class (we configure recipe_custom's
            # RemoteAgentLoopManager -> sandbox harness). Falls back to verl's
            # default AgentLoopManagerTQ when unset.
            from verl.trainer.ppo.v1 import AgentLoopManagerTQ
            from verl.utils.import_utils import load_class_from_fqn

            fqn = self.config.actor_rollout_ref.rollout.get("agent", {}).get("agent_loop_manager_class")
            cls = load_class_from_fqn(fqn, "AgentLoopManager") if fqn else AgentLoopManagerTQ
            self.agent_loop_manager = cls.create(
                config=self.config,
                llm_client=self.trainer.get_llm_client(),
                teacher_client=self.trainer.get_teacher_client(),
                reward_loop_worker_handles=self.trainer.get_reward_handles(),
            )

        def run(self, config):
            import os as _os
            from pprint import pprint

            import transfer_queue as tq
            from verl.trainer.ppo.v1 import get_trainer_cls

            # Register the omni/observer reward manager (@register fires on import)
            # so the trainer resolves reward.reward_manager.name -> our manager,
            # which folds the observer diff (extra_info["observer_report"]) into
            # the judge. No-op if the registry is absent.
            try:
                import trainer.observer_reward_manager  # noqa: F401
            except Exception as exc:  # noqa: BLE001 -- registry absent off-cluster
                print(f"[agent-rl] observer reward manager not registered ({exc})", flush=True)

            # Patch the harness hook factory to accept FQN hook names so the
            # agent_loop_config `hooks:` (ObserverDiffHook / MkdirDeliverableHook)
            # load without editing verl source. import == install.
            try:
                import trainer.observer_hook_register  # noqa: F401
            except Exception as exc:  # noqa: BLE001 -- recipe_custom absent off-cluster
                print(f"[agent-rl] observer hook factory patch not installed ({exc})", flush=True)

            # Patch the harness factory to accept FQN harness names so our
            # MultiTurnHermesHarness (agents.multi_turn_harness) loads via
            # agent_loop_config `harness.name` without editing verl source.
            try:
                import trainer.harness_register  # noqa: F401
            except Exception as exc:  # noqa: BLE001 -- recipe_custom absent off-cluster
                print(f"[agent-rl] harness factory patch not installed ({exc})", flush=True)

            trainer_cls = get_trainer_cls(config.trainer.v1.trainer_mode)  # custom_sync
            config.transfer_queue.enable = True

            # verl V1 _init_dataloader unconditionally builds a val dataset and
            # copy_to_local(None) crashes on val_files=null/missing. We evaluate
            # offline (test_freq=-1 / val_before_train=false), so alias val_files
            # -> train_files when empty or pointing at a missing file. Preserves
            # the config's null intent while satisfying V1's hard val requirement.
            _vf = config.data.get("val_files", None)
            _val_missing = bool(_vf) and isinstance(_vf, str) and not _os.path.exists(_vf)
            if not _vf or _val_missing:
                _reason = "empty" if not _vf else f"missing file ({_vf})"
                OmegaConf.update(config, "data.val_files", config.data.train_files, force_add=True)
                print(
                    f"[agent-rl] data.val_files {_reason} -> aliasing to train_files "
                    "(V1 requires a loadable val dataloader; in-loop validation is off, "
                    "so this placeholder is never used to validate).",
                    flush=True,
                )

            pprint(OmegaConf.to_container(config, resolve=True))
            OmegaConf.resolve(config)
            self.config = config

            tq.init(config.transfer_queue)
            try:
                self.trainer = trainer_cls(config=config)
                self.trainer.init()
                # NOTE: no CL injection here -- stock PPO/GRPO objective.
                self.init_agent_loop_manager()
                self.trainer.fit(self.agent_loop_manager)
            finally:
                tq.close()

    return AgentRLTaskRunnerV1


# Module-level lazy proxy so ``run_ppo(cfg, task_runner_class=AgentRLTaskRunnerV1)``
# works without importing ray at module import (off-cluster / unit-test friendly).
# run_ppo calls ``.remote()`` / ``.options(...).remote()`` on it.
class _AgentRLTaskRunnerV1Proxy:
    _cls = None

    def _resolve(self):
        if _AgentRLTaskRunnerV1Proxy._cls is None:
            _AgentRLTaskRunnerV1Proxy._cls = _make_agent_rl_task_runner_v1()
        return _AgentRLTaskRunnerV1Proxy._cls

    def remote(self, *a, **k):
        return self._resolve().remote(*a, **k)

    def options(self, *a, **k):
        return self._resolve().options(*a, **k)


AgentRLTaskRunnerV1 = _AgentRLTaskRunnerV1Proxy()


def run_agent_ppo(cfg: Any, resume_from: str | None = None) -> None:
    """Entry: run GRPO via verl's native V1 ``run_ppo`` with our task runner.

    Mirrors the reference launch (debug_rl_qwen35_9b.sh): ``run_ppo`` +
    ``trainer.use_v1=True`` + ``trainer.v1.trainer_mode=custom_sync`` +
    ``agent_loop_manager_class=RemoteAgentLoopManager``. We do NOT reimplement the
    training framework; we use verl's recipe hook (``run_ppo(config,
    task_runner_class=...)``) to swap in ``AgentRLTaskRunnerV1``.

    Ray workers do NOT inherit the driver's shell env: only vars listed in
    ``runtime_env.env_vars`` reach the actors. ``run_ppo`` builds the runtime_env
    from ``get_ppo_ray_runtime_env(config)`` merged with
    ``config.ray_kwargs.ray_init.runtime_env`` -- so we stuff the vars that must
    reach every actor (PYTHONPATH for source-checkout imports, VERL_USE_EXTERNAL_
    MODULES for per-worker patch registration, reward-judge creds, allocator /
    diagnostics) into that config path BEFORE calling run_ppo.
    """
    import os

    import ray  # noqa: F401 -- ensures verl's ray init path is consistent
    from verl.trainer.main_ppo import run_ppo

    cfg = merge_verl_config(cfg)
    if resume_from:
        OmegaConf.update(cfg, "trainer.resume_mode", "resume_path", force_add=True)
        OmegaConf.update(cfg, "trainer.resume_from_path", str(resume_from), force_add=True)

    # Env that must reach every Ray actor (worker does not inherit driver shell).
    _passthrough: dict[str, str] = {}
    for _k in (
        "PYTHONPATH",                 # source-checkout imports (verl/lightllm/src)
        "VERL_USE_EXTERNAL_MODULES",  # per-worker external patch registration
        "AGENT_RL_FAKE_ROLLOUT",      # debug: skip sandbox, fabricate trajectories
        "AGENT_RL_FAKE_ROLLOUT_LEN",
        "VERIFIER_ENABLE",            # VerifierHook runs in AgentSessionWorker
        "VERIFIER_GEN_MAX_TOKENS",
        # reward judge credentials (RewardLoopWorker in the actor process)
        "TOKENHUB_API_KEY",
        "JUDGE_API_BASE",
        "JUDGE_MODEL",
        "REWARD_API_BASE",
        "REWARD_MODEL",
        "REWARD_API_KEY",
        "REWARD_JUDGE_MAX_TOKENS",
        # sandbox (e2b Tencent) + web tool credentials for the harness
        "E2B_API_KEY",
        "E2B_DOMAIN",
        "SERPER_API_KEY",
        "JINA_API_KEY",
        "HARNESS_LOG_DIR",
        # memory allocator (long-run gateway OOM guard)
        "LD_PRELOAD",
        "MALLOC_CONF",
        "MALLOC_ARENA_MAX",
        "MALLOC_TRIM_THRESHOLD_",
        # file logger + diagnostics
        "VERL_FILE_LOGGER_PATH",
        "NCCL_DEBUG",
        "RAY_DEDUP_LOGS",
        "VERL_LOGGING_LEVEL",
    ):
        _v = os.environ.get(_k)
        if _v is not None:
            _passthrough[_k] = _v

    # NCCL cuMem off (lightllm torch_memory_saver conflicts with NCCL default
    # cuMem P2P -> TP rendezvous deadlock). Overridable via AGENT_RL_NCCL_CUMEM.
    _passthrough.setdefault("NCCL_CUMEM_ENABLE", os.environ.get("AGENT_RL_NCCL_CUMEM", "0"))

    if _passthrough:
        _existing = OmegaConf.select(cfg, "ray_kwargs.ray_init.runtime_env.env_vars") or {}
        OmegaConf.update(
            cfg,
            "ray_kwargs.ray_init.runtime_env.env_vars",
            {**_existing, **_passthrough},
            force_add=True,
        )
        print(f"[agent-rl] forwarding env to Ray workers: {sorted(_passthrough)}", flush=True)

    # verl-native run_ppo does ray.init (+ transfer_queue env) and starts the task
    # runner actor. We pass AgentRLTaskRunnerV1 in place of the default TaskRunnerV1.
    run_ppo(cfg, task_runner_class=AgentRLTaskRunnerV1)
