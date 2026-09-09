"""Unit tests for the execution-grounded Verifier (agents/verifier.py).

Off-GPU, no network: a scripted ChatClient drives the tool-use loop and a fake
sandbox returns canned execution results. Covers: run_check is issued and
executed, the grounded verdict overrides correctness, the score recompute in the
integration helper, and the degrade-on-failure contract.
"""

from __future__ import annotations

import json

from agents.verifier import Verifier, _execute_verifier_tool


class FakeExec:
    def __init__(self, stdout="", stderr="", ok=True):
        self.stdout = stdout
        self.stderr = stderr
        self.ok = ok


class FakeSandbox:
    """Records run_code calls; returns a canned ExecResult per matched substring."""

    def __init__(self, responses: dict[str, FakeExec] | None = None, default=None):
        self.responses = responses or {}
        self.default = default or FakeExec(stdout="", ok=True)
        self.calls: list[str] = []

    def run_code(self, code: str, language: str = "python"):
        self.calls.append(code)
        for needle, resp in self.responses.items():
            if needle in code:
                return resp
        return self.default

    def kill(self):
        pass


class ScriptedToolClient:
    """chat_with_tools returns queued messages in order (tool_calls then final JSON)."""

    def __init__(self, script: list[dict]):
        self.script = list(script)
        self.seen: list[list[dict]] = []

    def chat_with_tools(self, messages, *, tools=None, max_tokens: int = 1024) -> dict:
        self.seen.append(list(messages))
        return self.script.pop(0) if self.script else {"role": "assistant", "content": ""}


def _tool_call(tid, name, args):
    return {
        "role": "assistant",
        "content": "",
        "tool_calls": [{"id": tid, "function": {"name": name, "arguments": json.dumps(args)}}],
    }


# --- tool executor ----------------------------------------------------------


def test_run_check_executes_in_sandbox():
    sb = FakeSandbox(responses={"sum": FakeExec(stdout="42\n", ok=True)})
    out = _execute_verifier_tool("run_check", {"code": "print(sum([40,2]))  # sum"}, sb)
    d = json.loads(out)
    assert d["stdout"].strip() == "42"
    assert d["ok"] is True
    assert sb.calls, "run_code should have been invoked"


def test_read_file_tool_reads_source():
    sb = FakeSandbox(default=FakeExec(stdout=json.dumps({"path": "/x.csv", "content": "a,b\n1,2"})))
    out = _execute_verifier_tool("read_file", {"path": "/x.csv"}, sb)
    assert "a,b" in out


def test_tool_without_sandbox_errors_not_crash():
    out = _execute_verifier_tool("run_check", {"code": "x"}, None)
    assert "no sandbox" in out


def test_unknown_tool_returns_error():
    sb = FakeSandbox()
    out = _execute_verifier_tool("frobnicate", {}, sb)
    assert "unknown tool" in out


# --- verify() end-to-end (scripted LLM + fake sandbox) ----------------------


def test_verify_grounds_correctness_via_run_check():
    # Agent claimed sum=100; verifier recomputes from source and finds 42 -> low score.
    sb = FakeSandbox(responses={"csv": FakeExec(stdout="42\n", ok=True)})
    client = ScriptedToolClient(
        [
            _tool_call("c1", "run_check", {"code": "import csv  # recompute from csv"}),
            {
                "role": "assistant",
                "content": '{"correctness": 0.1, "correctness_reason": "real sum is 42, agent said 100"}',
            },
        ]
    )
    v = Verifier(client=client, max_tool_rounds=4)
    res = v.verify(task="sum the csv", trajectory="[assistant] the sum is 100", sandbox=sb)
    assert res["verified"] is True
    assert res["correctness"] == 0.1
    assert "42" in res["correctness_reason"]
    assert sb.calls, "verifier should have executed a check in the sandbox"


def test_verify_high_score_when_agent_correct():
    sb = FakeSandbox(responses={"csv": FakeExec(stdout="42\n", ok=True)})
    client = ScriptedToolClient(
        [
            _tool_call("c1", "run_check", {"code": "x  # csv"}),
            {"role": "assistant", "content": '{"correctness": 0.95, "correctness_reason": "matches real 42"}'},
        ]
    )
    v = Verifier(client=client)
    res = v.verify(task="sum the csv", trajectory="[assistant] the sum is 42", sandbox=sb)
    assert res["verified"] is True
    assert res["correctness"] == 0.95


def test_verify_returns_unverified_without_sandbox():
    v = Verifier(client=ScriptedToolClient([]))
    res = v.verify(task="t", trajectory="x", sandbox=None)
    assert res["verified"] is False


def test_verify_degrades_on_no_verdict():
    # LLM never emits a parseable verdict -> verified False (caller keeps plain judge).
    sb = FakeSandbox()
    client = ScriptedToolClient(
        [
            {"role": "assistant", "content": "I am not sure."},  # no JSON -> break
            {"role": "assistant", "content": "still no json"},  # final nudge also fails
        ]
    )
    v = Verifier(client=client, max_tool_rounds=2)
    res = v.verify(task="t", trajectory="x", sandbox=sb)
    assert res["verified"] is False


def test_verify_direct_verdict_no_tools():
    sb = FakeSandbox()
    client = ScriptedToolClient(
        [{"role": "assistant", "content": '{"correctness": 0.5, "correctness_reason": "ok"}'}]
    )
    v = Verifier(client=client)
    res = v.verify(task="t", trajectory="x", sandbox=sb)
    assert res["verified"] is True
    assert res["correctness"] == 0.5


def test_verify_stamps_timing_and_counters():
    """verify() records verify_secs + LLM/run_check counts for the perf audit."""
    sb = FakeSandbox(responses={"csv": FakeExec(stdout="42\n", ok=True)})
    client = ScriptedToolClient(
        [
            _tool_call("c1", "run_check", {"code": "x  # csv"}),
            {"role": "assistant", "content": '{"correctness": 0.9, "correctness_reason": "ok"}'},
        ]
    )
    v = Verifier(client=client)
    res = v.verify(task="t", trajectory="x", sandbox=sb)
    assert res["verify_secs"] is not None and res["verify_secs"] >= 0
    assert res["n_llm_calls"] == 2  # one tool round + one final verdict
    assert res["n_run_check"] == 1
    assert res["n_tool_calls"] == 1


def test_verify_never_raises_on_client_boom():
    class Boom:
        def chat_with_tools(self, messages, *, tools=None, max_tokens: int = 1024) -> dict:
            raise RuntimeError("upstream 500")

    v = Verifier(client=Boom())
    res = v.verify(task="t", trajectory="x", sandbox=FakeSandbox())
    assert res["verified"] is False

