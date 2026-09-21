---
title: 보장의 등급을 나눠 말하는 표현
description: 책임을 사람에게 배정하고, 제도가 비워 둔 자리를 관행으로 메우고, 유동적인 것과 고정된 것을 한 문장에서 가르고, 규칙의 강도를 대상별로 조절하고, 예외에 선행 절차를 붙이는 문장 5개.
weight: -32
date: 2026-09-22
source: "AIP-181 — Stability levels"
sourceURL: https://google.aip.dev/181
---

# 보장의 등급을 나눠 말하는 표현

구글의 API 설계 지침 모음인 AIP 가운데 *Stability levels*는 API의 각 부분이 어느 정도까지
안 바뀐다고 약속되는지를 알파·베타·안정, 그리고 실험·프리뷰·정식 출시로 나눠 규정한다.
"이건 보장하고 저건 보장하지 않는다"를 각 세우지 않고 적는 문장이 많아 발췌했다 — 지원 범위,
폐기 공지, 오너십 문서를 쓸 때 그대로 쓸 수 있는 틀이다.

> **원문** — Google API Improvement Proposals, *AIP-181: Stability levels*,
> [google.aip.dev/181](https://google.aip.dev/181) (2019-02-18 제정),
> [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) 라이선스.
> 원본 마크다운은 [aip-dev/google.aip.dev](https://github.com/aip-dev/google.aip.dev/blob/master/aip/general/0181.md).
>
> 영어 문장은 원문 그대로 인용했고, 한글 설명과 응용 문장은 이 노트에서 새로 쓴 것이다.

{{< sentence
  en="Management and mitigation of call-time compatibility changes is the responsibility of the producer."
  ko="호출 시점 호환성 변경을 관리하고 그 여파를 줄이는 일은 제공자의 책임이다."
  source="AIP-181 · Stability axes"
  sourceURL="https://google.aip.dev/181"
  note="`Management and mitigation of X is the responsibility of Y.` — 위험을 '누가 조심해야 하나'가 아니라 **누구 몫인가**로 배정하는 문형이다. 동사를 쓰지 않고 `management and mitigation`이라는 명사구로 일을 한 덩어리로 묶어 두면, 평소의 관리와 터진 뒤의 수습이 같은 사람에게 붙는다. `mitigation`은 '막는다'가 아니라 **피해를 줄인다**라서, 변경이 언젠가 일어난다는 것을 이미 인정한 채로 책임을 나누는 말이 된다. 경계가 애매한 두 팀 사이에 선을 그을 때 한 줄로 쓴다."
  app1="Management and mitigation of alert noise on this service is the responsibility of the owning team, not the on-call rotation."
  app1ko="이 서비스의 알림 소음을 관리하고 줄이는 일은 온콜 당번이 아니라 서비스를 소유한 팀의 책임이다."
  app2="Rotation of the shared credentials is the responsibility of the platform team; revoking them after an incident is ours."
  app2ko="공용 자격 증명의 교체는 플랫폼 팀의 책임이고, 장애 뒤에 폐기하는 일은 우리 책임이다."
>}}

{{< sentence
  en="While policy does not guarantee stability, the extremely limited and targeted nature of their use means that direct communication with consumers about changes is both possible and encouraged."
  ko="정책이 안정성을 보장하지는 않지만, 그 쓰임이 극히 제한적이고 대상이 좁다는 점 때문에 변경에 관해 소비자와 직접 소통하는 일이 가능하기도 하고 권장되기도 한다."
  source="AIP-181 · Experimental"
  sourceURL="https://google.aip.dev/181"
  note="`While policy does not guarantee X, the ... nature of Y means that Z is both possible and encouraged.` — 제도가 비워 둔 자리를 **관행으로 메운다**고 말하는 문형이다. 앞 절에서 보장이 없다는 것을 먼저 인정해 버리기 때문에, 뒤 절이 변명이 아니라 설명으로 읽힌다. 힘은 `the ... nature of Y means that`에 있다. 한계(쓰는 사람이 몇 안 된다)를 그대로 **가능성의 근거**로 뒤집는 자리다. `both possible and encouraged`는 '해도 된다'와 '하는 편이 낫다'를 한 번에 붙이는 짝. 공식 지원이 없는 내부 도구나 실험 기능의 처지를 설명할 때 쓴다."
  app1="While the runbook does not guarantee a fix, the narrow scope of this failure mode means that paging the author directly is both possible and encouraged."
  app1ko="런북이 해결을 보장하지는 않지만, 이 장애 유형의 범위가 좁다는 점 때문에 작성자를 직접 호출하는 일이 가능하기도 하고 권장되기도 한다."
  app2="While the SLA does not cover this internal endpoint, the small number of callers means that announcing breaking changes in the team channel is both possible and expected."
  app2ko="SLA가 이 내부 엔드포인트를 다루지는 않지만, 호출하는 곳이 적다는 점 때문에 팀 채널에 호환성 깨지는 변경을 공지하는 일이 가능하기도 하고 당연하기도 하다."
>}}

{{< sentence
  en="Version expiration is a multi-phased event consisting of onboarding window closure followed by final turndown and rejection of the version. The timing of these events varies, but is always stated upfront to set expectations."
  ko="버전 만료는 신규 유입 창구를 닫은 뒤 최종 중단과 해당 버전 거부가 이어지는, 여러 단계로 이루어진 사건이다. 각 단계의 시점은 그때그때 다르지만, 기대치를 맞추기 위해 언제나 미리 알린다."
  source="AIP-181 · Preview expiration"
  sourceURL="https://google.aip.dev/181"
  note="`X varies, but is always stated upfront to set expectations.` — **무엇이 유동적이고 무엇이 고정인지를 한 문장 안에서 갈라 놓는** 문형이다. 일정이 정해지지 않았다는 사실을 숨기지 않은 채, 그래도 약속할 수 있는 것(미리 알린다)을 `but` 뒤에 붙인다. `to set expectations`가 목적을 밝혀 주어서, 공지가 형식적인 절차가 아니라 **상대의 기대를 관리하는 행위**로 자리 잡는다. 앞 문장처럼 과정을 먼저 단계로 쪼개 이름을 붙여 두면, '언제 끝나냐'는 질문이 '지금 어느 단계냐'로 바뀐다."
  app1="The rollback window varies by service, but is always stated upfront in the change request to set expectations."
  app1ko="롤백 가능 시간은 서비스마다 다르지만, 기대치를 맞추기 위해 변경 요청서에 언제나 미리 적어 둔다."
  app2="Deprecation is a multi-phased event consisting of new integrations being turned away, followed by a warning on every call and then removal of the endpoint."
  app2ko="폐기는 신규 연동을 받지 않는 것으로 시작해 호출마다 경고가 뜨고 그다음 엔드포인트가 사라지는, 여러 단계로 이루어진 사건이다."
>}}

{{< sentence
  en="The contents of such a version have typically progressed through the previous stability levels of experimental and preview before reaching general availability. This is especially important for non-trivial features that warrant thorough evaluation, but is not strictly a requirement for smaller, self-explanatory features."
  ko="그런 버전에 담긴 것들은 보통 정식 출시에 이르기 전에 실험과 프리뷰라는 앞 단계의 안정성 등급을 거쳐 온다. 이는 충분한 검토가 필요한 묵직한 기능에서 특히 중요하지만, 더 작고 따로 설명이 필요 없는 기능에는 엄격한 요건이 아니다."
  source="AIP-181 · General availability"
  sourceURL="https://google.aip.dev/181"
  note="`This is especially important for X, but is not strictly a requirement for Y.` — 규칙을 적으면서 **그 규칙이 어디까지 빡빡한지를 같은 문장에서 조절하는** 문형이다. 앞 문장의 `typically`가 이미 '원칙이 아니라 관행'이라고 밝혀 두었기 때문에, 뒤에서 예외를 열어도 규칙이 무너지지 않는다. `not strictly a requirement`는 '안 해도 된다'가 아니라 **요건으로 강제하지는 않는다**는 뜻이어서 권장은 그대로 살아 있다. 체크리스트나 리뷰 기준을 문서로 만들 때, 모든 항목을 같은 강도로 쓰지 않으려고 꺼낸다."
  app1="A design review before implementation is especially important for changes that touch authentication, but is not strictly a requirement for copy edits and config bumps."
  app1ko="구현 전 설계 리뷰는 인증을 건드리는 변경에서 특히 중요하지만, 문구 수정이나 설정값 조정에는 엄격한 요건이 아니다."
  app2="Two reviewers are especially important for migrations that cannot be rolled back, but are not strictly a requirement for additive schema changes."
  app2ko="되돌릴 수 없는 마이그레이션에서는 리뷰어 두 명이 특히 중요하지만, 컬럼을 더하기만 하는 스키마 변경에는 엄격한 요건이 아니다."
>}}

{{< sentence
  en="However, features that are facing deprecation or substantial redesign can change in incompatible ways between two consecutive generally available versions. This will happen after the API producer has fulfilled the necessary processes for communicating the change and facilitating consumer migration as appropriate for the change."
  ko="다만 폐기를 앞두었거나 대대적으로 다시 설계되는 기능은 연속된 두 정식 출시 버전 사이에서도 호환되지 않는 방식으로 바뀔 수 있다. 그런 일은 API 제공자가 변경을 알리고 소비자의 이전을 돕는, 그 변경에 걸맞은 절차를 마친 뒤에 일어난다."
  source="AIP-181 · General availability"
  sourceURL="https://google.aip.dev/181"
  note="`X can change in incompatible ways. This will happen after Y has fulfilled the necessary processes for ...` — 예외를 열어 준 뒤 **그 예외가 아무 때나 일어나지는 않는다는 것을 다음 문장에서 못 박는** 짝이다. 첫 문장은 `can`으로 가능성만 열고, 둘째 문장이 `This will happen after ~`로 **선행 조건**을 건다. 조건을 `only if`로 걸면 금지처럼 들리는데 시간 순서(`after`)로 말하면 절차가 된다 — 막는 게 아니라 순서를 정하는 문장이다. 끝의 `as appropriate for the change`는 절차의 무게를 변경의 크기에 맞추겠다는 단서다."
  app1="However, endpoints that are facing deprecation can start returning errors between two minor releases. This will happen after we have announced the date and published a migration guide."
  app1ko="다만 폐기를 앞둔 엔드포인트는 마이너 릴리스 사이에서도 오류를 반환하기 시작할 수 있다. 그런 일은 우리가 날짜를 공지하고 이전 안내를 낸 뒤에 일어난다."
  app2="However, accounts flagged in the audit can lose write access between two review cycles. This will happen after the owning team has been notified and given a window to justify the access."
  app2ko="다만 감사에서 표시된 계정은 리뷰 주기 사이에도 쓰기 권한을 잃을 수 있다. 그런 일은 소유 팀에 통지하고 그 권한이 필요한 이유를 소명할 기간을 준 뒤에 일어난다."
>}}
