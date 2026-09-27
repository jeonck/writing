---
title: 무엇으로 간주하고 시작할지 선언하는 표현
description: 유추로 신뢰 경계를 다시 긋고, 흔한 관행과 표준을 갈라놓고, 사용자가 찔러 볼 것을 전제로 요구사항을 세우는 문장 5개.
weight: -38
date: 2026-09-28
source: "NeMo Guardrails Docs — Security Guidelines for LLM Integrations"
sourceURL: https://github.com/NVIDIA/NeMo-Guardrails/blob/main/docs/resources/security/guidelines.mdx
---

# 무엇으로 간주하고 시작할지 선언하는 표현

LLM에 검색·데이터베이스·코드 실행 같은 **외부 자원을 붙일 때** 그 사이에 무엇을 놓아야
하는지를 정리한 지침 문서. 규칙을 나열하기 전에 "LLM을 무엇으로 취급할 것인가"를 먼저
선언하고, 그 취급 방식에서 개별 규칙을 끌어내는 구조다. 그래서 **규칙보다 전제를 적는
문장**이 좋다. 새 기술을 기존 신뢰 경계 안에 배치하고, 아직 표준이 없다는 사실을 숨기지
않으면서 지금의 규칙을 정당화하는 문형을 골랐다.

> **원문** — NVIDIA NeMo Guardrails contributors, *Security Guidelines for LLM Integrations*,
> [NVIDIA/NeMo-Guardrails · docs/resources/security/guidelines.mdx](https://github.com/NVIDIA/NeMo-Guardrails/blob/main/docs/resources/security/guidelines.mdx)
> (main 브랜치, 2026-09-28 확인), [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0).
>
> 영어 문장은 원문 그대로 인용했고, 한글 설명과 응용 문장은 이 노트에서 새로 쓴 것이다.

{{< sentence
  en="Consider the LLM to be, in effect, a web browser under the complete control of the user, and all content it generates is untrusted."
  ko="LLM을 사실상 사용자가 완전히 통제하는 웹 브라우저로 간주하라. 그리고 그것이 생성하는 모든 내용은 신뢰할 수 없는 것으로 보라."
  source="NeMo Guardrails Docs · Security Guidelines, The Golden Rule"
  sourceURL="https://github.com/NVIDIA/NeMo-Guardrails/blob/main/docs/resources/security/guidelines.mdx"
  note="`Consider X to be, in effect, Y, and <Y에서 곧바로 따라오는 결론>.` — 취급 규칙이 아직 없는 대상을 **이미 규칙이 확립된 것**에 갖다 붙여 그 결론까지 물려받는 문형이다. `in effect`가 이 문장의 안전장치다. '정말 브라우저다'가 아니라 '따지고 보면 같은 자리에 있다'는 뜻이라, 사실 주장이 아니라 **취급 방침**이 된다. 그래서 'LLM은 브라우저가 아니다'라는 반박은 빗나간다. 유추의 근거를 `under the complete control of the user`, 즉 **누가 통제권을 쥐고 있는지**로 잡아 둔 것이 핵심이다. 통제권이 저쪽에 있다는 사실 하나만 공유되면 뒤 절의 결론(`all content it generates is untrusted`)은 설명 없이 따라온다. 새 도구나 새 데이터 출처를 기존 신뢰 경계의 어디에 놓을지 정하는 문서의 첫 문장으로 쓴다."
  app1="Consider a CI runner to be, in effect, a shell session opened by anyone who can push to the branch, and every artifact it produces is untrusted until signed."
  app1ko="CI 러너를 사실상 그 브랜치에 푸시할 수 있는 누구나 열어 놓을 수 있는 셸 세션으로 간주하라. 그리고 러너가 만든 모든 산출물은 서명되기 전까지 신뢰하지 않는다."
  app2="Consider a vendor dashboard to be, in effect, a third-party script running inside our admin console, and the data it sends back is untrusted input."
  app2ko="외부 업체 대시보드를 사실상 우리 관리자 콘솔 안에서 돌아가는 서드파티 스크립트로 간주하라. 그리고 거기서 돌아오는 데이터는 신뢰할 수 없는 입력으로 다룬다."
>}}

{{< sentence
  en="It is currently common practice to include a specific verb (e.g., “FINISH”) to indicate that the LLM should return the result to the user – effectively making user interaction an external resource as well – however, this area is new enough that there is no such thing as a “standard practice”."
  ko="LLM이 결과를 사용자에게 돌려주어야 한다는 것을 나타내려고 특정 동사(예: “FINISH”)를 넣는 것이 지금은 흔한 관행이다 — 사실상 사용자와의 상호작용까지 하나의 외부 자원으로 만드는 셈이다 — 하지만 이 분야는 “표준 관행”이라 할 것이 없을 만큼 새롭다."
  source="NeMo Guardrails Docs · Security Guidelines, Assumed Interaction Model"
  sourceURL="https://github.com/NVIDIA/NeMo-Guardrails/blob/main/docs/resources/security/guidelines.mdx"
  note="`It is currently common practice to X – <X를 다시 분류해 주는 삽입구> – however, this area is new enough that there is no such thing as a 'standard practice'.` — 관행을 소개하면서 **그 관행에 표준의 권위는 주지 않는** 문형이다. `common practice`와 `standard practice`를 한 문장 안에 나란히 놓아 **많이들 한다 ≠ 정해져 있다**를 갈라놓고, `currently`로 지금의 이야기라는 시한을 붙인다. 없는 이유를 `new enough that ~`으로 대는 것이 요령이다. 누구의 태만도 탓하지 않으면서 '아직 없다'가 설명된다. 대시 사이 삽입구(`effectively making ~`)는 방금 말한 구현을 **개념 차원에서 다시 이름 붙이는** 자리다. 사내 관례를 문서로 옮기면서 그것이 합의된 표준은 아니라고 못 박을 때 쓴다."
  app1="It is currently common practice to page the service owner directly for anything touching billing – effectively treating one team as a second on-call rotation – however, this arrangement is new enough that there is no such thing as an agreed escalation path."
  app1ko="결제를 건드리는 일은 서비스 담당자에게 곧바로 호출을 보내는 것이 지금은 흔한 관행이다 — 사실상 한 팀을 2차 온콜 로테이션으로 쓰는 셈이다 — 하지만 이 방식은 합의된 에스컬레이션 경로라 할 것이 없을 만큼 최근에 생겼다."
  app2="It is currently common practice to record agent tool calls in the application log – effectively making the audit trail a by-product of debugging – however, this area is new enough that there is no such thing as a retention rule for it."
  app2ko="에이전트의 도구 호출을 애플리케이션 로그에 남기는 것이 지금은 흔한 관행이다 — 사실상 감사 기록을 디버깅의 부산물로 만드는 셈이다 — 하지만 이 영역은 보존 기간 규칙이라 할 것이 없을 만큼 새롭다."
>}}

{{< sentence
  en="It should be assumed that users of the service will attempt to discover internal APIs and/or verbs that their specific prompt or LLM session does not enable and that they do not have the authorization to use; a user should not be able to detect that some internal API exists based on interactions with the LLM."
  ko="서비스 사용자는 자기 프롬프트나 LLM 세션에서 활성화되지 않았고 쓸 권한도 없는 내부 API나 동사를 찾아내려 시도할 것이라고 전제해야 한다. 사용자는 LLM과의 상호작용만으로 어떤 내부 API가 존재한다는 사실을 알아낼 수 없어야 한다."
  source="NeMo Guardrails Docs · Security Guidelines, Fail gracefully and secretly"
  sourceURL="https://github.com/NVIDIA/NeMo-Guardrails/blob/main/docs/resources/security/guidelines.mdx"
  note="`It should be assumed that <사람들이 할 일>; <그래서 지켜져야 할 상태>.` — 세미콜론 하나로 **전제 한 줄과 요구사항 한 줄**을 붙여 끝내는 문형이다. `It should be assumed that ~`은 '그럴 수도 있다'는 가능성 언급이 아니라 **설계의 기본값으로 깔아 두라는 지시**다. 주어를 비인칭으로 둔 덕에 특정 사용자를 의심하는 말로 읽히지 않는다. 뒤 절이 `should not be able to`인 것이 중요하다. 금지('하지 마라')가 아니라 **가능성의 제거**를 요구하므로 검증 기준이 사람의 행위가 아니라 시스템의 상태가 되고, 그래서 테스트로 옮길 수 있다. 위협을 전제로 적고 거기서 요구사항을 끌어낼 때 쓴다."
  app1="It should be assumed that engineers will try paths their role does not grant and that they do not need for the task at hand; a caller should not be able to tell from an error page whether a hidden admin route exists."
  app1ko="엔지니어는 자기 역할에 부여되지 않았고 지금 맡은 일에 필요하지도 않은 경로를 시도해 볼 것이라고 전제해야 한다. 호출한 쪽은 에러 페이지만 보고 숨겨진 관리자 경로가 있는지 없는지 알아낼 수 없어야 한다."
  app2="It should be assumed that a failed deploy will be retried by hand before anyone reads the runbook; the second attempt should not be able to leave the cluster in a state the first one did not."
  app2ko="실패한 배포는 누가 런북을 읽기도 전에 손으로 다시 시도될 것이라고 전제해야 한다. 두 번째 시도가 첫 번째 시도라면 만들지 않았을 상태를 클러스터에 남길 수 있어서는 안 된다."
>}}

{{< sentence
  en="Wherever possible, any external interface should default to denying requests, with specific permitted requests and actions placed on an allow list."
  ko="가능한 모든 곳에서 외부 인터페이스는 기본적으로 요청을 거부해야 하며, 구체적으로 허용된 요청과 동작만 허용 목록에 올린다."
  source="NeMo Guardrails Docs · Security Guidelines, Prefer allow-lists and fail-closed"
  sourceURL="https://github.com/NVIDIA/NeMo-Guardrails/blob/main/docs/resources/security/guidelines.mdx"
  note="`Wherever possible, X should default to <거부>, with <예외> placed on an allow list.` — 규칙의 **기본값과 예외 경로를 한 문장에 같이** 담는 문형이다. `default to`가 이 문장의 무게를 다 지고 있다. '거부하라'가 아니라 '아무것도 정해지지 않았을 때 거부로 떨어져라'는 뜻이어서, 빠뜨린 경우까지 규칙이 덮는다. `Wherever possible`은 예외를 미리 인정하는 완충인데, 바로 뒤에 허용 목록이라는 구체적 장치가 붙어 있어 빠져나갈 구멍으로 읽히지 않는다. `with ~ placed on`이라는 수동태는 **누가 올리는지를 흐리면서** 절차의 존재만 남기므로, 담당자가 아직 정해지지 않은 단계에서도 쓸 수 있다. 권한·네트워크·기능 플래그의 기본값을 정하는 문장으로 쓴다."
  app1="Wherever possible, a new service account should default to reading nothing, with the specific buckets and tables it needs placed on an allow list reviewed at each release."
  app1ko="가능한 모든 곳에서 새 서비스 계정은 기본적으로 아무것도 읽지 못해야 하며, 그 계정에 필요한 버킷과 테이블만 릴리스마다 검토되는 허용 목록에 올린다."
  app2="Wherever possible, an agent should default to refusing tool calls it was not configured for, with the specific tools and argument shapes placed on an allow list."
  app2ko="가능한 모든 곳에서 에이전트는 설정되지 않은 도구 호출을 기본적으로 거부해야 하며, 허용되는 도구와 인수 형태만 허용 목록에 올린다."
>}}

{{< sentence
  en="Integrating LLMs with external resources is inherently an exercise in API security. When designing these interfaces, early and timely involvement with security experts can reduce the risk associated with these interfaces as well as speed development."
  ko="LLM을 외부 자원과 통합하는 일은 본질적으로 API 보안을 하는 일이다. 이런 인터페이스를 설계할 때 보안 전문가를 이르게, 때맞춰 참여시키면 인터페이스에 따르는 위험을 줄일 수 있고 개발 속도도 높일 수 있다."
  source="NeMo Guardrails Docs · Security Guidelines, Engage with security teams proactively"
  sourceURL="https://github.com/NVIDIA/NeMo-Guardrails/blob/main/docs/resources/security/guidelines.mdx"
  note="`X is inherently an exercise in Y.` + `can reduce <위험> as well as speed <상대가 아끼는 것>.` — 낯선 일을 **이미 다들 아는 분야의 일로 되돌려 놓는** 문형이다. `an exercise in Y`는 'Y와 비슷하다'가 아니라 'Y를 하는 것이다'라서, 그 분야의 기존 절차와 사람을 그대로 끌어올 근거가 된다. 새로 규칙을 만들자는 말보다 반발이 적다. 뒤 문장은 설득의 정석이다. 이익을 두 개 대는데 하나(`reduce the risk`)는 내 관심사이고 다른 하나(`speed development`)는 **거절할 사람의 관심사**다. `as well as`가 둘을 대등하게 묶어 놓기 때문에, 보안 검토가 속도의 대가가 아니라 속도의 수단으로 읽힌다. 새 작업을 기존 리뷰 절차 안으로 넣자고 제안할 때 쓴다."
  app1="Reviewing a prompt template is inherently an exercise in input validation. Bringing in the people who own the parser early can reduce the escaping bugs we ship as well as shorten review."
  app1ko="프롬프트 템플릿을 리뷰하는 일은 본질적으로 입력 검증을 하는 일이다. 파서를 맡은 사람을 일찍 불러들이면 우리가 내보내는 이스케이프 버그를 줄일 수 있고 리뷰도 짧아진다."
  app2="Writing a migration runbook is inherently an exercise in incident response. Walking it through with the on-call engineer before the change window can reduce the time we spend deciding during an outage as well as cut the number of rollback steps."
  app2ko="마이그레이션 런북을 쓰는 일은 본질적으로 장애 대응을 하는 일이다. 변경 작업 전에 온콜 엔지니어와 함께 훑어 보면 장애 중에 판단하느라 쓰는 시간을 줄일 수 있고 롤백 단계 수도 줄일 수 있다."
>}}
