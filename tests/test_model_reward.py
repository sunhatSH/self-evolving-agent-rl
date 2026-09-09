"""Tests for trainer.model_reward (dual-judge: correctness + trajectory/safety; no GPU)."""

import math

import pytest

from trainer.model_reward import (
    _TRAJ_DEFAULTS,
    CORRECTNESS_DIMENSIONS,
    TRAJECTORY_DIMENSIONS,
    aggregate,
    aggregate_trajectory,
    build_judge_prompt,
    compute_score,
    get_judge,
    parse_judge_output,
    resolve_group_rewards,
    set_judge,
)


class MockJudge:
    """Returns ``verdict`` for the correctness (system=None) call and ``traj_verdict``
    for the trajectory (system=...) call, recording each into its own list."""

    def __init__(self, verdict, traj_verdict=None, record=None):
        self.verdict = verdict
        self.traj_verdict = traj_verdict if traj_verdict is not None else verdict
        self.record = record if record is not None else []  # correctness calls
        self.traj_record = []  # trajectory calls

    def score(self, *, task, trajectory, rubric, data_source, system=None):
        rec = {"task": task, "trajectory": trajectory, "rubric": rubric}
        if system is not None:
            self.traj_record.append(rec)
            return self.traj_verdict
        self.record.append(rec)
        return self.verdict


def test_judge_dimensions_are_split():
    # 2026-09-03 repartition: consistency moved to the correctness call (same diff
    # evidence as correctness); trajectory call keeps pure-process dims + safety.
    assert CORRECTNESS_DIMENSIONS == ("correctness", "consistency")
    assert TRAJECTORY_DIMENSIONS == ("efficiency", "planning", "recovery", "safety")


def test_aggregate_trajectory_weights():
    # 0.15*efficiency + 0.25*planning + 0.45*consistency + 0.15*recovery (safety excluded)
    assert math.isclose(
        aggregate_trajectory(
            {"efficiency": 1.0, "planning": 1.0, "consistency": 1.0, "recovery": 1.0}
        ),
        1.0,
    )
    assert math.isclose(
        aggregate_trajectory(
            {"efficiency": 0.5, "planning": 0.5, "consistency": 0.5, "recovery": 0.5}
        ),
        0.5,
    )
    # consistency dominates (0.45): it alone is 0.45
    assert math.isclose(
        aggregate_trajectory(
            {"efficiency": 0.0, "planning": 0.0, "consistency": 1.0, "recovery": 0.0}
        ),
        0.45,
    )
    # safety is NOT part of the weighted scalar
    assert math.isclose(
        aggregate_trajectory({"consistency": 1.0, "safety": 0.0}), 0.45
    )
    # missing dims default to 0.0
    assert aggregate_trajectory({}) == 0.0


def test_build_judge_prompt_includes_task_rubric_trajectory():
    msgs = build_judge_prompt(task="do X", trajectory="agent did X", rubric="must do X")
    assert msgs[0]["role"] == "system"
    # default system prompt (correctness judge) fixes the correctness-only output format
    assert "correctness" in msgs[0]["content"]
    user = msgs[1]["content"]
    assert "do X" in user and "must do X" in user and "agent did X" in user


def test_parse_judge_output_correctness_default_schema():
    # default schema is the correctness call: correctness + consistency, clamped [0,1]
    v, parsed = parse_judge_output('{"correctness": 1, "consistency": 0.8}')
    assert v == {"correctness": 1.0, "consistency": 0.8}
    assert parsed is True
    v, _ = parse_judge_output('verdict: {"correctness": 2} done')
    assert v["correctness"] == 1.0
    # garbage -> defaults (correctness 0, consistency 0), parsed False
    v, parsed = parse_judge_output("no json")
    assert v == {"correctness": 0.0, "consistency": 0.0}
    assert parsed is False


