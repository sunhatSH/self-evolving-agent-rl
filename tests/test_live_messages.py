"""Unit tests for the live-messages side-channel (trainer/live_messages.py).

Covers: write_batch -> load_map round-trip (incl. [Sandbox Output] preserved),
per-task_id pop order (rollout.n grouping), reset/cleanup, and the malformed-line /
missing-file degrade paths.
"""

from __future__ import annotations

import json

import pytest

from trainer import live_messages as lm


@pytest.fixture(autouse=True)
def _cwd(tmp_path, monkeypatch):
    # Side files live under rollouts/training/<exp>/ relative to cwd.
    monkeypatch.chdir(tmp_path)
    yield


def _traj(sandbox_out: str):
    return [
        {"role": "user", "content": "sum data.csv"},
        {"role": "assistant", "content": "<tool_call>read_file</tool_call>"},
        {"role": "user", "content": f"[Sandbox Output]\n{sandbox_out}"},
        {"role": "assistant", "content": "the sum is 42"},
    ]


def test_write_load_roundtrip_preserves_tool_output():
    exp = "exp_rt"
    lm.write_batch(exp, ["T1"], [_traj("value\n10\n12\n20")])
    m = lm.load_map(exp)
    assert "T1" in m
    msgs = m["T1"][0]
    # the [Sandbox Output] message survived (this is the whole point)
    assert any("[Sandbox Output]" in str(x.get("content", "")) for x in msgs)
    assert any(x.get("role") == "user" and "value" in x.get("content", "") for x in msgs)


def test_pop_order_matches_write_order_per_task():
    exp = "exp_pop"
    # two rollouts share task_id T1 (verl rollout.n grouping), one for T2
    lm.write_batch(
        exp,
        ["T1", "T1", "T2"],
        [_traj("first"), _traj("second"), _traj("other")],
    )
    pop = lm.LiveMessagePopper(lm.load_map(exp))
    a = pop.pop("T1")
    b = pop.pop("T1")
    c = pop.pop("T1")  # exhausted
    assert "first" in json.dumps(a, ensure_ascii=False)
    assert "second" in json.dumps(b, ensure_ascii=False)
    assert c is None
    assert pop.pop("T2") is not None
    assert pop.pop("unknown") is None


def test_reset_truncates_previous_step():
    exp = "exp_reset"
    lm.write_batch(exp, ["OLD"], [_traj("stale")])
    lm.write_batch(exp, ["NEW"], [_traj("fresh")])  # write_batch resets first
    m = lm.load_map(exp)
    assert "OLD" not in m
    assert "NEW" in m


def test_skips_empty_taskid_and_messages():
    exp = "exp_skip"
    lm.write_batch(exp, ["", "T1"], [_traj("x"), []])
    m = lm.load_map(exp)
    assert m == {}  # "" skipped, T1 had empty messages skipped


def test_load_missing_file_returns_empty():
    assert lm.load_map("no_such_exp") == {}


def test_popper_none_mapping():
    pop = lm.LiveMessagePopper(None)
    assert pop.pop("anything") is None


def test_malformed_line_skipped(tmp_path):
    exp = "exp_bad"
    p = lm.pending_path(exp)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(
        '{"task_id": "T1", "messages": [{"role":"user","content":"ok"}]}\n'
        "NOT JSON AT ALL\n"
        '{"task_id": "T2", "messages": [{"role":"user","content":"ok2"}]}\n',
        encoding="utf-8",
    )
    m = lm.load_map(exp)
    assert set(m.keys()) == {"T1", "T2"}  # bad line skipped, good ones kept


def test_cleanup_removes_file():
    exp = "exp_clean"
    lm.write_batch(exp, ["T1"], [_traj("x")])
    assert lm.pending_path(exp).exists()
    lm.cleanup(exp)
    assert not lm.pending_path(exp).exists()
    lm.cleanup(exp)  # idempotent, no raise


class _FakePrompts:
    def __init__(self, extra_info):
        self.non_tensor_batch = {"extra_info": extra_info}


def test_extract_record_ids_from_prompts():
    from trainer.agent_rollout_manager import extract_record_ids_from_prompts

    p = _FakePrompts([{"record_id": "D1_a"}, {"task_id": "D2_b"}, {"other": 1}])
    rids = extract_record_ids_from_prompts(p)
    assert rids == ["D1_a", "D2_b", ""]  # record_id, task_id fallback, then ""


def test_extract_record_ids_absent_returns_empty():
    from trainer.agent_rollout_manager import extract_record_ids_from_prompts

    class P:
        non_tensor_batch = {}

    assert extract_record_ids_from_prompts(P()) == []


# NOTE: tests for ``_persist_rollout_status`` were removed — that helper lived in
# the deleted ``trainer.cl_replay_hook_v1`` (CL replay hook) and has no surviving
# equivalent in this project.



