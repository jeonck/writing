---
title: 보장의 범위와 시점을 갈라 적는 표현
description: 적용 대상 밖을 같은 문장에서 잘라 내고, 강한 단어의 세기를 낮춰 정의하고, 결국 그렇게 되지만 언제인지는 알 수 없다고 말하는 문장 5개.
weight: -41
date: 2026-10-01
source: "Kubernetes Docs · Network Policies"
sourceURL: https://kubernetes.io/docs/concepts/services-networking/network-policies/
---

# 보장의 범위와 시점을 갈라 적는 표현

파드 사이의 통신을 어디까지 제어할 수 있는지를 다룬 쿠버네티스 공식 문서. 규칙을 설명하는 문서인데도
**그 규칙이 닿지 않는 곳**과 **보장이 언제 실현되는지 알 수 없다는 사실**을 같은 문단에서 꺼내 적는
문형이 많아 발췌했다. 정책을 공지하거나 비동기 처리의 한계를 설명할 때 그대로 옮겨 쓸 수 있는 틀이다.

> **원문** — Kubernetes 문서 기여자, *Network Policies*,
> [Kubernetes Documentation](https://kubernetes.io/docs/concepts/services-networking/network-policies/),
> [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) 라이선스.
> 라이선스(리포지터리 `LICENSE` = Attribution 4.0 International)와 발췌는 이 문서의 원본인
> [kubernetes/website 리포지터리](https://github.com/kubernetes/website/blob/main/content/en/docs/concepts/services-networking/network-policies.md)에서
> 직접 확인했다 (2026-10-01 확인).
>
> 영어 문장은 원문 그대로 인용했고, 한글 설명과 응용 문장은 이 노트에서 새로 쓴 것이다.

{{< sentence
  en="NetworkPolicies apply to a connection with a pod on one or both ends, and are not relevant to other connections."
  ko="네트워크폴리시는 한쪽 끝이나 양쪽 끝에 파드가 있는 연결에 적용되며, 그 밖의 연결과는 무관하다."
  source="Kubernetes Docs · Network Policies"
  sourceURL="https://kubernetes.io/docs/concepts/services-networking/network-policies/"
  note="`X applies to A, and is not relevant to B.` — 적용 대상을 말하는 그 문장 안에서 **대상 밖까지 같이 잘라 내는** 형태다. 앞 절만 쓰면 읽는 사람은 나머지도 어느 정도는 보호된다고 믿는데, `and are not relevant to`가 그 여지를 없앤다. `are not applied to`(적용되지 않는다)보다 한 단계 강한 말이라는 게 핵심 — 그 영역에서는 아예 판단 근거가 되지 않는다는 뜻이다. `on one or both ends`처럼 **경계가 걸쳐 있을 때 조건을 세는 방식**도 그대로 훔칠 만하다. 규칙·도구·정책의 적용 범위를 공지할 때 첫 문장으로 세운다."
  app1="The rate limiter applies to requests that carry an API token on either end, and is not relevant to internal service-to-service calls."
  app1ko="이 레이트 리미터는 어느 한쪽 끝에 API 토큰이 실린 요청에 적용되며, 내부 서비스 간 호출과는 무관하다."
  app2="This runbook applies to incidents that page the on-call engineer, and is not relevant to tickets filed during business hours."
  app2ko="이 런북은 온콜 담당자를 호출한 장애에 적용되며, 업무 시간에 접수된 티켓과는 무관하다."
>}}

{{< sentence
  en="&quot;Isolation&quot; here is not absolute, rather it means &quot;some restrictions apply&quot;."
  ko="여기서 말하는 '격리'는 절대적인 것이 아니라 '일부 제한이 적용된다'는 뜻이다."
  source="Kubernetes Docs · Network Policies · The two sorts of pod isolation"
  sourceURL="https://kubernetes.io/docs/concepts/services-networking/network-policies/"
  note="`X here is not absolute, rather it means Y.` — 쓰고 있는 단어를 바꾸지 않고 **세기만 낮춰 다시 정의하는** 문형이다. 셋이 각각 일을 한다: `here`가 '일반적인 뜻이 아니라 이 문서 안에서는'이라고 범위를 걸고, `not absolute`가 독자가 기대할 최대 해석을 먼저 꺾고, `rather it means`가 실제 크기를 그 자리에 앉힌다. 격리·차단·검증·승인처럼 **이미 굳어 버린 강한 단어**를 쓸 수밖에 없을 때, 용어를 새로 만드는 대신 이 한 줄로 기대치를 맞춰 둔다."
  app1="'Verified' here is not absolute, rather it means 'the signature matched a key we already trusted'."
  app1ko="여기서 말하는 '검증됨'은 절대적인 것이 아니라 '이미 신뢰하던 키와 서명이 일치했다'는 뜻이다."
  app2="'Approved' here is not absolute, rather it means 'no reviewer objected within two business days'."
  app2ko="여기서 말하는 '승인됨'은 절대적인 것이 아니라 '영업일 이틀 안에 아무 리뷰어도 이견을 내지 않았다'는 뜻이다."
>}}

{{< sentence
  en="For a connection from a source pod to a destination pod to be allowed, both the egress policy on the source pod and the ingress policy on the destination pod need to allow the connection. If either side does not allow the connection, it will not happen."
  ko="출발 파드에서 목적 파드로 가는 연결이 허용되려면, 출발 파드의 이그레스 정책과 목적 파드의 인그레스 정책이 모두 그 연결을 허용해야 한다. 어느 한쪽이라도 허용하지 않으면 그 연결은 일어나지 않는다."
  source="Kubernetes Docs · Network Policies · The two sorts of pod isolation"
  sourceURL="https://kubernetes.io/docs/concepts/services-networking/network-policies/"
  note="`For X to be allowed, both A and B need to ... If either side does not ..., it will not happen.` — 두 조건이 **함께** 충족돼야 함을 말한 뒤, 같은 규칙을 곧바로 반대쪽에서 한 번 더 적는 구조다. `both A and B`만 써 두면 독자는 '대체로 그렇다'로 받아들이는데, 뒤 문장의 `If either side does not`이 예외 없음을 못 박는다. 마무리를 `it will be denied`가 아니라 **주체 없는 `it will not happen`**으로 둔 것도 의도적이다 — 누가 막았느냐를 따지는 대화로 흐르지 않고, 조건이 안 맞으면 그냥 성립하지 않는다는 사실만 남는다. 이중 승인, 게이트 두 개짜리 배포를 설명할 때 그대로 쓴다."
  app1="For a release to go out, both the security review and the on-call sign-off need to approve it. If either side does not approve, the release will not happen."
  app1ko="릴리스가 나가려면 보안 리뷰와 온콜 승인이 모두 그것을 승인해야 한다. 어느 한쪽이라도 승인하지 않으면 릴리스는 일어나지 않는다."
  app2="For a schema change to land, both the migration test and the rollback test need to pass. If either one does not pass, the merge will not happen."
  app2ko="스키마 변경이 반영되려면 마이그레이션 테스트와 롤백 테스트가 모두 통과해야 한다. 어느 한쪽이라도 통과하지 않으면 머지는 일어나지 않는다."
>}}

{{< sentence
  en="Every created NetworkPolicy will be handled by a network plugin eventually, but there is no way to tell from the Kubernetes API when exactly that happens."
  ko="생성된 모든 네트워크폴리시는 결국 네트워크 플러그인이 처리하지만, 그 처리가 정확히 언제 일어나는지는 쿠버네티스 API로 알 길이 없다."
  source="Kubernetes Docs · Network Policies · Pod lifecycle"
  sourceURL="https://kubernetes.io/docs/concepts/services-networking/network-policies/"
  note="`X will happen eventually, but there is no way to tell from Y when exactly that happens.` — **결과는 보장하되 시점은 보장하지 않는다**를 한 문장에 담는 형태다. 앞 절의 `eventually`가 최종 수렴을 약속해 신뢰를 남기고, 뒤 절이 그 시점을 볼 수단이 없다고 잘라 낸다. 여기서 `we don't know`가 아니라 `there is no way to tell from Y`인 것이 중요하다 — 담당자의 무지가 아니라 **인터페이스의 한계**로 읽히기 때문에 '그럼 좀 알아봐 달라'는 요청이 따라붙지 않는다. 비동기 반영, 전파 지연, 캐시 무효화를 공지할 때의 표준형."
  app1="Every revoked token will be rejected at the edge eventually, but there is no way to tell from the dashboard when exactly that happens."
  app1ko="폐기된 모든 토큰은 결국 엣지에서 거부되지만, 그 거부가 정확히 언제부터인지는 대시보드로 알 길이 없다."
  app2="Every merged config change will reach all regions eventually, but there is no way to tell from the deploy log when exactly that happens."
  app2ko="머지된 모든 설정 변경은 결국 모든 리전에 도달하지만, 그 도달이 정확히 언제인지는 배포 로그로 알 길이 없다."
>}}

{{< sentence
  en="Because the network plugin may implement NetworkPolicy in a distributed manner, it is possible that pods may see a slightly inconsistent view of network policies when the pod is first created, or when pods or policies change."
  ko="네트워크 플러그인이 네트워크폴리시를 분산된 방식으로 구현할 수 있기 때문에, 파드가 처음 생성될 때나 파드 또는 정책이 바뀔 때 파드가 정책을 조금씩 다르게 볼 수 있다."
  source="Kubernetes Docs · Network Policies · Pod lifecycle"
  sourceURL="https://kubernetes.io/docs/concepts/services-networking/network-policies/"
  note="`Because A, it is possible that X may see a slightly inconsistent view of Y when B.` — 원인을 `Because` 절로 **먼저** 세워 두면, 뒤따라오는 불일치가 버그 보고가 아니라 구조에서 따라 나온 결과로 읽힌다. 순서를 뒤집어 불일치부터 말하면 곧바로 '언제 고치나'가 되니 이 순서를 지킨다. `it is possible that ~ may`는 완화가 두 번 겹친 군더더기 같지만, '반드시 그렇다'도 '드물다'도 아닌 **가능성만** 선언해야 하는 자리에서 실제로 쓰인다. `a slightly inconsistent view`는 `slightly`로 크기를 미리 재 두어 독자가 과하게 놀라지 않게 하는 장치다. 롤아웃 중, 복제 지연 중의 상태를 설명할 때."
  app1="Because the feature flag service caches decisions per node, it is possible that users may see a slightly inconsistent view of the new checkout flow during a rollout."
  app1ko="기능 플래그 서비스가 노드별로 판단을 캐시하기 때문에, 롤아웃 중에는 사용자가 새 결제 흐름을 조금씩 다르게 볼 수 있다."
  app2="Because the audit log is shipped per region, it is possible that reviewers may see a slightly inconsistent view of the incident timeline while the incident is still open."
  app2ko="감사 로그가 리전별로 전송되기 때문에, 장애가 아직 진행 중일 때는 검토자가 장애 타임라인을 조금씩 다르게 볼 수 있다."
>}}
