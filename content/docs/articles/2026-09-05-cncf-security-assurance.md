---
title: 보장하지 않는 것을 먼저 말하는 표현
description: 문서의 사정거리를 자르고, 두 개념이 서로를 보장하지 않는다고 못 박고, 선택의 비용을 경고하는 문장 5개.
weight: -16
date: 2026-09-05
source: "CNCF Cloud Native Security Whitepaper v2"
sourceURL: https://github.com/cncf/tag-security/blob/main/community/resources/security-whitepaper/v2/cloud-native-security-whitepaper.md
---

# 보장하지 않는 것을 먼저 말하는 표현

CNCF TAG Security가 낸 *Cloud Native Security Whitepaper*는 개발·배포·운영 각 단계에
보안을 어떻게 끼워 넣을지를 CISO와 아키텍트에게 설명하는 문서다. 도구를 추천하는 문서가
아니라 **무엇이 무엇을 보장하지 않는지**를 계속 갈라 놓는 문서라서, 단정 대신 범위를 긋는
문형이 많다. 문서 자신의 사정거리를 자르는 문장, 컴플라이언스와 보안을 서로 바꿔 쓰지 말라고
못 박는 문장, 선택지를 막지 않으면서 비용만 붙이는 문장을 다섯 개 뽑았다. 설계 문서 서문,
감사 소견, ADR처럼 **결론을 좁혀서 말해야 하는 글**에 그대로 옮겨 쓸 수 있다.

