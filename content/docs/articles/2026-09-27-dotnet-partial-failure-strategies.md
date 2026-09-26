---
title: 대책을 권하면서 그 한계를 같이 적는 표현
description: 금지를 권고로 말하고, 예외를 먼저 떼어 놓고, 임계값의 근거를 괄호로 붙이고, 적용 범위를 스스로 좁히는 문장 5개.
weight: -37
date: 2026-09-27
source: ".NET Architecture Guides — Strategies to handle partial failure"
sourceURL: https://learn.microsoft.com/en-us/dotnet/architecture/microservices/implement-resilient-applications/partial-failure-strategies
---

# 대책을 권하면서 그 한계를 같이 적는 표현

분산 시스템에서 **일부만 죽는 실패**(partial failure)를 어떻게 받아낼지 여섯 가지 전략으로
정리한 문서. 비동기 통신, 지수 백오프 재시도, 타임아웃, 서킷 브레이커, 폴백, 큐 상한을 차례로
권한다. 전략 문서인데도 **"이렇게 하라"로 끝내지 않고 그 권고가 어디까지 듣는지, 왜 그 숫자로
정했는지를 매 항목마다 한 줄씩 붙여 놓는다.** 대책을 제안하는 글에서 반박을 미리 흡수하는
문형이 필요해서 발췌했다.

