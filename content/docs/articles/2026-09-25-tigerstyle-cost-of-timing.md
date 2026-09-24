---
title: 비용이 어디에 쌓이는지 말하는 표현
description: 기본 조건과 목적을 가르고, 통념을 뒤집고, 비용을 시점·주체별로 갈라 놓는 문장 5개.
weight: -35
date: 2026-09-25
source: "TigerStyle (TigerBeetle)"
sourceURL: https://github.com/tigerbeetle/tigerbeetle/blob/main/docs/TIGER_STYLE.md
---

# 비용이 어디에 쌓이는지 말하는 표현

분산 금융 데이터베이스 TigerBeetle이 **자기 팀의 코딩 스타일을 왜 그렇게 정했는지** 설명하는 문서.
규칙 목록이 아니라 규칙의 근거를 파는 글이라, 어떤 관행을 도입하자고 설득하거나 반대로 그 관행의
값을 치르자고 요구하는 문형이 계속 나온다. 특히 **비용을 언제, 누가 치르는지**를 한 문장 안에서
갈라 놓는 방식이 좋아 발췌했다.

> **원문** — TigerBeetle contributors, *TigerStyle*,
> [tigerbeetle/tigerbeetle · docs/TIGER_STYLE.md](https://github.com/tigerbeetle/tigerbeetle/blob/main/docs/TIGER_STYLE.md)
> (main 브랜치, 2026-09-25 확인), [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0).
>
> 영어 문장은 원문 그대로 인용했고, 한글 설명과 응용 문장은 이 노트에서 새로 쓴 것이다.

{{< sentence
  en="Put this way, style is more than readability, and readability is table stakes, a means to an end rather than an end in itself."
  ko="이렇게 놓고 보면 스타일은 가독성 이상이고, 가독성은 기본 조건일 뿐 그 자체가 목적이 아니라 목적에 이르는 수단이다."
  source="TigerStyle · Why Have Style?"
  sourceURL="https://github.com/tigerbeetle/tigerbeetle/blob/main/docs/TIGER_STYLE.md"
  note="`X is more than Y, and Y is table stakes`는 상대가 내세운 것을 깎아내리지 않으면서 **기대치를 한 단 올리는** 문형이다. `table stakes`는 포커에서 판에 앉으려면 올려야 하는 최소 금액으로, '잘해서 자랑할 일이 아니라 없으면 아예 대화가 안 되는 최저선'이라는 뜻. 이어지는 `a means to an end rather than an end in itself`가 그 최저선을 **수단의 자리로 강등**시켜, 논의를 그 너머로 끌고 간다. `Put this way`는 앞에서 내린 정의를 받아 다시 표현할 때 쓰는 연결어다."
  app1="Green CI is more than a gate, and green CI is table stakes, a means to an end rather than an end in itself."
  app1ko="CI 통과는 관문 이상이고, CI 통과는 기본 조건일 뿐 그 자체가 목적이 아니라 목적에 이르는 수단이다."
  app2="Passing the audit is table stakes, a means to an end rather than an end in itself; what we are after is a control that keeps working between audits."
  app2ko="감사 통과는 기본 조건일 뿐, 그 자체가 목적이 아니라 목적에 이르는 수단이다. 우리가 원하는 것은 감사와 감사 사이에도 계속 작동하는 통제다."
>}}

{{< sentence
  en="What could go wrong? What's wrong? Which question would we rather ask? The former, because code, like steel, is less expensive to change while it's hot."
  ko="무엇이 잘못될 수 있는가? 무엇이 잘못됐는가? 우리는 어느 쪽을 묻고 싶은가? 앞의 것이다. 강철처럼 코드도 뜨거울 때 바꾸는 편이 덜 비싸기 때문이다."
  source="TigerStyle · Technical Debt"
  sourceURL="https://github.com/tigerbeetle/tigerbeetle/blob/main/docs/TIGER_STYLE.md"
  note="질문 두 개를 나란히 던지고 `Which question would we rather ask?`로 독자에게 고르게 한 뒤, `The former, because ~`로 답과 근거를 한 번에 주는 구조다. 결론을 먼저 선언하지 않고 **대비를 세워 두고 고르게 만들기** 때문에, 읽는 사람이 그 결론을 자기 것으로 받아들인다. `The former` / `The latter`는 앞서 놓은 두 항목을 되받는 대명사라 질문을 다시 쓰지 않아도 된다. 시제 차이(`could go wrong` vs `'s wrong`)만으로 예방과 사후 대응을 가르는 것도 그대로 훔칠 만하다."
  app1="What could page us at 3am? What paged us at 3am? Which question would we rather ask? The former, because an alert is cheaper to fix before anyone is woken by it."
  app1ko="무엇이 새벽 3시에 우리를 깨울 수 있는가? 무엇이 새벽 3시에 우리를 깨웠는가? 우리는 어느 쪽을 묻고 싶은가? 앞의 것이다. 알림은 누군가 깨어나기 전에 고치는 편이 싸기 때문이다."
  app2="Which review comment would we rather write: why is this permission here, or why was this permission abused? The former, because access is easier to narrow before it is granted."
  app2ko="어느 쪽 리뷰 코멘트를 쓰고 싶은가. 이 권한은 왜 여기 있는가, 아니면 이 권한은 왜 악용됐는가. 앞의 것이다. 권한은 부여되기 전에 좁히는 편이 쉽기 때문이다."
>}}

{{< sentence
  en="Contrary to popular belief, simplicity is also not the first attempt but the hardest revision."
  ko="통념과 달리 단순함 역시 첫 시도가 아니라 가장 힘든 개정판이다."
  source="TigerStyle · On Simplicity And Elegance"
  sourceURL="https://github.com/tigerbeetle/tigerbeetle/blob/main/docs/TIGER_STYLE.md"
  note="`Contrary to popular belief, X is not A but B` — 통념을 먼저 세워 두고 그 자리에 다른 것을 앉히는 **교정 문형**. `not A but B`는 A를 부정하는 데서 끝나지 않고 B를 그 자리에 **대체로** 밀어 넣기 때문에, `X is B`라고만 쓰는 것보다 훨씬 세게 읽힌다. `also`는 앞에서 이미 한 번 통념을 깬 뒤 '이것도 마찬가지'라고 얹는 부사다. 흔한 오해를 상대가 말하기 전에 선점할 때 쓴다."
  app1="Contrary to popular belief, a runbook is not the first draft but the version rewritten after the third incident."
  app1ko="통념과 달리 런북은 첫 초안이 아니라 세 번째 장애를 겪고 다시 쓴 판본이다."
  app2="Contrary to popular belief, the hard part of this migration was not the cutover but the six months of keeping both paths correct."
  app2ko="통념과 달리 이 마이그레이션의 어려운 부분은 전환 그 자체가 아니라, 두 경로를 모두 정확하게 유지한 여섯 달이었다."
>}}

{{< sentence
  en="Standardizing on Zig for tooling is important to ensure that we reduce dimensionality, as the team, and therefore the range of personal tastes, grows. This may be slower for you in the short term, but makes for more velocity for the team in the long term."
  ko="도구를 Zig로 표준화하는 것은, 팀이 커지고 따라서 개인 취향의 폭도 넓어질 때 차원을 줄이기 위해 중요하다. 이는 단기적으로 당신에게는 더 느릴 수 있지만, 장기적으로 팀에는 더 큰 속도를 만들어 준다."
  source="TigerStyle · Tooling"
  sourceURL="https://github.com/tigerbeetle/tigerbeetle/blob/main/docs/TIGER_STYLE.md"
  note="`This may be slower for you in the short term, but makes for more velocity for the team in the long term.` — **비용을 누가 언제 치르는지**를 한 문장에 박아 넣는 문형이다. `for you` / `for the team`이 주체를, `in the short term` / `in the long term`이 시간축을 각각 대비시켜 두 축이 동시에 뒤집힌다. `may be`가 상대의 불편을 부정하지 않고 인정해 주기 때문에 명령이 아니라 설득으로 읽힌다. 앞 문장의 `as the team ... grows`는 그 규칙이 **언제부터 이득이 되는지**의 조건을 미리 깔아 두는 장치다."
  app1="Writing the migration behind a feature flag may be slower for you in the short term, but makes for a safer rollback for the team in the long term."
  app1ko="마이그레이션을 기능 플래그 뒤에 두고 작업하는 것은 단기적으로 당신에게는 더 느릴 수 있지만, 장기적으로 팀에는 더 안전한 롤백을 만들어 준다."
  app2="Requiring a second reviewer on every schema change may be slower for the author in the short term, but makes for fewer incidents for the on-call in the long term."
  app2ko="스키마 변경마다 리뷰어를 한 명 더 요구하는 것은 단기적으로 작성자에게는 더 느릴 수 있지만, 장기적으로 온콜에게는 장애를 줄여 준다."
>}}

{{< sentence
  en="Dependencies, in general, inevitably lead to supply chain attacks, safety and performance risk, and slow install times. For foundational infrastructure in particular, the cost of any dependency is further amplified throughout the rest of the stack."
  ko="의존성은 일반적으로 공급망 공격, 안전성과 성능의 위험, 느린 설치 시간을 필연적으로 불러온다. 특히 기반 인프라에서는 어떤 의존성이든 그 비용이 스택의 나머지 전체에 걸쳐 한층 더 증폭된다."
  source="TigerStyle · Dependencies"
  sourceURL="https://github.com/tigerbeetle/tigerbeetle/blob/main/docs/TIGER_STYLE.md"
  note="`X, in general, ... For Y in particular, ... is further amplified` — **일반 원칙을 먼저 깔고, 내 맥락에서 그 원칙이 왜 더 세게 적용되는지**를 잇는 두 문장 구조. `in general`과 `in particular`가 짝으로 움직이며 범위를 좁히고, `further`가 '새로운 문제가 아니라 같은 문제의 증폭'임을 표시한다. 남들과 같은 기준으로는 부족하다고 주장할 때, 예외를 요구하는 대신 **강도를 올려** 말하는 방법이다. `the cost of any dependency`처럼 `any`를 쓰면 개별 사례를 하나씩 따지는 논쟁을 미리 막는다."
  app1="Flaky tests, in general, erode trust in CI. For the release branch in particular, the cost of a flaky test is further amplified across every team waiting to ship."
  app1ko="간헐적으로 실패하는 테스트는 일반적으로 CI에 대한 신뢰를 깎아먹는다. 특히 릴리스 브랜치에서는 그 비용이 배포를 기다리는 모든 팀에 걸쳐 한층 더 증폭된다."
  app2="Over-broad permissions, in general, widen the blast radius of a mistake. For a shared CI runner in particular, the cost of one extra scope is further amplified across every repository it builds."
  app2ko="지나치게 넓은 권한은 일반적으로 실수의 폭발 반경을 키운다. 특히 공용 CI 러너에서는 스코프 하나가 더 늘어난 비용이 그 러너가 빌드하는 모든 리포지터리에 걸쳐 한층 더 증폭된다."
>}}
