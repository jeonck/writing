---
title: 책임지는 범위를 먼저 긋는 표현
description: 적용 대상 밖을 먼저 잘라 내고, 기본값이 안전하지 않다고 자기 입으로 말하고, 예외를 이름표로 도려내고, 신뢰의 사정거리를 끊기는 지점까지 쪼개고, 가정에 고지 의무를 붙이는 문장 5개.
weight: -29
date: 2026-09-18
source: "Envoy Proxy Documentation — Threat model"
sourceURL: https://www.envoyproxy.io/docs/envoy/latest/intro/arch_overview/security/threat_model
---

# 책임지는 범위를 먼저 긋는 표현

Envoy 프록시 공식 문서의 *Threat model* 장은 **무엇을 보안 취약점으로 볼 것인가**를 정하는
문서다. 눈에 띄는 것은 분량의 대부분이 무엇을 막겠다가 아니라 **어디까지가 우리 책임인가**를
적는 데 쓰인다는 점이다. 적용 대상 밖을 먼저 도려내고, 자기 기본 설정이 안전하지 않다고 자기
입으로 밝히고, 무엇을 신뢰하는지와 그 신뢰가 어디서 끊기는지를 따로 적는다. 그래서 이 문서에는
범위를 좁히면서도 발뺌으로 읽히지 않는 문형이 모여 있다 — 좁히는 근거를 판단이 아니라 **표시나
조건**에 걸어 두기 때문이다. 보안 감사 회신, 지원 범위 공지, 온콜 정책, 아키텍처 문서에 그대로
옮겨 쓸 다섯 문장을 골랐다.

