"""Tests.

CPU-runnable unit tests for the self-evolving multi-agent RL system. GPU/verl
full-stack smoke is marked ``@pytest.mark.gpu`` and skips without a cluster.

Layout (surviving suites):
    test_configs.py             -- run/*.yaml load + verl Hydra schema (agent_rl)
    test_collect.py             -- native-field collection -> scheduler -> ingest
    test_agent_rollout_manager.py -- AgentSchedulerAgentLoopManager wiring
    test_agents.py              -- observer / questioner / reward(judge) agents
    test_model_reward.py        -- external LLM-judge compute_score path
    test_sandbox_client.py      -- SandboxClient contract + backend registry
    test_session_pool.py        -- session sandbox pool / winner-sync slots
    test_simulated_session.py   -- simulated multi-turn session driver
    test_live_messages.py       -- live message streaming boundary
    test_verifier*.py           -- verifier + verifier hook
    test_image_trajectory_drop.py / test_force_screenshot_and_drop.py
                                -- image trajectory filtering (E13)
    test_policy_loss_padding_patch.py -- verl policy-loss padding patch (torch-gated)
    test_verl_smoke.py          -- minimal verl integration smoke (gpu/verl-gated)
    ... plus dataset / dockerfile / env / qc helpers.
"""
