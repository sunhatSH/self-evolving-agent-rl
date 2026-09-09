"""Unit tests for VerifierHook (trainer/verifier_hook.py) + omni/compute_score 回流.

Off-cluster: recipe_custom absent -> hook uses the fallback AgentRunHook base. A
fake async sandbox records exec/write_file; _gen_check_code is monkeypatched so no
real LLM/network is hit. Covers: VERIFIER_ENABLE gate, source-list probe + check
execution, verifier_report shape, degrade paths, and the reward_info -> extra_info
-> correctness-rubric wiring.
"""

from __future__ import annotations

import asyncio

import pytest

from trainer import verifier_hook as vh
from trainer.verifier_hook import VerifierHook


class FakeExec:
    def __init__(self, stdout="", stderr="", exit_code=0):
        self.stdout = stdout
        self.stderr = stderr
        self.exit_code = exit_code


class FakeSandbox:
    """Async sandbox: exec returns canned results by substring; records calls."""

    def __init__(self, responses=None, default=None):
        self.responses = responses or {}
        self.default = default or FakeExec(stdout="", exit_code=0)
        self.exec_calls = []
        self.written = {}

    async def exec(self, command, *, timeout=120, **kw):
        self.exec_calls.append(command)
        for needle, resp in self.responses.items():
            if needle in command:
                return resp
        return self.default

    async def write_file(self, path, content):
        self.written[path] = content


class Ctx:
    def __init__(self, instruction=""):
        self.instruction = instruction
        self.extra = {}


class State:
    def __init__(self, reward_info=None):
        self.reward_info = reward_info if reward_info is not None else {}


@pytest.fixture(autouse=True)
def _enable(monkeypatch):
    monkeypatch.setenv("VERIFIER_ENABLE", "1")
    yield


# --- gate --------------------------------------------------------------------


def test_disabled_is_noop(monkeypatch):
    monkeypatch.setenv("VERIFIER_ENABLE", "0")
    sb = FakeSandbox()
    st = State()
    asyncio.run(VerifierHook().run(sb, Ctx("t"), st))
    assert st.reward_info == {}  # nothing written, no exec
    assert sb.exec_calls == []


def test_hook_instantiable_has_run():
    # fallback base marks run @abstractmethod -> instantiation proves run is implemented
    h = VerifierHook()
    assert h.run_on_agent_error is True


# --- three-stage flow --------------------------------------------------------


def test_run_generates_executes_and_writes_report(monkeypatch):
    # source-list probe returns a listing; the generated check prints a verdict.
    sb = FakeSandbox(
        responses={
            "os.walk": FakeExec(stdout='{"./inputs/data.csv": {"size": 10, "head": "value\\n10\\n12\\n20"}}'),
            "_cl_verifier_check.py": FakeExec(stdout="GROUND TRUTH sum=42 | AGENT said 100 | MISMATCH", exit_code=0),
        }
    )

    async def fake_gen(task, produced, source_files, timeout=120):
        assert "data.csv" in source_files  # the probe output was passed to 出题
        return "import csv; print('check')"

    monkeypatch.setattr(vh, "_gen_check_code", fake_gen)

    st = State({"observer_report": "out.txt: the sum is 100"})
    asyncio.run(VerifierHook().run(sb, Ctx("sum data.csv"), st))

    vr = st.reward_info["verifier_report"]
    assert vr["status"] == "ok"
    assert "MISMATCH" in vr["check_stdout"]
    assert vr["check_ok"] is True
    # the generated check was written to the sandbox and executed
    assert "/tmp/_cl_verifier_check.py" in sb.written
    assert any("_cl_verifier_check.py" in c for c in sb.exec_calls)


def test_no_check_generated_degrades(monkeypatch):
    sb = FakeSandbox()

    async def fake_gen(task, produced, source_files, timeout=120):
        return ""  # LLM produced nothing usable

    monkeypatch.setattr(vh, "_gen_check_code", fake_gen)
    st = State()
    asyncio.run(VerifierHook().run(sb, Ctx("t"), st))
    assert st.reward_info["verifier_report"]["status"] == "no_check_generated"


def test_gen_exception_degrades_not_raises(monkeypatch):
    sb = FakeSandbox()

    async def boom(task, produced, source_files, timeout=120):
        raise RuntimeError("judge 500")

    monkeypatch.setattr(vh, "_gen_check_code", boom)
    st = State()
    # must not raise
    asyncio.run(VerifierHook().run(sb, Ctx("t"), st))
    assert st.reward_info["verifier_report"]["status"] == "error"


