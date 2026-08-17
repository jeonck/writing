---
title: 노트 작성 가이드
description: sentence 숏코드 파라미터와 노트를 쓸 때 지키는 원칙.
weight: 1
---

# 노트 작성 가이드

## 1. 새 노트 파일 만들기

```bash
hugo new docs/articles/my-article.md
```

`archetypes/default.md`가 프런트매터와 카드 한 개의 뼈대를 채워 준다.
직접 만들 때는 아래 프런트매터를 쓴다.

```yaml
---
title: 아티클 제목
weight: 10          # 사이드바 정렬 순서 (작을수록 위)
date: 2026-08-17
source: 매체 이름
sourceURL: https://example.com/article
---
```

## 2. 문장 카드 추가하기

문장 하나가 카드 하나다. `sentence` 숏코드를 쓴다.

```go-html-template
{{</* sentence
  en="원문 영어 문장"
  ko="한국어 직역"
  source="매체 이름"
  sourceURL="https://example.com/article"
  note="왜 이렇게 썼는지에 대한 한글 설명. **마크다운**을 쓸 수 있다."
  app1="응용 문장 1"
  app1ko="응용 문장 1의 한국어"
  app2="응용 문장 2"
  app2ko="응용 문장 2의 한국어"
*/>}}
```

### 파라미터

| 이름 | 필수 | 설명 |
| --- | --- | --- |
| `en` | ✅ | 발췌한 원문 문장 |
| `ko` |  | 한국어 직역 |
| `note` |  | 한글 설명. 마크다운 렌더링됨 |
| `source` |  | 출처 표기 |
| `sourceURL` |  | 출처 링크 (있으면 `source`가 링크가 된다) |
| `app1` / `app1ko` | ✅ | 첫 번째 응용 문장과 그 한국어 |
| `app2` / `app2ko` | ✅ | 두 번째 응용 문장과 그 한국어 |

> [!WARNING]
> 값에 큰따옴표(`"`)가 들어가면 `&quot;`로 쓰거나 작은따옴표로 바꾼다.
> 숏코드 파라미터는 큰따옴표로 감싸기 때문에 그대로 넣으면 파싱이 깨진다.

## 3. 쓸 때 지키는 것

- **한글 설명은 번역이 아니다.** 직역은 `ko`에 넣고, `note`에는 *왜 이 표현인지* — 구조, 뉘앙스, 대체 표현 — 를 쓴다.
- **응용 문장은 내 맥락으로.** 원문 주제를 그대로 두면 외워지지 않는다. 내가 실제로 쓸 상황으로 바꾼다.
- **한 페이지에 5~8문장.** 그 이상이면 아티클을 나눈다.
- **발췌는 짧게.** 원문을 길게 옮기지 말고 한 문장 단위로 끊는다.

## 4. 로컬에서 확인

```bash
hugo server -D
```

## 5. 배포

`main` 브랜치에 push하면 GitHub Actions가 빌드해서
<https://writing.metacog.co.kr> 로 배포한다.

```bash
git add -A && git commit -m "note: 새 아티클" && git push
```
