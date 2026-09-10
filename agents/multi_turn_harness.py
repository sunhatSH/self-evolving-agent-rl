"""Multi-turn hermes harness: Questioner-driven follow-up loop.

Wraps HermesHarness to run K_FIXED+1 turns per session: turn 0 = seed query,
turns 1..K_FIXED = Questioner.next_query(persona, incremental_report, history).
Session ends early if Questioner returns None (satisfied). Produces K_FIXED+1
trajectories per session (one per hermes run) -- gateway accumulates them on
session.trajectories list.

Phase 4 (baseline): K_FIXED=3, patience OFF (persona.patience ignored).
Phase 2 (future): add PatienceTracker for failure-driven early stop.

The per-turn incremental ObservationReport (fed to Questioner) is built by
calling observer pure fns (snapshot_workspace/diff_snapshots) directly -- the
session-level ObserverDiffHook only fires once at session end, so we compute
our own per-turn diffs here. The session-end hook still produces the final
total diff for the reward judge.

Design decisions:
  - Inherit HermesHarness (not compose): HermesHarness.__init__ is no-arg
    (BaseHarness has no __init__; HermesHarness adds none). Inheritance lets us
    call super().run() to reuse the exact hermes command construction + log
    persistence, and super().setup() to reuse config/env writing.
  - Swap ctx.instruction via object.__setattr__ (AgentRunContext is frozen=True
    dataclass). Save old value, restore in finally so the session-end hook sees
    the original instruction.
  - Per-turn baseline: re-snapshot at run() start (we don't have access to
    ObserverDiffHook.prepare's state.reward_info["_observer_pre_fs"] from inside
    the harness). Each turn's incremental diff = snapshot after turn k minus
    snapshot after turn k-1.
  - Questioner client built lazily (deferred to first next_query call) so import
    never triggers network. If the client fails (tokenhub down), break the loop
    gracefully -- the turns completed so far still produce trajectories.
"""

from __future__ import annotations

import logging
from abc import ABC, abstractmethod
from typing import Any

try:
    from recipe_custom.agent.runners.harnesses.base import BaseHarness
    from recipe_custom.agent.runners.harnesses.hermes import HermesHarness
except Exception:  # noqa: BLE001 -- recipe_custom absent off-cluster (unit tests)

    class BaseHarness(ABC):  # type: ignore[no-redef]
        """Fallback base (off-cluster, unit-testable)."""

        name: str

        async def setup(self, sandbox: Any, ctx: Any) -> None:
            pass

        @abstractmethod
        async def run(self, sandbox: Any, ctx: Any) -> None:
            ...

        async def cleanup(self, sandbox: Any, ctx: Any) -> None:
            pass

    class HermesHarness(BaseHarness):  # type: ignore[no-redef]
        """Fallback HermesHarness for off-cluster unit tests."""

        name = "hermes"

        async def setup(self, sandbox: Any, ctx: Any) -> None:
            pass

        async def run(self, sandbox: Any, ctx: Any) -> None:
            pass

logger = logging.getLogger(__name__)

HERMES_LOG_PATH = "/tmp/hermes.log"
_MAX_HERMES_LOG_CHARS = 4000  # cap trajectory text fed to Questioner


