---
title: 도구가 못 하는 일을 먼저 말하는 표현
description: 기능을 말한 뒤 보증을 거두고, 범주를 바꿔 기대를 되돌리고, 빠진 기능이 결정임을 밝히고, 애쓴 뒤에도 남는 한계를 양보로 남기고, 두 방향의 실패를 트레이드오프로 세우는 문장 5개.
weight: -50
date: 2026-10-10
source: "Presidio · FAQ"
sourceURL: https://data-privacy-stack.github.io/presidio/faq/
---

# 도구가 못 하는 일을 먼저 말하는 표현

텍스트와 이미지에서 개인정보(PII)를 찾아 가리는 오픈소스 라이브러리 Presidio의 공식 FAQ다.
무엇을 탐지하는지보다 **무엇을 보장하지 않는지**에 지면을 많이 쓴 문서라서 골랐다. 자동
탐지의 한계, 일부러 넣지 않은 인증 기능, 오탐과 미탐 사이의 균형을 변명처럼 들리지 않게
적어 둔 문장들이다. 도구나 지표를 소개하면서 그 사정거리를 같이 못 박아야 할 때 —
보안 스캐너 결과를 보고할 때, 자동화의 적용 범위를 적을 때, 대시보드 숫자를 인용할 때 —
그대로 틀을 가져다 쓸 수 있다.

