---
title: 설계 결정을 기록으로 남기는 표현
description: 반복되는 제안을 기각하는 문형, 의무와 권고를 갈라 적는 삽입구, 하나씩 풀기보다 애초에 피한 이유, 어떤 조치가 없애는 것의 열거, 산출물의 지위를 깎아서 공개하는 고지 — 설계 판단을 글로 남길 때 쓰는 문장 5개.
weight: -45
date: 2026-10-05
source: "CloudEvents · Primer"
sourceURL: https://github.com/cloudevents/spec/blob/main/cloudevents/primer.md
---

# 설계 결정을 기록으로 남기는 표현

CloudEvents 스펙의 비규범(non-normative) 부록. 스펙 본문이 기술 세부만 다루도록,
"왜 그렇게 정했는가"와 "왜 그건 안 넣었는가"를 따로 모아 둔 문서다. 그래서 설계
리뷰에서 반복되는 제안을 기각하고, 의무와 권고를 구별하고, 어떤 산출물의 지위를
미리 깎아 두는 문장이 빽빽하다. 결정을 글로 남겨야 하는 사람에게 그대로 쓸 틀이
많아 발췌했다.

> **원문** — CloudEvents Authors, *CloudEvents Primer*,
> [cloudevents/spec](https://github.com/cloudevents/spec/blob/main/cloudevents/primer.md)
> (CNCF), [Apache License 2.0](https://github.com/cloudevents/spec/blob/main/LICENSE)
> — Copyright 2018 CloudEvents Authors.
>
> 영어 문장은 원문 그대로 인용했고, 한글 설명과 응용 문장은 이 노트에서 새로 쓴 것이다.

{{< sentence
  en="This is a common suggestion by those new to the concepts of CloudEvents. After much deliberation, the working group has come to the conclusion that routing is unnecessary in the spec: any protocol (e.g. HTTP, MQTT, XMPP, or a Pub/Sub bus) already defines semantics for routing."
  ko="이것은 CloudEvents 개념을 처음 접한 사람들이 흔히 하는 제안이다. 오랜 논의를 거쳐 워킹 그룹은 라우팅이 스펙에 필요하지 않다는 결론에 이르렀다. 어떤 프로토콜이든(예: HTTP, MQTT, XMPP, 혹은 Pub/Sub 버스) 이미 라우팅 의미를 정의하고 있기 때문이다."
  source="CloudEvents Primer · Non-Goals"
  sourceURL="https://github.com/cloudevents/spec/blob/main/cloudevents/primer.md#non-goals"
  note="`This is a common suggestion by those new to X. After much deliberation, <주체> has come to the conclusion that Y: Z already defines ...` — **반복되는 제안을 기각하면서 제안자를 깎지 않는** 문형. 첫 문장이 제안을 틀렸다고 하지 않고 `a common suggestion by those new to`로 **분류**한다. 그러면 거절이 그 사람에 대한 평가가 아니라 '처음 오면 누구나 하는 질문'의 처리로 읽힌다. `After much deliberation`은 즉답이 아니라 이미 소진된 논의라는 신호여서, 같은 제안을 다시 들고 오는 비용을 미리 올려 둔다. 결정적인 부분은 콜론 뒤다 — 근거가 '우리는 안 한다'가 아니라 `already defines`, 즉 **다른 층이 이미 하고 있다**는 사실이다. 설계 리뷰 기록, FAQ, ADR의 기각 항목에 그대로 쓴다."
  app1="This is a common request from those new to our on-call rotation. After much deliberation, the platform team has come to the conclusion that per-service paging rules are unnecessary in the alert config: the routing tree already defines an owner for every alert."
  app1ko="이것은 우리 온콜 로테이션에 처음 들어온 사람들이 흔히 하는 요청이다. 오랜 논의를 거쳐 플랫폼 팀은 서비스별 호출 규칙이 알림 설정에 필요하지 않다는 결론에 이르렀다. 라우팅 트리가 이미 모든 알림의 담당자를 정의하고 있기 때문이다."
  app2="This is a common suggestion from those new to the review checklist. After much deliberation, we have come to the conclusion that a separate security sign-off is unnecessary for dependency bumps: the deploy pipeline already blocks any image with a critical CVE."
  app2ko="이것은 리뷰 체크리스트를 처음 보는 사람들이 흔히 하는 제안이다. 오랜 논의를 거쳐 우리는 의존성 버전 올리기에 별도의 보안 승인이 필요하지 않다는 결론에 이르렀다. 배포 파이프라인이 이미 치명적 CVE가 있는 이미지를 막고 있기 때문이다."
>}}

{{< sentence
  en="It is important to note that constraints such as these, where they are not mandated via a &quot;MUST&quot;, are recommendations to increase the likelihood of interoperability between multiple implementations and deployments."
  ko="이런 제약들은, MUST로 의무화되지 않은 경우, 여러 구현과 배포 사이의 상호운용 가능성을 높이기 위한 권고임을 유념해야 한다."
  source="CloudEvents Primer · Interoperability Constraints"
  sourceURL="https://github.com/cloudevents/spec/blob/main/cloudevents/primer.md#interoperability-constraints"
  note="`X, where they are not mandated via a &quot;MUST&quot;, are recommendations to increase the likelihood of Y.` — 한 문서 안에 섞여 있는 **의무와 권고를 갈라 주는** 문형. 요령은 조건을 삽입구로 문장 **중간에** 끼우는 것이다. `Constraints are recommendations unless mandated via a MUST`처럼 뒤로 빼면 조건이 예외처럼 들리는데, 쉼표 두 개로 가둬 두면 '어느 것이 의무인지 보는 법'이 주어의 일부가 된다. 그리고 권고를 권고로만 두지 않고 `recommendations to increase the likelihood of Y`로 **목적까지** 적는다. `increase the likelihood of`는 보장이 아니라 확률을 올린다는 정직한 표현이라, 안 지켰을 때 무엇이 흔들리는지가 드러난다. 체크리스트, 코딩 규약, 운영 표준을 쓸 때 첫 단락에 놓는 문장이다."
  app1="It is important to note that the items on this checklist, where they are not enforced by a blocking check, are recommendations to increase the likelihood of a clean rollback."
  app1ko="이 체크리스트의 항목들은, 차단 검사로 강제되지 않는 경우, 깔끔한 롤백의 가능성을 높이기 위한 권고임을 유념해야 한다."
  app2="It is important to note that naming conventions such as these, where they are not enforced by the linter, are recommendations to increase the likelihood of a reviewer finding the right file on the first try."
  app2ko="이런 네이밍 규칙들은, 린터로 강제되지 않는 경우, 리뷰어가 첫 시도에 맞는 파일을 찾을 가능성을 높이기 위한 권고임을 유념해야 한다."
>}}

{{< sentence
  en="While it might be possible to define clear rules for how to solve each of the potential problems that arise, the authors decided that it would be better to simply avoid all of them in the first place by only having one location in the serialization for unknown, or even new, properties."
  ko="생길 수 있는 문제들을 각각 어떻게 풀지 명확한 규칙을 정하는 것도 가능하겠지만, 저자들은 직렬화에서 알려지지 않은 속성 — 심지어 새로 생긴 속성까지 — 이 놓일 자리를 하나로만 두어 그 문제들을 애초에 전부 피하는 편이 낫다고 판단했다."
  source="CloudEvents Primer · JSON Extensions"
  sourceURL="https://github.com/cloudevents/spec/blob/main/cloudevents/primer.md#json-extensions"
  note="`While it might be possible to define clear rules for how to solve each of A, we decided that it would be better to simply avoid all of them in the first place by B.` — **하나씩 대응하는 안을 인정하고 나서, 문제를 없애는 구조를 고른 이유**를 적는 문형. 단순화를 주장할 때 가장 흔한 실패는 상대 안을 '그건 안 된다'로 치는 것인데, 여기서는 `it might be possible`로 가능함을 먼저 내준다. 그러면 다툼이 가능/불가능이 아니라 **비용**으로 옮겨간다. `simply`와 `in the first place`가 그 비용 차이를 한 단어씩 담당하고, 마지막 `by B`에 구조적 수단(자리를 하나로 둔다)을 박아 둔 덕분에 판단이 취향으로 읽히지 않는다. 설계 문서, 리팩터링 제안, 장애 재발 방지책에 쓴다."
  app1="While it might be possible to define clear rules for how to reconcile each of the conflicts that arise between the two caches, we decided that it would be better to simply avoid all of them in the first place by letting only one service write to that table."
  app1ko="두 캐시 사이에서 생기는 충돌들을 각각 어떻게 맞출지 명확한 규칙을 정하는 것도 가능하겠지만, 우리는 그 테이블에 쓰는 서비스를 하나로만 두어 그 충돌들을 애초에 전부 피하는 편이 낫다고 판단했다."
  app2="While it might be possible to document how to handle each of the edge cases a nullable timestamp introduces, we decided that it would be better to simply avoid all of them in the first place by making the column required at write time."
  app2ko="널 허용 타임스탬프가 만드는 경계 사례들을 각각 어떻게 다룰지 문서로 정리하는 것도 가능하겠지만, 우리는 그 컬럼을 쓰기 시점에 필수로 만들어 그 사례들을 애초에 전부 피하는 편이 낫다고 판단했다."
>}}

{{< sentence
  en="However, persisting an event removes the contextual information available during transmission such as the identity and rights of the producer, fidelity validation mechanisms, or confidentiality protections."
  ko="그러나 이벤트를 영속화하면 전송 중에는 쓸 수 있었던 문맥 정보 — 생산자의 신원과 권한, 충실성 검증 수단, 기밀성 보호 같은 것 — 가 사라진다."
  source="CloudEvents Primer · Non-Goals"
  sourceURL="https://github.com/cloudevents/spec/blob/main/cloudevents/primer.md#non-goals"
  note="`However, X removes the <정보> available during Y, such as a, b, or c.` — 어떤 조치가 **없애는 것**을 열거하는 문형. 보안·감사 맥락에서 '그건 위험하다'고 쓰면 상대가 반박할 거리가 없어 대화가 그냥 끝나 버린다. 이 문형은 대신 `removes the ... available during ...`로 **어느 시점에 있었던 무엇이 사라지는지**를 가리켜서, 상대가 '그럼 그 세 가지를 따로 남기자'로 응답할 수 있게 만든다. 요령은 `such as` 뒤 세 항목의 추상도를 맞추는 것이다 — 여기서는 신원·검증·기밀성으로 셋 다 보안 속성 층위에 있다. 감사 로그 설계, 데이터 이관, 스냅샷 복구를 설명할 때 쓴다."
  app1="However, exporting the audit trail to a flat file removes the metadata available during the request, such as the authenticated principal, the mTLS peer certificate, or the originating IP."
  app1ko="그러나 감사 기록을 단순 파일로 내보내면 요청 중에는 쓸 수 있었던 메타데이터 — 인증된 주체, mTLS 피어 인증서, 발신 IP 같은 것 — 가 사라진다."
  app2="However, replaying the queue from a snapshot removes the guarantees available during live delivery, such as per-key ordering, the original timestamps, or the deduplication window."
  app2ko="그러나 큐를 스냅샷에서 재생하면 실시간 전달 중에는 쓸 수 있었던 보장 — 키별 순서, 원래 타임스탬프, 중복 제거 구간 같은 것 — 이 사라진다."
>}}

{{< sentence
  en="Extensions which are documented in this way have no special status, and may take breaking changes (including being removed entirely). They are not part of the main versioned CloudEvents specification, and are only present as a form of collaboration."
  ko="이런 방식으로 문서화된 확장은 특별한 지위를 갖지 않으며, 호환성을 깨는 변경을 겪을 수 있다(완전히 제거되는 것까지 포함한다). 그것들은 버전이 매겨진 CloudEvents 본 스펙의 일부가 아니고, 협업의 한 형태로만 존재한다."
  source="CloudEvents Primer · CloudEvents Extension Attributes"
  sourceURL="https://github.com/cloudevents/spec/blob/main/cloudevents/primer.md#cloudevents-extension-attributes"
  note="`X have no special status, and may take breaking changes (including being removed entirely). They are not part of A, and are only present as B.` — 어떤 산출물을 공개하면서 **그 지위를 먼저 깎아 두는** 고지 문형. 사람들은 공개된 것을 곧 약속으로 읽기 때문에, 나중에 치울 수 있는 물건은 내놓는 자리에서 기대치를 낮춰야 한다. `no special status`가 그 일을 하고, 괄호 안 `including being removed entirely`는 **최악의 경우를 내 손으로 적어 두는** 장치다 — 가장 심한 가능성을 내가 먼저 말하면 나중에 그게 배신이 되지 않는다. 두 번째 문장은 `not part of A` / `only present as B`로 부정과 긍정을 한 짝으로 묶어, 뭐가 아닌지만 말하고 끝나지 않게 한다. 내부 도구, 실험용 API 필드, 임시 대시보드를 공유할 때 그대로 쓴다."
  app1="Dashboards published under the team folder have no special status, and may take breaking changes (including being deleted entirely). They are not part of the on-call runbook, and are only present as a place to try queries."
  app1ko="팀 폴더 아래에 올라간 대시보드는 특별한 지위를 갖지 않으며, 호환성을 깨는 변경을 겪을 수 있다(완전히 삭제되는 것까지 포함한다). 그것들은 온콜 런북의 일부가 아니고, 쿼리를 시험해 보는 자리로만 존재한다."
  app2="Fields added under the debug prefix have no special status, and may take breaking changes (including being removed entirely). They are not part of the public API contract, and are only present to help us read production logs."
  app2ko="debug 접두사 아래에 추가된 필드는 특별한 지위를 갖지 않으며, 호환성을 깨는 변경을 겪을 수 있다(완전히 제거되는 것까지 포함한다). 그것들은 공개 API 계약의 일부가 아니고, 운영 로그를 읽는 데 도움을 주기 위해서만 존재한다."
>}}
