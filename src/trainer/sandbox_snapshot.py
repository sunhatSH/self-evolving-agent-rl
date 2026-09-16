"""沙箱工作区状态存/恢复(跨 step 状态继承).

方案: tar+base64(独立验证通过, scripts/test_sandbox_restore.py):
  存: cd workspace && tar czf - . | base64 -w0  → base64 字符串
  恢复: files.write(.snapshot.b64) → base64 -d | tar xzf -

跨 step 数据流:
  step t: observer_hook.run 沙箱关闭前 → snapshot_workspace_b64 → reward_info["_workspace_snapshot"]
          → TQ → cross_step._extract_best_per_group 取最优组的快照
          → build_cross_step_batch 放进 extra_info["_workspace_snapshot"]
  step t+1: observer_hook.prepare 沙箱创建后 → 若 ctx.extra.extra_info 带快照 → restore_workspace_b64

不依赖 e2b 快照 API(create_snapshot/fork), 用 tar+base64 跨沙箱, 稳定 + 含嵌套目录.
"""

from __future__ import annotations

from typing import Any

_WORKSPACE = "/home/user/workspace"
_MAX_SNAPSHOT_BYTES = 64 * 1024 * 1024  # 64MB base64 上限 (真实 workspace 数据分析产出可达 10MB+)


async def _exec(sandbox: Any, cmd: str, timeout: int = 120) -> tuple[str, str, int]:
    """跑一条 shell 命令, 返回 (stdout, stderr, exit_code).

    用 recipe_custom sandbox 的 async `exec` 接口(observer_hook/verifier_hook 同款).
    exec 返回对象带 .stdout/.stderr/.exit_code(或 returncode)。
    """
    res = await sandbox.exec(cmd, timeout=timeout)
    stdout = getattr(res, "stdout", "") or ""
    stderr = getattr(res, "stderr", "") or ""
    code = getattr(res, "exit_code", None)
    if code is None:
        code = getattr(res, "returncode", 0)
    return stdout, stderr, int(code or 0)


async def snapshot_workspace_b64(sandbox: Any, workdir: str = _WORKSPACE) -> str | None:
    """把 workspace tar+base64 → base64 字符串. 失败/超限返回 None."""
    try:
        cmd = f"cd {workdir} 2>/dev/null && tar czf - . 2>/dev/null | base64 -w0"
        stdout, stderr, code = await _exec(sandbox, cmd, timeout=120)
        if code != 0:
            print(f"[cross-step] snapshot_workspace failed (code={code}): {stderr[:200]}", flush=True)
            return None
        b64 = stdout.strip()
        if not b64:
            return None
        if len(b64) > _MAX_SNAPSHOT_BYTES:
            print(
                f"[cross-step] snapshot too large ({len(b64)} > {_MAX_SNAPSHOT_BYTES}), skip",
                flush=True,
            )
            return None
        return b64
    except Exception as exc:  # noqa: BLE001 -- best-effort, never crash rollout
        print(f"[cross-step] snapshot_workspace exception: {exc}", flush=True)
        return None


async def restore_workspace_b64(sandbox: Any, b64_data: str, workdir: str = _WORKSPACE) -> bool:
    """把 base64 tar 解包到新沙箱的 workspace. 成功 True, 失败 False."""
    if not b64_data:
        return False
    try:
        await _exec(sandbox, f"mkdir -p {workdir}", timeout=30)
        # base64 经 write_file 写进临时文件(避免命令行长度限制), 再 decode+untar
        await sandbox.write_file(f"{workdir}/.snapshot.b64", b64_data)
        cmd = f"cd {workdir} && base64 -d .snapshot.b64 | tar xzf - && rm -f .snapshot.b64"
        stdout, stderr, code = await _exec(sandbox, cmd, timeout=120)
        if code != 0:
            print(f"[cross-step] restore_workspace failed (code={code}): {stderr[:200]}", flush=True)
            return False
        print(f"[cross-step] restored workspace snapshot ({len(b64_data)} b64 chars)", flush=True)
        return True
    except Exception as exc:  # noqa: BLE001
        print(f"[cross-step] restore_workspace exception: {exc}", flush=True)
        return False
