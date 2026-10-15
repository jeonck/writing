---
title: 강제할 수 없는 것을 부탁으로 적는 표현
description: 오해를 내 입으로 먼저 꺼내 뒤집고, 권한 없는 부탁에 권한 없음을 함께 적고, 자유와 의무의 경계를 한 문장에 긋고, 예외에 문턱 셋을 걸어 두고, 규칙 위의 최종 기준을 남기는 문장 5개.
weight: -56
date: 2026-10-16
source: "CISA · An open source agency"
sourceURL: https://github.com/cisagov/development-guide/blob/develop/open-source-policy/policy.md
---

# 강제할 수 없는 것을 부탁으로 적는 표현

미국 사이버보안·인프라보안국(CISA)이 공개한 개발 가이드 중 **오픈소스 정책** 문서다. 기관이 만든
코드를 왜 공개로 개발하는지, 공개한 코드를 누가 어디까지 쓸 수 있는지, 공개하지 않는 예외는 어떤
조건에서만 성립하는지를 한 페이지에 적어 둔 글이다. 오픈소스 라이선스 지식보다 **집행력이 없는
자리에서 쓰는 문장**이 배울 점이라 골랐다 — 요구할 권리가 없는데도 부탁을 적어야 하고, 널리 퍼진
오해를 특정인을 지목하지 않고 닫아야 하고, 예외를 금지하지 못하면서도 아무나 쓰지 못하게 해야 하는
글이다. 다른 팀에 관행을 부탁할 때, 리뷰나 감사에서 같은 통념이 반복될 때, 긴급 승인 생략 규칙을
적을 때 그대로 틀을 가져다 쓸 수 있다.

