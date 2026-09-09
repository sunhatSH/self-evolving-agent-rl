"""Let verl's harness factory (create_harness) accept FQN names -- zero-intrusion monkey-patch.

Mirrors ``trainer.observer_hook_register`` (which patches ``create_hook``):
when ``spec.name`` contains "." (e.g. ``agents.multi_turn_harness.MultiTurnHermesHarness``),
load the class via ``load_class_from_fqn`` and instantiate; otherwise fall back
to the original factory (built-in names like "hermes"/"openclaw" work as before).

Idempotent, import-time install, no verl source changes.

Trigger: ``import trainer.harness_register`` (alongside observer_hook_register).
"""

from __future__ import annotations

import inspect

_PATCHED = False


def install() -> None:
    """Monkey-patch recipe_custom harness factory to accept FQN harness names. Idempotent."""
    global _PATCHED
    if _PATCHED:
        return

    try:
        from recipe_custom.agent.runners.harnesses import factory as _factory
    except Exception as exc:  # noqa: BLE001 -- recipe_custom absent off-cluster
        print(f"[agent-rl] harness factory patch skipped (recipe_custom unavailable: {exc})", flush=True)
        return

    from verl.utils.import_utils import load_class_from_fqn

    _orig_create_harness = _factory.create_harness

    def _create_harness_with_fqn(spec):
        # Non-dict / no name -> delegate to original implementation.
        name = getattr(spec, "name", None) if spec else None
        if not name or "." not in str(name):
            return _orig_create_harness(spec)

        # name is FQN (contains "."): dynamically load our harness class.
        harness_cls = load_class_from_fqn(str(name), "BaseHarness")
        settings = dict(getattr(spec, "settings", None) or {})
        # Probe __init__ signature: accept settings (built-in style) or no-arg.
        try:
            params = inspect.signature(harness_cls.__init__).parameters
            if "settings" in params:
                return harness_cls(settings=settings)
        except (TypeError, ValueError):
            pass
        return harness_cls()

    _factory.create_harness = _create_harness_with_fqn
    _PATCHED = True
    print("[agent-rl] harness factory patched (create_harness supports FQN)", flush=True)


# import-time install (mirrors observer_hook_register pattern).
install()