def test_write_file_failure_falls_back_to_dash_c(monkeypatch):
    class NoWriteSandbox(FakeSandbox):
        async def write_file(self, path, content):
            raise OSError("read-only fs")

    sb = NoWriteSandbox(
        responses={"os.walk": FakeExec(stdout="{}"), "print(": FakeExec(stdout="ran via -c", exit_code=0)}
    )

    async def fake_gen(task, produced, source_files, timeout=120):
        return "print('x')"

    monkeypatch.setattr(vh, "_gen_check_code", fake_gen)
    st = State()
    asyncio.run(VerifierHook().run(sb, Ctx("t"), st))
    vr = st.reward_info["verifier_report"]
    assert vr["status"] == "ok"
    # executed via `python3 -c` since write_file failed
    assert any("-c" in c for c in sb.exec_calls)


# --- reward wiring: verifier_report -> extra_info -> correctness rubric -------


def test_omni_forwards_verifier_report(monkeypatch):
    """model_reward_omni copies reward_info['verifier_report'] into extra_info."""
    import trainer.model_reward_omni as omni

    captured = {}

    def fake_cl_compute_score(data_source, response, ground_truth, *, extra_info=None, **kw):
        captured["extra_info"] = extra_info
        return {"score": 0.0, "correctness": 0.0}

    monkeypatch.setattr(omni, "_cl_compute_score", fake_cl_compute_score)
    omni.compute_score(
        "resp",
        "",
        data_source="agentic_cl",
        extra_info={},
        data_non_tensor_batch={"reward_info": {"verifier_report": {"status": "ok", "check_stdout": "sum=42"}}},
    )
    assert captured["extra_info"]["verifier_report"]["check_stdout"] == "sum=42"


def test_compute_score_does_not_inject_gt(monkeypatch):
    """2026-09-03: correctness no longer uses GT/answer_key — judge grades from what's
    VISIBLE (source_data + diff), never a precomputed 'expected value'. answer_key in
    extra_info must NOT leak into the correctness rubric."""
    import trainer.model_reward as mr

    seen = {}

    class SpyJudge:
        def score(self, *, task, trajectory, rubric, data_source, system=None):
            if system is None:
                seen["main_rubric"] = rubric
                return {"correctness": 0.5, "consistency": 0.5}
            return {"efficiency": 0.5, "planning": 0.5, "recovery": 0.5, "safety": 1.0}

    mr.compute_score(
        "agentic_cl",
        "the agent implemented f",
        "",
        extra_info={
            "task": "implement f",
            # even if an answer_key / checkers is present, it must be ignored now
            "answer_key": {"type": "static", "acceptance_points": [{"point": "SECRET_GT_POINT"}]},
            "checkers": [{"question": "SECRET_CHECK", "answer": 42}],
        },
        judge=SpyJudge(),
    )
    rub = seen.get("main_rubric", "")
    assert "SECRET_GT_POINT" not in rub  # GT not injected
    assert "SECRET_CHECK" not in rub  # D-class checkers not injected
    # the three visible-correctness criteria are present
    assert "Existence & completeness" in rub
    assert "Claim" in rub and "consistency" in rub.lower()
    assert "Method & structure" in rub


def test_compute_score_folds_source_data_into_correctness_rubric():
    """compute_score puts the captured source-input files into the correctness rubric
    so the judge can verify against the REAL inputs (F17 anti-hallucination anchor)."""
    import trainer.model_reward as mr

    seen = {}

    class SpyJudge:
        def score(self, *, task, trajectory, rubric, data_source, system=None):
            # call A (correctness+consistency) passes system=None; call B passes _TRAJECTORY_SYSTEM
            if system is None:
                seen["main_rubric"] = rubric
                return {"correctness": 0.5, "consistency": 0.5}
            return {"efficiency": 0.5, "planning": 0.5, "recovery": 0.5, "safety": 1.0}

    mr.compute_score(
        "agentic_cl",
        "the agent said sum=100",
        "",
        extra_info={
            "task": "sum data.csv",
            "source_data": "### ./inputs/data.csv\nvalue\n10\n12\n20",
        },
        judge=SpyJudge(),
    )
    assert "Source input files" in seen.get("main_rubric", "")
    assert "10\n12\n20" in seen.get("main_rubric", "")
