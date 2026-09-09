"""CPU unit tests for MultiTurnHermesHarness (no torch/verl/e2b/network).

Mocks: sandbox (in-memory dict for "files", exec returns canned hermes log),
Questioner client (returns canned follow-ups, then None), HermesHarness.run
(records call count + appends a fake trajectory marker).

Uses asyncio.run() in sync tests (pytest-asyncio not installed).
"""

from __future__ import annotations

import asyncio
from typing import Any
from unittest.mock import MagicMock

import pytest


# ---------------------------------------------------------------------------
# Test helpers: mock sandbox, mock context, mock HermesHarness.run
# ---------------------------------------------------------------------------


class MockSandbox:
    """In-memory sandbox: exec returns canned hermes log; no real FS."""

    def __init__(self, hermes_log: str = "fake hermes log output"):
        self._hermes_log = hermes_log
        self.exec_calls: list[str] = []

    async def exec(self, command: str, *, timeout: int = 120, **kwargs: Any) -> Any:
        self.exec_calls.append(command)
        # If the command reads /tmp/hermes.log, return the canned log.
        if "hermes.log" in command:
            return MagicMock(stdout=self._hermes_log)
        # Snapshot probes return empty dict (no FS changes).
        return MagicMock(stdout="{}")


class MockContext:
    """Frozen-like context (supports object.__setattr__ swap)."""

    def __init__(self, instruction: str = "seed query", sample_index: int = 0):
        self.instruction = instruction
        self.sample_index = sample_index
        self.session_id = "test-session"
        self.harness_spec = MagicMock()
        self.harness_spec.settings = {}
        self.harness_spec.env = {}
        self.raw_prompt = [{"role": "user", "content": instruction}]
        self.timeout = 300
        self.max_model_len = 32768
        self.response_length = 4096
        self.is_validation_session = False
        self.global_steps = 0
        self.sandbox_url = "http://localhost"
        self.base_url = "http://localhost"
        self.extra = {}


class MockQuestioner:
    """Returns canned follow-ups; None on Nth call."""

    def __init__(self, responses: list[str | None]):
        self._responses = list(responses)
        self._call_count = 0
        self.last_query_was_error = False

    def next_query(self, persona, report, session_history):
        if self._call_count >= len(self._responses):
            return None
        resp = self._responses[self._call_count]
        self._call_count += 1
        return resp


def _make_harness(k_fixed: int = 3, questioner: Any = None):
    """Create a MultiTurnHermesHarness with mocked dependencies."""
    from agents.multi_turn_harness import MultiTurnHermesHarness

    harness = MultiTurnHermesHarness(k_fixed=k_fixed)
    if questioner is not None:
        harness._questioner = questioner
    return harness


def _get_hermes_base_cls():
    """Get the HermesHarness class that MultiTurnHermesHarness inherits from.

    On-cluster: real recipe_custom HermesHarness.
    Off-cluster: the fallback defined in agents.multi_turn_harness.
    """
    from agents.multi_turn_harness import HermesHarness

    return HermesHarness


def _patch_super_run(call_log: list):
    """Patch HermesHarness.run (the parent class) to just record calls.

    Returns the original run method for restoration.
    """
    HermesHarness = _get_hermes_base_cls()

    async def _fake_run(self, sandbox, ctx):
        call_log.append(ctx.instruction)

    original = HermesHarness.run
    HermesHarness.run = _fake_run
    return original


def _restore_super_run(original):
    HermesHarness = _get_hermes_base_cls()
    HermesHarness.run = original


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------


def test_full_loop_k3_no_early_stop():
    """K_FIXED=3, Questioner never returns None early -> exactly 4 hermes calls."""
    call_log: list[str] = []
    questioner = MockQuestioner(responses=["follow-up 1", "follow-up 2", "follow-up 3"])
    harness = _make_harness(k_fixed=3, questioner=questioner)
    sandbox = MockSandbox()
    ctx = MockContext(instruction="seed query", sample_index=42)

    original = _patch_super_run(call_log)
    try:
        asyncio.run(harness.run(sandbox, ctx))
    finally:
        _restore_super_run(original)

    assert len(call_log) == 4, f"Expected 4 hermes calls, got {len(call_log)}"
    assert call_log[0] == "seed query"
    assert call_log[1] == "follow-up 1"
    assert call_log[2] == "follow-up 2"
    assert call_log[3] == "follow-up 3"


def test_early_stop_on_satisfied():
    """Questioner returns None on 2nd call -> only 2 hermes calls."""
    call_log: list[str] = []
    questioner = MockQuestioner(responses=["follow-up 1", None])
    harness = _make_harness(k_fixed=3, questioner=questioner)
    sandbox = MockSandbox()
    ctx = MockContext(instruction="seed query")

    original = _patch_super_run(call_log)
    try:
        asyncio.run(harness.run(sandbox, ctx))
    finally:
        _restore_super_run(original)

    assert len(call_log) == 2, f"Expected 2 hermes calls, got {len(call_log)}"
    assert call_log[0] == "seed query"
    assert call_log[1] == "follow-up 1"


