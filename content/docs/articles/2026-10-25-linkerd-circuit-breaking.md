---
title: 추정으로 조치하고, 녹색 신호만으로는 복귀를 허락하지 않는 표현
description: 관측으로 상태를 추정한다고 적는 표현, 조치는 추정에 걸고 해제는 판정에 거는 표현, 설정의 부재로 기본값을 선언하는 표현, 이름이 겹치는 다른 것을 지목해 떼어 놓는 표현, 불충분한 근거를 기각하고 필요조건을 다시 적는 표현 5개.
weight: -65
date: 2026-10-25
source: "Linkerd Docs · Circuit Breaking"
sourceURL: https://linkerd.io/2-edge/reference/circuit-breaking/
---

# 추정으로 조치하고, 녹색 신호만으로는 복귀를 허락하지 않는 표현

Linkerd 서비스 메시의 서킷 브레이킹 레퍼런스. 설정 애노테이션을 나열하는 기능 문서지만,
다루는 주제가 **상대가 고장났다는 판단을 무슨 근거로 내리고 언제 거두는가**라서 문장들이
전부 추정과 사실 사이의 거리를 조심스럽게 적는다. 관측한 것(호출이 실패했다)과 알고 싶은
것(상대가 고장났다)이 다르다는 걸 매번 표시하고, 조치의 근거를 추정에 두면서 해제는 시간이
아니라 판정에 걸고, 헬스 체크가 녹색이라는 사실을 부정하지 않으면서 그것만으로는 부족하다고
적는다 — 장애 대응과 감사 문서에서 그대로 필요한 문형들이라서 발췌했다.