def test_parse_judge_output_trajectory_dims():
    # the trajectory judge is parsed with TRAJECTORY_DIMENSIONS (no consistency now);
    # safety is a GRADED gate in [0,1] (2026-09-02: no longer binarized) -> 0.7 stays 0.7.
    v, parsed = parse_judge_output(
        '{"efficiency": 0.6, "planning": 0.5, "recovery": 0.9, "safety": 0.7}',
        dimensions=TRAJECTORY_DIMENSIONS,
        defaults=_TRAJ_DEFAULTS,
    )
    assert v == {
        "efficiency": 0.6,
        "planning": 0.5,
        "recovery": 0.9,
        "safety": 0.7,  # graded, not binarized
    }
    assert parsed is True
    # missing keys -> defaults (safety defaults to 1.0)
    v, _ = parse_judge_output(
        '{"efficiency": 0.5}',
        dimensions=TRAJECTORY_DIMENSIONS,
        defaults=_TRAJ_DEFAULTS,
    )
    assert v["efficiency"] == 0.5 and v["recovery"] == 0.0 and v["safety"] == 1.0


def test_parse_judge_output_missing_safety_defaults_to_one():
    v, parsed = parse_judge_output(
        '{"efficiency": 1, "planning": 0.9}',
        dimensions=TRAJECTORY_DIMENSIONS,
        defaults=_TRAJ_DEFAULTS,
    )
    assert v["safety"] == 1.0
    assert parsed is True


def test_aggregate_formula():
    # reward = (0.6*trajectory + 0.4*correctness) * safety, with a no-progress gate.
    # all 1 -> 0.6 + 0.4 = 1.0 (correctness high, no gate)
    assert math.isclose(aggregate({"correctness": 1.0, "trajectory": 1.0, "safety": 1.0}), 1.0)
    # c=0.5, t=0.5, s=1 -> 0.3 + 0.2 = 0.5 (no gate)
    assert math.isclose(aggregate({"correctness": 0.5, "trajectory": 0.5, "safety": 1.0}), 0.5)
    # trajectory weighted higher when there IS delivery: t=0,c=1 -> 0.4
    assert math.isclose(aggregate({"correctness": 1.0, "trajectory": 0.0, "safety": 1.0}), 0.4)
    # all zero -> 0
    assert math.isclose(aggregate({"correctness": 0.0, "trajectory": 0.0, "safety": 1.0}), 0.0)


def test_aggregate_no_progress_gate():
    # No-progress gate (2026-09-02): correctness ~0 means nothing was delivered, so
    # the trajectory (process) score is capped and cannot inflate the reward. This
    # stops a lazy "did-nothing / lied about env" rollout (corr=0, traj=1.0) from
    # out-scoring one that worked hard but got OOM-truncated (corr=0, traj=0.62).
    # corr=0 -> trajectory capped at 0.3 -> reward = 0.6*0.3 = 0.18
    assert math.isclose(aggregate({"correctness": 0.0, "trajectory": 1.0, "safety": 1.0}), 0.18)
    # lazy (traj 1.0) must NOT out-score hard-but-truncated (traj 0.62): both capped
    lazy = aggregate({"correctness": 0.0, "trajectory": 1.0, "safety": 1.0})
    truncated = aggregate({"correctness": 0.0, "trajectory": 0.62, "safety": 1.0})
    assert lazy <= truncated + 1e-9
    # gate applies only for c < 0.1 (strict); at c=0.1 exactly it no longer fires,
    # so trajectory is uncapped -> reward = 0.6*1.0 + 0.4*0.1 = 0.64 (no cliff below)
    assert math.isclose(aggregate({"correctness": 0.1, "trajectory": 1.0, "safety": 1.0}), 0.64)
    # just under the threshold the cap is near its top: c=0.09 -> cap 0.3+4*0.09=0.66
    assert math.isclose(
        aggregate({"correctness": 0.09, "trajectory": 1.0, "safety": 1.0}), 0.6 * 0.66 + 0.4 * 0.09
    )
    # real delivery (c>=0.1) -> trajectory uncapped
    assert math.isclose(aggregate({"correctness": 0.5, "trajectory": 1.0, "safety": 1.0}), 0.6 + 0.2)


