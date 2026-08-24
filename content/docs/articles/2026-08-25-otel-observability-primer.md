---
title: 개념을 정의하고 판정 기준을 세우는 표현
description: 능력으로 개념을 정의하고, 형용사에 합격 조건을 붙이고, 익숙한 도구의 한계를 지적하는 문장 5개.
weight: -5
date: 2026-08-25
source: "OpenTelemetry Docs — Observability primer"
sourceURL: https://opentelemetry.io/docs/concepts/observability-primer/
---

# 개념을 정의하고 판정 기준을 세우는 표현

관측 가능성, 신뢰성, SLI, 분산 추적 같은 낱말을 처음 만나는 사람에게 설명하는 OpenTelemetry 공식
입문 문서. 새 개념을 소개하는 글에 필요한 문형 — **능력으로 정의하기**, `properly` 같은 모호한
형용사에 판정 조건 붙이기, 규범을 명령 대신 정의로 세우기, 이미 쓰고 있는 도구의 한계를 적으로
돌리지 않고 지적하기, 문제와 해법을 두 문장으로 붙이기 — 이 고루 들어 있어 발췌했다.

> **원문** — OpenTelemetry Authors, *Observability primer*,
> [OpenTelemetry Documentation](https://opentelemetry.io/docs/concepts/observability-primer/)
> ([원본 마크다운](https://github.com/open-telemetry/opentelemetry.io/blob/main/content/en/docs/concepts/observability-primer.md)),
> [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) 라이선스.
>
> 영어 문장은 원문 그대로 인용했고, 한글 설명과 응용 문장은 이 노트에서 새로 쓴 것이다.

{{< sentence
  en="Observability lets you understand a system from the outside by letting you ask questions about that system without knowing its inner workings."
  ko="관측 가능성은, 시스템의 내부 동작을 알지 못해도 그 시스템에 대해 질문할 수 있게 해 줌으로써 바깥에서 시스템을 이해하게 해 준다."
  source="OpenTelemetry Docs · Observability primer"
  sourceURL="https://opentelemetry.io/docs/concepts/observability-primer/"
  note="`X lets you A by letting you B without C.` — 추상적인 개념을 **그것으로 무엇을 할 수 있는지**로 정의하는 문형이다. `Observability is the property that ...` 같은 속성 정의로 열면 정의를 읽고도 뭘 얻는지 모르는 채 끝나지만, `lets you`는 첫 낱말부터 독자를 주인공 자리에 놓는다. 구조를 뜯어보면 `lets you`가 두 번 반복되며 층을 쌓는다 — 앞의 것은 **결과**(이해한다), `by letting you` 뒤의 것은 그 결과에 이르는 **수단**(질문한다). 그리고 정의의 값어치는 대개 마지막 `without C` 절에 있다. 이 문장이 파는 것은 '이해'가 아니라 '내부를 몰라도 된다'는 면제이기 때문이다. 새 도구나 새 개념을 소개하는 문서의 첫 문장, 그리고 도입 제안의 한 줄 요약에 그대로 쓴다."
  app1="A good runbook lets you recover a service under pressure by letting you follow a fixed sequence without rereading the design document."
  app1ko="좋은 런북은, 설계 문서를 다시 읽지 않고도 정해진 순서를 따라갈 수 있게 해 줌으로써 압박 속에서 서비스를 복구하게 해 준다."
  app2="Structured audit logging lets you answer an auditor on your own by letting you reconstruct who changed what without interviewing the team that owns the system."
  app2ko="구조화된 감사 로깅은, 시스템을 소유한 팀을 인터뷰하지 않고도 누가 무엇을 바꿨는지 재구성할 수 있게 해 줌으로써 감사자에게 스스로 답하게 해 준다."
>}}

{{< sentence
  en="An application is properly instrumented when developers don't need to add more instrumentation to troubleshoot an issue, because they have all of the information they need."
  ko="애플리케이션은, 개발자가 문제를 파악하려고 계측을 더 추가할 필요가 없을 때 제대로 계측된 것이다. 필요한 정보를 이미 다 가지고 있기 때문이다."
  source="OpenTelemetry Docs · Observability primer"
  sourceURL="https://opentelemetry.io/docs/concepts/observability-primer/"
  note="`X is properly Y when <더 할 일이 없을 때>, because <그 이유>.` — `properly`, `enough`, `sufficient`처럼 **사람마다 기준이 다른 낱말에 판정 조건을 붙이는** 문형이다. 이런 형용사는 그냥 두면 회의가 끝나지 않는다. 여기서 `when` 절이 주는 기준이 특이한 점은 **부정형 테스트**라는 것이다 — 무엇을 갖췄는지 세지 않고 '더 보탤 것이 남았는지'를 묻는다. 갖춘 것을 세는 기준은 항목을 늘리면 계속 통과하지만, 부정형 기준은 실제 상황(장애를 파악하는 중)에서 한 번이라도 부족하면 바로 불합격이라 속일 수 없다. 뒤의 `because` 절은 그 통과가 운이 아니었음을 설명해 기준을 완성한다. 완료 기준(DoD), 문서화 기준, 온보딩 자료의 합격선을 정할 때 그대로 옮겨 쓴다."
  app1="A postmortem is properly written when the next responder doesn't need to ask anyone what happened, because the timeline has all of the context they need."
  app1ko="포스트모템은, 다음 대응자가 무슨 일이 있었는지 누구에게도 묻지 않아도 될 때 제대로 쓰인 것이다. 타임라인이 그가 필요로 하는 맥락을 다 담고 있기 때문이다."
  app2="An alert is properly tuned when the on-call engineer doesn't need to open a dashboard to decide whether to act, because the notification has all of the information they need."
  app2ko="알림은, 온콜 담당자가 대응할지 말지 정하려고 대시보드를 열 필요가 없을 때 제대로 조정된 것이다. 알림 자체가 그가 필요로 하는 정보를 다 담고 있기 때문이다."
>}}

{{< sentence
  en="A good SLI measures your service from the perspective of your users."
  ko="좋은 SLI는 사용자의 관점에서 당신의 서비스를 측정한다."
  source="OpenTelemetry Docs · Observability primer"
  sourceURL="https://opentelemetry.io/docs/concepts/observability-primer/"
  note="`A good X <동사> from the perspective of Y.` — 규범을 **명령이 아니라 정의로** 세우는 문형이다. `An SLI should measure ...`라고 쓰면 지시가 되어 '우리 사정은 다르다'는 반박을 부르지만, `A good X ...`는 좋은 것이 무엇인지 서술할 뿐이라 반박할 표면이 없다. 대신 어기는 쪽이 스스로 '나쁜 X'를 만든 셈이 되므로 실제 구속력은 더 세다. `from the perspective of Y`는 **무엇을 재느냐가 아니라 어디에서 재느냐**를 지정한다는 점이 핵심이다 — 같은 지표라도 관측 지점을 옮기면 다른 숫자가 나오고, 논쟁은 거의 항상 그 지점에서 갈린다. 문장이 짧을수록 회의에서 그대로 인용되니 수식어를 더 붙이지 않는다. 기준·원칙 문서의 항목 제목으로 쓰기 좋다."
  app1="A good alert threshold measures your system from the perspective of the on-call engineer who has to act on it."
  app1ko="좋은 알림 임계값은 그 알림에 실제로 대응해야 하는 온콜 담당자의 관점에서 시스템을 측정한다."
  app2="A good review comment describes the change from the perspective of the person who will read this code six months from now."
  app2ko="좋은 리뷰 코멘트는 여섯 달 뒤에 이 코드를 읽을 사람의 관점에서 변경을 설명한다."
>}}

{{< sentence
  en="Logs aren't enough for tracking code execution, as they usually lack contextual information, such as where they were called from."
  ko="로그는 코드 실행을 추적하기에는 충분하지 않다. 어디에서 호출되었는지 같은 맥락 정보가 대개 빠져 있기 때문이다."
  source="OpenTelemetry Docs · Observability primer"
  sourceURL="https://opentelemetry.io/docs/concepts/observability-primer/"
  note="`X aren't enough for Y, as they usually lack Z, such as W.` — 이미 모두가 쓰고 있는 도구의 **한계를 지적하되 그 도구를 부정하지는 않는** 문형이다. 새 계층을 도입하자는 제안의 표준 도입부이기도 하다. `are useless`나 `are the wrong tool`이라고 쓰는 순간 지금 그것으로 버티고 있는 사람들이 방어 태세로 돌아서지만, `aren't enough`는 그들이 해 온 일을 인정한 채 '여기서 더 필요하다'로만 이어진다. `for Y`가 **어느 용도에서** 부족한지를 좁히는 것도 같은 효과다 — 로그 전체가 아니라 실행 추적이라는 한 용도만 문제 삼는다. `as`는 `because`보다 톤이 낮아 이유를 힘주지 않고 덧붙이고, `usually`는 예외를 인정해 반례 하나로 무너지지 않게 하며, `such as W`의 구체적인 예 하나가 막연한 불평을 검증 가능한 지적으로 바꾼다."
  app1="Unit tests aren't enough for catching this class of regression, as they usually lack production-like inputs, such as the malformed records we see on retries."
  app1ko="유닛 테스트는 이런 종류의 회귀를 잡기에는 충분하지 않다. 재시도 때 들어오는 깨진 레코드처럼 운영과 비슷한 입력이 대개 빠져 있기 때문이다."
  app2="Access logs aren't enough for an audit trail, as they usually lack the reason for the action, such as which ticket authorized the change."
  app2ko="접근 로그는 감사 증적으로 쓰기에는 충분하지 않다. 어느 티켓이 그 변경을 승인했는지처럼 행위의 근거가 대개 빠져 있기 때문이다."
>}}

{{< sentence
  en="Without tracing, finding the root cause of performance problems in a distributed system can be challenging. Tracing makes debugging and understanding distributed systems less daunting by breaking down what happens within a request as it flows through a distributed system."
  ko="추적이 없으면 분산 시스템에서 성능 문제의 근본 원인을 찾는 일이 어려울 수 있다. 추적은 요청이 분산 시스템을 흘러가는 동안 그 안에서 무슨 일이 일어나는지를 쪼개어 보여 줌으로써, 분산 시스템을 디버깅하고 이해하는 일을 덜 버겁게 만든다."
  source="OpenTelemetry Docs · Observability primer"
  sourceURL="https://opentelemetry.io/docs/concepts/observability-primer/"
  note="`Without X, doing Y can be challenging. X makes Y less daunting by V-ing.` — 문제와 해법을 **두 문장 한 쌍**으로 붙이는 문형이다. 앞 문장이 X 없는 세상을 그리고, 뒤 문장이 같은 낱말 Y를 그대로 받아 X를 답으로 놓는다. 낱말을 바꾸지 않고 되풀이하는 것이 이 쌍의 접착제다. 첫 문장의 `can be`가 톤을 정한다 — `is impossible`이라고 쓰면 지금 X 없이 해내고 있는 사람들의 경험과 정면으로 부딪혀 신뢰를 잃지만, `can be challenging`은 '늘 그렇다'가 아니라 '그럴 수 있다'라서 아무도 부정할 수 없다. 뒤 문장은 효용을 **감정의 낮춤**(`less daunting`)으로 말해 과장을 피하고 — 없앤다가 아니라 덜하게 한다 — 결정적으로 `by V-ing`로 **작동 방식**을 붙인다. 이 절이 빠지면 남는 건 광고 문구다. 도구 도입 제안서나 RFC의 첫 문단에 그대로 쓴다."
  app1="Without a written rollback plan, deciding when to abort a release can be contentious. The plan makes the decision less contentious by naming in advance which metric ends the deployment."
  app1ko="문서화된 롤백 계획이 없으면 릴리스를 언제 중단할지 정하는 일이 논쟁거리가 될 수 있다. 계획은 어느 지표가 배포를 끝내는지 미리 못 박아 둠으로써, 그 결정을 덜 다투게 만든다."
  app2="Without structured logs, reconstructing an incident timeline can be tedious. Structured logs make the reconstruction less tedious by giving every event the same fields to sort and filter on."
  app2ko="구조화된 로그가 없으면 장애 타임라인을 재구성하는 일이 지루해질 수 있다. 구조화된 로그는 모든 이벤트에 정렬하고 걸러 낼 같은 필드를 부여함으로써, 그 재구성을 덜 지루하게 만든다."
>}}