> **원문** — Linkerd authors, *Circuit Breaking*,
> [Linkerd Documentation](https://linkerd.io/2-edge/reference/circuit-breaking/)
> ([원본 리포지터리](https://github.com/linkerd/website/blob/main/linkerd.io/content/2-edge/reference/circuit-breaking.md)),
> [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0).
>
> 영어 문장은 원문 그대로 인용했고, 한글 설명과 응용 문장은 이 노트에서 새로 쓴 것이다.

{{< sentence
  en="In circuit breaking, an application which makes network calls to remote backends monitors whether those calls succeed or fail, in an attempt to determine whether that backend is in a failed state."
  ko="서킷 브레이킹에서는, 원격 백엔드로 네트워크 호출을 하는 애플리케이션이 그 호출들이 성공하는지 실패하는지를 관측하면서, 그 백엔드가 고장 상태인지 판정해 보려 한다."
  source="Linkerd Docs · Circuit Breaking"
  sourceURL="https://linkerd.io/2-edge/reference/circuit-breaking/"
  note="`A monitors whether B, in an attempt to determine whether C.` — **관측한 것과 알고 싶은 것을 한 문장 안에서 분리해 두는** 문형이다. B(호출이 성공했는지)는 직접 보이는 사실이고 C(백엔드가 고장 상태인지)는 거기서 추론하는 것인데, 둘을 `in an attempt to`로 잇는다. 이 전치사구가 전부를 결정한다. `to determine whether`라고만 쓰면 판정이 성공한다는 전제가 깔리지만, `in an attempt to`는 **시도라고만 적고 성공은 주장하지 않는다**. 그래서 오탐이 났을 때 이 문장이 틀린 말이 되지 않는다. 지표로 상태를 추론하는 장치를 설명할 때 — 알림, 헬스 체크, 이상 탐지, 접근 권한 회수 판단 — 무엇을 보고 무엇을 짐작하는지 구분해서 적고 싶으면 이 틀을 쓴다."
  app1="In this rollout check, the deploy pipeline monitors whether the canary pods stay ready for ten minutes, in an attempt to determine whether the new image is safe for the rest of the fleet."
  app1ko="이 롤아웃 점검에서는 배포 파이프라인이 카나리 파드가 10분 동안 ready를 유지하는지 관측하면서, 새 이미지가 나머지 전체에 올려도 안전한지 판정해 보려 한다."
  app2="In this access review, the platform team monitors whether each service account was used in the last ninety days, in an attempt to determine whether the permission is still needed."
  app2ko="이 접근 권한 검토에서는 플랫폼팀이 각 서비스 계정이 지난 90일 안에 쓰였는지 관측하면서, 그 권한이 아직 필요한지 판정해 보려 한다."
>}}

{{< sentence
  en="If a given backend is believed to be in a failed state, its circuit breaker is &quot;tripped&quot;, and no subsequent requests are sent to that backend until it is determined to have returned to normal."
  ko="어떤 백엔드가 고장 상태라고 판단되면 그 백엔드의 서킷 브레이커가 &quot;열리고&quot;, 정상으로 돌아왔다고 판정될 때까지 그 백엔드로는 이후 요청이 전달되지 않는다."
  source="Linkerd Docs · Circuit Breaking"
  sourceURL="https://linkerd.io/2-edge/reference/circuit-breaking/"
  note="`If X is believed to be Y, <조치>, and <차단> until it is determined to have returned to normal.` — 조치는 추정에 걸고 **해제는 시간이 아니라 판정에 거는** 문형이다. 앞의 `is believed to be`가 솜씨 좋은 자리다. `is in a failed state`라고 단정하면 뒤에 오탐이 드러날 때 문장이 거짓이 되지만, `is believed to be`로 적으면 차단의 근거가 사실이 아니라 **판단**이었다고 처음부터 기록된다. 뒤쪽 `until it is determined to have returned to normal`은 그 짝이다. `for five minutes`처럼 시간으로 끝내지 않고 완료형 부정사로 **돌아왔다는 판정이 다시 서야 한다**고 적어서, 해제가 기다림이 아니라 또 한 번의 확인이 된다. 두 동사 모두 행위자가 없는 수동태라는 점도 의도적이다 — 누가 판단했는지를 비우면 문장이 절차의 서술이 되고, 사람을 지목하는 말로 읽히지 않는다. 격리·차단·권한 회수 조치를 적을 때, 근거와 해제 조건을 한 문장에 함께 남겨야 할 때."
  app1="If a tenant is believed to be sending malformed events, its ingest key is suspended, and no further batches are accepted from that tenant until it is determined to have returned to normal."
  app1ko="어떤 테넌트가 형식이 깨진 이벤트를 보내고 있다고 판단되면 그 테넌트의 수집 키가 정지되고, 정상으로 돌아왔다고 판정될 때까지 그 테넌트로부터는 이후 배치가 더 받아들여지지 않는다."
  app2="If a build agent is believed to be compromised, its registry credentials are revoked, and no release jobs are scheduled on that agent until it is determined to have returned to a known-good state."
  app2ko="어떤 빌드 에이전트가 침해되었다고 판단되면 그 에이전트의 레지스트리 자격 증명이 폐기되고, 알려진 정상 상태로 돌아왔다고 판정될 때까지 그 에이전트에는 릴리스 작업이 배정되지 않는다."
>}}

{{< sentence
  en="If no failure accrual annotations are present on a Service, proxies will not perform failure accrual."
  ko="어떤 Service에 실패 누적 애노테이션이 하나도 붙어 있지 않으면, 프록시는 실패 누적을 수행하지 않는다."
  source="Linkerd Docs · Circuit Breaking"
  sourceURL="https://linkerd.io/2-edge/reference/circuit-breaking/"
  note="`If no X are present, Y will not do Z.` — 기본값을 스위치의 상태가 아니라 **설정의 부재**로 적는 문형이다. 같은 내용을 `failure accrual is disabled by default`라고 쓸 수도 있는데, 그러면 어딘가에 끌 수 있는 스위치가 있다는 뜻이 되고 읽는 사람은 그 스위치를 찾으러 간다. `If no X are present`는 찾을 스위치가 없다고 말한다 — 적지 않으면 아무 일도 일어나지 않고, **쓰려면 쓴다고 적어야 한다**. 주어를 설정이 아니라 설정의 없음으로 둔 것이 그 차이를 만든다. `no ... are present`에서 `no`를 명사 쪽에 붙인 것도 계산이다. `if the annotations are not present`보다 **하나도 없는 경우**를 더 분명히 가리킨다. opt-in 기능의 기본 동작을 적을 때, 설정이 비어 있을 때 시스템이 무엇을 하지 않는지 오해 없이 못 박아야 할 때."
  app1="If no retention labels are present on a bucket, the cleanup job will not delete anything."
  app1ko="어떤 버킷에 보존 기간 라벨이 하나도 붙어 있지 않으면, 정리 작업은 아무것도 삭제하지 않는다."
  app2="If no owners are listed in the service catalog entry, the alert router will not page anyone."
  app2ko="서비스 카탈로그 항목에 담당자가 하나도 적혀 있지 않으면, 알림 라우터는 아무도 호출하지 않는다."
>}}

{{< sentence
  en="In the context of HTTP failure accrual, a probe request is an actual application request, and should not be confused with HTTP readiness and liveness probes."
  ko="HTTP 실패 누적의 문맥에서 프로브 요청은 실제 애플리케이션 요청이며, HTTP readiness·liveness 프로브와 혼동해서는 안 된다."
  source="Linkerd Docs · Circuit Breaking"
  sourceURL="https://linkerd.io/2-edge/reference/circuit-breaking/"
  note="`In the context of X, A is an actual B, and should not be confused with C.` — **같은 이름이 두 군데서 다른 것을 가리킬 때** 쓰는 문형이다. 세 부분이 각각 다른 일을 한다. `In the context of X`가 먼저 어느 문맥에서 하는 말인지 울타리를 쳐서, 다른 문맥의 용법을 틀렸다고 하지 않는다. `an actual`은 실체를 못 박는다 — `is a real request`나 `is a normal request`보다 `an actual`이 **흉내가 아니라 그것 자체**라는 쪽을 가리킨다. 마지막 `should not be confused with C`가 핵심인데, `is different from C`와 결이 다르다. 후자는 차이만 알리지만 전자는 **그 혼동이 실제로 일어난다**는 전제를 깔고 있어서, 읽는 쪽이 자기가 지금 그 혼동을 하고 있었는지 점검하게 된다. 용어가 겹치는 문서, 회고에서 시각의 정의를 맞출 때, 리뷰 코멘트에서 상대가 다른 것을 보고 있다고 짚을 때."
  app1="In the context of this postmortem, recovery time is an actual customer-visible metric, and should not be confused with the moment we closed the incident channel."
  app1ko="이 회고의 문맥에서 복구 시간은 실제로 고객에게 보이는 지표이며, 우리가 장애 채널을 닫은 시점과 혼동해서는 안 된다."
  app2="In the context of the audit scope, a control owner is an actual named person who signs off on the evidence, and should not be confused with the team that operates the system."
  app2ko="감사 범위의 문맥에서 통제 책임자는 증빙에 실제로 서명하는 지명된 사람이며, 그 시스템을 운영하는 팀과 혼동해서는 안 된다."
>}}

{{< sentence
  en="This means that a circuit breaker will not allow an endpoint to exit probation just because it responds successfully to health checks — actual application traffic must succeed for the endpoint to become available again."
  ko="즉 서킷 브레이커는 어떤 엔드포인트가 헬스 체크에 정상 응답한다는 이유만으로 그 엔드포인트의 관찰 상태를 풀어 주지 않는다 — 그 엔드포인트가 다시 가용 상태가 되려면 실제 애플리케이션 트래픽이 성공해야 한다."
  source="Linkerd Docs · Circuit Breaking"
  sourceURL="https://linkerd.io/2-edge/reference/circuit-breaking/"
  note="`X will not allow Y just because Z — W must succeed for Y to happen.` — 앞의 문장(바로 위 카드)이 용어를 떼어 놓은 뒤, 그 구분에서 나오는 결론을 적는 문형이다. 대시 앞은 **불충분한 근거를 기각**하고 대시 뒤는 **충분한 근거를 필요조건으로** 다시 세운다. `will not allow ... just because`가 하는 일이 정확하다. 헬스 체크가 통과했다는 사실을 부정하지 않는다 — 통과했을 수 있다 — 다만 **그것만으로는 안 된다**고 한다. 사실을 다투지 않으니 반박할 자리가 없다. 대시 뒤를 `W must succeed for Y to happen`으로 적은 것도 계산이다. `we also check real traffic`처럼 우리가 하는 일로 적으면 재량으로 읽혀서 예외를 논의할 수 있지만, `must ... for ... to`는 조건이어서 협상할 자리가 사라진다. 완화 해제·복구 선언의 기준을 합의할 때, `대시보드는 녹색인데요`라는 말에 답해야 할 때."
  app1="This means that we will not take a service out of degraded status just because the dashboard is green again — a real customer request must complete end to end for us to call the incident recovered."
  app1ko="즉 우리는 대시보드가 다시 녹색이 되었다는 이유만으로 서비스를 성능 저하 상태에서 꺼내지 않는다 — 장애가 복구되었다고 말하려면 실제 고객 요청 하나가 끝에서 끝까지 완료되어야 한다."
  app2="This means that the review will not let a finding be closed just because the scanner stopped reporting it — the owning team must show the fix in a merged diff for the finding to be closed."
  app2ko="즉 검토는 스캐너가 더 이상 그것을 보고하지 않는다는 이유만으로 발견 사항을 닫아 주지 않는다 — 그 발견 사항이 닫히려면 담당 팀이 머지된 디프에서 수정을 보여 주어야 한다."
>}}
