---
title: 위협 모델링 문서의 표현
description: 개념을 다시 정의하고, 흔한 오해를 미리 끊고, 방법론의 차이를 인정한 채 공통점만 남기는 문장 5개.
weight: -4
date: 2026-08-24
source: "OWASP Cheat Sheet Series — Threat Modeling"
sourceURL: https://cheatsheetseries.owasp.org/cheatsheets/Threat_Modeling_Cheat_Sheet.html
---

# 위협 모델링 문서의 표현

위협 모델링이 무엇이고 어떤 순서로 하는지, 그리고 개발팀이 왜 이걸 부담스러워하는지까지 정리한
OWASP 공식 치트시트. 방법론을 소개하는 글에 필요한 문형 — 개념을 좁혀 다시 정의하기,
**흔한 오해를 먼저 끊어 두기**, 유파의 차이를 인정하면서도 공통점만 골라내기, 제안의 비용을
스스로 인정하기 — 이 고루 들어 있어 발췌했다.

> **원문** — OWASP Cheat Sheet Series contributors, *Threat Modeling Cheat Sheet*,
> [OWASP Cheat Sheet Series](https://cheatsheetseries.owasp.org/cheatsheets/Threat_Modeling_Cheat_Sheet.html)
> ([원본 마크다운](https://github.com/OWASP/CheatSheetSeries/blob/master/cheatsheets/Threat_Modeling_Cheat_Sheet.md)),
> [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) 라이선스.
>
> 영어 문장은 원문 그대로 인용했고, 한글 설명과 응용 문장은 이 노트에서 새로 쓴 것이다.

{{< sentence
  en="In the context of application security, threat modeling is a structured, repeatable process used to gain actionable insights into the security characteristics of a particular system."
  ko="애플리케이션 보안이라는 맥락에서 위협 모델링은, 특정 시스템의 보안 특성에 대해 실행 가능한 통찰을 얻기 위해 쓰는 구조화되고 반복 가능한 절차다."
  source="OWASP Cheat Sheet Series · Threat Modeling"
  sourceURL="https://cheatsheetseries.owasp.org/cheatsheets/Threat_Modeling_Cheat_Sheet.html"
  note="`In the context of X, Y is a <성격> process used to <목적>.` — 여러 분야에서 다르게 쓰이는 낱말을 **내 분야 안으로 좁혀 다시 정의하는** 문형이다. 정의문을 그냥 `Y is ...`로 열면 '그건 우리 쪽에선 다른 뜻인데요'가 바로 따라붙지만, `In the context of X`를 앞에 달면 처음부터 사정거리를 선언하고 들어가므로 그 반박이 무력해진다. 정의의 무게는 형용사 두 개가 진다 — `structured`(즉흥이 아니다), `repeatable`(1회성이 아니다). `used to ...`는 '무엇인가'가 아니라 **'무엇을 위한 것인가'**로 정의를 마무리하는 장치이고, `actionable`은 '읽고 끝나는 통찰이 아니라 다음 행동이 나오는 통찰'을 한 단어로 못 박는다. 설계 문서 첫 문단이나 용어집 항목에 그대로 옮겨 쓸 수 있다."
  app1="In the context of incident response, a postmortem is a blameless, time-boxed process used to gain actionable insights into the failure modes of a particular service."
  app1ko="장애 대응이라는 맥락에서 포스트모템은, 특정 서비스의 실패 양상에 대해 실행 가능한 통찰을 얻기 위해 쓰는 비난 없는, 시간이 정해진 절차다."
  app2="In the context of release management, a rollback drill is a scheduled, low-risk process used to gain actionable insights into the recovery path of a particular deployment."
  app2ko="릴리스 관리라는 맥락에서 롤백 훈련은, 특정 배포의 복구 경로에 대해 실행 가능한 통찰을 얻기 위해 쓰는 정기적이고 위험이 낮은 절차다."
>}}

{{< sentence
  en="Threat modeling is ideally performed early in the SDLC, such as during the design phase. Moreover, it is not something that is performed once and never again."
  ko="위협 모델링은 SDLC 초기에, 이를테면 설계 단계에서 수행하는 것이 이상적이다. 게다가 이것은 한 번 하고 다시는 하지 않는 종류의 일이 아니다."
  source="OWASP Cheat Sheet Series · Threat Modeling"
  sourceURL="https://cheatsheetseries.owasp.org/cheatsheets/Threat_Modeling_Cheat_Sheet.html"
  note="`X is ideally done at T. Moreover, it is not something that is done once and never again.` — 권고를 한 줄 던진 뒤, 그 권고에서 **가장 흔히 나오는 오해를 곧바로 끊는** 두 문장 세트다. 앞 문장의 `ideally`가 핵심이다. '초기에 해야 한다'를 `must`로 쓰면 이미 개발이 진행된 팀은 자기 얘기가 아니라고 판단하고 읽기를 멈추지만, `ideally`는 '늦었어도 안 하는 것보다 낫다'는 여지를 남긴다. 뒤 문장의 `it is not something that is -ed`는 **부정 정의**로, X가 무엇인지 대신 X가 무엇이 아닌지를 말한다. `once and never again`은 `only once`보다 훨씬 세다 — 'never again'이 사람들이 실제로 하는 행동(한 번 만들고 방치)을 그대로 묘사하기 때문이다. 문서화, 접근 권한 검토, 위험 평가처럼 **한 번 하고 잊히는 모든 것**에 그대로 쓴다."
  app1="Access reviews are ideally performed early in the onboarding flow, such as during the first week. Moreover, they are not something that is performed once and never again."
  app1ko="접근 권한 검토는 온보딩 절차 초기에, 이를테면 첫 주에 수행하는 것이 이상적이다. 게다가 이것은 한 번 하고 다시는 하지 않는 종류의 일이 아니다."
  app2="The runbook is ideally written early in the rollout, such as before the first on-call rotation. Moreover, it is not something that is written once and never again."
  app2ko="런북은 롤아웃 초기에, 이를테면 첫 온콜 로테이션 전에 쓰는 것이 이상적이다. 게다가 이것은 한 번 쓰고 다시는 쓰지 않는 종류의 일이 아니다."
>}}

{{< sentence
  en="However, despite this diversity, most approaches do include the processes of system modeling, threat identification, and risk response in some form."
  ko="그러나 이런 다양성에도 불구하고, 대부분의 접근법은 시스템 모델링, 위협 식별, 위험 대응이라는 절차를 어떤 형태로든 포함하고 있다."
  source="OWASP Cheat Sheet Series · Threat Modeling"
  sourceURL="https://cheatsheetseries.owasp.org/cheatsheets/Threat_Modeling_Cheat_Sheet.html"
  note="`However, despite this diversity, most X do include A, B, and C in some form.` — **유파 싸움을 우회해 공통분모만 확보하는** 문형이다. 표준이 여럿이라 하나를 고르면 나머지 진영이 반발하는 자리에서 쓴다. 세 장치가 함께 작동한다. `despite this diversity`는 차이를 부정하지 않고 인정한 채 넘어가고(앞 문단에서 차이를 이미 인정했다는 신호이기도 하다), 강조의 조동사 `do include`는 '그래도 이건 다들 한다'에 목소리를 실으며, `in some form`이 **이름과 순서는 다를 수 있다**는 도피구를 열어 반례를 미리 막는다. 셋 중 `in some form`이 이 문장을 반박 불가능하게 만드는 핵심이다. `most`도 `all`이 아니라서 예외 하나로 무너지지 않는다. 도구 선정 회의나 표준 제정 문서에서 합의를 만들 때 꺼내 쓴다."
  app1="However, despite this diversity, most on-call teams do include the processes of triage, mitigation, and follow-up review in some form."
  app1ko="그러나 이런 다양성에도 불구하고, 대부분의 온콜 팀은 분류, 완화, 사후 검토라는 절차를 어떤 형태로든 포함하고 있다."
  app2="However, despite this diversity, most release pipelines do include the processes of static analysis, dependency scanning, and manual approval in some form."
  app2ko="그러나 이런 다양성에도 불구하고, 대부분의 릴리스 파이프라인은 정적 분석, 의존성 스캔, 수동 승인이라는 절차를 어떤 형태로든 포함하고 있다."
>}}

{{< sentence
  en="Additionally, the threat modeling process can be complex and time-consuming. It requires a systematic approach and in-depth analysis, which is often difficult to reconcile with tight schedules and the pressure to deliver new functionalities."
  ko="게다가 위협 모델링 절차는 복잡하고 시간이 많이 들 수 있다. 체계적인 접근과 깊이 있는 분석을 요구하는데, 이는 빠듯한 일정 및 새 기능을 내놓아야 한다는 압박과 양립시키기 어려운 경우가 많다."
  source="OWASP Cheat Sheet Series · Threat Modeling"
  sourceURL="https://cheatsheetseries.owasp.org/cheatsheets/Threat_Modeling_Cheat_Sheet.html"
  note="`X requires A and B, which is often difficult to reconcile with C.` — 자기가 권하는 일의 **비용을 스스로 먼저 꺼내는** 문형이다. 좋은 제안서는 반대 의견을 상대가 말하기 전에 자기 입으로 말한다. 핵심 낱말은 `reconcile`이다. `conflicts with`는 '둘 중 하나를 버려라'로 들리지만 `reconcile`은 **양립시키는 것이 어렵다**는 뜻이라 조정의 여지를 남긴다 — 그래서 이 문장은 포기가 아니라 다음 문단의 해법으로 이어진다. `which`가 앞 절 전체를 받아 '그 요구 자체가 문제'라고 지목하고, `often`이 예외를 남겨 단정을 피한다. `the pressure to deliver ...`처럼 **압박을 명사로 만들어** 주어 자리에 놓으면 특정 팀이나 사람을 탓하지 않고 구조를 지목할 수 있다. 리뷰 기준을 높이자거나 테스트를 늘리자고 제안할 때 이 문장 다음에 완화책을 붙이면 된다."
  app1="Additionally, the audit evidence process can be tedious and repetitive. It requires a fixed format and a named owner for every control, which is often difficult to reconcile with rotating responsibilities and the pressure to close findings quickly."
  app1ko="게다가 감사 증적 절차는 지루하고 반복적일 수 있다. 모든 통제 항목에 대해 정해진 형식과 지정된 담당자를 요구하는데, 이는 돌아가는 담당 체계 및 지적 사항을 빨리 닫아야 한다는 압박과 양립시키기 어려운 경우가 많다."
  app2="Additionally, the review process can be slow and detail-heavy. It requires small diffs and written context, which is often difficult to reconcile with hard deadlines and the pressure to unblock other teams."
  app2ko="게다가 리뷰 절차는 느리고 세부에 파고들 수 있다. 작은 diff와 문서화된 맥락을 요구하는데, 이는 빠듯한 마감 및 다른 팀을 풀어 줘야 한다는 압박과 양립시키기 어려운 경우가 많다."
>}}

{{< sentence
  en="The threat model must be reviewed by all stakeholders, not just the development or security teams."
  ko="위협 모델은 개발팀이나 보안팀만이 아니라 모든 이해관계자가 검토해야 한다."
  source="OWASP Cheat Sheet Series · Threat Modeling"
  sourceURL="https://cheatsheetseries.owasp.org/cheatsheets/Threat_Modeling_Cheat_Sheet.html"
  note="`X must be reviewed by A, not just B.` — 의무를 규정하면서 **검토 범위를 넓히는** 짧은 문형이다. 힘은 `not just`에서 나온다. `not B`라고 쓰면 '보안팀은 빠지라'는 배제가 되어 반발을 부르지만, `not just B`는 **B는 당연히 포함하되 거기서 끝내지 말라**는 확장이라 아무도 잃지 않는다. 원문이 `should`가 아니라 `must`를 쓴 것도 눈여겨볼 만하다 — 이 치트시트는 대부분 `should`로 권고하다가 이 한 줄에서만 의무로 올린다. 즉 `must`는 남발하지 않을 때만 무게가 생긴다. 정책·체크리스트에서 '누가 봐야 하는가'를 정할 때, 그리고 리뷰가 늘 같은 두 사람에게만 돌 때 그대로 쓴다."
  app1="The incident timeline must be reviewed by all responders, not just the person who was paged."
  app1ko="장애 타임라인은 호출을 받은 사람만이 아니라 모든 대응자가 검토해야 한다."
  app2="The migration plan must be reviewed by all downstream owners, not just the team that owns the schema."
  app2ko="마이그레이션 계획은 스키마를 소유한 팀만이 아니라 모든 하위 소비자 담당자가 검토해야 한다."
>}}
