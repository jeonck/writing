# 매일 발췌 노트 추가 — 실행 사양

이 문서는 매일 아침 도는 클라우드 루틴이 따르는 절차다. 루틴은 이 파일을 읽고
그대로 수행한다. 동작을 바꾸려면 루틴이 아니라 **이 파일을 고친다**.

목표: **실제 아티클에서 발췌한 노트 한 편**을 `content/docs/articles/`에 추가하고
커밋·푸시한다. 푸시하면 배포 워크플로가 사이트를 갱신한다.

---

## 1. 출처 고르기 — 오픈 라이선스만

재배포가 허용된 원문만 쓴다. 공개 사이트에 문장 5개를 싣기 때문이다.
**라이선스는 그 페이지에서 직접 눈으로 확인한다.** 확인되지 않으면 후보를 버린다.

허용되는 것:

| 출처 | 라이선스 | 확인 방법 |
| --- | --- | --- |
| arXiv 논문 | CC BY / CC BY-SA / CC0 인 것만 | abs 페이지의 License 표기 |
| 미국 연방정부 간행물 (NASA, NIST, CISA 등) | Public Domain | 기관 저작권 안내 |
| Wikipedia / MDN | CC BY-SA | 문서 하단 라이선스 |
| 오픈소스 공식 문서 | CC BY 등 명시된 것 | 리포지터리 LICENSE |

**금지:** 일반 언론사 기사, 유료 매체, 라이선스 표기가 없는 개인 블로그.
arXiv 기본 라이선스(arXiv perpetual non-exclusive license)는 **재배포 허용이
아니므로 쓰지 않는다.**

### 클라우드 샌드박스의 망 제한 — 먼저 읽을 것

루틴이 도는 샌드박스는 **송신 프록시가 대부분의 호스트를 막는다.** 확인된 사항
(2026-08-18 실행):

- 차단: `arxiv.org`, `en.wikipedia.org`, `developer.mozilla.org`, `www.cisa.gov`,
  `nvlpubs.nist.gov` — WebFetch도 curl도 `EGRESS_BLOCKED` 또는 프록시 403이 난다
- 통과: `raw.githubusercontent.com`, `api.github.com`

그러므로 **GitHub에 원본이 있는 오픈 라이선스 문서**를 1순위로 쓴다. 원문 텍스트와
LICENSE를 모두 `raw.githubusercontent.com`에서 직접 받아 확인할 수 있다.

후보 (돌아가며 쓴다):

| 리포지터리 | 내용 | 산문 라이선스 |
| --- | --- | --- |
| `mdn/content` | 웹 표준·보안·HTTP 가이드 | CC BY-SA 2.5 |
| `kubernetes/website` | 쿠버네티스 개념·운영 문서 | CC BY 4.0 |
| `github/docs` | GitHub 제품 문서 | CC BY 4.0 |
| `rust-lang/book` | Rust 프로그래밍 서적 | MIT / Apache-2.0 |
| `torvalds/linux` (`Documentation/`) | 커널 문서 | GPL-2.0 (인용 가능) |

절차:

1. `https://raw.githubusercontent.com/<repo>/main/LICENSE` (또는 `LICENSE.md`)로
   **산문 라이선스를 먼저 확인한다.** 코드와 산문의 라이선스가 다른 경우가 많다.
2. 본문 마크다운을 `raw.githubusercontent.com`에서 받아 문장을 고른다.
3. 검증은 **raw URL**로 돌린다 (사람이 읽는 페이지는 샌드박스에서 접근이 막힌다):
   `python3 pipeline/verify_excerpts.py <노트> https://raw.githubusercontent.com/...`
4. 노트의 `sourceURL`은 **사람이 읽는 페이지 주소**를 쓴다. 리포지터리 경로에서
   유도하되(`files/en-us/web/security/attacks/csrf/index.md` →
   `https://developer.mozilla.org/en-US/docs/Web/Security/Attacks/CSRF`) 샌드박스에서는
   그 주소가 살아 있는지 확인할 수 없으니, 경로 규칙을 신중히 따르고 원본 리포지터리
   링크도 함께 남긴다.

이 목록에서 못 찾겠으면 다른 오픈 라이선스 리포지터리를 찾아도 된다. 차단된 호스트를
반복해서 두드리느라 시간을 쓰지 말 것.

주제는 사이트 주인의 관심사에 맞춘다 — AI/LLM, 보안, 네트워크, 감사·거버넌스,
소프트웨어 엔지니어링. 매일 같은 우물만 파지 말고 출처 종류를 번갈아 쓴다.

## 2. 중복 피하기

- `pipeline/used-sources.json`의 `used` 목록에 이미 있는 원문은 쓰지 않는다.
- `content/docs/articles/`의 기존 노트도 훑어 같은 원문·같은 문형이 겹치지 않게 한다.

