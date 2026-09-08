---
title: 규칙이 실제로 어떻게 적용되는지 못 박는 표현
description: 위험한 기본값을 먼저 밝히고, 충돌 시 무엇이 이기는지 선언하고, 되지만 하지 말라고 말하는 문장 5개.
weight: -20
date: 2026-09-09
source: "Istio Documentation — Security"
sourceURL: https://istio.io/latest/docs/concepts/security/
---

# 규칙이 실제로 어떻게 적용되는지 못 박는 표현

Istio 공식 문서의 *Security* 페이지는 서비스 메시 안에서 인증·인가 정책이 어떤 순서로
평가되고, 정책을 바꿨을 때 언제부터 실제로 적용되는지를 설명한다. 정책을 다루는 문서라
**규칙의 경계를 말로 확정하는 문장**이 계속 나온다 — 아무 정책도 없을 때 기본으로 무슨
일이 벌어지는지, 허용과 거부가 부딪치면 무엇이 이기는지, 시스템이 어디까지는 보장하고
어디부터는 보장하지 않는지. 권한 설계 문서, 릴리스 정책 공지, 마이그레이션 계획서, 코드
리뷰 코멘트처럼 **내가 정한 규칙을 남이 오해 없이 따라야 하는 글**에 그대로 옮겨 쓸 다섯
문장을 골랐다.

