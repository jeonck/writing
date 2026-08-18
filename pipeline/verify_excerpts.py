#!/usr/bin/env python3
"""발췌 노트의 영어 문장이 원문에 축자 그대로 존재하는지 검증한다.

노트 파일에서 sentence 숏코드의 en="..." 값을 모두 뽑아, 원문(URL 또는 로컬
파일)의 텍스트에 그대로 들어 있는지 확인한다. 하나라도 일치하지 않으면 0이
아닌 코드로 종료하므로, 노트를 커밋하기 전 게이트로 쓴다.

비교 전 양쪽에 같은 정규화를 적용한다: HTML 태그 제거, 엔티티 복원, 공백
축약, 구두점 앞 공백 제거(원문 HTML의 이탤릭 태그가 남기는 흔적), 따옴표·
대시의 유니코드 변형 통일. 즉 타이포그래피 차이는 통과시키되 단어는 하나도
바뀌면 안 된다.

사용법:
    python3 pipeline/verify_excerpts.py <노트.md> <원문 URL 또는 파일>

예:
    python3 pipeline/verify_excerpts.py \
        content/docs/articles/my-note.md https://arxiv.org/html/2607.25379v1
"""

import html
import re
import sys
import unicodedata
import urllib.request

UA = "Mozilla/5.0 (compatible; writing-notes-verifier/1.0)"

QUOTE_MAP = {
    "‘": "'", "’": "'", "‚": "'", "‛": "'",
    "“": '"', "”": '"', "„": '"', "‟": '"',
    "‐": "-", "‑": "-", "‒": "-", "–": "-",
    "—": "-", "―": "-", "−": "-",
    " ": " ", " ": " ", " ": " ",
}


def normalize(text: str) -> str:
    text = unicodedata.normalize("NFKC", text)
    for src, dst in QUOTE_MAP.items():
        text = text.replace(src, dst)
    text = re.sub(r"\s+", " ", text)
    text = re.sub(r"\s+([.,;:!?)\]])", r"\1", text)
    text = re.sub(r"([(\[])\s+", r"\1", text)
    return text.strip()


def fetch(source: str) -> str:
    if re.match(r"^https?://", source):
        req = urllib.request.Request(source, headers={"User-Agent": UA})
        with urllib.request.urlopen(req, timeout=60) as resp:
            raw = resp.read().decode("utf-8", errors="replace")
    else:
        raw = open(source, encoding="utf-8", errors="replace").read()
    body = re.sub(r"<(script|style)\b.*?</\1>", " ", raw, flags=re.S | re.I)
    body = re.sub(r"<[^>]+>", " ", body)
    return normalize(html.unescape(body))


def excerpts(note_path: str) -> list[str]:
    note = open(note_path, encoding="utf-8").read()
    return [html.unescape(m) for m in re.findall(r'^\s*en="(.*)"\s*$', note, re.M)]


def main() -> int:
    if len(sys.argv) != 3:
        print(__doc__.strip())
        return 2
    note_path, source = sys.argv[1], sys.argv[2]

    found = excerpts(note_path)
    if not found:
        print(f"FAIL  {note_path}: en=\"...\" 발췌를 하나도 찾지 못했다")
        return 1

    corpus = fetch(source)
    if len(corpus) < 500:
        print(f"FAIL  원문 텍스트가 너무 짧다({len(corpus)}자) — 가져오기 실패로 본다: {source}")
        return 1

    bad = 0
    for sentence in found:
        ok = normalize(sentence) in corpus
        print(("OK    " if ok else "MISS  ") + sentence[:90])
        bad += 0 if ok else 1

    print(f"\n발췌 {len(found)}개 중 {len(found) - bad}개 일치, {bad}개 불일치")
    if bad:
        print("원문에 없는 문장은 인용이 아니다. 원문 표현으로 고치거나 그 문장을 버려라.")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
