"""把已生成的英文论文配图翻译成中文版(图生图 images/edits).

比纯文生图稳: 保留原图布局/配色/箭头/位置, 只把文字标签换成简体中文.

用法:
  set -a; source .env; set +a
  python3 scripts/translate_figures_zh.py                    # 翻译所有 assets/fig_*.png(跳过已有 _zh)
  python3 scripts/translate_figures_zh.py --only fig_fig2_dataflow.png
  python3 scripts/translate_figures_zh.py --force            # 覆盖重译
"""
from __future__ import annotations

import argparse
import base64
import glob
import os
import sys
import time

import requests

_BASE = "https://tokenhub.sensetime.com/v1"
_DEFAULT_MODEL = "gpt-image-2.5-flare/azure_L/qwb"
_ASSETS = os.path.join(os.path.dirname(__file__), "..", "assets")
_PROMPT = (
    "Redraw this exact diagram keeping the IDENTICAL layout, boxes, arrows, colors, icons "
    "and positions unchanged, but translate ALL text labels from English to Simplified "
    "Chinese. Keep all numbers, symbols (S, N, R, 2N, 0.3, x8), stage numbers and structure "
    "exactly the same. Use a clean legible Chinese sans-serif font. Do not add or remove "
    "any element; only swap English words to their natural Chinese equivalents."
)


def _translate(model: str, src: str, dst: str, key: str, size: str) -> bool:
    for attempt in range(1, 4):
        try:
            with open(src, "rb") as f:
                files = {"image": (os.path.basename(src), f, "image/png")}
                data = {"model": model, "prompt": _PROMPT, "n": "1", "size": size}
                r = requests.post(
                    f"{_BASE}/images/edits",
                    headers={"Authorization": f"Bearer {key}"},
                    files=files, data=data, timeout=300,
                )
        except Exception as exc:  # noqa: BLE001
            print(f"    attempt {attempt}: request error {exc}", flush=True)
            time.sleep(5)
            continue
        if r.status_code != 200:
            print(f"    attempt {attempt}: HTTP {r.status_code} {r.text[:200]}", flush=True)
            time.sleep(5)
            continue
        try:
            item = r.json()["data"][0]
        except Exception:  # noqa: BLE001
            print(f"    attempt {attempt}: bad json {r.text[:200]}", flush=True)
            time.sleep(5)
            continue
        if item.get("b64_json"):
            with open(dst, "wb") as f:
                f.write(base64.b64decode(item["b64_json"]))
        elif item.get("url"):
            img = requests.get(item["url"], timeout=180)
            with open(dst, "wb") as f:
                f.write(img.content)
        else:
            print(f"    attempt {attempt}: no image", flush=True)
            time.sleep(5)
            continue
        print(f"    ✅ {os.path.basename(dst)} ({os.path.getsize(dst)} bytes)", flush=True)
        return True
    print("    ❌ failed after 3 attempts", flush=True)
    return False


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", nargs="*", help="只翻译这些文件名(assets/ 下)")
    ap.add_argument("--force", action="store_true")
    ap.add_argument("--model", default=_DEFAULT_MODEL)
    ap.add_argument("--size", default="1536x1024")
    args = ap.parse_args()

    key = os.environ.get("TOKENHUB_API_KEY")
    if not key:
        print("TOKENHUB_API_KEY not set. Run: set -a; source .env; set +a", flush=True)
        return 1

    # 源图 = assets/fig_*.png 且不是 _zh 的
    srcs = sorted(
        p for p in glob.glob(os.path.join(_ASSETS, "fig_*.png"))
        if not p.endswith("_zh.png")
    )
    if args.only:
        want = {os.path.basename(x) for x in args.only}
        srcs = [p for p in srcs if os.path.basename(p) in want]

    print(f"model={args.model} translate {len(srcs)} figures → _zh.png", flush=True)
    ok, skip, fail = 0, 0, 0
    for src in srcs:
        dst = src[:-4] + "_zh.png"
        print(f"\n{os.path.basename(src)} → {os.path.basename(dst)}", flush=True)
        if os.path.exists(dst) and not args.force:
            print("    (exists, skip; --force to overwrite)", flush=True)
            skip += 1
            continue
        if _translate(args.model, src, dst, key, args.size):
            ok += 1
        else:
            fail += 1
    print(f"\n=== done: {ok} translated, {skip} skipped, {fail} failed ===", flush=True)
    return 0 if fail == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
