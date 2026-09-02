---
title: 원인을 묻지 않고 위험을 정의하는 표현
description: 원인과 무관하게 취약점을 정의하고, 옆 개념과 선을 긋고, 치웠다고 믿었던 것이 남아 있다고 지적하는 문장 5개.
weight: -14
date: 2026-09-03
source: "OWASP Top 10 for LLM Applications — LLM06:2025 Excessive Agency"
sourceURL: https://github.com/OWASP/www-project-top-10-for-large-language-model-applications/blob/main/2_0_vulns/LLM06_ExcessiveAgency.md
---

# 원인을 묻지 않고 위험을 정의하는 표현

OWASP의 LLM 애플리케이션 Top 10 중 여섯 번째 항목 'Excessive Agency'는 LLM에게 넘긴
도구 호출 권한이 어디까지 위험해지는지를 다룬다. 원인 규명을 미뤄 둔 채 위험을 정의하고,
비슷한 항목과 관할을 나누고, 남아 있는 권한을 비난 없이 지적하는 문형이 많아 발췌했다.

> **원문** — OWASP GenAI Security Project, *LLM06:2025 Excessive Agency*,
> [OWASP Top 10 for LLM Applications 2.0](https://github.com/OWASP/www-project-top-10-for-large-language-model-applications/blob/main/2_0_vulns/LLM06_ExcessiveAgency.md),
> [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) 라이선스.
>
> 영어 문장은 원문 그대로 인용했고, 한글 설명과 응용 문장은 이 노트에서 새로 쓴 것이다.

{{< sentence
  en="Excessive Agency is the vulnerability that enables damaging actions to be performed in response to unexpected, ambiguous or manipulated outputs from an LLM, regardless of what is causing the LLM to malfunction."
  ko="과도한 행위 권한은 LLM이 왜 오작동하는지와 무관하게, LLM의 예상 밖 출력·모호한 출력·조작된 출력에 반응해 피해를 주는 행동이 실행되도록 만드는 취약점이다."
  source="OWASP LLM Top 10 · LLM06 Description"
  sourceURL="https://github.com/OWASP/www-project-top-10-for-large-language-model-applications/blob/main/2_0_vulns/LLM06_ExcessiveAgency.md"
  note="`X is the vulnerability that enables A, regardless of what is causing B.` — 정의에서 **원인을 의도적으로 빼는** 구문이다. `enables ~ to be performed`라는 수동태가 '누가 했는지'를 지우고, 그런 일이 벌어질 수 있는 **상태 자체**를 취약점으로 만든다. `regardless of what is causing`은 원인 논쟁(모델이 헛것을 본 건가, 공격을 받은 건가)을 통째로 괄호 밖으로 밀어낸다. 원인 규명이 끝나기 전에 위험을 먼저 정의해야 할 때 그대로 쓴다. 형용사 셋을 나열한 `unexpected, ambiguous or manipulated`도 조건의 범위를 넓히는 장치다."
  app1="The outage risk here is the deploy path that lets an unreviewed change reach production, regardless of what is causing the review to be skipped."
  app1ko="여기서의 장애 위험은 리뷰가 왜 생략되는지와 무관하게, 리뷰를 거치지 않은 변경이 운영에 도달하도록 열려 있는 배포 경로다."
  app2="The finding is the permission that allows a shared account to delete audit logs, regardless of who is using the account."
  app2ko="이번 지적 사항은 그 계정을 누가 쓰는지와 무관하게, 공용 계정이 감사 로그를 지울 수 있게 열려 있는 권한이다."
>}}

{{< sentence
  en="Note: Excessive Agency differs from Insecure Output Handling which is concerned with insufficient scrutiny of LLM outputs."
  ko="참고: 과도한 행위 권한은 안전하지 않은 출력 처리와 다르다. 후자는 LLM 출력을 충분히 검사하지 않는 문제를 다룬다."
  source="OWASP LLM Top 10 · LLM06 Description"
  sourceURL="https://github.com/OWASP/www-project-top-10-for-large-language-model-applications/blob/main/2_0_vulns/LLM06_ExcessiveAgency.md"
  note="`A differs from B which is concerned with C.` — 헷갈리기 쉬운 **옆 개념과 선을 긋는** 한 문장이다. 새 개념을 설명한 직후 `Note:`로 짧게 끼워 넣는 **위치**가 절반이다. 미리 끊어 두지 않으면 독자가 둘을 섞어 읽는다. `is concerned with`는 상대 개념을 깎지 않고 '그쪽이 다루는 범위는 여기까지'라고 **관할만 나눈다**. 리뷰나 감사에서 '그건 다른 항목입니다'를 각 세우지 않고 말할 때."
  app1="Note: this alert differs from the saturation alert which is concerned with sustained load rather than a single spike."
  app1ko="참고: 이 알림은 포화 알림과 다르다. 포화 알림은 한 번의 급증이 아니라 지속되는 부하를 다룬다."
  app2="Access review differs from key rotation which is concerned with how long a credential stays valid."
  app2ko="접근 권한 검토는 키 교체와 다르다. 키 교체는 자격 증명이 얼마나 오래 유효한 채로 남아 있는지를 다룬다."
>}}

{{< sentence
  en="Excessive Agency can lead to a broad range of impacts across the confidentiality, integrity and availability spectrum, and is dependent on which systems an LLM-based app is able to interact with."
  ko="과도한 행위 권한은 기밀성·무결성·가용성 전 영역에 걸쳐 넓은 범위의 영향을 낳을 수 있고, 그 영향은 LLM 기반 앱이 어떤 시스템과 상호작용할 수 있느냐에 달려 있다."
  source="OWASP LLM Top 10 · LLM06 Description"
  sourceURL="https://github.com/OWASP/www-project-top-10-for-large-language-model-applications/blob/main/2_0_vulns/LLM06_ExcessiveAgency.md"
  note="`X can lead to a broad range of impacts across A, and is dependent on B.` — 앞절에서 영향의 범위를 크게 벌려 놓고, 뒷절에서 그 크기가 **무엇에 달렸는지** 조건을 붙이는 두 겹 구조다. 겁만 주는 문장으로 끝나지 않게 만드는 것이 `is dependent on ~`이다: 범위는 넓지만 실제 크기는 연결된 시스템이 정한다. 영향도 평가를 쓸 때 **최대치와 결정 요인**을 한 문장에 담는 틀."
  app1="A leaked deploy token can lead to a broad range of impacts across build, release and rollback, and is dependent on which environments the token is scoped to."
  app1ko="배포 토큰이 유출되면 빌드·릴리스·롤백 전반에 걸쳐 넓은 범위의 영향이 생길 수 있고, 그 크기는 그 토큰이 어떤 환경까지 유효한지에 달려 있다."
  app2="The migration can lead to a broad range of impacts across latency, cost and on-call load, and is dependent on how much traffic we shift in the first week."
  app2ko="이번 마이그레이션은 지연 시간·비용·온콜 부담 전반에 걸쳐 넓은 범위의 영향을 낳을 수 있고, 그 크기는 첫 주에 트래픽을 얼마나 옮기느냐에 달려 있다."
>}}

{{< sentence
  en="An extension may have been trialled during a development phase and dropped in favor of a better alternative, but the original plugin remains available to the LLM agent."
  ko="어떤 확장은 개발 단계에서 시험 삼아 써 보다가 더 나은 대안이 나와 버려졌을 수 있지만, 원래의 플러그인은 여전히 LLM 에이전트가 쓸 수 있는 상태로 남아 있다."
  source="OWASP LLM Top 10 · Common Examples of Risks"
  sourceURL="https://github.com/OWASP/www-project-top-10-for-large-language-model-applications/blob/main/2_0_vulns/LLM06_ExcessiveAgency.md"
  note="`X may have been A and B, but Y remains available.` — 과거 추정형 `may have been`으로 '그때 치웠을 것이다'라는 **우리의 믿음**을 먼저 적어 준 뒤, `but ~ remains`로 현재 상태를 들이대는 구조다. 비난 대신 **시간차**를 보여 주기 때문에 지적이 부드럽다. `dropped in favor of a better alternative`는 그 결정이 옳았다는 것까지 인정해 준다 — 잘못은 결정이 아니라 **정리가 안 된 것**이다. 남아 있는 권한·엔드포인트·피처 플래그를 지적할 때 쓴다."
  app1="The old admin endpoint may have been added for a one-off migration and forgotten after it shipped, but it remains reachable from the public load balancer."
  app1ko="그 관리자 엔드포인트는 일회성 마이그레이션을 위해 추가됐다가 배포 뒤 잊혔을 수 있지만, 지금도 공개 로드밸런서에서 접근이 된다."
  app2="The contractor's account may have been created for last year's audit and closed out in the tracker, but the access key remains active."
  app2ko="그 외주 계정은 작년 감사 때 만들어졌고 트래커에서는 종료 처리됐을 수 있지만, 액세스 키는 여전히 살아 있다."
>}}

{{< sentence
  en="Implement authorization in downstream systems rather than relying on an LLM to decide if an action is allowed or not."
  ko="어떤 행동이 허용되는지를 LLM이 판단하게 두지 말고, 인가는 하위 시스템에서 구현하라."
  source="OWASP LLM Top 10 · Prevention and Mitigation Strategies"
  sourceURL="https://github.com/OWASP/www-project-top-10-for-large-language-model-applications/blob/main/2_0_vulns/LLM06_ExcessiveAgency.md"
  note="`Implement X rather than relying on Y to decide ~` — **판단의 자리를 옮기라는** 권고문이다. `rather than relying on`은 상대가 무능하다고 말하지 않고 '거기에 기대는 구조'만 문제 삼는다. 명령문 + `rather than -ing` 조합은 대안을 주절에, 폐기할 방식을 뒤 부사구에 두어 읽는 사람이 **할 일을 먼저** 보게 만든다. 설계 리뷰에서 '그건 앞단이 알아서 걸러 줍니다'를 반박할 때."
  app1="Enforce the quota in the gateway rather than relying on each client to respect the documented limit."
  app1ko="문서에 적힌 한도를 클라이언트가 알아서 지켜 주기를 기대하지 말고, 쿼터는 게이트웨이에서 강제하라."
  app2="Validate the schema at ingestion rather than relying on the dashboard to reveal that a field went missing."
  app2ko="필드가 사라진 것을 대시보드가 드러내 주기를 기대하지 말고, 스키마는 수집 시점에 검증하라."
>}}