> **원문** — Presidio 기여자들, *Frequently Asked Questions (FAQ)*,
> [data-privacy-stack/presidio](https://github.com/data-privacy-stack/presidio/blob/main/docs/faq.md)
> (문서 사이트: [Presidio FAQ](https://data-privacy-stack.github.io/presidio/faq/)),
> [MIT](https://github.com/data-privacy-stack/presidio/blob/main/LICENSE) 라이선스.
>
> 영어 문장은 원문 그대로 인용했고, 한글 설명과 응용 문장은 이 노트에서 새로 쓴 것이다.

{{< sentence
  en="Presidio can help identify sensitive/PII data in un/structured text. However, because it is using automated detection mechanisms, there is no guarantee that Presidio will find all sensitive information. Consequently, additional systems and protections should be employed."
  ko="Presidio는 비정형·정형 텍스트에서 민감정보와 개인정보를 식별하는 데 도움이 될 수 있다. 다만 자동 탐지 방식을 쓰기 때문에, 모든 민감정보를 찾아낸다는 보장은 없다. 따라서 추가적인 시스템과 보호 수단을 함께 두어야 한다."
  source="Presidio FAQ · What is Presidio?"
  sourceURL="https://data-privacy-stack.github.io/presidio/faq/"
  note="`X can help do A. However, because ..., there is no guarantee that .... Consequently, ....` — 기능을 말하고, 보증을 거두고, 그래서 무엇을 더 해야 하는지까지 세 문장에 나눠 담는 틀이다. 첫 문장이 `detects`가 아니라 `can help identify`인 게 핵심이다. 처음부터 **거들 뿐**이라고 범위를 깎아 두면 두 번째 문장의 `no guarantee`가 번복이 아니라 예고된 결론으로 읽힌다. `because it is using ~`은 한계의 **원인을 방식 자체**에 돌려서 이번 버전의 결함이 아니라 접근법의 성질임을 알린다. 마지막 `Consequently ... should be employed`는 수동태라 누구 책임인지 지목하지 않고 할 일만 남긴다 — 책임을 떠넘긴다는 인상 없이 상대에게 넘기고 싶을 때 쓴다."
  app1="Static analysis can help surface injection risks in the service. However, because it only reasons about code paths it can see, there is no guarantee that it will flag every unsafe query. Consequently, manual review of the data layer should remain in the release checklist."
  app1ko="정적 분석은 서비스의 인젝션 위험을 드러내는 데 도움이 될 수 있다. 다만 눈에 보이는 코드 경로만 따지기 때문에, 위험한 쿼리를 모두 집어낸다는 보장은 없다. 따라서 데이터 계층의 수동 리뷰는 릴리스 체크리스트에 남겨 두어야 한다."
  app2="The dashboard can help spot the regression early. However, because it samples one request in a hundred, there is no guarantee that a rare failure will show up at all. Consequently, error budgets should be read together with the raw logs."
  app2ko="대시보드는 회귀를 일찍 발견하는 데 도움이 될 수 있다. 다만 100건 중 1건만 표본으로 잡기 때문에, 드문 실패가 드러난다는 보장은 아예 없다. 따라서 에러 예산은 원본 로그와 함께 읽어야 한다."
>}}

{{< sentence
  en="Presidio is a library or SDK rather than a service. It is meant to be customized to the user's or organization's specific needs."
  ko="Presidio는 서비스가 아니라 라이브러리 또는 SDK다. 사용자나 조직의 구체적인 필요에 맞춰 커스터마이즈해 쓰도록 만든 것이다."
  source="Presidio FAQ · What is Presidio?"
  sourceURL="https://data-privacy-stack.github.io/presidio/faq/"
  note="`A is X rather than Y. It is meant to be ....` — 상대가 잘못 넣어 둔 **범주를 바꿔 기대를 되돌리는** 문형이다. `rather than`은 `not`과 달리 Y를 틀렸다고 하지 않고 분류만 교체하므로, 상대가 반박당한 기분 없이 기대를 수정한다. 뒤이은 `It is meant to be ~`가 결정적이다. 지금 그렇다는 서술이 아니라 **그렇게 쓰도록 만들어진 것**이라는 설계 의도라, 손이 더 간다는 말이 결함이 아니라 전제가 된다. 바로 쓸 수 있는 완제품을 기대하고 온 상대에게 그렇지 않다고 말할 때 꺼낸다."
  app1="The runbook is a decision aid rather than a script. It is meant to be adapted to whatever the on-call engineer actually sees in the graphs."
  app1ko="런북은 스크립트가 아니라 판단을 돕는 자료다. 당직자가 그래프에서 실제로 보는 것에 맞춰 바꿔 쓰도록 만든 것이다."
  app2="This review is a second opinion rather than an approval gate. It is meant to be weighed against the context only the owning team has."
  app2ko="이 리뷰는 승인 관문이 아니라 두 번째 의견이다. 담당 팀만 아는 맥락과 견주어 보도록 만든 것이다."
>}}

{{< sentence
  en="Presidio API endpoints do not include built-in authentication by design. The containers are intentionally kept lean to allow flexibility for different deployment scenarios."
  ko="Presidio의 API 엔드포인트에는 인증 기능이 설계상 들어 있지 않다. 컨테이너를 의도적으로 가볍게 유지해 여러 배포 상황에 맞출 여지를 둔 것이다."
  source="Presidio FAQ · Deployment"
  sourceURL="https://data-privacy-stack.github.io/presidio/faq/"
  note="`X does not include Y by design. ... is intentionally kept lean to allow ....` — 빠진 기능이 **누락이 아니라 결정**임을 밝히는 문형이다. 문장 끝에 붙은 `by design` 두 단어가 앞 절 전체의 성격을 바꾼다. 그것 없이 `does not include`만 쓰면 미완성 고백이 되고, 붙이면 선택이 된다. 그다음 문장이 왜 그런지를 대는데, `intentionally kept lean`은 비워 둔 것을 **절제**로 읽히게 하고 `to allow flexibility for ~`는 그 빈자리의 수혜자가 쓰는 사람임을 말한다. 기능 요청을 거절할 때, 또는 우리 쪽에서 안 하는 일을 상대 쪽 할 일로 넘길 때 쓴다."
  app1="The ingestion service does not include retries by design. The client libraries are intentionally kept thin to allow each team to pick a backoff policy that fits its own latency budget."
  app1ko="인그레스트 서비스에는 재시도가 설계상 들어 있지 않다. 클라이언트 라이브러리를 의도적으로 얇게 유지해, 각 팀이 자기 지연 예산에 맞는 백오프 정책을 고를 수 있게 한 것이다."
  app2="The alert does not include an automatic rollback by design. The runbook is intentionally kept short to allow the on-call engineer to judge whether the deploy is actually the cause."
  app2ko="이 알림에는 자동 롤백이 설계상 들어 있지 않다. 런북을 의도적으로 짧게 유지해, 당직자가 정말 배포가 원인인지 판단할 수 있게 한 것이다."
>}}

{{< sentence
  en="While Presidio leverages context words and other logic to improve the detection quality, it could still falsely detect non-entity values as PII entities."
  ko="Presidio는 문맥 단어와 그 밖의 로직을 활용해 탐지 품질을 끌어올리지만, 그래도 개인정보가 아닌 값을 개인정보로 잘못 탐지할 수 있다."
  source="Presidio FAQ · False Positives"
  sourceURL="https://data-privacy-stack.github.io/presidio/faq/"
  note="`While X does A to improve B, it could still C.` — 애쓴 것을 먼저 인정하고 그래도 남는 한계를 뒤에 두는 양보 구문이다. `While` 절에 **우리가 한 일**을 넣으면 뒤의 고백이 손 놓고 있었다는 말로 읽히지 않는다. 무게는 `still`에 실린다. `could C`만 쓰면 단순 가능성이지만 `could still C`는 **대책을 쓴 뒤에도 남는** 잔여 위험이 되어, 더 해 보라는 요구를 미리 막는다. `it could`의 조동사도 일부러 약한 것을 골랐다 — `will`이면 결함 보고가 되고, `could`면 알려진 한계가 된다. 완화 대책을 설명한 직후, 그래도 남는 오차를 적을 때 쓴다."
  app1="While the pipeline deduplicates alerts by fingerprint and suppresses known flapping, it could still page two engineers for the same root cause."
  app1ko="파이프라인은 지문으로 알림을 중복 제거하고 알려진 플래핑을 억제하지만, 그래도 같은 근본 원인으로 두 명을 호출할 수 있다."
  app2="While the audit script cross-checks each grant against the ticket that requested it, it could still miss access that was granted outside the normal process."
  app2ko="감사 스크립트는 권한 하나하나를 그것을 요청한 티켓과 교차 확인하지만, 그래도 정상 절차 밖에서 부여된 접근 권한은 놓칠 수 있다."
>}}

{{< sentence
  en="Every PII identification logic would have its errors, and there is a trade-off between false positives (falsely detected text) and false negatives (PII entities which are not detected)."
  ko="개인정보 식별 로직에는 어느 것이나 오류가 있고, 오탐(잘못 탐지된 텍스트)과 미탐(탐지되지 않은 개인정보) 사이에는 트레이드오프가 있다."
  source="Presidio FAQ · False Positives"
  sourceURL="https://data-privacy-stack.github.io/presidio/faq/"
  note="`Every X would have its errors, and there is a trade-off between A (...) and B (...).` — 우리 구현의 결함을 **그 부류 전체의 성질**로 끌어올려 놓고, 이어서 두 방향의 실패를 대립쌍으로 세우는 문형이다. `Every X would have ~`의 `would`는 미래가 아니라 일반 법칙을 가리키는 쓰임으로, 측정값 없이도 성립하는 진술이 된다. 두 번째 절이 하는 일은 더 중요하다. 오차를 **줄일 양**이 아니라 **고를 방향**으로 바꿔 놓으면, 다음 대화가 왜 틀렸느냐가 아니라 어느 쪽으로 틀리는 편이 나으냐가 된다. 괄호로 용어를 그 자리에서 풀어 주는 것도 그대로 쓸 만하다 — 각주로 빼지 않고 문장 안에서 해결한다."
  app1="Every threshold on this alert would have its errors, and there is a trade-off between noise (pages nobody acts on) and silence (incidents nobody sees until a customer calls)."
  app1ko="이 알림의 임계값은 어떻게 잡아도 오류가 있고, 소음(아무도 대응하지 않는 호출)과 침묵(고객이 전화할 때까지 아무도 모르는 장애) 사이에는 트레이드오프가 있다."
  app2="Every review policy would have its costs, and there is a trade-off between blocking on one owner (slow merges) and allowing any approver (changes nobody with context has read)."
  app2ko="리뷰 정책은 어떻게 잡아도 비용이 있고, 담당자 한 명을 반드시 기다리는 것(느린 머지)과 누구든 승인하게 두는 것(맥락을 아는 사람이 아무도 읽지 않은 변경) 사이에는 트레이드오프가 있다."
>}}