> **원문** — CNCF TAG Security, *Cloud Native Security Whitepaper v2.0*,
> [github.com/cncf/tag-security](https://github.com/cncf/tag-security/blob/main/community/resources/security-whitepaper/v2/cloud-native-security-whitepaper.md)
> (2022-05-17), 문서 라이선스
> [CC BY 4.0](https://github.com/cncf/tag-security/blob/main/LICENSE.md).
>
> 영어 문장은 원문 그대로 인용했고, 한글 설명과 응용 문장은 이 노트에서 새로 쓴 것이다.

{{< sentence
  en="This document does not intend to provide general education on security concepts or cloud computing concepts. It also does not recommend specific technologies or tools; however, it may cite examples of technology or tools that address the topic discussed."
  ko="이 문서는 보안 개념이나 클라우드 컴퓨팅 개념을 일반적으로 교육하려는 것이 아니다. 특정 기술이나 도구를 추천하지도 않는다. 다만 논의되는 주제를 다루는 기술이나 도구의 예를 인용할 수는 있다."
  source="Cloud Native Security Whitepaper v2 · Cloud Native Goals"
  sourceURL="https://github.com/cncf/tag-security/blob/main/community/resources/security-whitepaper/v2/cloud-native-security-whitepaper.md"
  note="`X does not intend to A. It also does not B; however, it may C.` — 문서 첫머리에서 **사정거리를 미리 잘라 두는** 3단 구조다. `does not intend to`는 '못 한다'가 아니라 '그럴 목적이 아니다'다. 능력이 아니라 의도를 부정하기 때문에 변명처럼 들리지 않는다. `It also does not`으로 제외 항목을 하나 더 얹은 뒤, 세미콜론 다음의 `however, it may`가 좁은 예외를 남긴다. 이 예외 절이 핵심이다 — 없으면 본문에 도구 이름이 나올 때마다 독자가 앞선 선언과 모순으로 읽는다. 설계 문서·RFC·감사 보고서 서문에서 '이 문서가 답하지 않는 질문'을 적을 때 쓴다."
  app1="This runbook does not intend to explain how the payment service works. It also does not cover database failover; however, it may point to the pages that do."
  app1ko="이 런북은 결제 서비스의 동작 원리를 설명하려는 것이 아니다. 데이터베이스 페일오버도 다루지 않는다. 다만 그것을 다루는 문서를 가리킬 수는 있다."
  app2="This review does not intend to relitigate the API design. It also does not block on naming; however, it may flag names that contradict the convention we already agreed on."
  app2ko="이 리뷰는 API 설계를 다시 논쟁하려는 것이 아니다. 이름 짓기를 이유로 머지를 막지도 않는다. 다만 이미 합의한 관례와 어긋나는 이름은 짚을 수 있다."
>}}

{{< sentence
  en="Thus, compliance and security assurance are complementary processes but are not interchangeable. A compliant system is not guaranteed to be secure, nor a secure system is guaranteed to be compliant."
  ko="따라서 컴플라이언스와 보안 보증은 서로를 보완하는 과정이지만 서로 바꿔 쓸 수 있는 것은 아니다. 컴플라이언스를 통과한 시스템이 안전하다고 보장되지 않으며, 안전한 시스템이 컴플라이언스를 만족한다고 보장되지도 않는다."
  source="Cloud Native Security Whitepaper v2 · Security Assurance"
  sourceURL="https://github.com/cncf/tag-security/blob/main/community/resources/security-whitepaper/v2/cloud-native-security-whitepaper.md"
  note="자주 뒤섞이는 두 개념을 갈라 세우는 **두 문장 짝**이다. 먼저 `A and B are complementary processes but are not interchangeable.`로 관계를 규정하고, 다음 문장에서 `X is not guaranteed to be Y, nor Y ... to be X`로 **양방향을 모두** 끊는다. `complementary`가 앞에 오는 순서가 중요하다 — 한쪽을 깎아내리는 말이 아니라 역할이 다르다는 말로 읽히게 만든다. `is not guaranteed to be`는 '아니다'가 아니라 '보장되지 않는다'여서, 반례를 들이대지 않고 추론만 끊어 준다. 참고로 원문의 뒷절은 `nor a secure system is guaranteed`로 도치가 빠져 있는데(규범 문법은 `nor is a secure system guaranteed`), 인용이므로 원문 그대로 두었다. 응용 문장에서는 도치를 살렸다."
  app1="Test coverage and correctness are complementary measures but are not interchangeable. A well-covered module is not guaranteed to be correct, nor is a correct module guaranteed to be well covered."
  app1ko="테스트 커버리지와 정확성은 서로를 보완하는 척도지만 바꿔 쓸 수 있는 것은 아니다. 커버리지가 높은 모듈이 정확하다고 보장되지 않고, 정확한 모듈이 커버리지가 높다고 보장되지도 않는다."
  app2="An approved review and a safe deploy are complementary signals but are not interchangeable. An approved change is not guaranteed to be safe in production, nor is a change that shipped safely guaranteed to have been reviewed carefully."
  app2ko="리뷰 승인과 무사한 배포는 서로를 보완하는 신호지만 바꿔 쓸 수 있는 것은 아니다. 승인된 변경이 운영에서 안전하다고 보장되지 않고, 무사히 나간 변경이 꼼꼼히 리뷰됐다고 보장되지도 않는다."
>}}

{{< sentence
  en="Using an external CA may involve a non-trivial amount of work in maintaining the Certificate Authority Infrastructure, so this option should be selected with caution."
  ko="외부 CA를 쓰면 인증 기관 인프라를 유지하는 데 만만치 않은 양의 작업이 따를 수 있다. 그러므로 이 선택지는 신중하게 골라야 한다."
  source="Cloud Native Security Whitepaper v2 · Control Plane Authentication and Certificate Root of Trust"
  sourceURL="https://github.com/cncf/tag-security/blob/main/community/resources/security-whitepaper/v2/cloud-native-security-whitepaper.md"
  note="`Doing X may involve a non-trivial amount of work in Y, so this option should be selected with caution.` — 선택지를 막지 않고 **비용만 붙여 돌려주는** 문형이다. `non-trivial`은 형태상 완곡어지만 실제로는 경고다. 정확한 공수를 모를 때 숫자 대신 쓰기 좋고, 과장 없이 무게를 실어 준다. 뒤의 `should be selected with caution`은 수동태라 누구의 판단 착오도 지목하지 않는다. ADR이나 대안 비교에서 한쪽을 눌러 두되 결정권은 상대에게 남길 때."
  app1="Rolling our own retry layer may involve a non-trivial amount of work in getting idempotency right, so this option should be selected with caution."
  app1ko="재시도 계층을 직접 만들면 멱등성을 제대로 맞추는 데 만만치 않은 작업이 따를 수 있다. 그러므로 이 선택지는 신중하게 골라야 한다."
  app2="Pinning every base image to a digest may involve a non-trivial amount of work in tracking upstream security patches, so this option should be selected with caution."
  app2ko="모든 베이스 이미지를 다이제스트로 고정하면 업스트림 보안 패치를 따라가는 데 만만치 않은 작업이 따를 수 있다. 그러므로 이 선택지는 신중하게 골라야 한다."
>}}

{{< sentence
  en="Minor changes to a workload, or the infrastructure where the workload has been deployed, may have far-reaching security consequences."
  ko="워크로드에, 또는 그 워크로드가 배포된 인프라에 가하는 사소한 변경이 멀리까지 미치는 보안 결과를 낳을 수 있다."
  source="Cloud Native Security Whitepaper v2 · Code Review"
  sourceURL="https://github.com/cncf/tag-security/blob/main/community/resources/security-whitepaper/v2/cloud-native-security-whitepaper.md"
  note="`Minor changes to X may have far-reaching Y consequences.` — 원인의 크기와 결과의 크기를 **일부러 어긋나게 놓는** 문장이다. `minor`와 `far-reaching`이 한 문장 안에서 맞부딪히면서, 근거를 대지 않고도 '작아 보인다고 넘기지 말라'는 요구가 선다. 이런 문장은 대개 절차(리뷰, 2인 승인)를 도입하기 직전에 놓인다 — 귀찮은 절차가 왜 필요한지를 한 줄로 정당화하기 때문이다. 삽입구 `or the infrastructure where ~`로 대상 범위를 슬쩍 넓히는 것도 같이 훔칠 만하다."
  app1="Minor changes to a feature flag, or the config service that serves it, may have far-reaching availability consequences."
  app1ko="피처 플래그에, 또는 그 플래그를 내려 주는 설정 서비스에 가하는 사소한 변경이 멀리까지 미치는 가용성 결과를 낳을 수 있다."
  app2="Minor changes to an IAM policy may have far-reaching blast-radius consequences, so we review them with the same weight as schema migrations."
  app2ko="IAM 정책의 사소한 변경이 폭발 반경에 멀리까지 미치는 결과를 낳을 수 있다. 그래서 우리는 스키마 마이그레이션과 같은 무게로 리뷰한다."
>}}

{{< sentence
  en="Immediate forwarding of logs to a location inaccessible via cluster-level credentials also defeats an attacker's attempt to cover their tracks by disabling logs or deleting their activity logs."
  ko="클러스터 수준 자격 증명으로는 접근할 수 없는 곳으로 로그를 즉시 전달해 두면, 로그를 끄거나 활동 기록을 지워 흔적을 덮으려는 공격자의 시도까지 무력화된다."
  source="Cloud Native Security Whitepaper v2 · Audit Log Analysis"
  sourceURL="https://github.com/cncf/tag-security/blob/main/community/resources/security-whitepaper/v2/cloud-native-security-whitepaper.md"
  note="`X defeats an attacker's attempt to A by B.` — 통제를 설명할 때 '무엇을 막는다'가 아니라 **어떤 수법을 헛되게 만든다**고 적는 방식이다. 공격자의 행동을 `attempt to A`(무엇을 노리고) + `by B`(어떤 수단으로)까지 쪼개 놓기 때문에, 읽는 사람이 이 통제가 공격의 어느 단계에서 작동하는지 알 수 있다. `defeats`는 `prevents`보다 '이미 시작된 시도를 무산시킨다'는 쪽이다. 주어 자리의 긴 명사구(`Immediate forwarding of logs to ~`)는 통제 하나를 통째로 이름 붙여 앉히는 흔한 방식이니 함께 익혀 둔다."
  app1="Writing the deploy history to an append-only store defeats an attacker's attempt to hide a rollout by editing the release record afterwards."
  app1ko="배포 이력을 추가만 가능한 저장소에 남겨 두면, 나중에 릴리스 기록을 고쳐 롤아웃을 숨기려는 시도가 무력화된다."
  app2="Requiring a second approver on production access defeats an insider's attempt to widen their own permissions by filing and approving their own request."
  app2ko="운영 접근에 두 번째 승인자를 두면, 자기 요청을 올려 스스로 승인하는 식으로 권한을 넓히려는 내부자의 시도가 무력화된다."
>}}
