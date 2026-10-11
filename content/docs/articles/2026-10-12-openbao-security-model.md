---
title: 신뢰하지 않겠다고 설계로 적는 표현
description: 신뢰하지 않음을 설계 전제로 선언하고, 공격자의 능력으로 범위를 끊고, 규칙에 이름을 붙인 뒤 조건문으로 다시 적고, 같은 사고를 조건으로 분류하고, 설계가 무엇을 면하게 해 주는지 말하는 문장 5개.
weight: -52
date: 2026-10-12
source: "OpenBao Docs · Security model"
sourceURL: https://openbao.org/docs/internals/security/
---

# 신뢰하지 않겠다고 설계로 적는 표현

비밀 관리 시스템 OpenBao(HashiCorp Vault의 MPL 라이선스 포크)의 공식 문서 중 보안 모델
페이지다. 무엇을 위협 모델에 넣고 무엇을 범위 밖으로 빼는지, 클라이언트·서버·스토리지
사이에 어떤 신뢰 관계를 전제하는지, 루트 키를 왜 쪼개 두는지를 적어 둔 문서다. 암호 기술
자체보다 **신뢰 경계를 말하는 말투**가 배울 점이라 골랐다 — 신뢰하지 않는다는 말을 불안이
아니라 설계로 적고, 못 막는 것을 변명 없이 먼저 적고, 규칙은 이름과 판정 절차 두 벌로 적는다.
보안 설계 문서를 쓸 때, 감사에서 범위를 잘라 적을 때, 리뷰에서 사람에 대한 신뢰를 전제로
돌아가는 절차를 지적할 때 그대로 틀을 가져다 쓸 수 있다.

