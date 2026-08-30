---
title: 테스트를 염두에 둔 설계 문서의 표현
description: 완료의 뜻을 다시 정하고, 금지 대신 교체를 제안하고, 좋은 방안이 몰래 늘리는 의존성을 꺼내 보이는 문장 5개.
weight: -11
date: 2026-08-31
source: "Engineering Fundamentals Playbook — Testing"
sourceURL: https://microsoft.github.io/code-with-engineering-playbook/automated-testing/
---

# 테스트를 염두에 둔 설계 문서의 표현

Microsoft ISE의 엔지니어링 플레이북 중 테스트 장이다. 절반은 테스트 기법 목록이지만, 앞쪽
'Build for Testing' 절은 **테스트하기 좋은 시스템을 어떻게 설계할 것인가**를 파라미터화와
로깅으로 풀어 놓는다. 이 노트는 그 내용보다 **팀 표준 문서가 사람을 설득하는 방식**을 훔치려고
골랐다. 이 문서는 명령하지 않는다. 대신 '완료'라는 단어의 뜻을 다시 정하고, 금지 대신 교체를
제안하고, 상대 방안의 장점을 먼저 인정한 뒤 숨은 의존성에 이름을 붙이고, 규칙의 수혜자를 사람으로
지목한다. 설계 리뷰와 팀 컨벤션 문서에 그대로 옮겨 쓸 문형만 다섯 개 뽑았다.