> **원문** — Istio Authors, *Security*,
> [istio.io](https://istio.io/latest/docs/concepts/security/) (Istio Documentation), 문서 라이선스
> [Apache-2.0](https://github.com/istio/istio.io/blob/master/LICENSE)
> ([원본 마크다운](https://github.com/istio/istio.io/blob/master/content/en/docs/concepts/security/index.md)).
>
> 영어 문장은 원문 그대로 인용했고, 한글 설명과 응용 문장은 이 노트에서 새로 쓴 것이다.

{{< sentence
  en="When requests carry no token, they are accepted by default. To reject requests without tokens, provide authorization rules that specify the restrictions for specific operations, for example paths or actions."
  ko="요청에 토큰이 없으면 기본적으로 통과된다. 토큰 없는 요청을 거부하려면, 경로나 동작처럼 특정 오퍼레이션에 대한 제한을 지정하는 인가 규칙을 두어라."
  source="Istio Documentation · Request authentication"
  sourceURL="https://istio.io/latest/docs/concepts/security/"
  note="`When X, they are accepted by default. To reject X, do Y.` — **기본값이 느슨한 쪽이라는 사실을 감추지 않고 먼저 말한 다음**, 곧바로 닫는 방법을 붙이는 2단 구조다. `by default`는 변명이 아니라 현재 동작에 대한 사실 진술이라 방어적으로 읽히지 않는다. 두 번째 문장을 명령문(`provide ~`)으로 두는 게 핵심 — 읽는 사람 손에 할 일이 남는다. 위험한 기본값을 문서에 적어야 할 때 이 순서를 그대로 쓴다."
  app1="When an alert has no owner, it is routed to the on-call by default. To stop that, add a routing rule that names the owning team for each service."
  app1ko="알림에 담당자가 지정되어 있지 않으면 기본적으로 온콜에게 넘어간다. 그렇게 되지 않게 하려면, 서비스마다 담당 팀을 지정하는 라우팅 규칙을 추가하라."
  app2="When a bucket has no policy attached, every request from inside the network is allowed by default. To reject anonymous reads, provide an explicit deny for requests without an authenticated principal."
  app2ko="버킷에 정책이 붙어 있지 않으면 네트워크 내부의 모든 요청이 기본적으로 허용된다. 익명 읽기를 거부하려면, 인증된 주체가 없는 요청에 대한 명시적 거부를 두어라."
>}}

{{< sentence
  en="The deny policy takes precedence over the allow policy. Requests matching allow policies can be denied if they match a deny policy. Istio evaluates deny policies first to ensure that an allow policy can't bypass a deny policy."
  ko="거부 정책이 허용 정책보다 우선한다. 허용 정책에 해당하는 요청이라도 거부 정책에 걸리면 거부될 수 있다. Istio는 허용 정책이 거부 정책을 우회하지 못하도록 거부 정책을 먼저 평가한다."
  source="Istio Documentation · Authorization policies"
  sourceURL="https://istio.io/latest/docs/concepts/security/"
  note="선언 → 결과 → 근거의 3단이다. `A takes precedence over B`로 순위를 못 박고, 다음 문장에서 그 순위가 실제로 어떤 요청을 죽이는지 보여 주고, 마지막에 `X ~ first to ensure that Y can't Z`로 왜 그 순서인지 설계 의도를 댄다. `takes precedence over`는 '더 중요하다'가 아니라 **부딪쳤을 때 이긴다**는 뜻이고, `to ensure that ~ can't ~`는 막으려는 시나리오를 이름 붙여 보여 주는 목적절이다. 규칙 두 개가 충돌할 여지가 있는 문서라면 이 3단을 통째로 옮긴다."
  app1="The freeze window takes precedence over the release schedule. Changes approved for this week can still be held if they land inside the freeze."
  app1ko="배포 동결 기간이 릴리스 일정보다 우선한다. 이번 주에 승인된 변경이라도 동결 기간에 걸리면 보류될 수 있다."
  app2="We evaluate the rollback criteria first to ensure that a green dashboard can't override a failing canary."
  app2ko="초록색 대시보드가 실패한 카나리를 덮어쓰지 못하도록, 우리는 롤백 기준을 먼저 평가한다."
>}}

{{< sentence
  en="You can change an authentication policy at any time and Istio pushes the new policies to the workloads almost in real time. However, Istio can't guarantee that all workloads receive the new policy at the same time."
  ko="인증 정책은 언제든 바꿀 수 있고, Istio는 새 정책을 워크로드에 거의 실시간으로 밀어 넣는다. 다만 모든 워크로드가 새 정책을 동시에 받는다는 것까지는 Istio가 보장하지 못한다."
  source="Istio Documentation · Updating authentication policies"
  sourceURL="https://istio.io/latest/docs/concepts/security/"
  note="기능을 먼저 시원하게 서술한 뒤 `However, X can't guarantee that ~`로 **보장하지 않는 딱 한 가지**를 잘라 낸다. 앞 문장의 `almost in real time`이 이미 복선이다 — `almost`를 넣어 두었기 때문에 뒤에 오는 한정이 말 바꾸기로 보이지 않는다. `can't guarantee that ~`은 '안 된다'가 아니라 **거기까지는 책임 범위가 아니다**라는 선언이라, 이어서 단계적 전환을 권하는 근거가 된다. 기능 문서나 SLA에 한계를 적으면서도 톤을 낮추고 싶지 않을 때 쓴다."
  app1="You can rotate the token at any time and the config service distributes it within seconds. However, we can't guarantee that every worker picks up the new token before its current request finishes."
  app1ko="토큰은 언제든 교체할 수 있고, 설정 서비스가 몇 초 안에 배포한다. 다만 모든 워커가 진행 중인 요청을 끝내기 전에 새 토큰을 받는다는 것까지는 보장하지 못한다."
  app2="The feature flag takes effect on the next request. However, we can't guarantee that both regions see the same value while the rollout is in progress."
  app2ko="기능 플래그는 다음 요청부터 적용된다. 다만 롤아웃이 진행되는 동안 두 리전이 같은 값을 본다는 것까지는 보장하지 못한다."
>}}

{{< sentence
  en="Even after installing the Istio sidecar on the server, the operator cannot enable mutual TLS without breaking existing communications."
  ko="서버에 Istio 사이드카를 설치한 뒤에도, 운영자는 기존 통신을 끊지 않고서는 상호 TLS를 켤 수 없다."
  source="Istio Documentation · Permissive mode"
  sourceURL="https://istio.io/latest/docs/concepts/security/"
  note="`Even after X-ing, ... cannot Y without Z-ing` — **한 단계를 이미 해냈는데도 여전히 막혀 있다**를 한 문장에 담는 문형이다. `Even after`가 '이만큼 했는데도'라는 힘을 만들고, `cannot Y without Z-ing`가 그 상태에서 밀어붙였을 때 치를 대가를 이름 붙여 준다. 원문은 이 문장 바로 뒤에 중간 단계(permissive mode)를 꺼내는데, **막다른 길을 먼저 그려 두면 우회로가 타협이 아니라 설계로 읽힌다.** 마이그레이션 계획서에서 '그래서 한 번에 못 바꾼다'를 감정 없이 말할 때 그대로 쓴다."
  app1="Even after moving the reads to the new cluster, we cannot drop the old schema without breaking the nightly reporting jobs."
  app1ko="읽기를 새 클러스터로 옮긴 뒤에도, 야간 리포팅 잡을 깨지 않고서는 옛 스키마를 지울 수 없다."
  app2="Even after adding the audit log, we cannot tell who approved the change without asking the team."
  app2ko="감사 로그를 붙인 뒤에도, 팀에 물어보지 않고서는 누가 그 변경을 승인했는지 알 수 없다."
>}}

{{< sentence
  en="Thus, you can have multiple mesh-wide or namespace-wide policies in a mesh or namespace. However, it is still a good practice to avoid having multiple mesh-wide or namespace-wide request authentication policies."
  ko="따라서 하나의 메시나 네임스페이스 안에 메시 전역 또는 네임스페이스 전역 정책을 여러 개 둘 수 있다. 그렇더라도 메시 전역·네임스페이스 전역 요청 인증 정책을 여러 개 두는 것은 피하는 편이 좋다."
  source="Istio Documentation · Authentication policies"
  sourceURL="https://istio.io/latest/docs/concepts/security/"
  note="`you can X. However, it is still a good practice to avoid X` — **되긴 되는데 하지 마라**를 금지가 아니라 권고로 말하는 문형이다. 앞 문장이 가능하다는 사실을 먼저 인정해 주기 때문에 뒤 문장이 잔소리로 읽히지 않는다. 열쇠는 `still`이다 — '그게 가능하다는 걸 알고도 여전히'라는 뜻이라, **읽는 사람이 준비한 반박(되는데 왜요?)을 미리 흡수한다.** 동작하는 코드에 반대해야 하는 코드 리뷰 코멘트에 그대로 옮겨 쓴다."
  app1="You can call the API without a request ID. However, it is still a good practice to send one, so that a failure can be traced back to the caller later."
  app1ko="요청 ID 없이도 이 API를 호출할 수 있다. 그렇더라도 나중에 장애를 호출자까지 되짚을 수 있도록 하나 보내 두는 편이 좋다."
  app2="This works without taking the lock. However, it is still a good practice to take it, because the next caller may not be single-threaded."
  app2ko="락을 잡지 않아도 이 코드는 동작한다. 그렇더라도 다음 호출자가 단일 스레드가 아닐 수 있으니 락을 잡는 편이 좋다."
>}}
