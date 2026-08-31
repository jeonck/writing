---
title: 기준을 세우면서 그 경계를 함께 긋는 표현
description: 등급의 뜻을 못 박고, 양쪽 실패를 나란히 놓고, 확대해석을 미리 차단하는 문장 5개.
weight: -12
date: 2026-09-01
source: "SLSA Specification v1.2 — Guiding principles"
sourceURL: https://slsa.dev/spec/v1.2/principles
---

# 기준을 세우면서 그 경계를 함께 긋는 표현

SLSA(Supply-chain Levels for Software Artifacts)는 소프트웨어 공급망의 무결성을 레벨과 트랙으로
나눠 기술하는 보안 명세다. 이 노트가 고른 'Guiding principles' 장은 요구사항 목록이 아니라
**그 요구사항을 왜 그렇게 설계했는지**를 적어 놓은 곳이라, 표준 문서가 자기 기준을 정당화하는
방식이 그대로 드러난다. 등급이 무엇을 뜻하는지 먼저 못 박고, 숫자를 정하기 전에 양극단의 실패를
나란히 놓고, 판단을 규칙이 아니라 경험칙으로 남기고, 두 작업의 비용 차이로 결론을 끌어내고,
마지막에는 문서 전체가 어디까지 적용되는지를 스스로 잘라 둔다. 사내 표준, 심각도 정의, 감사
기준을 쓸 때 그대로 옮겨 쓸 문형만 다섯 개 뽑았다.