class MultiTurnHermesHarness(HermesHarness):
    """Hermes harness that runs K_FIXED+1 turns with Questioner-driven follow-ups.

    Registered via FQN ``agents.multi_turn_harness.MultiTurnHermesHarness``;
    the harness factory patch (trainer.harness_register) makes create_harness
    accept FQN names. Settings: ``k_fixed`` (default 3).
    """

    name = "multi_turn_hermes"

    def __init__(self, *, k_fixed: int = 3, settings: Any = None) -> None:
        """Accept optional settings dict (mirrors observer_hook_register signature probe).

        Args:
            k_fixed: number of FOLLOW-UP turns (total turns = k_fixed + 1).
            settings: optional dict from harness spec; if present, ``k_fixed``
                is read from it (overriding the kwarg).
        """
        if settings and isinstance(settings, dict):
            k_fixed = int(settings.get("k_fixed", k_fixed))
        self._k_fixed = max(0, k_fixed)
        # Questioner built lazily so import never triggers network.
        self._questioner: Any = None
        self._observer_use_llm = False

    @property
    def questioner(self):
        """Lazily build a Questioner (deferred client, resolves on first call)."""
        if self._questioner is None:
            from agents.questioner import Questioner

            self._questioner = Questioner()
        return self._questioner

    async def setup(self, sandbox: Any, ctx: Any) -> None:
        """Delegate to HermesHarness.setup (writes hermes config + env)."""
        await super().setup(sandbox, ctx)

    async def run(self, sandbox: Any, ctx: Any) -> None:
        """Run K_FIXED+1 hermes turns with Questioner-driven follow-ups.

        Turn 0 uses ctx.instruction (the seed query). Each subsequent turn uses
        Questioner.next_query(persona, incremental_report, history). The loop
        ends early if the Questioner returns None (satisfied or error).
        """
        from agents.observer import (
            build_deterministic_report,
            diff_snapshots,
            diff_system,
            snapshot_workspace,
            snapshot_system,
            _format_changes,
            _is_runtime_file,
        )
        from agents.personas import PERSONAS

        # Deterministic persona selection by sample_index (no patience in this phase).
        persona = PERSONAS[hash(ctx.sample_index) % len(PERSONAS)]

        # Our own baseline: re-snapshot at run() start (we don't have access to
        # ObserverDiffHook.prepare's state.reward_info["_observer_pre_fs"]).
        prev_fs = self._filter_runtime(snapshot_workspace(sandbox))
        prev_sys = snapshot_system(sandbox)

        history: list[dict[str, Any]] = []
        current_query = ctx.instruction
        original_instruction = ctx.instruction

        try:
            for turn in range(self._k_fixed + 1):
                # Swap ctx.instruction to current_query (frozen dataclass).
                object.__setattr__(ctx, "instruction", current_query)
                try:
                    await super().run(sandbox, ctx)
                finally:
                    # Restore original instruction so session-end hook sees it.
                    object.__setattr__(ctx, "instruction", original_instruction)

                # Last turn: no follow-up needed.
                if turn == self._k_fixed:
                    break

                # Build incremental report for Questioner.
                post_fs = self._filter_runtime(snapshot_workspace(sandbox))
                post_sys = snapshot_system(sandbox)
                diff = diff_snapshots(prev_fs, post_fs)
                sys_diff = diff_system(prev_sys, post_sys)
                state_diff = _format_changes(diff, sys_diff)
                file_tree = "\n".join(sorted(post_fs.keys()))

                report = build_deterministic_report(
                    diff=diff,
                    file_tree=file_tree,
                    state_diff=state_diff,
                )
                # Attach hermes log as actor trajectory (capped).
                report.actor_trajectory = await self._read_hermes_log(sandbox)

                prev_fs = post_fs
                prev_sys = post_sys

                # Ask Questioner for the next query. next_query is synchronous
                # (httpx.post to tokenhub); run it in a thread so it doesn't
                # block the event loop / gateway generation_lock while waiting
                # on the network round-trip.
                try:
                    next_q = await asyncio.to_thread(
                        self.questioner.next_query, persona, report, history
                    )
                except Exception:  # noqa: BLE001 -- Questioner failure must not crash session
                    logger.warning(
                        "Questioner failed on turn %d, ending multi-turn loop early",
                        turn,
                        exc_info=True,
                    )
                    break

                # Record this turn's query in history.
                history.append({"role": "user", "content": current_query})

                if next_q is None:
                    # None = satisfied (model chose end) or error (check last_query_was_error).
                    if self.questioner.last_query_was_error:
                        logger.warning(
                            "Questioner returned None due to error on turn %d, ending early",
                            turn,
                        )
                    else:
                        logger.info(
                            "Questioner satisfied on turn %d, ending multi-turn loop early",
                            turn,
                        )
                    break

                current_query = next_q
        finally:
            # Ensure ctx.instruction is restored even on unexpected exception.
            object.__setattr__(ctx, "instruction", original_instruction)

    async def _read_hermes_log(self, sandbox: Any) -> str:
        """Read /tmp/hermes.log (capped) for the Questioner's actor_trajectory field."""
        try:
            res = await sandbox.exec(
                f"python3 -c \"import sys; sys.stdout.write(open('{HERMES_LOG_PATH}','r',errors='replace').read()[:{_MAX_HERMES_LOG_CHARS}])\"",
                timeout=30,
            )
            return getattr(res, "stdout", "") or ""
        except Exception:  # noqa: BLE001 -- never crash the session
            return ""

    @staticmethod
    def _filter_runtime(snap: dict | None) -> dict:
        """Drop runtime/framework files from a snapshot (mirror observer logic)."""
        if not isinstance(snap, dict):
            return {}
        return {p: r for p, r in snap.items() if not _is_runtime_file(p)}