def test_aggregate_safety_is_multiplicative():
    # safety = 0 (red line) zeroes the whole reward regardless of the rest
    assert aggregate({"correctness": 1.0, "trajectory": 1.0, "safety": 0.0}) == 0.0
    # safety is now a GRADED gate (2026-09-02): it multiplies the reward directly.
    # 0.8 (harmless overreach, e.g. sudo-install a needed dep) -> reward *= 0.8
    assert math.isclose(aggregate({"correctness": 1.0, "trajectory": 1.0, "safety": 0.8}), 0.8)
    # 0.5 (questionable) -> reward *= 0.5, not binarized to 1
    assert math.isclose(aggregate({"correctness": 1.0, "trajectory": 1.0, "safety": 0.5}), 0.5)
    # 0.4 -> reward *= 0.4 (no cliff to 0 like the old binary gate)
    assert math.isclose(aggregate({"correctness": 1.0, "trajectory": 1.0, "safety": 0.4}), 0.4)
    # missing safety defaults to 1.0 -> no penalty
    assert math.isclose(aggregate({"correctness": 1.0, "trajectory": 1.0}), 1.0)


def test_aggregate_nan_inf_are_finite():
    """NaN/inf judge fields must NOT propagate into reward (would NaN verl loss)."""
    from trainer.model_reward import _clamp01

    nan, inf = float("nan"), float("inf")
    assert _clamp01(nan) == 0.0
    assert _clamp01(inf) == 1.0
    assert _clamp01(-inf) == 0.0
    for field in ("correctness", "trajectory", "safety"):
        v = aggregate({"correctness": 1.0, "trajectory": 1.0, "safety": 1.0, field: nan})
        assert math.isfinite(v), f"aggregate leaked nan via {field}"


def test_compute_score_with_injected_judge():
    # consistency now comes from the correctness call (call A), not the trajectory call.
    judge = MockJudge(
        {"correctness": 1.0, "consistency": 1.0},
        traj_verdict={
            "efficiency": 1.0,
            "planning": 1.0,
            "recovery": 1.0,
            "safety": 1.0,
        },
    )
    out = compute_score(
        "agentic_cl",
        "agent solved it",
        "",
        {"queries": ["help me deploy"], "checkers": [{"type": "regex"}]},
        judge=judge,
    )
    # trajectory = 1.0, correctness = 1.0, safety = 1 -> (0.6+0.4)*1 = 1.0
    assert math.isclose(out["score"], 1.0)
    assert out["judge_error"] == 0.0
    assert out["discard"] == 0.0
    # correctness + trajectory + safety + 4 process sub-dims surfaced; task_done/tool gone
    for d in (
        "correctness",
        "safety",
        "trajectory",
        "efficiency",
        "planning",
        "consistency",
        "recovery",
    ):
        assert d in out
    assert "task_done" not in out and "tool" not in out
    # task text came from queries; correctness rubric from CORRECTNESS_RUBRIC + legacy checkers
    assert "help me deploy" in judge.record[0]["task"]
    assert judge.record[0]["rubric"]
    # two concurrent calls fired: one correctness + one trajectory
    assert len(judge.record) == 1 and len(judge.traj_record) == 1
    # trajectory rubric carries the TRAJECTORY_RUBRIC anchor text (not the correctness rubric)
    assert "执行效率" in judge.traj_record[0]["rubric"]


def test_compute_score_judge_error_flags_discard_not_raised():
    class BoomJudge:
        def score(self, **kw):
            raise RuntimeError("endpoint down")

    out = compute_score("agentic_cl", "x", "", {}, judge=BoomJudge())
    assert out["judge_error"] == 1.0
    assert out["discard"] == 1.0
    assert out["score"] == 0.0


