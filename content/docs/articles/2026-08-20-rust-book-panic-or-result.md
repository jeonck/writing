---
title: 에러 처리 지침 문서의 표현
description: 도구와 사람의 판단 경계를 긋고, 결정권을 호출자에게 넘기고, 조치를 규정으로 못 박는 문장 5개.
weight: 0
date: 2026-08-20
source: "The Rust Programming Language · 9.3"
sourceURL: https://doc.rust-lang.org/book/ch09-03-to-panic-or-not-to-panic.html
---

# 에러 처리 지침 문서의 표현

언제 프로그램을 멈춰 세우고(`panic!`) 언제 실패를 값으로 돌려줄지(`Result`)를 다룬 장.
"이럴 땐 이렇게 하라"를 명령조로 밀어붙이지 않고, **조건을 좁히고 이유를 붙여 규정하는** 문형이 많아 발췌했다.

> **원문** — Steve Klabnik · Carol Nichols, *The Rust Programming Language*,
> [9.3 To panic! or Not to panic!](https://doc.rust-lang.org/book/ch09-03-to-panic-or-not-to-panic.html)
> ([rust-lang/book](https://github.com/rust-lang/book/blob/main/src/ch09-03-to-panic-or-not-to-panic.md)),
> [MIT](https://github.com/rust-lang/book/blob/main/LICENSE-MIT) /
> [Apache-2.0](https://github.com/rust-lang/book/blob/main/LICENSE-APACHE) 라이선스.
>
> 영어 문장은 원문 그대로 인용했고, 한글 설명과 응용 문장은 이 노트에서 새로 쓴 것이다.

{{< sentence
  en="Let’s explore why, then discuss situations in which the compiler can’t tell that failure is impossible, but you as a human can."
  ko="왜 그런지 살펴본 뒤, 컴파일러는 실패가 불가능하다는 것을 분간하지 못하지만 사람인 당신은 분간할 수 있는 상황들을 이야기하자."
  source="The Rust Programming Language · 9.3"
  sourceURL="https://doc.rust-lang.org/book/ch09-03-to-panic-or-not-to-panic.html"
  note="앞은 `Let’s X, then discuss Y` — 이 장에서 무엇을 어떤 순서로 다룰지 미리 깔아 두는 도입 문형이다. 뒤는 `A can’t tell that P, but B can`, **도구와 사람의 판단 경계를 긋는** 골격. 여기서 `tell`은 '말하다'가 아니라 '분간하다'이고, 마지막 `but you as a human can`은 동사를 되풀이하지 않고 `can`에서 끊어 대비만 남긴다. 자동화가 못 잡는 영역을 사람이 맡는다고 말할 때 그대로 쓴다."
  app1="Let’s look at the alert first, then discuss the cases where the monitor can’t tell that the spike is harmless, but the on-call engineer can."
  app1ko="먼저 알림을 보고, 그다음 모니터는 이 스파이크가 무해하다는 것을 분간하지 못하지만 온콜 엔지니어는 분간할 수 있는 경우들을 이야기하자."
  app2="The scanner can’t tell that this credential is a test fixture, but the reviewer can."
  app2ko="스캐너는 이 자격 증명이 테스트용이라는 것을 분간하지 못하지만, 리뷰어는 분간할 수 있다."
>}}

{{< sentence
  en="When you’re writing an example to illustrate some concept, also including robust error-handling code can make the example less clear."
  ko="어떤 개념을 보여 주려고 예제를 쓸 때, 견고한 에러 처리 코드까지 함께 넣으면 예제가 오히려 덜 명확해질 수 있다."
  source="The Rust Programming Language · 9.3"
  sourceURL="https://doc.rust-lang.org/book/ch09-03-to-panic-or-not-to-panic.html"
  note="`also including X can make Y less clear` — **좋은 것을 더했는데 결과가 나빠진다**고 말하는 문형이다. `also`가 '원래 목적 밖에서 덧붙인 것'임을 표시해 X 자체를 나쁘다고 하지 않고, 동명사구를 주어로 세워 사람이 아니라 선택을 지적한다. `can`이 단정을 가능성으로 낮춘다. 무언가를 빼자고 제안할 때의 기본형."
  app1="When you’re writing a runbook for an outage, also documenting every edge case can make the runbook less usable."
  app1ko="장애 대응 런북을 쓸 때, 모든 예외 상황까지 함께 적으면 런북이 오히려 덜 쓸모 있어질 수 있다."
  app2="When you’re asking for a quick review, also attaching the full design history can make the request harder to answer."
  app2ko="빠른 리뷰를 부탁할 때, 설계 이력 전체까지 함께 붙이면 오히려 답하기 더 어려운 요청이 될 수 있다."
>}}

{{< sentence
  en="If someone calls your code and passes in values that don’t make sense, it’s best to return an error if you can so that the user of the library can decide what they want to do in that case."
  ko="누군가 당신의 코드를 호출하면서 말이 되지 않는 값을 넘긴다면, 가능하다면 에러를 반환하는 편이 가장 좋다. 그래야 그 라이브러리를 쓰는 사람이 그 상황에서 무엇을 할지 스스로 정할 수 있다."
  source="The Rust Programming Language · 9.3"
  sourceURL="https://doc.rust-lang.org/book/ch09-03-to-panic-or-not-to-panic.html"
  note="`it’s best to X if you can so that Y can decide ...` — **판단을 상대에게 넘기는** 권고 문형이다. 세 겹으로 힘을 조절한다: `it’s best to`는 규칙이 아니라 권고, `if you can`은 못 할 수도 있다는 여지, `so that ... can decide`는 그렇게 하는 이유. '내가 대신 정하지 않겠다'는 태도를 한 문장에 담을 때 쓴다."
  app1="If a downstream team sends us a malformed payload, it’s best to reject it with a clear error if we can so that they can decide whether to retry or fix the producer."
  app1ko="다운스트림 팀이 형식이 깨진 페이로드를 보내면, 가능하다면 명확한 에러로 거절하는 편이 가장 좋다. 그래야 그 팀이 재시도할지 생산자를 고칠지 스스로 정할 수 있다."
  app2="If the config is missing a value, it’s best to fail at startup if we can so that the operator can decide what to set before traffic arrives."
  app2ko="설정에 값이 빠져 있으면, 가능하다면 기동 시점에 실패하는 편이 가장 좋다. 그래야 트래픽이 들어오기 전에 운영자가 무엇을 채울지 정할 수 있다."
>}}

{{< sentence
  en="When your code performs an operation that could put a user at risk if it’s called using invalid values, your code should verify the values are valid first and panic if the values aren’t valid."
  ko="유효하지 않은 값으로 호출됐을 때 사용자를 위험에 빠뜨릴 수 있는 연산을 코드가 수행한다면, 그 코드는 먼저 값이 유효한지 검증하고 유효하지 않으면 멈춰야 한다."
  source="The Rust Programming Language · 9.3"
  sourceURL="https://doc.rust-lang.org/book/ch09-03-to-panic-or-not-to-panic.html"
  note="조건절 안에 조건을 한 겹 더 넣어(`an operation that could ... if it’s called ...`) **이 규정이 어디까지만 적용되는지**를 좁힌 문장이다. 앞은 `could`(가능성)로 낮춰 말하고 뒤는 `should`(의무)로 못 박는 대비가 핵심 — 위험은 과장하지 않으면서 조치는 흔들리지 않는다. `verify ... first and ... if ...`로 순서까지 지정해 두면 그대로 점검 항목이 된다."
  app1="When a job performs a deletion that could put customer data at risk if it’s run with an empty filter, the job should verify the filter is non-empty first and abort if it isn’t."
  app1ko="빈 필터로 실행됐을 때 고객 데이터를 위험에 빠뜨릴 수 있는 삭제를 배치 작업이 수행한다면, 그 작업은 먼저 필터가 비어 있지 않은지 검증하고 비어 있으면 중단해야 한다."
  app2="When an endpoint performs an action that could expose another tenant’s records if it’s called with a spoofed ID, the handler should verify ownership first and reject the request if it can’t."
  app2ko="위조된 ID로 호출됐을 때 다른 테넌트의 레코드를 노출할 수 있는 동작을 엔드포인트가 수행한다면, 핸들러는 먼저 소유권을 검증하고 확인되지 않으면 요청을 거절해야 한다."
>}}

{{< sentence
  en="Panicking when the contract is violated makes sense because a contract violation always indicates a caller-side bug, and it’s not a kind of error you want the calling code to have to explicitly handle."
  ko="계약이 깨졌을 때 멈추는 것은 타당하다. 계약 위반은 언제나 호출자 쪽 버그를 뜻하고, 호출하는 코드가 일일이 처리해야 할 종류의 에러가 아니기 때문이다."
  source="The Rust Programming Language · 9.3"
  sourceURL="https://doc.rust-lang.org/book/ch09-03-to-panic-or-not-to-panic.html"
  note="`X makes sense because A, and it’s not a kind of B you want C to have to handle` — 조치를 정당화하면서 **그 문제의 범주 자체를 재분류하는** 문형이다. `always indicates`가 원인을 하나로 단정해 '예외 처리로 덮을 일이 아니다'라는 결론을 준비하고, 뒤 절은 '기술적으로 불가능하다'가 아니라 **그렇게 떠넘기면 안 된다는 설계 판단**을 말한다. `to have to`의 '억지로 떠맡는' 뉘앙스가 톤을 결정한다."
  app1="Failing the build when the schema check breaks makes sense because a schema break always indicates a producer-side change, and it’s not a kind of failure you want each consumer to have to handle at runtime."
  app1ko="스키마 검사가 깨졌을 때 빌드를 실패시키는 것은 타당하다. 스키마 파손은 언제나 생산자 쪽 변경을 뜻하고, 소비자마다 런타임에 떠맡아야 할 종류의 실패가 아니기 때문이다."
  app2="Blocking the merge when the owner is missing makes sense because an unowned service always indicates a gap in the on-call rotation, and it’s not a kind of risk you want the next incident to have to surface."
  app2ko="담당자가 비어 있을 때 머지를 막는 것은 타당하다. 주인 없는 서비스는 언제나 온콜 로테이션의 구멍을 뜻하고, 다음 장애가 대신 드러내 줘야 할 종류의 위험이 아니기 때문이다."
>}}