## 3. 문장 5개 고르기

원문 본문에서 **완결된 문장 5개**를 고른다. 기준:

- **문형이 서로 달라야 한다.** 다섯 개가 모두 대조 구문이면 실패다. 재정의,
  증거의 한정, 오해 차단, 역할 규정, 조건과 결과, 양보, 인과 등에서 골고루 뽑는다.
- **구조를 그대로 훔쳐 쓸 수 있어야 한다.** 내용이 흥미로운 문장이 아니라,
  **틀이 재사용되는** 문장을 고른다.
- 정의되지 않은 약어 범벅, 인용 표시(`[12]`)가 박힌 문장, 표·목록 조각은 피한다.
- 문장은 원문 그대로 옮긴다. 다듬거나 줄이지 않는다. 주어가 대명사라 홀로
  이해되지 않으면 **앞 문장까지 포함해 통째로** 인용한다.

## 4. 노트 파일 쓰기

경로: `content/docs/articles/YYYY-MM-DD-<영문-슬러그>.md` (날짜는 KST 기준)

```markdown
---
title: <한국어 제목 — 다른 노트처럼 "~의 표현" 형태>
description: <이 노트에서 무엇을 건질 수 있는지 한 줄>
weight: <기존 노트 중 가장 작은 weight - 1. 음수도 괜찮다 — 새 노트가 위로 온다>
date: YYYY-MM-DD
source: "<짧은 출처 표기>"
sourceURL: <원문 URL>
---

# <제목>

<이 아티클이 무엇을 다루는지 1~2문장. 왜 이 문장들을 골랐는지 한 줄.>

> **원문** — <저자>, *<원문 제목>*, [<출처>](<URL>) (<날짜>), [<라이선스>](<라이선스 URL>).
>
> 영어 문장은 원문 그대로 인용했고, 한글 설명과 응용 문장은 이 노트에서 새로 쓴 것이다.

<sentence 숏코드 5개>
```

각 문장은 `sentence` 숏코드 하나다. 파라미터는 [작성 가이드](../content/docs/guide/how-to-write.md) 참고.

- `note` — **번역이 아니다.** 직역은 `ko`에 넣고, `note`에는 *왜 이 표현인지* 를
  쓴다: 문형의 이름과 작동 방식, 어느 단어가 톤을 결정하는지, 언제 꺼내 쓰는지.
  `백틱`으로 문형 골격(`X tells you A. It says nothing about B.`)을 보여 주면 좋다.
- `app1` / `app2` — 원문 주제를 그대로 두지 말고 **사이트 주인의 맥락**(운영,
  장애 대응, 보안 감사, 코드 리뷰, 팀 커뮤니케이션)으로 옮긴다. 한국어도 함께.
- 파라미터 값은 큰따옴표로 감싸므로 값 안에 `"`를 쓰지 않는다. 필요하면 `&quot;`.

## 5. 검증 — 통과 못 하면 커밋하지 않는다

```bash
python3 pipeline/verify_excerpts.py <노트 경로> <원문 URL>
```

발췌가 원문에 축자로 없으면 실패한다. **실패한 문장은 인용이 아니라 창작이다.**
원문 표현으로 고치거나 그 문장을 버리고 다른 문장으로 채운다. 검증기를
느슨하게 고쳐서 통과시키는 것은 금지.

이어서 빌드가 깨지지 않는지 본다. `hugo`가 있으면:

```bash
hugo --minify
```

`hugo`가 없으면 건너뛰되 실행 요약에 적는다. 숏코드 파라미터의 따옴표 균형은
눈으로 한 번 더 확인한다.

## 6. 상태 기록과 커밋

`pipeline/used-sources.json`의 `used`에 항목을 추가한다:

```json
{"url": "<원문 URL>", "title": "<원문 제목>", "license": "<라이선스>", "date": "YYYY-MM-DD", "note": "<노트 파일 경로>"}
```

그리고 커밋·푸시한다.

```bash
git add content/docs/articles pipeline/used-sources.json
git commit -m "note: <원문 제목 요약> 발췌"
git push
```

## 7. 실패했을 때

**빈손으로 끝내는 것이 나쁜 노트를 올리는 것보다 낫다.** 다음 경우 커밋하지 말고
무엇을 왜 못 했는지 요약만 남긴다.

- 오픈 라이선스 원문을 못 찾았다
- 원문을 가져오지 못했다 (본문 접근 실패)
- 쓸 만한 문장이 5개가 안 된다
- 검증기를 통과하지 못했다

어떤 경우에도 **문장을 지어내거나, 원문에 없는 표현으로 다듬거나, 라이선스를
확인하지 않은 채 진행하지 않는다.**