> **원문** — The Envoy Project Authors, *Threat model*,
> [Envoy Proxy Documentation](https://www.envoyproxy.io/docs/envoy/latest/intro/arch_overview/security/threat_model)
> (원본: [`envoyproxy/envoy` · `docs/root/intro/arch_overview/security/threat_model.rst`](https://github.com/envoyproxy/envoy/blob/main/docs/root/intro/arch_overview/security/threat_model.rst)),
> [Apache-2.0](https://github.com/envoyproxy/envoy/blob/main/LICENSE).
> Copyright The Envoy Project Authors.
>
> 영어 문장은 원문 그대로 인용했고, 한글 설명과 응용 문장은 이 노트에서 새로 쓴 것이다.

{{< sentence
  en="Issues that do not affect Envoy in published release configurations are not covered by the threat model and will not be considered security issues."
  ko="공개된 릴리스 구성에서 Envoy에 영향을 주지 않는 문제는 이 위협 모델의 적용 대상이 아니며, 보안 문제로 취급되지 않는다."
  source="Envoy Threat model · Build configurations"
  sourceURL="https://www.envoyproxy.io/docs/envoy/latest/intro/arch_overview/security/threat_model"
  note="`X that do not affect A in B are not covered by C and will not be considered D.` — 적용 대상 밖을 먼저 도려내는 문형이다. 주어가 사람이 아니라 **문제 자체**(`Issues that ...`)라서, 누가 잘못 제보했다는 말이 한 글자도 들어가지 않는다. 거르는 기준은 `in published release configurations` — 우리가 실제로 내보내는 구성에서 재현되느냐라는 **검사 가능한 조건**이지 중요도에 대한 판단이 아니다. 뒤가 두 겹인 것도 눈여겨볼 만하다: `not covered by`는 이 문서의 사정거리를 말하고, `will not be considered`는 앞으로도 그렇게 다루지 않겠다는 **대응 의사**를 말한다. 문서 범위만 말하고 끝내면 그럼 다른 경로로 봐 달라는 요청이 남는데, 두 번째 절이 그 여지를 닫는다. 보안 제보를 분류할 때, 감사 범위를 회신할 때, 버그를 릴리스 대상에서 뺄 때 쓴다."
  app1="Findings that do not reproduce in the configuration we actually deploy are not covered by this review and will not be considered release blockers."
  app1ko="우리가 실제로 배포하는 구성에서 재현되지 않는 지적은 이번 검토의 적용 대상이 아니며, 릴리스 중단 사유로 취급되지 않는다."
  app2="Alerts that do not affect a user-facing path are not covered by the paging policy and will not be considered incidents."
  app2ko="사용자에게 닿는 경로에 영향을 주지 않는 알림은 호출 정책의 적용 대상이 아니며, 장애로 취급되지 않는다."
>}}

{{< sentence
  en="Note that we do not currently consider the default settings for Envoy to be safe from an availability perspective."
  ko="다만 우리는 현재 Envoy의 기본 설정이 가용성 관점에서 안전하다고 보지 않는다는 점에 유의하라."
  source="Envoy Threat model · Confidentiality, integrity and availability"
  sourceURL="https://www.envoyproxy.io/docs/envoy/latest/intro/arch_overview/security/threat_model"
  note="`Note that we do not currently consider X to be safe from a Y perspective.` — 자기 쪽 기본값이 안전하지 않다고 **먼저 말해 버리는** 문형이다. 이런 문장은 보통 쓰기 어려운데, 세 장치가 그것을 가능하게 만든다. `currently`는 시점을 박아 영구 결함이 아니라 **지금 상태**로 만들고, `from a Y perspective`는 축을 하나로 좁혀 전면 부정으로 번지지 않게 막는다(가용성 얘기지 기밀성 얘기가 아니다). `we do not consider ~ to be safe`는 안전하지 않다고 단정하는 대신 **안전하다고 보증하지 않는다**는 쪽이라, 상대가 확인해야 할 몫을 그대로 남겨 둔다. 인수인계에서 기본 설정 그대로 쓰지 말라고 알릴 때, 예시 설정이 운영 기준이 아님을 밝힐 때 쓴다."
  app1="Note that we do not currently consider the default retry settings to be safe from a load perspective."
  app1ko="다만 우리는 현재 기본 재시도 설정이 부하 관점에서 안전하다고 보지 않는다는 점에 유의하라."
  app2="Note that we do not currently consider the sample configuration in the README to be safe from a multi-tenancy perspective."
  app2ko="다만 우리는 현재 README의 예시 설정이 멀티테넌시 관점에서 안전하다고 보지 않는다는 점에 유의하라."
>}}

{{< sentence
  en="Anything in the Envoy core may be used in both untrusted and trusted deployments, with the exception of features explicitly marked as alpha; alpha features are only supported in trusted deployments and do not qualify for treatment under the threat model below."
  ko="Envoy 코어에 있는 것은 신뢰할 수 없는 배포 환경과 신뢰할 수 있는 배포 환경 양쪽에서 쓸 수 있다. 다만 알파로 명시적으로 표시된 기능은 예외다. 알파 기능은 신뢰할 수 있는 배포 환경에서만 지원되며, 아래 위협 모델의 처리 대상이 될 자격이 없다."
  source="Envoy Threat model · Core and extensions"
  sourceURL="https://www.envoyproxy.io/docs/envoy/latest/intro/arch_overview/security/threat_model"
  note="`Anything in X may be used in both A and B, with the exception of Y explicitly marked as Z; Y is only supported in A and does not qualify for treatment under C.` — 먼저 전부 열어 준 다음 예외를 **이름표로 도려내는** 문형이다. 순서가 핵심이다. 허용을 앞에 두면 문장 전체가 제한이 아니라 보장으로 읽히고, 예외는 그 보장에서 빠지는 목록이 된다. `explicitly marked as`가 예외의 정의를 **표시**에 걸어 둔 것도 중요하다 — 알파인지 아닌지를 대화로 다투지 않고 기능에 붙은 표식 하나로 끝내기 때문에, 경계선이 사람마다 달라지지 않는다. 마지막 절은 예외의 처지를 두 갈래로 나눠 적는다: `only supported in`은 **써도 되는 곳**, `do not qualify for treatment under`는 **받을 수 있는 대우**. 하나만 적으면 반드시 나머지를 묻는 질문이 돌아온다. 실험 기능의 지원 범위를 공지할 때, 사내 플랫폼의 보증 범위를 나눌 때 쓴다."
  app1="Anything in the shared platform may be used in both customer-facing and internal services, with the exception of modules explicitly marked as experimental; experimental modules are only supported in internal services and do not qualify for treatment under the on-call policy below."
  app1ko="공용 플랫폼에 있는 것은 고객에게 노출되는 서비스와 내부 서비스 양쪽에서 쓸 수 있다. 다만 실험 단계로 명시적으로 표시된 모듈은 예외다. 실험 모듈은 내부 서비스에서만 지원되며, 아래 온콜 정책의 처리 대상이 될 자격이 없다."
  app2="Anything in the reporting warehouse may be used in both audited and exploratory analyses, with the exception of views explicitly marked as draft; draft views are only supported in exploratory analyses and do not qualify for treatment under the sign-off process below."
  app2ko="리포팅 웨어하우스에 있는 것은 감사 대상 분석과 탐색용 분석 양쪽에서 쓸 수 있다. 다만 초안으로 명시적으로 표시된 뷰는 예외다. 초안 뷰는 탐색용 분석에서만 지원되며, 아래 승인 절차의 처리 대상이 될 자격이 없다."
>}}

{{< sentence
  en="The control plane management server is generally trusted. We do not consider wire-level exploits against the xDS transport protocol to be a concern as a result. However, the configuration delivered to Envoy over xDS may originate from untrusted sources and may not be fully sanitized."
  ko="컨트롤 플레인 관리 서버는 일반적으로 신뢰한다. 그 결과로 xDS 전송 프로토콜을 겨냥한 전송 계층 익스플로잇은 우려 대상으로 보지 않는다. 그러나 xDS를 통해 Envoy에 전달되는 설정은 신뢰할 수 없는 출처에서 왔을 수 있고, 완전히 정화되지 않았을 수 있다."
  source="Envoy Threat model · Data and control plane"
  sourceURL="https://www.envoyproxy.io/docs/envoy/latest/intro/arch_overview/security/threat_model"
  note="`X is generally trusted. We do not consider A to be a concern as a result. However, what X delivers may originate from untrusted sources and may not be fully sanitized.` — 신뢰의 **사정거리가 어디서 끊기는지**를 세 문장으로 나눠 적는 문형이다. 첫 문장은 신뢰를 선언하고, 둘째 문장의 `as a result`는 그 신뢰에서 **무엇을 안 보기로 했는지**를 결론으로 꺼내 놓는다. 이 연결을 드러내 두면 나중에 전제가 바뀌었을 때 무엇을 다시 봐야 하는지가 문서에 남는다. 진짜 일은 `However`가 한다 — 신뢰가 걸려 있는 것은 **경로**(누가 보냈나)이고, 그 경로로 오는 **내용**(무엇이 담겼나)은 신뢰 대상이 아니라는 절단이다. 뒤의 두 `may`도 각각 다른 곳을 짚는다: `may originate from`은 출처, `may not be fully sanitized`는 상태. 내부망이니 괜찮다는 말을 받을 때, 사내 시스템이 외부 입력을 중계하고 있을 때 꺼내 쓴다."
  app1="The build server is generally trusted. We do not consider a forged webhook against the pipeline endpoint to be a concern as a result. However, the manifests the pipeline applies may originate from untrusted forks and may not be fully reviewed."
  app1ko="빌드 서버는 일반적으로 신뢰한다. 그 결과로 파이프라인 엔드포인트를 겨냥한 위조 웹훅은 우려 대상으로 보지 않는다. 그러나 파이프라인이 적용하는 매니페스트는 신뢰할 수 없는 포크에서 왔을 수 있고, 완전히 검토되지 않았을 수 있다."
  app2="The internal network is generally trusted. We do not consider packet-level tampering between our services to be a concern as a result. However, the payloads one service forwards to another may originate from public uploads and may not be fully sanitized."
  app2ko="내부 네트워크는 일반적으로 신뢰한다. 그 결과로 우리 서비스들 사이의 패킷 단위 변조는 우려 대상으로 보지 않는다. 그러나 한 서비스가 다른 서비스로 넘기는 페이로드는 공개 업로드에서 왔을 수 있고, 완전히 정화되지 않았을 수 있다."
>}}

{{< sentence
  en="We generally assume that services utilized for side calls during the request processing, e.g. external authorization, credential suppliers, rate limit services, are trusted. When this is not the case, an extension will explicitly state this in its documentation."
  ko="요청 처리 중에 부수적으로 호출하는 서비스들, 예컨대 외부 인가, 자격 증명 공급자, 레이트 리밋 서비스는 일반적으로 신뢰한다고 가정한다. 그렇지 않은 경우에는 해당 익스텐션이 자기 문서에 그 사실을 명시한다."
  source="Envoy Threat model · Data and control plane"
  sourceURL="https://www.envoyproxy.io/docs/envoy/latest/intro/arch_overview/security/threat_model"
  note="`We generally assume that X, e.g. A, B, C, are trusted. When this is not the case, Y will explicitly state this in its documentation.` — 가정을 적고, 그 **가정이 깨질 때 누가 어디에 적을지**를 같은 자리에서 정해 두는 문형이다. `generally`는 예외를 미리 인정하는 단어라 가정을 절대 명제로 만들지 않고, `e.g.` 뒤의 나열은 추상적인 가정에 **확인할 수 있는 이름**을 붙여 읽는 사람이 자기 시스템을 대조해 볼 수 있게 한다. 뒷문장이 이 문형의 값어치다: 예외가 있을 수 있다에서 끝내지 않고 `will explicitly state this in its documentation`으로 **고지 의무의 주체와 장소**를 지정한다. 그래서 나중에 예외가 드러나도 누가 말했어야 했는지를 두고 다툴 일이 없다. 아키텍처 문서의 전제를 적을 때, 런북에서 의존 대상의 신뢰 수준을 밝힐 때, 리뷰에서 이 코드가 뭘 믿고 있느냐고 물을 때 쓴다."
  app1="We generally assume that the systems we call during a deploy, e.g. the artifact registry, the secret store, the feature flag service, are trusted. When this is not the case, a runbook will explicitly state this in its rollback section."
  app1ko="배포 중에 호출하는 시스템들, 예컨대 아티팩트 레지스트리, 시크릿 저장소, 기능 플래그 서비스는 일반적으로 신뢰한다고 가정한다. 그렇지 않은 경우에는 런북이 롤백 절에 그 사실을 명시한다."
  app2="We generally assume that the inputs handled inside a worker, e.g. queue payloads, cached documents, retried jobs, are already validated. When this is not the case, the handler will explicitly state this in its docstring."
  app2ko="워커 안에서 다루는 입력들, 예컨대 큐 페이로드, 캐시된 문서, 재시도된 작업은 이미 검증되었다고 일반적으로 가정한다. 그렇지 않은 경우에는 해당 핸들러가 독스트링에 그 사실을 명시한다."
>}}