> **원문** — SLSA Working Group (OpenSSF), *SLSA Specification v1.2 — Guiding principles*,
> [slsa.dev](https://slsa.dev/spec/v1.2/principles)
> ([github.com/slsa-framework/slsa](https://github.com/slsa-framework/slsa/blob/releases/v1.2/spec/principles.md)),
> [Community Specification License 1.0](https://github.com/slsa-framework/slsa/blob/main/LICENSE.md).
>
> 영어 문장은 원문 그대로 인용했고, 한글 설명과 응용 문장은 이 노트에서 새로 쓴 것이다.

{{< sentence
  en="Levels should represent security milestones, not just incremental progress."
  ko="레벨은 단순히 점진적인 진전이 아니라 보안 이정표를 나타내야 한다."
  source="SLSA Specification v1.2 · Guiding principles"
  sourceURL="https://slsa.dev/spec/v1.2/principles"
  note="`X should represent A, not just B.` — 등급이나 단계를 만들 때 **그 단계가 무엇을 뜻하는지**를 먼저 못 박는 문형이다. `not just`가 하는 일이 핵심인데, B를 틀렸다고 하지 않는다. B도 맞지만 그것만으로는 자격이 안 된다는 뜻이라, 이미 B를 해 온 사람을 부정하지 않으면서 문턱만 올린다(`not` 단독이었다면 지금까지의 노력을 통째로 무효로 만든다). 동사 `represent`도 계산된 선택이다. `achieve`나 `require`가 아니라 나타내다이므로, 레벨이 달성 항목의 묶음이 아니라 **의미의 단위**라는 것이 문장 안에서 정해진다. 등급·티어·심각도를 새로 설계할 때, 한 단계를 올리려면 무엇이 필요한지를 적기 전에 이 문형으로 그 단계의 뜻부터 적는다."
  app1="A severity level should represent user-visible impact, not just how loud the alert was."
  app1ko="심각도 등급은 단순히 알림이 얼마나 요란했는지가 아니라 사용자가 겪은 영향을 나타내야 한다."
  app2="A review approval should represent that someone understood the change, not just that the tests passed."
  app2ko="리뷰 승인은 단순히 테스트가 통과했다는 것이 아니라 누군가 그 변경을 이해했다는 것을 나타내야 한다."
>}}

{{< sentence
  en="Too many levels makes SLSA hard to understand and remember; too few makes each level hard to achieve."
  ko="레벨이 너무 많으면 SLSA를 이해하고 기억하기 어려워지고, 너무 적으면 각 레벨을 달성하기 어려워진다."
  source="SLSA Specification v1.2 · Guiding principles"
  sourceURL="https://slsa.dev/spec/v1.2/principles"
  note="`Too many X does A; too few does B.` — 세미콜론으로 **양극단의 실패를 나란히** 놓는 대칭 문형이다. 힘은 두 실패의 성격이 서로 다르다는 데서 나온다. 한쪽은 이해의 실패, 다른 쪽은 달성의 실패다. 양쪽에 같은 종류의 손해를 놓으면 그저 정도 문제로 읽히지만, 다른 종류의 손해를 놓으면 **적정선이 중간 어딘가에 있다**는 것이 문장만으로 서게 된다. 접속사를 지우고 세미콜론을 쓴 것도 의도적이다. `but`이나 `while`을 넣으면 한쪽이 주장, 다른 쪽이 양보로 기울지만 세미콜론은 둘을 동급으로 세운다. 뒤 절에서 `levels makes`를 반복하지 않고 `too few makes`로 줄인 생략이 대칭을 더 또렷하게 만든다. 임계값, 보존 기간, 필수 리뷰어 수처럼 **숫자를 정해야 하는 논의**를 열 때, 내가 고른 값을 방어하기 전에 이 문장으로 축을 먼저 세운다."
  app1="Too short a retention window makes incidents impossible to reconstruct; too long makes the audit surface bigger than anyone can review."
  app1ko="보존 기간이 너무 짧으면 장애를 되짚을 수 없고, 너무 길면 감사 대상이 누구도 다 볼 수 없을 만큼 커진다."
  app2="Too many required approvers makes every change wait on someone; too few makes the approval a formality."
  app2ko="필수 승인자가 너무 많으면 모든 변경이 누군가를 기다리게 되고, 너무 적으면 승인이 형식이 된다."
>}}

{{< sentence
  en="As a rule of thumb, a new track may be warranted if it addresses threats unrelated to another track."
  ko="경험칙으로, 새 트랙은 다른 트랙과 무관한 위협을 다룰 때 정당화될 수 있다."
  source="SLSA Specification v1.2 · Guiding principles"
  sourceURL="https://slsa.dev/spec/v1.2/principles"
  note="`As a rule of thumb, X may be warranted if Y.` — 판단 기준을 규칙이 아니라 **경험칙**으로 내놓는 문형이다. 완화 장치가 두 겹으로 걸려 있다. `As a rule of thumb`이 예외의 존재를 먼저 인정하고, `may be warranted`가 결론을 자동화하지 않는다. 조건 Y를 만족해도 결정은 여전히 사람이 한다는 뜻이다. 그래서 이 문장은 지키기 쉬우면서도 **논의의 출발점을 고정**한다. 새 트랙을 제안하는 사람은 이제 Y를 만족한다는 것부터 말해야 하고, 반대하는 사람도 Y를 두고 다투게 된다. 톤을 정하는 단어는 `warranted`다. `allowed`(허가된다)나 `needed`(필요하다)가 아니라 정당화된다이므로, 판단의 책임이 규칙이 아니라 제안자 쪽에 남는다. 새 서비스, 새 저장소, 새 온콜처럼 매번 사람이 판단해야 하는 문제에 기준선을 적을 때 쓴다."
  app1="As a rule of thumb, a separate on-call rotation may be warranted if the pages it would take are ones the current rotation cannot act on."
  app1ko="경험칙으로, 별도의 온콜 로테이션은 그것이 받게 될 호출이 지금 로테이션에서는 조치할 수 없는 것일 때 정당화될 수 있다."
  app2="As a rule of thumb, a new dashboard may be warranted if it answers a question no existing panel is scoped to answer."
  app2ko="경험칙으로, 새 대시보드는 기존 어떤 패널도 답하도록 만들어지지 않은 질문에 답할 때 정당화될 수 있다."
>}}

{{< sentence
  en="Hardening and verifying platforms is difficult and expensive manual work, and each trusted platform expands the attack surface of the supply chain. Verifying that an artifact is produced by a trusted platform, though, is easy to automate."
  ko="플랫폼을 하드닝하고 검증하는 일은 어렵고 비싼 수작업이며, 신뢰하는 플랫폼이 하나 늘 때마다 공급망의 공격 표면도 넓어진다. 다만 어떤 산출물이 신뢰된 플랫폼에서 만들어졌는지를 검증하는 일은 자동화하기 쉽다."
  source="SLSA Specification v1.2 · Guiding principles"
  sourceURL="https://slsa.dev/spec/v1.2/principles"
  note="`A is expensive manual work, and each X expands Y. B, though, is easy to automate.` — 두 작업의 **비용 비대칭**을 드러내서 설계 결론을 끌어내는 2단 구성이다. 앞 문장이 비용을 두 종류로 쪼갠 것이 먼저 눈에 띈다. 수작업의 값에 더해 **늘어나는 것이 무엇인지**(공격 표면)를 같이 말한다. 비싸다는 말만으로는 대개 설득이 되지 않고, 늘어나는 쪽을 이름 붙여야 상대가 그 항목을 자기 계산에 넣는다. 뒤집기는 `though`가 하는데, 문두가 아니라 **주어 뒤 쉼표 사이에 끼워 넣은** 점이 중요하다. `However,`로 시작하면 반전이 미리 예고되어 앞 문장을 듣는 둥 마는 둥 하게 되지만, 삽입된 `though`는 대비 대상을 끝까지 말하게 한 다음에 뒤집는다. 무엇을 사람이 하고 무엇을 자동화할지 가르는 제안서에서, 두 선택지의 값을 나란히 놓는 자리에 쓴다."
  app1="Reviewing every config change by hand is slow and error-prone work, and each reviewer we add widens the window in which the change sits unmerged. Checking that a change matches an approved template, though, is easy to automate."
  app1ko="설정 변경을 하나하나 손으로 검토하는 일은 느리고 실수가 나기 쉬운 작업이며, 리뷰어를 한 명 더할 때마다 변경이 머지되지 못한 채 머무는 시간도 길어진다. 다만 어떤 변경이 승인된 템플릿과 맞는지를 확인하는 일은 자동화하기 쉽다."
  app2="Interviewing each team about their data flows is slow and expensive work, and every extra questionnaire we send lowers the rate at which we get answers back. Checking which services actually opened a connection to the database, though, is easy to automate."
  app2ko="팀마다 데이터 흐름을 인터뷰하는 일은 느리고 비싼 작업이며, 설문을 하나 더 보낼 때마다 회수율은 떨어진다. 다만 어떤 서비스가 실제로 데이터베이스에 연결을 열었는지를 확인하는 일은 자동화하기 쉽다."
>}}

{{< sentence
  en="Nothing in this specification should be taken to mean that SLSA requires participants to reveal their legal identity."
  ko="이 명세의 어떤 내용도 SLSA가 참여자에게 법적 신원을 밝히도록 요구한다는 뜻으로 받아들여져서는 안 된다."
  source="SLSA Specification v1.2 · Guiding principles"
  sourceURL="https://slsa.dev/spec/v1.2/principles"
  note="`Nothing in X should be taken to mean that Y.` — 문서가 **자기 자신에 대한 오독을 미리 차단**하는 선언 문형이다. 바로 앞 문단에서 이미 요구하지 않는다고 말해 놓고도 이 문장을 따로 세우는 이유가 있다. 개별 조항을 부인하는 것과 **문서 전체의 함의를 부인**하는 것은 다르기 때문이다. 주어를 `Nothing in this specification`으로 둔 덕분에 독자가 뒤에서 어떤 조항을 읽든 이 문장이 그 위에 걸린다. 술어가 `does not mean`이 아니라 `should not be taken to mean`인 것도 계산이다. 잘못이 문서가 아니라 **읽는 행위** 쪽에 놓이므로, 이미 그렇게 읽고 있던 사람도 체면을 잃지 않고 물러설 수 있다. 정책, 사내 표준, 감사 기준을 쓸 때 확대 적용될 것이 뻔한 조항 바로 옆에 한 줄로 붙인다."
  app1="Nothing in this runbook should be taken to mean that the on-call engineer needs approval before rolling back."
  app1ko="이 런북의 어떤 내용도 온콜 엔지니어가 롤백 전에 승인을 받아야 한다는 뜻으로 받아들여져서는 안 된다."
  app2="Nothing in this audit finding should be taken to mean that the team introduced the misconfiguration."
  app2ko="이 감사 지적의 어떤 내용도 해당 팀이 그 잘못된 설정을 만들어 넣었다는 뜻으로 받아들여져서는 안 된다."
>}}