> **원문** — .NET documentation contributors, *Strategies to handle partial failure*,
> [.NET Architecture Guides — Microservices](https://learn.microsoft.com/en-us/dotnet/architecture/microservices/implement-resilient-applications/partial-failure-strategies)
> (원본: [dotnet/docs · partial-failure-strategies.md](https://github.com/dotnet/docs/blob/main/docs/architecture/microservices/implement-resilient-applications/partial-failure-strategies.md),
> main 브랜치 2026-09-27 확인), [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
>
> 영어 문장은 원문 그대로 인용했고, 한글 설명과 응용 문장은 이 노트에서 새로 쓴 것이다.

{{< sentence
  en="It's highly advisable not to create long chains of synchronous HTTP calls across the internal microservices because that incorrect design will eventually become the main cause of bad outages."
  ko="내부 마이크로서비스들 사이에 동기 HTTP 호출의 긴 사슬을 만들지 않기를 강력히 권한다. 그 잘못된 설계가 결국 심각한 장애의 주된 원인이 될 것이기 때문이다."
  source=".NET Architecture Guides · Strategies to handle partial failure"
  sourceURL="https://learn.microsoft.com/en-us/dotnet/architecture/microservices/implement-resilient-applications/partial-failure-strategies"
  note="`It's highly advisable not to X because that <이름 붙인 설계> will eventually become the main cause of Y.` — 금지를 명령이 아니라 **권고의 최상급**으로 말하는 문형이다. `highly advisable not to`는 `must not`보다 한 칸 약하지만 `should not`보다 세서, 규칙을 강제할 권한이 없는 문서(가이드, 설계 리뷰 의견)에서 쓰기 좋다. 두 번째 장치는 `that incorrect design`이다. 앞에서 말한 행동을 되받아 부르면서 **거기에 이름을 붙여 판정**해 버린다 — 행동을 한 번 더 설명하지 않고도 이미 나쁜 것으로 규정된다. `will eventually become the main cause of`는 '지금 안 터졌다'는 반박을 미리 막는다: 지금이 아니라 나중에, 부수 원인이 아니라 주된 원인이 된다고 시간을 근거로 삼는다."
  app1="It's highly advisable not to keep patching production by hand because that undocumented practice will eventually become the main cause of failed audits."
  app1ko="운영 환경을 수동으로 계속 손보지 않기를 강력히 권한다. 그 기록 없는 관행이 결국 감사 부적합의 주된 원인이 될 것이기 때문이다."
  app2="It's highly advisable not to merge while a test is skipped as flaky because that habit will eventually become the main cause of red builds nobody reads."
  app2ko="테스트를 불안정하다는 이유로 건너뛴 채 머지하지 않기를 강력히 권한다. 그 습관이 결국 아무도 읽지 않는 빨간 빌드의 주된 원인이 될 것이기 때문이다."
>}}

{{< sentence
  en="On the contrary, except for the front-end communications between the client applications and the first level of microservices or fine-grained API Gateways, it's recommended to use only asynchronous (message-based) communication once past the initial request/response cycle, across the internal microservices."
  ko="반대로, 클라이언트 애플리케이션과 첫 번째 계층의 마이크로서비스 또는 세분화된 API 게이트웨이 사이의 프런트엔드 통신을 제외하면, 최초의 요청/응답 주기를 지난 다음부터는 내부 마이크로서비스들 사이에서 비동기(메시지 기반) 통신만 쓰기를 권한다."
  source=".NET Architecture Guides · Strategies to handle partial failure"
  sourceURL="https://learn.microsoft.com/en-us/dotnet/architecture/microservices/implement-resilient-applications/partial-failure-strategies"
  note="`Except for A, it's recommended to use only B.` — **예외를 먼저 떼어 놓고 나머지 전부에 규칙을 거는** 순서다. `only`가 규칙을 닫아 버리기 때문에, 그 앞에 `except for`로 문 하나를 미리 열어 두지 않으면 반드시 '그럼 로그인 화면은?' 같은 예외 질문이 돌아온다. 예외를 뒤에 덧붙이면 변명처럼 들리고, 앞에 두면 **범위를 정확히 아는 사람이 쓴 규칙**으로 읽힌다. `once past the initial request/response cycle`은 예외의 경계를 사람이나 컴포넌트 이름이 아니라 **시점**으로 잡은 것이라 조직이 바뀌어도 살아남는다. 다만 원문의 `On the contrary`는 앞 문장을 부정할 때 쓰는 말이어서, 앞의 금지에 대안을 잇는 이 자리에는 `Conversely`나 `By contrast`가 더 자연스럽다 — 문형만 가져오고 이 연결어는 바꿔 쓰는 것을 권한다."
  app1="Except for the first acknowledgment from the on-call engineer, it's recommended to use only the incident channel for status updates, once the incident has been declared."
  app1ko="온콜 담당자의 최초 확인을 제외하면, 장애가 선언된 다음부터는 상태 공유를 장애 채널에서만 하기를 권한다."
  app2="Except for break-glass accounts, it's recommended to use only short-lived tokens for production access, across all internal services."
  app2ko="비상용 계정을 제외하면, 모든 내부 서비스에서 운영 환경 접근에는 수명이 짧은 토큰만 쓰기를 권한다."
>}}

{{< sentence
  en="In general, clients should be designed not to block indefinitely and to always use timeouts when waiting for a response. Using timeouts ensures that resources are never tied up indefinitely."
  ko="일반적으로 클라이언트는 무한정 블로킹하지 않도록, 그리고 응답을 기다릴 때는 항상 타임아웃을 쓰도록 설계되어야 한다. 타임아웃을 쓰면 자원이 무한정 붙잡혀 있는 일이 결코 없다는 것이 보장된다."
  source=".NET Architecture Guides · Strategies to handle partial failure"
  sourceURL="https://learn.microsoft.com/en-us/dotnet/architecture/microservices/implement-resilient-applications/partial-failure-strategies"
  note="`X should be designed not to A and to always B. Using B ensures that C is never D.` — **금지와 의무를 한 문장에 병렬로 묶고, 다음 문장에서 그 수단이 보장하는 것을 못 박는** 2단 구조다. `not to A and to always B`처럼 `to`를 두 번 걸어 놓으면 '하지 마라'와 '해라'가 같은 요구의 앞뒤 면으로 읽혀서, 규칙 두 개를 따로 외우지 않아도 된다. 앞의 `In general`은 예외 여지를 남겨 규칙이 교조적으로 들리지 않게 하는 완충재다. 힘은 두 번째 문장에 있다: `ensures that ~ never ~`는 수단이 막아 주는 **최악의 경우**를 직접 지목하기 때문에, 근거를 길게 설명하지 않고 한 줄로 끝낼 수 있다. 설계 리뷰 기준이나 요구사항 문서의 항목을 쓸 때 그대로 쓴다."
  app1="In general, runbooks should be designed not to name individuals and to always name a role when an approval is required. Naming roles ensures that a step is never blocked on one person being awake."
  app1ko="일반적으로 런북은 개인 이름을 쓰지 않도록, 그리고 승인이 필요한 곳에는 항상 역할을 적도록 설계되어야 한다. 역할로 적으면 어떤 단계도 특정인이 깨어 있는지에 발목 잡히는 일이 결코 없다는 것이 보장된다."
  app2="In general, batch jobs should be designed not to retry forever and to always write a failure record before exiting. Writing that record ensures that a silent failure is never mistaken for a quiet night."
  app2ko="일반적으로 배치 작업은 무한히 재시도하지 않도록, 그리고 종료 전에 항상 실패 기록을 남기도록 설계되어야 한다. 그 기록을 남기면 조용히 죽은 실패가 조용한 밤으로 오해되는 일이 결코 없다는 것이 보장된다."
>}}

{{< sentence
  en="If the error rate exceeds a configured limit, a &quot;circuit breaker&quot; trips so that further attempts fail immediately. (If a large number of requests are failing, that suggests the service is unavailable and that sending requests is pointless.)"
  ko="오류율이 설정된 한계를 넘으면 '서킷 브레이커'가 작동해서 이후의 시도는 즉시 실패한다. (많은 수의 요청이 실패하고 있다면, 그것은 그 서비스를 쓸 수 없는 상태이고 요청을 보내는 것이 무의미하다는 점을 시사한다.)"
  source=".NET Architecture Guides · Strategies to handle partial failure"
  sourceURL="https://learn.microsoft.com/en-us/dotnet/architecture/microservices/implement-resilient-applications/partial-failure-strategies"
  note="`If A exceeds a configured limit, B so that C. (If D, that suggests E and that F.)` — 규칙을 먼저 쓰고 **괄호로 그 규칙의 추론 근거를 뒤에 붙이는** 문형이다. 괄호는 본문의 흐름을 끊지 않으면서 '왜 그렇게 정했는지'를 끼워 넣는 자리여서, 규칙을 읽고 넘어갈 사람과 근거까지 따질 사람을 한 문단에서 같이 만족시킨다. 안쪽 골격 `that suggests E and that F`는 **관찰 하나에서 추론 두 개를 병렬로 뽑아내는** 구조이고, `suggests`가 단정 대신 추정으로 톤을 낮춘다 — 실패율만 보고 원인을 확정할 수는 없다는 사실을 문법으로 인정하는 셈이다. `exceeds a configured limit`은 숫자를 본문에 박지 않고 설정값으로 미루기 때문에, 임계값이 바뀌어도 문서를 고칠 일이 없다."
  app1="If the queue depth exceeds a configured limit, the consumer stops polling so that producers see backpressure immediately. (If the queue keeps growing, that suggests the consumer is the bottleneck and that adding producers will only make it worse.)"
  app1ko="큐 적재량이 설정된 한계를 넘으면 컨슈머가 폴링을 멈춰서 프로듀서가 즉시 백프레셔를 감지한다. (큐가 계속 늘어난다면, 그것은 컨슈머가 병목이고 프로듀서를 늘리는 것은 상황을 더 나쁘게만 만든다는 점을 시사한다.)"
  app2="If failed logins for one account exceed a configured limit, the account is locked so that further attempts fail immediately. (If a single account sees thousands of attempts, that suggests the credentials are being guessed and that telling the owner matters more than the lockout itself.)"
  app2ko="한 계정의 로그인 실패가 설정된 한계를 넘으면 그 계정이 잠겨서 이후의 시도는 즉시 실패한다. (한 계정에 수천 번의 시도가 들어왔다면, 그것은 자격 증명이 추측되고 있다는 점, 그리고 계정 잠금 자체보다 소유자에게 알리는 일이 더 중요하다는 점을 시사한다.)"
>}}

{{< sentence
  en="In this approach, the client process performs fallback logic when a request fails, such as returning cached data or a default value. This is an approach suitable for queries, and is more complex for updates or commands."
  ko="이 방식에서는 요청이 실패했을 때 클라이언트 프로세스가 폴백 로직을 수행한다. 캐시된 데이터나 기본값을 반환하는 것 같은 식이다. 이것은 조회에 적합한 방식이고, 갱신이나 명령에 대해서는 더 복잡해진다."
  source=".NET Architecture Guides · Strategies to handle partial failure"
  sourceURL="https://learn.microsoft.com/en-us/dotnet/architecture/microservices/implement-resilient-applications/partial-failure-strategies"
  note="`This is an approach suitable for A, and is more complex for B.` — 자기가 방금 권한 대책의 **적용 범위를 스스로 좁히는** 문형이다. 핵심은 `is more complex for`다. `does not work for`(안 된다)나 `should not be used for`(쓰지 마라)가 아니라 **비용이 더 든다**고 말하기 때문에, 금지하지 않으면서 경고할 수 있고 상대가 굳이 그 길로 갈 때도 말을 바꾸지 않아도 된다. `suitable for A, and ... for B`로 한 문장에서 두 영역을 갈라 놓으면, 읽는 사람이 자기 상황이 어느 쪽인지 바로 판정한다 — 제안서에서 '그래서 우리 경우엔?'이라는 질문을 한 줄로 미리 받아 내는 자리다. `an approach`라고 관사를 붙여 부르는 것도 장치인데, 유일한 정답이 아니라 **선택지 하나**라고 스스로 격을 낮춰 둔다."
  app1="Serving stale cached data during an outage is an approach suitable for dashboards, and is more complex for anything a customer is billed on."
  app1ko="장애 중에 오래된 캐시 데이터를 내보내는 것은 대시보드에 적합한 방식이고, 고객에게 과금되는 대상에 대해서는 더 복잡해진다."
  app2="Rolling back to the previous release is an approach suitable for code-only changes, and is more complex for changes that have already migrated the schema."
  app2ko="이전 릴리스로 되돌리는 것은 코드만 바뀐 변경에 적합한 방식이고, 스키마 마이그레이션이 이미 적용된 변경에 대해서는 더 복잡해진다."
>}}
