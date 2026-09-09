"""Source-side side-channel for live rollout messages (with tool outputs).

== Why ==

The training rollout produces, per row, a full multi-turn ``messages`` list that
INCLUDES the sandbox tool outputs (``rollout/collect.py`` appends each tool result
as a ``{"role": "user", "content": "[Sandbox Output]\\n..."}`` message). Those live
messages are put on ``non_tensor["messages"]`` at rollout
(``agent_rollout_manager.trajectories_to_dataproto``), but after the DataProto makes a
full round-trip through verl's transfer_queue + train step, the persist hook
(``_persist_rollout_status``) reads them back EMPTY (an unresolved v1-runtime batch-
shape issue, flagged at ``trajectory_adapter_v1`` line 15). It then falls back to
decoding ``response_token_ids``, which reconstructs only ``[user(prompt),
assistant(response)]`` two blobs and DROPS the tool outputs. So the on-disk
``rollout_status`` dump cannot show the source data the judge actually saw.

== What this does ==

Capture the live ``messages`` at the SOURCE (in ``generate_sequences``, where they
are definitely intact) into a per-experiment JSONL side file, keyed by ``task_id``.
``_persist_rollout_status`` then PREFERS these over the token-decode fallback, so the
dump keeps the full multi-turn transcript incl. ``[Sandbox Output]``. This does NOT
touch the training tensors -- it is a persistence/audit side-channel only.

Alignment: verl repeats each query ``rollout.n`` times, so multiple rollouts share a
``task_id``. We store a LIST per task_id and the reader pops them in write order
(rollout order), matching how the dump groups by task_id. The file is rewritten each
rollout step (``reset_and_write``) so a step only ever reads its own rollout's
messages; stale rows from a previous step never leak in.
"""

from __future__ import annotations

import json
import os
import threading
from pathlib import Path
from typing import Any

# Serialise appends across the ThreadPoolExecutor sessions (same reason as the
# winners.jsonl lock in simulated_session): large `messages` payloads (> PIPE_BUF)
# must not interleave into corrupt lines.
_LOCK = threading.Lock()

# One pending file per experiment. Written during rollout, consumed at persist.
# Not step-suffixed: the rollout manager can't see global_steps, and the persist
# hook rewrites/consumes it each step, so a single current-rollout file is enough.
_PENDING_NAME = ".live_messages.pending.jsonl"


def pending_path(exp_name: str) -> Path:
    """Path of the per-experiment pending side file (same dir as rollout_status)."""
    return Path(f"rollouts/training/{exp_name}") / _PENDING_NAME


def reset(exp_name: str) -> None:
    """Truncate the pending file so a fresh rollout step starts clean.

    Called once at the start of each rollout's write burst. Best-effort: a missing
    parent dir is created; any error is swallowed (the side-channel is optional).
    """
    try:
        p = pending_path(exp_name)
        p.parent.mkdir(parents=True, exist_ok=True)
        with _LOCK, open(p, "w", encoding="utf-8"):
            pass  # truncate
    except OSError:
        pass


def append(exp_name: str, task_id: str, messages: list[dict[str, Any]]) -> None:
    """Append one ``{task_id, messages}`` record to the pending file (thread-safe).

    Best-effort: any serialisation / IO error is swallowed so a persistence hiccup
    never breaks the rollout that produced real training tensors.
    """
    if not task_id or not messages:
        return
    try:
        line = json.dumps({"task_id": str(task_id), "messages": messages}, ensure_ascii=False)
    except (TypeError, ValueError):
        return
    try:
        p = pending_path(exp_name)
        p.parent.mkdir(parents=True, exist_ok=True)
        with _LOCK, open(p, "a", encoding="utf-8") as f:
            f.write(line + "\n")
    except OSError:
        pass


def write_batch(exp_name: str, task_ids: list[str], messages_list: list[list[dict[str, Any]]]) -> None:
    """Reset then write a whole rollout's rows at once (one row per trajectory).

    ``task_ids`` and ``messages_list`` are aligned by index (row order). Rows with a
    falsy task_id or empty messages are skipped. Best-effort, never raises.
    """
    reset(exp_name)
    for tid, msgs in zip(task_ids, messages_list, strict=False):
        append(exp_name, tid, msgs)


def load_map(exp_name: str) -> dict[str, list[list[dict[str, Any]]]]:
    """Load the pending file into ``{task_id: [messages, messages, ...]}`` (write order).

    Returns an empty dict when the file is absent / unreadable, so the reader simply
    falls back to its existing behaviour. Malformed lines are skipped individually.
    """
    p = pending_path(exp_name)
    out: dict[str, list[list[dict[str, Any]]]] = {}
    if not p.exists():
        return out
    try:
        with open(p, encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    rec = json.loads(line)
                except (TypeError, ValueError):
                    continue
                tid = rec.get("task_id")
                msgs = rec.get("messages")
                if tid and isinstance(msgs, list) and msgs:
                    out.setdefault(str(tid), []).append(msgs)
    except OSError:
        return {}
    return out


class LiveMessagePopper:
    """Pop live message-lists per task_id in write order (rollout order).

    Built from ``load_map``; ``pop(task_id)`` returns the next unused message-list for
    that task_id, or None when exhausted / absent. Lets ``_persist_rollout_status``
    consume one live transcript per rollout row while iterating a task_id's group.
    """

    def __init__(self, mapping: dict[str, list[list[dict[str, Any]]]] | None):
        self._map = mapping or {}
        self._idx: dict[str, int] = {}

    def pop(self, task_id: str) -> list[dict[str, Any]] | None:
        lst = self._map.get(str(task_id))
        if not lst:
            return None
        i = self._idx.get(str(task_id), 0)
        if i >= len(lst):
            return None
        self._idx[str(task_id)] = i + 1
        return lst[i]


def cleanup(exp_name: str) -> None:
    """Remove the pending file after a step's dump is written (best-effort)."""
    try:
        os.remove(pending_path(exp_name))
    except OSError:
        pass
