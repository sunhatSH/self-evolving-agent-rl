"""Single-turn hermes harness (reverted from multi-turn).

This class was previously a K-turn Questioner-driven follow-up loop. The
paradigm has shifted to **cross-step multi-turn**: multi-turn now happens
across training steps (step t+1's seed query comes from the Questioner
evaluating step t's ObserverReport), NOT within a single session. So the
harness reverts to single-turn: it runs hermes ONCE per session, exactly
like the parent HermesHarness.

The class is kept (rather than deleting it and reverting
``default_agent_loop`` to ``hermes_agent``) so that the FQN registration
machinery stays intact for future use and existing tests that reference
``MultiTurnHermesHarness`` continue to import cleanly. ``__init__`` still
accepts ``k_fixed`` for backward compatibility but ignores it — a
deprecation warning is logged so stale configs that still set ``k_fixed``
are surfaced.

Design decisions:
  - Inherit HermesHarness (not compose): call ``super().run()`` to reuse the
    exact hermes command construction + log persistence, and ``super().setup()``
    to reuse config/env writing.
  - No ctx.instruction swap: the seed query is used as-is (no Questioner).
  - No per-turn observer diff: the session-level ObserverDiffHook fires once
    at session end and produces the total diff for the reward judge.
"""

from __future__ import annotations

import logging
import warnings
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


class MultiTurnHermesHarness(HermesHarness):
    """Single-turn pass-through harness (reverted from multi-turn).

    Registered via FQN ``agents.multi_turn_harness.MultiTurnHermesHarness``;
    the harness factory patch (trainer.harness_register) makes create_harness
    accept FQN names.

    ``run()`` delegates to ``HermesHarness.run()`` exactly once — no K-turn
    loop, no Questioner, no per-turn observer diff. Multi-turn is now
    cross-step, not session-internal.
    """

    name = "multi_turn_hermes"

    def __init__(self, *, k_fixed: int = 3, settings: Any = None) -> None:
        """Accept k_fixed for backward compat; ignore it (single-turn now).

        Args:
            k_fixed: deprecated — previously the number of follow-up turns.
                Now ignored; a deprecation warning is logged if non-zero.
            settings: optional dict from harness spec; ``k_fixed`` is read
                from it for the warning check, then discarded.
        """
        if settings and isinstance(settings, dict):
            k_fixed = int(settings.get("k_fixed", k_fixed))
        if k_fixed:
            warnings.warn(
                "MultiTurnHermesHarness.k_fixed=%d is ignored — "
                "harness is single-turn (multi-turn is cross-step, not "
                "session-internal)." % k_fixed,
                DeprecationWarning,
                stacklevel=2,
            )
        self._k_fixed = k_fixed  # kept for backward-compat attribute access

    async def setup(self, sandbox: Any, ctx: Any) -> None:
        """Delegate to HermesHarness.setup (writes hermes config + env)."""
        await super().setup(sandbox, ctx)

    async def run(self, sandbox: Any, ctx: Any) -> None:
        """Run hermes ONCE (single-turn pass-through to HermesHarness.run).

        Multi-turn is now cross-step: step t+1's seed query comes from the
        Questioner evaluating step t's ObserverReport, not from a
        within-session K-turn loop.
        """
        await super().run(sandbox, ctx)
