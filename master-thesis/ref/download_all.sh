#!/usr/bin/env bash
# 下载 ref.bib 全部 arXiv 文献 PDF 到 ref/。
# 按 arXiv id 去重：现有文件名含 id（如 ..._2402.03300.pdf）则跳过。
# 命名规则：<bibkey>_<arxiv_id>.pdf
set -uo pipefail
cd "$(dirname "${BASH_SOURCE[0]}")"
MAP="$1"   # tsv: key<TAB>id

ok=0; skip=0; fail=0; failed=()
while IFS=$'\t' read -r key id; do
  [[ -z "$id" ]] && continue
  # 已存在（任何文件名含此 id）则跳过
  if ls ./*"${id}"*.pdf >/dev/null 2>&1; then
    echo "SKIP  $id (already present)"; ((skip++)); continue
  fi
  out="${key}_${id}.pdf"
  for attempt in 1 2 3 4 5; do
    echo "GET   $out (try $attempt)"
    if curl -fsL -C - --max-time 900 --retry 2 -o "$out" "https://arxiv.org/pdf/${id}" && [[ -s "$out" ]]; then
      # 校验是 PDF 不是错误页
      if head -c 4 "$out" | grep -q '%PDF'; then
        echo "OK    $out"; ((ok++)); break
      fi
    fi
    sleep 5
    [[ $attempt -eq 5 ]] && { echo "FAIL  $id"; ((fail++)); failed+=("$key $id"); rm -f "$out"; }
  done
  sleep 1
done < "$MAP"

echo "======================================"
echo "OK=$ok  SKIP=$skip  FAIL=$fail"
((fail>0)) && { echo "失败列表:"; printf '  %s\n' "${failed[@]}"; }
echo "当前 ref/ 中 PDF 数: $(ls ./*.pdf 2>/dev/null | wc -l)"