> **원문** — Microsoft ISE, *Engineering Fundamentals Playbook — Testing*,
> [microsoft.github.io](https://microsoft.github.io/code-with-engineering-playbook/automated-testing/)
> ([github.com/microsoft/code-with-engineering-playbook](https://github.com/microsoft/code-with-engineering-playbook/blob/main/docs/automated-testing/README.md)),
> [CC BY 4.0](https://github.com/microsoft/code-with-engineering-playbook/blob/main/LICENSE).
>
> 영어 문장은 원문 그대로 인용했고, 한글 설명과 응용 문장은 이 노트에서 새로 쓴 것이다.

{{< sentence
  en="We consider code to be incomplete if it is not accompanied by tests"
  ko="우리는 테스트가 딸려 있지 않은 코드를 완료되지 않은 것으로 본다."
  source="Engineering Fundamentals Playbook · Testing"
  sourceURL="https://microsoft.github.io/code-with-engineering-playbook/automated-testing/"
  note="`We consider X to be Y if it is not accompanied by Z.` — 팀의 기준을 규칙이 아니라 **정의**로 선언하는 문형이다. '테스트를 써라'는 요구는 지킬지 말지를 고르게 하지만, 이 문장은 고를 것을 남기지 않는다 — *완료*라는 말의 뜻 자체를 바꿔 버리기 때문이다. 판단 주체를 `We`로 둔 것도 계산된 선택이다. 규정이 위에서 내려온 게 아니라 우리가 합의한 것으로 읽힌다. `if it is not accompanied by`가 결정적인데, 능동으로 요구하지 않고 **결여된 상태를 서술**하기 때문에 지적의 대상이 사람이 아니라 산출물이 된다. 완료 정의(DoD), 리뷰 기준, 온보딩 문서의 첫 줄에 그대로 쓴다."
  app1="We consider an incident to be open if it is not accompanied by a written timeline."
  app1ko="우리는 기록된 타임라인이 딸려 있지 않은 장애를 아직 닫히지 않은 것으로 본다."
  app2="We consider a permission change to be unreviewed if it is not accompanied by the ticket that requested it."
  app2ko="우리는 그것을 요청한 티켓이 딸려 있지 않은 권한 변경을 리뷰되지 않은 것으로 본다."
>}}

{{< sentence
  en="Rather than hard-code any variables, consider making everything a configurable parameter with a reasonable default."
  ko="어떤 변수든 하드코딩하기보다, 모든 것을 합리적인 기본값을 가진 설정 가능한 파라미터로 만드는 쪽을 고려해 보라."
  source="Engineering Fundamentals Playbook · Testing"
  sourceURL="https://microsoft.github.io/code-with-engineering-playbook/automated-testing/"
  note="`Rather than X, consider Y with Z.` — 금지가 아니라 **교체**를 제안하는 문형이다. `Rather than`은 상대가 하던 것을 먼저 이름 붙여 놓고 그 옆에 다른 선택지를 놓기만 한다(하지 마라가 아니라 이것 대신 저것). `consider`는 명령을 권고로 한 칸 낮춘다 — `Make everything a parameter.`였다면 읽는 사람은 곧장 예외를 찾기 시작한다. 진짜 배울 곳은 꼬리인 `with a reasonable default`다. 제안이 거절되는 이유는 대개 아이디어가 나빠서가 아니라 **제안에 딸려 오는 비용** 때문인데(설정할 게 늘어난다), 이 자리에서 그 비용을 미리 지워 준다. 제안 문장을 쓸 때마다 이 꼬리 자리를 비워 두지 않는 습관이 핵심이다."
  app1="Rather than page the on-call for every failed job, consider routing retryable failures to a queue with a daily digest."
  app1ko="실패한 작업마다 온콜을 호출하기보다, 재시도 가능한 실패는 하루 한 번 모아 보내는 큐로 보내는 쪽을 고려해 보라."
  app2="Rather than block the release on a manual sign-off, consider gating it on a check that anyone on the team can re-run."
  app2ko="수동 승인으로 릴리스를 막기보다, 팀의 누구든 다시 돌릴 수 있는 검사에 릴리스를 걸어 두는 쪽을 고려해 보라."
>}}

{{< sentence
  en="Logging to external systems like Azure Monitor is desirable for traceability across services. This requires logs to be dispatched from the local system to the external system and that is a dependency that can fail."
  ko="Azure Monitor 같은 외부 시스템으로 로그를 보내는 것은 서비스 전반의 추적성 면에서 바람직하다. 다만 그러려면 로그가 로컬 시스템에서 외부 시스템으로 보내져야 하고, 그것은 실패할 수 있는 의존성이다."
  source="Engineering Fundamentals Playbook · Testing"
  sourceURL="https://microsoft.github.io/code-with-engineering-playbook/automated-testing/"
  note="`X is desirable for Y. This requires Z and that is a dependency that can fail.` — 좋은 방안을 **인정한 다음** 그 방안이 몰래 늘리는 의존성을 꺼내 보이는 2단 구성이다. 첫 문장의 `is desirable for`는 칭찬이 아니라 발판이다. 장점을 내가 먼저 말해 두면 뒤 문장이 트집이 아니라 보완으로 읽힌다(반대로 위험부터 말하면 상대는 방어부터 한다). 뒤 문장의 힘은 마지막 절 `and that is a dependency that can fail`에 있다 — 앞 절을 되받아 **이름을 붙여 주기** 때문이다. '그거 위험해요'는 논쟁을 부르지만 '그건 실패할 수 있는 의존성입니다'는 목록에 항목을 하나 붙인다. 설계 리뷰에서 반대하지 않으면서 리스크를 남길 때 쓴다."
  app1="Storing the runbook in the wiki is desirable for discoverability. This requires the wiki to be reachable during an outage and that is a dependency that can fail."
  app1ko="런북을 위키에 두는 것은 찾기 쉬움 면에서 바람직하다. 다만 그러려면 장애가 난 중에도 위키에 접근할 수 있어야 하고, 그것은 실패할 수 있는 의존성이다."
  app2="Fetching secrets at startup is desirable for rotation. This requires the vault to answer before the pod passes its readiness probe and that is a dependency that can fail."
  app2ko="기동 시점에 시크릿을 받아 오는 것은 키 교체 면에서 바람직하다. 다만 그러려면 파드가 readiness 프로브를 통과하기 전에 볼트가 응답해야 하고, 그것은 실패할 수 있는 의존성이다."
>}}

{{< sentence
  en="When logging, it is important to include metadata that is relevant to the activity. For example, a Tenant ID, Customer ID, or Order ID. This allows someone reviewing the logs to understand the context of the activity and filter to a manageable set of logs."
  ko="로그를 남길 때는 그 활동과 관련된 메타데이터를 함께 넣는 것이 중요하다. 예를 들면 테넌트 ID, 고객 ID, 주문 ID 같은 것이다. 그렇게 해 두면 나중에 로그를 들여다보는 사람이 그 활동의 맥락을 이해하고, 감당할 만한 양으로 로그를 걸러 낼 수 있다."
  source="Engineering Fundamentals Playbook · Testing"
  sourceURL="https://microsoft.github.io/code-with-engineering-playbook/automated-testing/"
  note="`This allows someone doing X to A and B.` — 규칙의 **수혜자를 사람으로 지목**하는 문형이다. 같은 자리에 흔히 들어가는 말은 `for better observability` 같은 추상 명사인데, 그러면 왜 지켜야 하는지가 사라지고 규칙만 남는다. `someone reviewing the logs`처럼 **행위 중인 사람**을 세우면 읽는 사람이 그 장면을 떠올리게 되고, 규칙이 목적을 되찾는다(그리고 그 사람은 대개 몇 달 뒤의 나다). 목적어 두 개의 순서도 의도적이다 — `understand`(맥락을 안다) 다음에 `filter`(추려 낸다), 즉 인지적 이득과 실무적 이득을 나란히 놓는다. `to a manageable set`은 결과의 크기까지 약속해서 문장이 구호로 끝나지 않게 한다. 컨벤션을 적어 놓고 그 아래 이유를 한 줄 붙일 때, 이 문형이 '베스트 프랙티스이기 때문'보다 언제나 낫다."
  app1="This allows someone joining the incident an hour late to reconstruct what has already been tried and skip the checks that came back clean."
  app1ko="그렇게 해 두면 한 시간 늦게 장애에 합류한 사람이 이미 시도된 것을 되짚고, 이상 없이 끝난 확인은 건너뛸 수 있다."
  app2="This allows someone auditing the change a year later to see who approved it and narrow the diff to the files that touch customer data."
  app2ko="그렇게 해 두면 1년 뒤 그 변경을 감사하는 사람이 누가 승인했는지 확인하고, 고객 데이터를 건드리는 파일로 diff를 좁힐 수 있다."
>}}

{{< sentence
  en="Even if you are using App Insights to capture how long dependency calls are taking, it is often useful to know how long certain functions of your application took."
  ko="의존 호출이 얼마나 걸리는지를 App Insights로 잡고 있더라도, 애플리케이션의 특정 함수가 얼마나 걸렸는지를 아는 것은 종종 유용하다."
  source="Engineering Fundamentals Playbook · Testing"
  sourceURL="https://microsoft.github.io/code-with-engineering-playbook/automated-testing/"
  note="`Even if you are already using X, it is often useful to know Y.` — **'그건 이미 있는데요'를 미리 막는** 양보 문형이다. 새 계측, 새 문서, 새 절차를 제안할 때 가장 먼저 돌아오는 말이 그것인데, `Even if` 절이 그 반론을 내 문장 안으로 먼저 끌어와 버리면 상대는 반박할 자리를 잃고 **차이**를 듣게 된다. 톤을 정하는 단어는 `often`이다. `always`면 지금 방식이 틀렸다는 뜻이 되어 싸움이 되고, `sometimes`면 제안이 스스로 약해진다. `often`은 '늘은 아니지만 무시할 빈도는 아니다'라는 자리를 정확히 짚는다. 서술어가 `it is necessary`가 아니라 `it is useful`인 것도 마찬가지다 — 필요가 아니라 유용이라, 상대가 거절해도 체면이 상하지 않는다."
  app1="Even if you are already collecting pod restart counts, it is often useful to know which container in the pod exited first."
  app1ko="파드 재시작 횟수를 이미 모으고 있더라도, 그 파드 안에서 어떤 컨테이너가 먼저 죽었는지를 아는 것은 종종 유용하다."
  app2="Even if you are running a nightly vulnerability scan, it is often useful to know which of those findings are reachable from a public endpoint."
  app2ko="야간 취약점 스캔을 돌리고 있더라도, 그 발견들 가운데 무엇이 공개 엔드포인트에서 도달 가능한지를 아는 것은 종종 유용하다."
>}}