> **원문** — Cybersecurity and Infrastructure Security Agency (CISA), *CISA: An open source agency*,
> [cisagov/development-guide](https://github.com/cisagov/development-guide/blob/develop/open-source-policy/policy.md),
> 미국 내 퍼블릭 도메인이며 전 세계적으로 [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/)으로 권리를 포기한 문서.
>
> 영어 문장은 원문 그대로 인용했고, 한글 설명과 응용 문장은 이 노트에서 새로 쓴 것이다.

{{< sentence
  en="There is a misconception that FOSS that is distributed to the public should not be integrated or modified for use in sensitive systems. On the contrary, FOSS is often preferred for use in sensitive systems, due in part to its increased auditability."
  ko="공개적으로 배포되는 FOSS를 민감한 시스템에 통합하거나 수정해 쓰면 안 된다는 오해가 있다. 오히려 FOSS는 민감한 시스템에서 선호되는 경우가 많은데, 부분적으로는 감사 가능성이 더 높기 때문이다."
  source="CISA · Distribution of code"
  sourceURL="https://github.com/cisagov/development-guide/blob/develop/open-source-policy/policy.md"
  note="`There is a misconception that X. On the contrary, X is often preferred ..., due in part to its ...` — 반박할 생각을 **상대 입이 아니라 내 입으로** 먼저 꺼내는 문형이다. 전체를 결정하는 단어는 `misconception` — 틀렸다고 하지 않고 널리 퍼진 생각이라고 적기 때문에 그 말을 했던 사람을 지목하지 않고도 그 생각을 닫을 수 있다. `On the contrary`는 일부 수정이 아니라 **전면 반전**이라 통념이 통째로 뒤집히는 자리에만 쓴다. 절반만 틀렸다면 `That is only true when ...` 쪽이다. 세게 뒤집으면서도 깨지지 않는 이유는 뒤의 두 장치다 — `often`은 항상이라고 말하지 않고, `due in part to`는 그 이유 하나로 다 설명한다고 말하지 않는다. 근거를 하나(`increased auditability`)만 든 것도 계산이다. 목록을 늘리면 항목마다 반박거리가 생긴다. 리뷰나 감사에서 같은 통념이 반복될 때, 문서 맨 앞에서 그 통념을 미리 닫아 둘 때 쓴다."
  app1="There is a misconception that a rollback should not be attempted while an incident is still open. On the contrary, a rollback is often preferred during an open incident, due in part to its smaller blast radius."
  app1ko="장애가 아직 끝나지 않은 동안에는 롤백을 시도하면 안 된다는 오해가 있다. 오히려 장애가 진행 중일 때 롤백이 선호되는 경우가 많은데, 부분적으로는 영향 범위가 더 작기 때문이다."
  app2="There is a misconception that findings from an automated scan should not be opened as tickets without triage. On the contrary, scan findings are often preferred as the starting point for a review, due in part to their reproducibility."
  app2ko="자동 스캔에서 나온 발견 사항을 선별 없이 티켓으로 올리면 안 된다는 오해가 있다. 오히려 스캔 발견 사항이 점검의 출발점으로 선호되는 경우가 많은데, 부분적으로는 재현이 되기 때문이다."
>}}

{{< sentence
  en="The public can use our code as the basis of wholly proprietary and commercial systems. CISA would appreciate that users of our code disclose its lineage, but CISA maintains no legal right to require disclosure."
  ko="누구나 우리 코드를 전적으로 독점적이고 상업적인 시스템의 기반으로 쓸 수 있다. CISA는 우리 코드를 쓰는 사람들이 그 출처를 밝혀 주기를 바라지만, 밝히라고 요구할 법적 권리는 없다."
  source="CISA · Maximizing community involvement and reuse"
  sourceURL="https://github.com/cisagov/development-guide/blob/develop/open-source-policy/policy.md"
  note="`X can do A. We would appreciate that ..., but we maintain no <권리·수단> to require it.` — 강제할 수 없는 부탁을 **강제할 수 없다는 사실과 함께** 적는 문형이다. 순서가 전부다. 허용 범위를 먼저 그것도 `wholly`까지 붙여 완전히 인정해 두기 때문에, 뒤에 오는 부탁이 조건이나 압박으로 읽히지 않는다. 톤을 만드는 말은 `would appreciate` — 요구가 아니라 바람이다. 그리고 `maintains no legal right to require`가 그 부탁의 지위를 **내 쪽에서 먼저** 못 박는다. 이렇게 적으면 그거 의무인가요라는 왕복이 사라지고, 상대가 안 해도 관계가 상하지 않는다. 쓰지 말아야 할 대안이 분명하다 — `please make sure to`는 의무처럼 들려 나중에 해석 분쟁을 만들고, `we require`는 집행할 수 없는 요구라 한 번 무시되면 다음 요구까지 같이 약해진다. 권한 없는 팀에 관행을 부탁할 때, 공유한 템플릿이나 도구의 사용자에게 바라는 것을 적을 때 쓴다."
  app1="Any team can fork the pipeline templates and run them on their own runners. We would appreciate that teams record the version they forked from, but we maintain no mechanism to require it."
  app1ko="어느 팀이든 파이프라인 템플릿을 포크해서 자기 러너에서 돌릴 수 있다. 우리는 각 팀이 어느 버전에서 포크했는지 기록해 주기를 바라지만, 그것을 요구할 수단은 없다."
  app2="Reviewers can approve a change without working through the optional security checklist. We would appreciate that they note which items they skipped, but we maintain no gate to require it."
  app2ko="리뷰어는 선택 항목인 보안 체크리스트를 다 보지 않고도 변경을 승인할 수 있다. 우리는 그들이 어느 항목을 건너뛰었는지 적어 주기를 바라지만, 그것을 요구할 게이트는 없다."
>}}

{{< sentence
  en="In addition, while open source licenses permit the user to modify FOSS for internal use without obligating them to distribute source code to the public, when the user chooses to distribute the modified FOSS outside the user's organization, then the code is subject to whatever license it carries."
  ko="또한 오픈소스 라이선스는 사용자가 내부 용도로 FOSS를 수정하는 것을 허용하고 그 소스 코드를 공개 배포할 의무까지 지우지는 않지만, 사용자가 수정한 FOSS를 자기 조직 밖으로 배포하기로 선택하면 그 코드는 자신이 지닌 라이선스의 적용을 받는다."
  source="CISA · Distribution of code"
  sourceURL="https://github.com/cisagov/development-guide/blob/develop/open-source-policy/policy.md"
  note="`while X permits A without obligating B, when <조건>, then <결과>.` — 자유와 의무의 경계를 **한 문장 안에서** 긋는 양보+조건 문형이다. 훔칠 자리는 `permit ... without obligating ...`라는 두 겹이다. 허용만 적으면 사람들은 그 뒤까지 허용인 줄 알고, 의무만 적으면 아무도 쓰지 않는다. 둘을 같은 절에 붙여야 마음대로 해도 되는 구간이 **어디서 끝나는지**가 생긴다. 경계를 넘기는 방아쇠를 `when the user chooses to`로 적은 것이 핵심이다 — 시점도 규모도 아니라 **선택**이다. 의무가 저절로 생기는 것이 아니라 당신이 한 행동에서 생긴다고 적는 것이므로, 나중에 몰랐다는 말이 성립하지 않는다. 긴 양보절 뒤에서 `then`을 생략하지 않은 것도 장치다. 조건과 결과가 한눈에 걸린다. 내부 사용은 자유지만 외부로 나가는 순간 절차가 붙는 규칙 — 사내 라이브러리 포크, 샘플 데이터, 장애 보고서 외부 공유 — 을 적을 때 쓴다."
  app1="While the sandbox account permits any team to create resources without obligating them to file a change request, when a team chooses to route production traffic to those resources, then the stack is subject to whatever review the production tier requires."
  app1ko="샌드박스 계정은 어느 팀이든 리소스를 만드는 것을 허용하고 변경 요청을 올릴 의무까지 지우지는 않지만, 어떤 팀이 그 리소스로 운영 트래픽을 보내기로 선택하면 그 구성은 운영 등급에 요구되는 검토의 적용을 받는다."
  app2="While the internal wiki permits an engineer to draft an incident timeline without obligating them to clear it with anyone, when the engineer chooses to send that timeline outside the company, then the document is subject to whatever review applies to customer-facing reports."
  app2ko="내부 위키는 엔지니어가 장애 타임라인을 초안으로 쓰는 것을 허용하고 누군가의 승인을 받을 의무까지 지우지는 않지만, 그 타임라인을 회사 밖으로 보내기로 선택하면 그 문서는 고객 대상 보고서에 적용되는 검토의 적용을 받는다."
>}}

{{< sentence
  en="Any further exemptions will be rare, documented publicly, and the result of compelling interest."
  ko="그 밖의 추가 예외는 드물 것이고, 공개적으로 문서화될 것이며, 설득력 있는 이해관계에 따른 결과일 것이다."
  source="CISA · Exceptions"
  sourceURL="https://github.com/cisagov/development-guide/blob/develop/open-source-policy/policy.md"
  note="`Any further exemptions will be rare, documented publicly, and the result of <높은 문턱>.` — 예외를 금지하지 않으면서 **문턱 셋을 걸어** 사실상 닫는 문장이다. 금지하지 않는 쪽을 택한 이유가 있다. 예외는 없다고 적으면 급할 때 문서를 무시하고 처리하게 되고, 그렇게 처리된 건은 기록에 남지 않는다. 그래서 막는 대신 조건을 셋 나열한다 — 빈도(`rare`), 가시성(`documented publicly`), 근거의 수준(`the result of compelling interest`). 하나라도 빼면 빠져나갈 길이 생긴다. 가장 센 단어는 `publicly`다. 예외를 받는 쪽에 실제로 비용을 지우는 것은 심사가 아니라 공개다. 시제가 `will be`인 것도 포인트 — 지난 사례를 평가하는 문장이 아니라 앞으로의 약속이라, 지금 예외를 승인할 사람까지 같이 묶인다. 긴급 배포, 승인 생략, 보존 기간 예외처럼 예외를 아예 못 막는 규칙을 적을 때 쓴다."
  app1="Any further exceptions to the two-reviewer rule will be rare, logged in the audit channel, and the result of a declared incident."
  app1ko="두 명 리뷰 규칙에 대한 그 밖의 추가 예외는 드물 것이고, 감사 채널에 기록될 것이며, 선언된 장애에 따른 결과일 것이다."
  app2="Any further waivers of the dependency scan will be rare, recorded in the release notes, and the result of a dated risk acceptance."
  app2ko="의존성 스캔에 대한 그 밖의 추가 면제는 드물 것이고, 릴리스 노트에 기재될 것이며, 날짜가 적힌 위험 수용에 따른 결과일 것이다."
>}}

{{< sentence
  en="If an existing solution cannot be found in the open source community, CISA may consider other options, including creating an open source solution itself. Ultimately, the software that best meets the needs and mission of CISA should be used."
  ko="오픈소스 커뮤니티에서 기존 해법을 찾을 수 없다면, CISA는 직접 오픈소스 해법을 만드는 것을 포함해 다른 선택지를 고려할 수 있다. 궁극적으로는 CISA의 필요와 임무에 가장 잘 맞는 소프트웨어를 써야 한다."
  source="CISA · Exceptions"
  sourceURL="https://github.com/cisagov/development-guide/blob/develop/open-source-policy/policy.md"
  note="`If A cannot be found, we may consider other options, including B. Ultimately, the X that best meets <목적> should be used.` — 원칙을 적어 둔 문서가 **그 원칙보다 위에 있는 기준**을 스스로 적어 두는 2단 마무리다. 첫 문장은 순서를 정한다. 찾는 것이 먼저, 만드는 것은 그다음이고, `may consider`로 약하게 적어 권한은 주되 기본 경로는 흔들지 않는다. 둘째 문장이 실제로 쓸 데가 많다. `Ultimately`는 앞의 규칙을 무효로 만들지 않으면서 **동점일 때 깨는 기준**만 지정하고, 그 기준을 취향이 아니라 `the needs and mission`, 즉 목적 쪽에 둔다. 그래서 규칙을 글자대로 들이대는 사람과 다툴 때 꺼낼 한 줄이 생긴다. 수동태 `should be used`도 의도적이다 — 누가 고르는지는 비워 두고 무엇을 보고 고르는지만 남긴다. 기술 선택 가이드나 표준 문서 끝에 최종 판단의 기준을 한 줄로 남길 때 쓴다."
  app1="If a managed service cannot be found that meets our retention requirements, the team may consider other options, including running the collector itself. Ultimately, the setup that best meets the on-call burden and the audit scope should be used."
  app1ko="우리 보존 요건을 만족하는 매니지드 서비스를 찾을 수 없다면, 팀은 수집기를 직접 운영하는 것을 포함해 다른 선택지를 고려할 수 있다. 궁극적으로는 온콜 부담과 감사 범위에 가장 잘 맞는 구성을 써야 한다."
  app2="If a fix cannot be found in the upstream project, we may consider other options, including carrying the patch ourselves. Ultimately, the approach that best meets the deadline and the review standard should be used."
  app2ko="업스트림 프로젝트에서 수정을 찾을 수 없다면, 우리는 패치를 직접 들고 가는 것을 포함해 다른 선택지를 고려할 수 있다. 궁극적으로는 기한과 리뷰 기준에 가장 잘 맞는 방식을 써야 한다."
>}}