> **원문** — HashiCorp, Inc. 및 OpenBao Contributors, *Security model*,
> [openbao/openbao](https://github.com/openbao/openbao/blob/main/website/content/docs/internals/security.mdx)
> (문서 사이트: [OpenBao Docs — Security model](https://openbao.org/docs/internals/security/)),
> [MPL-2.0](https://github.com/openbao/openbao/blob/main/LICENSE) 라이선스.
>
> 영어 문장은 원문 그대로 인용했고, 한글 설명과 응용 문장은 이 노트에서 새로 쓴 것이다.

{{< sentence
  en="The storage backends used by OpenBao are also untrusted by design. OpenBao uses a security barrier for all requests made to the backend."
  ko="OpenBao가 쓰는 스토리지 백엔드 역시 설계상 신뢰하지 않는다. OpenBao는 백엔드로 가는 모든 요청에 보안 장벽을 둔다."
  source="OpenBao Docs · External threat overview"
  sourceURL="https://openbao.org/docs/internals/security/"
  note="`X is untrusted by design.` — 신뢰하지 않는다는 말을 미비점이 아니라 **설계 전제**로 선언하는 문장이다. `by design` 세 글자가 방향을 바꾼다. `we do not trust the storage backend`라고 쓰면 운영자의 태도가 되고, 신뢰할 수 있게 만들라는 요구를 부른다. `untrusted by design`은 신뢰하지 않는 상태를 시스템의 속성으로 못 박아 그 요구 자체를 논점에서 뺀다. 두 번째 문장이 반드시 붙어야 한다는 점도 훔칠 부분이다 — 신뢰하지 않는다고만 적으면 불안만 남고, 바로 그 자리에서 대신 무엇을 두는지(`uses a security barrier for all requests`)를 적어야 선언이 설계가 된다. 앞의 `also`는 이미 클라이언트와 서버 사이에도 상호 신뢰가 없다고 적어 둔 것을 이어받는다. 신뢰 경계를 그려 보일 때, 내가 통제하지 못하는 구성 요소를 전제에서 빼 둘 때 쓴다."
  app1="The queue consumers are untrusted by design. Every message is validated against the schema again before it reaches the handler."
  app1ko="큐 소비자는 설계상 신뢰하지 않는다. 모든 메시지는 핸들러에 닿기 전에 스키마로 한 번 더 검증된다."
  app2="Values coming from the CI environment are untrusted by design. The deploy script reads every secret from the secret store itself before it runs."
  app2ko="CI 환경에서 넘어온 값은 설계상 신뢰하지 않는다. 배포 스크립트는 실행 전에 모든 비밀값을 비밀 저장소에서 직접 읽는다."
>}}

{{< sentence
  en="An attacker that can perform arbitrary operations against the storage backend can undermine security in any number of ways that are difficult or impossible to protect against."
  ko="스토리지 백엔드에 임의의 작업을 할 수 있는 공격자는, 막기 어렵거나 불가능한 수많은 방식으로 보안을 무너뜨릴 수 있다."
  source="OpenBao Docs · Threat model — Out of Scope"
  sourceURL="https://openbao.org/docs/internals/security/"
  note="`An attacker that can X can undermine Y in any number of ways that are difficult or impossible to protect against.` — 위협 모델에서 **무엇을 안 막는지**를 적는 문장이다. 범위를 빼는 근거를 의지(안 하기로 했다)에 두지 않고 **공격자에게 이미 주어진 능력**에 둔다. 전제인 `that can perform arbitrary operations`가 과한 권한을 이미 품고 있어서, 그 뒤의 방어가 무의미하다는 결론이 저절로 따라온다. `in any number of ways`는 경로를 하나하나 열거하지 않고도 열거가 끝나지 않는다는 말을 확보하는 표현이다 — 목록을 적는 쪽이 오히려 약하다. 빠진 항목을 지적받기 때문이다. `difficult or impossible`은 둘을 나란히 적어 과장을 피한다. 전부 불가능하다고 하면 반례 하나에 무너지지만, 이렇게 쓰면 버티는 주장이 된다. 감사 보고서나 설계 문서에서 범위 밖을 적을 때 그대로."
  app1="An attacker that can edit the pipeline definition can bypass the review gate in any number of ways that are difficult or impossible to protect against."
  app1ko="파이프라인 정의를 고칠 수 있는 공격자는, 막기 어렵거나 불가능한 수많은 방식으로 리뷰 게이트를 우회할 수 있다."
  app2="A caller that can set its own tenant ID can read rows that belong to other tenants in any number of ways that are difficult or impossible to protect against."
  app2ko="테넌트 ID를 스스로 지정할 수 있는 호출자는, 막기 어렵거나 불가능한 수많은 방식으로 다른 테넌트의 레코드를 읽을 수 있다."
>}}

{{< sentence
  en="OpenBao uses a strict default deny enforcement strategy. This means unless an associated policy allows for a given action, it will be denied."
  ko="OpenBao는 엄격한 기본 거부 집행 전략을 쓴다. 연결된 정책이 그 동작을 허용하지 않는 한 거부된다는 뜻이다."
  source="OpenBao Docs · Internal threat overview"
  sourceURL="https://openbao.org/docs/internals/security/"
  note="규칙에 이름을 붙인 뒤 `This means unless X, Y.`로 **같은 규칙을 판정 절차로 다시 적는** 2단 구조다. 첫 문장의 `default deny`는 외우기 쉬운 이름이지만 경계가 흐리고, 두 번째 문장은 분쟁이 생겼을 때 그대로 대입할 수 있는 절차다. 둘 중 하나만 적으면 글이 약해진다 — 이름만 적으면 해석이 갈리고, 절차만 적으면 기억에 남지 않는다. `unless`가 입증 책임을 뒤집는 것이 이 문형의 핵심이다. 거부하는 쪽이 이유를 대는 것이 아니라, 허용을 가리키는 정책을 내놓는 쪽이 말해야 한다. 수동태 `it will be denied`도 의도적이다 — 누가 거부했느냐를 지우고 규칙이 거부한 것으로 만들어, 담당자와의 실랑이를 애초에 막는다. 용어를 도입했으면 다음 문장에서 꼭 풀어 적는 습관으로 쓸 수 있다."
  app1="The merge check is fail closed. This means unless a required reviewer has approved the change, the merge button stays disabled."
  app1ko="머지 검사는 실패 시 차단으로 동작한다. 필수 리뷰어가 변경을 승인하지 않는 한 머지 버튼은 비활성 상태로 남는다는 뜻이다."
  app2="Egress from the cluster is default deny. This means unless a host appears in the allowlist, the request never leaves the node."
  app2ko="클러스터 외부로 나가는 트래픽은 기본 거부다. 허용 목록에 호스트가 올라 있지 않는 한 요청은 노드를 벗어나지 못한다는 뜻이다."
>}}

{{< sentence
  en="Within the OpenBao system, a critical security concern is an attacker attempting to gain access to secret material they are not authorized to. This is an internal threat if the attacker is already permitted to some level of access to OpenBao, and is able to authenticate."
  ko="OpenBao 시스템 안에서 중대한 보안 우려는, 권한이 없는 비밀 자료에 접근하려는 공격자다. 공격자가 이미 어느 수준의 접근 권한을 받았고 인증까지 통과할 수 있다면, 이는 내부 위협이다."
  source="OpenBao Docs · Internal threat overview"
  sourceURL="https://openbao.org/docs/internals/security/"
  note="`This is an X if A, and B.` — 같은 사고를 **조건으로 분류하는** 문장이다. 벌어진 일(권한 없는 비밀에 접근하려는 시도)은 하나인데, 공격자가 이미 안에 들어와 있느냐에 따라 이름이 내부 위협으로 달라진다. 분류를 심각도 같은 주관적 느낌이 아니라 확인 가능한 조건 두 개에 걸어 두었고, `and`로 묶어 둘 다 성립해야 한다는 것을 분명히 했다. 도입부도 그대로 쓸 만하다. `Within the X system,`으로 시야를 먼저 좁혀 두면 이어지는 단정이 전체에 대한 주장으로 읽히지 않는다. `a critical security concern is an attacker attempting to ~`처럼 사람이 아니라 **시도**를 주어 자리에 놓는 것도 의도적이다 — 누가 그랬는지 가려지지 않은 단계에서 행위만 가리켜 말할 수 있다. 장애·보안 사고를 등급별로 갈라 적을 때, 사후 보고서에서 같은 현상을 다른 이름으로 분류할 때 쓴다."
  app1="This is an insider incident if the actor already had a valid session, and the action falls inside the permissions we granted them."
  app1ko="행위자가 이미 유효한 세션을 갖고 있었고 그 동작이 우리가 부여한 권한 안에 들어온다면, 이는 내부자 사고다."
  app2="This is a regression if the same test passed on the previous commit, and the input has not changed since."
  app2ko="같은 테스트가 이전 커밋에서는 통과했고 그 뒤로 입력이 바뀌지 않았다면, 이는 회귀다."
>}}

{{< sentence
  en="By using a secret sharing technique, we avoid the need to place absolute trust in the holder of the root key, and avoid storing the root key at all."
  ko="비밀 분할 기법을 쓰면 루트 키 보관자를 절대적으로 신뢰할 필요가 없어지고, 루트 키를 아예 저장하지 않게 된다."
  source="OpenBao Docs · Internal threat overview"
  sourceURL="https://openbao.org/docs/internals/security/"
  note="`By using X, we avoid the need to Y, and avoid Z at all.` — 설계를 **무엇을 할 수 있게 되는지**가 아니라 **무엇을 면하게 되는지**로 설명하는 문장이다. `avoid the need to place absolute trust in ~`이 통제를 넣는 말투를 바꿔 놓는다. 보관자를 의심한다고 말하지 않고, 신뢰를 요구하지 않는 구조를 만들었다고 말한다 — 사람을 깎지 않으면서 사람에 대한 의존을 없앴다는 뜻이 된다. 통제를 제안할 때 상대가 방어적으로 나오는 이유는 대개 의심받았다고 느끼기 때문인데, 이 표현은 그 지점을 비켜 간다. 뒤의 `and avoid storing the root key at all`에서 `at all`은 부분적인 완화가 아니라 보관이라는 행위 자체가 사라졌다는 것을 분명히 한다. 설계 결정을 설명할 때, 리뷰에서 특정인에 대한 신뢰를 전제로 돌아가는 절차를 지적할 때 그대로."
  app1="By rotating the token on every deploy, we avoid the need to trust that the old one was never copied, and avoid keeping long-lived credentials at all."
  app1ko="배포마다 토큰을 교체하면 예전 토큰이 복사되지 않았다고 믿을 필요가 없어지고, 수명이 긴 자격 증명을 아예 두지 않게 된다."
  app2="By rebuilding the timeline from the audit log, we avoid the need to rely on anyone's recollection of the order of events, and avoid hand-edited spreadsheets at all."
  app2ko="감사 로그에서 타임라인을 다시 만들면 사건 순서에 대한 누군가의 기억에 의존할 필요가 없어지고, 손으로 고친 스프레드시트를 아예 쓰지 않게 된다."
>}}
