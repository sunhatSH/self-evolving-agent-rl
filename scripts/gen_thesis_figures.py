"""生成毕业论文配图: 读 assets/thesis_figure_prompts.py 的 10 张图提示词,
调 tokenhub gpt-image-2.5-flare 生成 PNG 存 assets/fig_<key>.png.

用法:
  set -a; source .env; set +a
  python3 scripts/gen_thesis_figures.py                 # 生成全部(跳过已存在)
  python3 scripts/gen_thesis_figures.py --only fig1_architecture fig4_self_evolve_loop
  python3 scripts/gen_thesis_figures.py --force         # 覆盖重生成
  python3 scripts/gen_thesis_figures.py --model gpt-image-2.5-sunburst/azure_L/qwb

依赖: TOKENHUB_API_KEY(从 .env). 长任务建议 tmux/nohup, 但 10 张图串行约几分钟, 前台也可.
"""
from __future__ import annotations

import argparse
import base64
import os
import sys
import time

import requests

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "assets"))
from thesis_figure_prompts import FIGURES  # noqa: E402

_BASE = "https://tokenhub.sensetime.com/v1"
_DEFAULT_MODEL = "gpt-image-2.5-flare/azure_L/qwb"  # 实测可用(2026-09-14)
_ASSETS = os.path.join(os.path.dirname(__file__), "..", "assets")
_SIZE = "1536x1024"  # 横版, 适合论文流程图; 若模型不支持退回 1024x1024


def _gen_one(model: str, prompt: str, out_path: str, key: str, size: str) -> bool:
    """调 tokenhub 生成一张图, 存 out_path. 成功 True."""
    for attempt in range(1, 4):
        try:
            r = requests.post(
                f"{_BASE}/images/generations",
                headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"},
                json={"model": model, "prompt": prompt, "n": 1, "size": size},
                timeout=300,
            )
        except Exception as exc:  # noqa: BLE001
            print(f"    attempt {attempt}: request error {exc}", flush=True)
            time.sleep(5)
            continue
        if r.status_code != 200:
            body = r.text[:300]
            print(f"    attempt {attempt}: HTTP {r.status_code} {body}", flush=True)
            # size 不支持 → 退回 1024x1024 再试
            if "size" in body.lower() and size != "1024x1024":
                size = "1024x1024"
            time.sleep(5)
            continue
        try:
            item = r.json()["data"][0]
        except Exception:  # noqa: BLE001
            print(f"    attempt {attempt}: bad json {r.text[:200]}", flush=True)
            time.sleep(5)
            continue
        # b64_json 或 url 两种返回
        if item.get("b64_json"):
            with open(out_path, "wb") as f:
                f.write(base64.b64decode(item["b64_json"]))
        elif item.get("url"):
            img = requests.get(item["url"], timeout=180)
            with open(out_path, "wb") as f:
                f.write(img.content)
        else:
            print(f"    attempt {attempt}: no image in response", flush=True)
            time.sleep(5)
            continue
        sz = os.path.getsize(out_path)
        print(f"    ✅ saved {out_path} ({sz} bytes)", flush=True)
        return True
    print(f"    ❌ failed after 3 attempts", flush=True)
    return False


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", nargs="*", help="只生成这些 key")
    ap.add_argument("--force", action="store_true", help="覆盖已存在的图")
    ap.add_argument("--model", default=_DEFAULT_MODEL)
    ap.add_argument("--size", default=_SIZE)
    args = ap.parse_args()

    key = os.environ.get("TOKENHUB_API_KEY")
    if not key:
        print("TOKENHUB_API_KEY not set. Run: set -a; source .env; set +a", flush=True)
        return 1

    figs = FIGURES
    if args.only:
        figs = [f for f in FIGURES if f["key"] in set(args.only)]
        if not figs:
            print(f"no figures match {args.only}; available: {[f['key'] for f in FIGURES]}", flush=True)
            return 1

    print(f"model={args.model} size={args.size} figures={len(figs)}", flush=True)
    ok, skip, fail = 0, 0, 0
    for f in figs:
        out = os.path.join(_ASSETS, f"fig_{f['key']}.png")
        print(f"\n[{f['title']}] -> {os.path.basename(out)}", flush=True)
        if os.path.exists(out) and not args.force:
            print(f"    (exists, skip; use --force to regenerate)", flush=True)
            skip += 1
            continue
        if _gen_one(args.model, f["prompt"], out, key, args.size):
            ok += 1
        else:
            fail += 1

    print(f"\n=== done: {ok} generated, {skip} skipped, {fail} failed ===", flush=True)
    return 0 if fail == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
