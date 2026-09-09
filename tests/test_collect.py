"""Native-field collection -> scheduler -> ingest (no GPU/verl/buffer package)."""

from rollout.collect import (
    GenStep,
    ingest_trajectories,
    make_react_agent_fn,
    parse_tool_call,
    trajectory_to_buffer_item,
)
from rollout.scheduler import RolloutScheduler, SessionSpec


# The replay_buffer package was removed from this project; ingest_trajectories
# only duck-types ``add_trajectory``, so a minimal stub exercises the same path.
_BUCKET_NAMES = [
    "workflow",
    "ops",
    "qa",
    "finance",
    "office",
    "communication",
    "safety",
    "coding",
    "research",
]


class _StubBuffer:
    bucket_names = _BUCKET_NAMES

    def __init__(self):
        self.items = []

    def add_trajectory(self, payload, bucket, meta):
        self.items.append((payload, bucket, meta))


class MockSandbox:
    def __init__(self, **kw):
        self.killed = False

    def run_code(self, code, language="python"):
        from rollout.sandbox_client import ExecResult

        # echo the arithmetic so the mock observation is deterministic
        return ExecResult(stdout="372", stderr="", ok=True)

    def kill(self):
        self.killed = True


def _mock_generate():
    """Two-step ReAct: first a tool call, then a final answer."""
    calls = {"n": 0}

    def gen(messages):
        calls["n"] += 1
        if calls["n"] % 2 == 1:
            text = '<toolcall>{"tool": "sandbox.exec_python", "code": "print(23*17-19)"}</toolcall>'
            return GenStep(text=text, response_ids=[10, 11, 12], logprobs=[-0.1, -0.2, -0.3])
        text = "结果是 372。"
        return GenStep(text=text, response_ids=[20, 21], logprobs=[-0.05, -0.06])

    return gen


def test_parse_tool_call():
    assert parse_tool_call('<toolcall>{"tool": "t", "code": "x"}</toolcall>') == ("t", "x")
    assert parse_tool_call("no call here") is None
    assert parse_tool_call("<toolcall>{bad json}</toolcall>") is None


def test_react_agent_collects_native_fields():
    agent_fn = make_react_agent_fn(_mock_generate(), max_turns=4, default_bucket="finance")
    traj = agent_fn(MockSandbox(), "计算 23×17−19", {}, slot_idx=0)
    # generated tokens (mask=1) + observation tokens (mask=0)
    mask = traj.meta["response_mask"]
    assert sum(mask) == 5  # 3 + 2 generated tokens
    assert len(mask) == len(traj.response_token_ids) == len(traj.logprobs)
    assert mask.count(0) >= 1  # at least one observation token, masked
    assert traj.bucket == "finance"  # from default_bucket
    # transcript has assistant + sandbox observation (user) messages
    roles = [m["role"] for m in traj.messages]
    assert "assistant" in roles
    # sandbox observations use role='user' with '[Sandbox Output]' prefix
    sandbox_msgs = [
        m for m in traj.messages if m["role"] == "user" and m["content"].startswith("[Sandbox Output]")
    ]
    assert len(sandbox_msgs) >= 1


def test_trajectory_to_buffer_item_carries_logprobs():
    agent_fn = make_react_agent_fn(_mock_generate(), max_turns=4, default_bucket="finance")
    traj = agent_fn(MockSandbox(), "q", {}, slot_idx=1)
    traj.reward = 1.0
    payload, bucket, meta = trajectory_to_buffer_item(traj)
    assert bucket == "finance"
    assert meta["original_logprobs"] == traj.logprobs
    assert meta["reward"] == 1.0
    assert "response_token_ids" in payload and "response_mask" in payload


def test_full_chain_into_buffer():
    """scheduler (2×2 mock) -> score -> ingest via duck-typed buffer."""
    agent_fn = make_react_agent_fn(_mock_generate(), max_turns=4, default_bucket="finance")
    sched = RolloutScheduler(
        agent_fn,
        sessions_per_step=2,
        slots=2,
        backend="mock",
        pool_factory=lambda spec, seed: _pool(spec, seed),
    )
    specs = [SessionSpec(session_id=f"s{j}", queries=["q1", "q2"]) for j in range(2)]
    trajs = sched.run_step(specs)
    assert len(trajs) == 2 * 2 * 2  # sessions × slots × queries

    # simple rule-ish scorer for the dry run
    for t in trajs:
        t.reward = 1.0 if "372" in (t.messages[-1]["content"]) else 0.0

    buffer = _StubBuffer()
    counts = ingest_trajectories(buffer, trajs, valid_buckets=buffer.bucket_names)
    assert counts["added"] == 8  # all tagged finance
    assert counts["skipped"] == 0
    assert len(buffer.items) == 8
    assert all(bucket == "finance" for _, bucket, _ in buffer.items)


def _pool(spec, seed):
    from rollout.session_pool import SessionSandboxPool

    return SessionSandboxPool(
        slots=2,
        backend="mock",
        sandbox_factory=lambda backend, **kw: MockSandbox(**kw),
        persona=spec.persona,
        seed=seed,
    )
