"""独立测试: e2b 沙箱状态存/恢复(不依赖训练 step, 几分钟验证).

方案: tar 打包 workspace → 下载到本地/base64 → 新沙箱解包注入(和原 CL agent_assets 一致).
验证: 沙箱 A 写文件 → 存快照 → 沙箱 B 恢复 → 读文件确认内容一致.

运行:
  source scripts/env/load_tencent_env.sh
  python3 scripts/test_sandbox_restore.py
"""
import base64
import sys

sys.path.insert(0, "src")

from rollout.sandbox_client import E2BSandbox  # noqa: E402


def snapshot_workspace(sb, workdir="/home/user/workspace") -> str:
    """把 workspace tar+base64, 返回 base64 字符串(可存进 seed)."""
    # tar 整个 workspace → base64 到 stdout
    cmd = f"cd {workdir} && tar czf - . 2>/dev/null | base64 -w0"
    out = sb._sb.commands.run(cmd, timeout=120, cwd="/tmp")
    if out.exit_code != 0:
        raise RuntimeError(f"snapshot failed: {out.stderr}")
    return (out.stdout or "").strip()


def restore_workspace(sb, b64_data: str, workdir="/home/user/workspace") -> None:
    """把 base64 tar 解包到新沙箱的 workspace."""
    # 先建目录, 再解包
    sb._sb.commands.run(f"mkdir -p {workdir}", timeout=30, cwd="/tmp")
    # base64 写进临时文件, 再 decode + untar (避免命令行长度限制, 用 files.write)
    sb._sb.files.write(f"{workdir}/.snapshot.b64", b64_data)
    cmd = f"cd {workdir} && base64 -d .snapshot.b64 | tar xzf - && rm .snapshot.b64"
    out = sb._sb.commands.run(cmd, timeout=120, cwd="/tmp")
    if out.exit_code != 0:
        raise RuntimeError(f"restore failed: {out.stderr}")


def main():
    print("=== 沙箱 A: 创建 + 写文件 ===", flush=True)
    sb_a = E2BSandbox(template="agentic-cl-sandbox", timeout=300)
    print(f"sandbox A id: {sb_a._sandbox_id}", flush=True)

    # 在 A 里写几个文件(模拟 actor 的产出)
    sb_a._sb.commands.run("mkdir -p /home/user/workspace", timeout=30, cwd="/tmp")
    sb_a._sb.files.write("/home/user/workspace/result.txt", "step1 actor 的产出: 数据分析完成")
    sb_a._sb.files.write("/home/user/workspace/data/report.csv", "col1,col2\n1,2\n3,4")
    sb_a._sb.commands.run(
        "echo '{\"analysis\": \"done\", \"rows\": 100}' > /home/user/workspace/state.json",
        timeout=30, cwd="/tmp",
    )
    # 确认 A 里有这些文件
    out = sb_a._sb.commands.run("find /home/user/workspace -type f | sort", timeout=30, cwd="/tmp")
    print(f"A workspace files:\n{out.stdout}", flush=True)

    print("\n=== 存快照(tar+base64) ===", flush=True)
    snap = snapshot_workspace(sb_a)
    print(f"snapshot size: {len(snap)} base64 chars (~{len(snap)*3//4} bytes)", flush=True)
    sb_a.kill()
    print("sandbox A killed", flush=True)

    print("\n=== 沙箱 B: 新建 + 恢复快照 ===", flush=True)
    sb_b = E2BSandbox(template="agentic-cl-sandbox", timeout=300)
    print(f"sandbox B id: {sb_b._sandbox_id}", flush=True)
    # B 是全新的, 先确认没有 A 的文件
    out = sb_b._sb.commands.run("find /home/user/workspace -type f 2>/dev/null | sort", timeout=30, cwd="/tmp")
    print(f"B workspace BEFORE restore:\n{out.stdout or '(empty)'}", flush=True)

    restore_workspace(sb_b, snap)

    print("\n=== 验证 B 恢复后的内容 ===", flush=True)
    out = sb_b._sb.commands.run("find /home/user/workspace -type f | sort", timeout=30, cwd="/tmp")
    print(f"B workspace AFTER restore:\n{out.stdout}", flush=True)

    # 逐个验证内容
    ok = True
    checks = [
        ("/home/user/workspace/result.txt", "step1 actor 的产出"),
        ("/home/user/workspace/data/report.csv", "col1,col2"),
        ("/home/user/workspace/state.json", "analysis"),
    ]
    for path, expect in checks:
        content = sb_b._sb.files.read(path)
        match = expect in content
        ok = ok and match
        print(f"  {'✅' if match else '❌'} {path}: {content[:50]!r}", flush=True)

    sb_b.kill()
    print("\n=== 结果 ===", flush=True)
    print("✅ 沙箱状态继承成功!" if ok else "❌ 沙箱状态继承失败", flush=True)
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