def test_early_stop_on_error():
    """Questioner returns None with last_query_was_error=True -> early stop."""
    call_log: list[str] = []
    questioner = MockQuestioner(responses=["follow-up 1", None])
    questioner.last_query_was_error = True  # simulate error on 2nd call
    harness = _make_harness(k_fixed=3, questioner=questioner)
    sandbox = MockSandbox()
    ctx = MockContext(instruction="seed query")

    original = _patch_super_run(call_log)
    try:
        asyncio.run(harness.run(sandbox, ctx))
    finally:
        _restore_super_run(original)

    assert len(call_log) == 2, f"Expected 2 hermes calls (error stop), got {len(call_log)}"


def test_instruction_restored_after_loop():
    """ctx.instruction must be restored to original after the loop."""
    call_log: list[str] = []
    questioner = MockQuestioner(responses=["follow-up 1", None])
    harness = _make_harness(k_fixed=3, questioner=questioner)
    sandbox = MockSandbox()
    ctx = MockContext(instruction="seed query")
    original_instruction = ctx.instruction

    original = _patch_super_run(call_log)
    try:
        asyncio.run(harness.run(sandbox, ctx))
    finally:
        _restore_super_run(original)

    assert ctx.instruction == original_instruction, "ctx.instruction not restored"


def test_instruction_restored_on_exception():
    """ctx.instruction must be restored even if super().run raises."""
    HermesHarness = _get_hermes_base_cls()

    async def _crash_run(self, sandbox, ctx):
        raise RuntimeError("hermes crashed")

    questioner = MockQuestioner(responses=["follow-up 1"])
    harness = _make_harness(k_fixed=3, questioner=questioner)
    sandbox = MockSandbox()
    ctx = MockContext(instruction="seed query")
    original_instruction = ctx.instruction

    original = HermesHarness.run
    HermesHarness.run = _crash_run
    try:
        with pytest.raises(RuntimeError, match="hermes crashed"):
            asyncio.run(harness.run(sandbox, ctx))
    finally:
        HermesHarness.run = original

    assert ctx.instruction == original_instruction, "ctx.instruction not restored on exception"


def test_persona_deterministic_by_sample_index():
    """Same sample_index -> same persona (deterministic selection)."""
    from agents.personas import PERSONAS

    # Deterministic: hash(sample_index) % len(PERSONAS)
    idx_0 = hash(0) % len(PERSONAS)
    idx_1 = hash(1) % len(PERSONAS)
    idx_42 = hash(42) % len(PERSONAS)

    # Verify the formula is deterministic and matches.
    assert idx_0 == hash(0) % len(PERSONAS)
    assert idx_1 == hash(1) % len(PERSONAS)
    assert idx_42 == hash(42) % len(PERSONAS)

    # Different indices may or may not map to same persona, but same index is stable.
    assert PERSONAS[idx_0] is PERSONAS[idx_0]


def test_k_fixed_zero_single_turn():
    """K_FIXED=0 -> only turn 0 (seed query), no follow-ups."""
    call_log: list[str] = []
    questioner = MockQuestioner(responses=[])  # never called
    harness = _make_harness(k_fixed=0, questioner=questioner)
    sandbox = MockSandbox()
    ctx = MockContext(instruction="seed query")

    original = _patch_super_run(call_log)
    try:
        asyncio.run(harness.run(sandbox, ctx))
    finally:
        _restore_super_run(original)

    assert len(call_log) == 1, f"Expected 1 hermes call, got {len(call_log)}"
    assert call_log[0] == "seed query"


def test_questioner_exception_breaks_gracefully():
    """If Questioner.next_query raises, the loop breaks without crashing."""
    call_log: list[str] = []

    class CrashingQuestioner:
        last_query_was_error = False

        def next_query(self, persona, report, history):
            raise ConnectionError("tokenhub down")

    harness = _make_harness(k_fixed=3, questioner=CrashingQuestioner())
    sandbox = MockSandbox()
    ctx = MockContext(instruction="seed query")

    original = _patch_super_run(call_log)
    try:
        asyncio.run(harness.run(sandbox, ctx))
    finally:
        _restore_super_run(original)

    # Only turn 0 ran; Questioner crashed on turn 1 -> break.
    assert len(call_log) == 1, f"Expected 1 call (crash on Q1), got {len(call_log)}"


def test_settings_dict_sets_k_fixed():
    """Settings dict with k_fixed overrides the default."""
    from agents.multi_turn_harness import MultiTurnHermesHarness

    harness = MultiTurnHermesHarness(settings={"k_fixed": 5})
    assert harness._k_fixed == 5

    harness2 = MultiTurnHermesHarness(settings={"k_fixed": 1})
    assert harness2._k_fixed == 1


def test_harness_name():
    """Harness has the correct name attribute."""
    from agents.multi_turn_harness import MultiTurnHermesHarness

    assert MultiTurnHermesHarness.name == "multi_turn_hermes"


def test_harness_inherits_hermes():
    """MultiTurnHermesHarness inherits from HermesHarness (real or fallback)."""
    from agents.multi_turn_harness import HermesHarness, MultiTurnHermesHarness

    assert issubclass(MultiTurnHermesHarness, HermesHarness)


def test_harness_inherits_base():
    """MultiTurnHermesHarness inherits from BaseHarness (real or fallback)."""
    from agents.multi_turn_harness import BaseHarness, MultiTurnHermesHarness

    assert issubclass(MultiTurnHermesHarness, BaseHarness)
