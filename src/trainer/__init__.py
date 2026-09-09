"""Training entry for the self-evolving multi-agent RL system (verl-based).

This package wires together:
- ``agent_rl_main`` -- config loading + CLI entry,
- ``agent_rl_runner`` -- a thin ``RayPPOTrainer`` construction that runs stock
  GRPO over multi-agent sandbox rollouts (no buffer, no custom loss),
- ``agent_rollout_manager`` -- the session-scheduler rollout manager that injects
  the Observer's diff-driven state evidence into the training reward.

We do NOT fork verl -- rollout/reward are wired via verl's official injection
points (``agent_loop_manager_class`` + the ``observer`` reward manager).
"""