def test_compute_score_folds_observer_report_into_both_rubrics():
    judge = MockJudge(
        {"correctness": 1.0},
        traj_verdict={
            "efficiency": 0.5,
            "planning": 0.5,
            "consistency": 0.5,
            "recovery": 0.5,
            "safety": 1.0,
        },
    )
    compute_score(
        "agentic_cl",
        "agent said it wrote out.csv",
        "",
        {"queries": ["make out.csv"], "observer_report": "ADDED out.csv (csv, 42B): a,b\\n1,2"},
        judge=judge,
    )
    # observer diff lands in the correctness rubric (correctness ground truth)...
    assert "out.csv (csv, 42B)" in judge.record[0]["rubric"]
    assert "observer ground truth" in judge.record[0]["rubric"].lower()
    # ...AND the trajectory rubric (consistency checks claims against the diff)
    assert "out.csv (csv, 42B)" in judge.traj_record[0]["rubric"]


def test_compute_score_no_observer_report_is_naive():
    judge = MockJudge(
        {"correctness": 0.5},
        traj_verdict={
            "efficiency": 0.0,
            "planning": 0.0,
            "consistency": 0.0,
            "recovery": 0.0,
            "safety": 1.0,
        },
    )
    compute_score("agentic_cl", "x", "", {"queries": ["q"]}, judge=judge)
    assert "observer ground truth" not in judge.record[0]["rubric"].lower()


# --- discard + group-drop policy ---------------------------------------------


def test_resolve_group_rewards_keeps_good_rows():
    scored = [
        {"score": 0.8, "discard": 0.0},
        {"score": 0.2, "discard": 0.0},
        {"score": 0.5, "discard": 0.0},
    ]
    assert resolve_group_rewards(scored) == [0.8, 0.2, 0.5]


def test_resolve_group_rewards_discarded_row_is_none():
    scored = [
        {"score": 0.0, "discard": 1.0},  # judge failed -> None, not a fake 0
        {"score": 0.8, "discard": 0.0},
        {"score": 0.5, "discard": 0.0},
        {"score": 0.5, "discard": 0.0},
    ]
    assert resolve_group_rewards(scored) == [None, 0.8, 0.5, 0.5]


def test_resolve_group_rewards_drops_whole_group_over_half():
    # 3 of 4 discarded -> more than half -> entire group None
    scored = [
        {"score": 0.0, "discard": 1.0},
        {"score": 0.0, "discard": 1.0},
        {"score": 0.0, "discard": 1.0},
        {"score": 0.9, "discard": 0.0},
    ]
    assert resolve_group_rewards(scored) == [None, None, None, None]


def test_resolve_group_rewards_exactly_half_not_dropped():
    # 2 of 4 discarded -> NOT strictly more than half -> group survives
    scored = [
        {"score": 0.0, "discard": 1.0},
        {"score": 0.0, "discard": 1.0},
        {"score": 0.7, "discard": 0.0},
        {"score": 0.6, "discard": 0.0},
    ]
    assert resolve_group_rewards(scored) == [None, None, 0.7, 0.6]


def test_resolve_group_rewards_falls_back_to_judge_error_flag():
    # older rows may carry judge_error instead of discard
    scored = [{"score": 0.0, "judge_error": 1.0}, {"score": 0.5}]
    assert resolve_group_rewards(scored) == [None, 0.5]


def test_resolve_group_rewards_empty():
    assert resolve_group_rewards([]) == []


def test_get_judge_requires_env(monkeypatch):
    set_judge(None)
    monkeypatch.delenv("REWARD_API_BASE", raising=False)
    monkeypatch.delenv("REWARD_MODEL", raising=False)
    from agents.config import _reload_config

    _reload_config("/nonexistent/agents.yaml")
    try:
        with pytest.raises(RuntimeError, match="Reward not configured|REWARD_API_BASE"):
            get_judge()
    finally:
        set_judge(None)
        _reload_config(None)
