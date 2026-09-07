---
title: 좋아 보이는 조치의 대가를 적는 표현
description: 이론상의 한계와 실무 상한을 나누고, 이득에 비용을 붙이고, 효과 없는 조치를 무효라고 못 박는 문장 5개.
weight: -19
date: 2026-09-08
source: "etcd Documentation — FAQ"
sourceURL: https://etcd.io/docs/v3.6/faq/
---

# 좋아 보이는 조치의 대가를 적는 표현

etcd 공식 문서의 *FAQ*는 분산 키-값 저장소를 실제로 운영하며 나오는 질문에 답한다 —
노드를 몇 개 둘 것인가, 죽은 멤버를 어떻게 교체하는가, 왜 디스크가 느려지면 리더가
바뀌는가. 이 문서가 특히 좋은 것은 **직관대로 손댔을 때 왜 더 나빠지는지**를 설명하는
자리가 계속 나온다는 점이다. 노드를 더 넣고, 리전을 넓히고, 걸리적거리는 검사를 끄는 —
전부 좋아 보이는 조치다. 문서는 그 조치를 나무라지 않고, 대신 **이득을 인정한 다음
대가를 같은 자리에 적는다.** 용량 산정, 장애 대응 중의 임시 조치 판단, 아키텍처 리뷰처럼
누군가의 제안을 반박해야 하는 글에 그대로 옮겨 쓸 다섯 문장을 골랐다.

> **원문** — etcd Authors, *FAQ*,
> [etcd.io](https://etcd.io/docs/v3.6/faq/) (etcd v3.6 Documentation), 문서 라이선스
> [CC BY 4.0](https://github.com/etcd-io/website/blob/main/LICENSE)
> ([원본 마크다운](https://github.com/etcd-io/website/blob/main/content/en/docs/v3.6/faq.md)).
>
> 영어 문장은 원문 그대로 인용했고, 한글 설명과 응용 문장은 이 노트에서 새로 쓴 것이다.

{{< sentence
  en="Theoretically, there is no hard limit. However, an etcd cluster probably should have no more than seven nodes."
  ko="이론상으로는 명확한 한계가 없다. 그러나 etcd 클러스터는 아마도 일곱 노드를 넘지 않는 편이 좋다."
  source="etcd FAQ · What is maximum cluster size?"
  sourceURL="https://etcd.io/docs/v3.6/faq/"
  note="`Theoretically, there is no hard limit. However, X probably should have no more than N.` — **이론상의 한계와 실무 상한을 두 문장으로 갈라놓는** 문형이다. 첫 문장에서 '안 된다'고 말하지 않기 때문에 이어지는 권고가 무지에서 나온 제약으로 보이지 않는다. 톤을 정하는 단어는 `probably should`다. `must not`이면 규칙이 되어 예외를 다투게 되지만, `probably should`는 권고로 남아 상대가 근거를 들고 넘어설 여지를 준다. 숫자를 제시해야 하는데 그 숫자가 물리적 한계가 아니라 경험칙일 때 — 용량 산정, PR 크기 기준, 온콜 로테이션 인원 — 그대로 쓴다."
  app1="Theoretically, there is no hard limit. However, a pull request probably should not touch more than four hundred lines."
  app1ko="이론상으로는 명확한 한계가 없다. 그러나 풀 리퀘스트는 아마도 400줄을 넘지 않는 편이 좋다."
  app2="Theoretically, there is no hard limit. However, an on-call rotation probably should have no fewer than six engineers."
  app2ko="이론상으로는 명확한 한계가 없다. 그러나 온콜 로테이션은 아마도 여섯 명보다 적지 않은 편이 좋다."
>}}

{{< sentence
  en="Deploying etcd across regions improves etcd's fault tolerance since members are in separate failure domains. The cost is higher consensus request latency from crossing data center boundaries."
  ko="etcd를 여러 리전에 걸쳐 배포하면 멤버들이 서로 다른 장애 도메인에 놓이므로 내결함성이 좋아진다. 그 대가는 데이터 센터 경계를 넘느라 늘어나는 합의 요청 지연이다."
  source="etcd FAQ · Does etcd work in cross-region or cross data center deployments?"
  sourceURL="https://etcd.io/docs/v3.6/faq/"
  note="`Doing X improves A since B. The cost is C.` — **이득을 먼저 온전히 인정하고, 비용을 별도 문장의 주어로 세우는** 문형이다. `but`으로 이어 붙이면 앞절이 형식적인 립서비스로 읽히지만, 마침표로 끊고 `The cost is ~`를 새 문장으로 세우면 비용이 반박이 아니라 **함께 적어 두는 항목**이 된다. `since B`는 이득이 왜 생기는지를 한 구절로 붙여 두어, 상대가 그 이득까지 의심할 필요를 없앤다. 아키텍처 리뷰나 도입 제안서에서 어느 쪽도 깎아내리지 않고 선택지를 나란히 놓을 때."
  app1="Running the scanner on every commit improves our detection speed since findings surface before review. The cost is longer feedback time on every pull request."
  app1ko="커밋마다 스캐너를 돌리면 리뷰 전에 결과가 드러나므로 탐지 속도가 좋아진다. 그 대가는 모든 풀 리퀘스트에서 길어지는 피드백 시간이다."
  app2="Keeping audit logs for seven years improves our investigation coverage since we can reconstruct old incidents. The cost is a storage bill that grows every quarter."
  app2ko="감사 로그를 7년간 보관하면 오래된 사고를 재구성할 수 있으므로 조사 범위가 넓어진다. 그 대가는 분기마다 늘어나는 스토리지 비용이다."
>}}

{{< sentence
  en="Since the quorum increased, this extra member buys nothing in terms of fault tolerance; the cluster is still one node failure away from being unrecoverable."
  ko="정족수가 함께 늘었으므로, 이 추가 멤버는 내결함성 면에서 아무것도 사 주지 못한다. 클러스터는 여전히 노드 하나만 더 죽으면 복구 불가 상태다."
  source="etcd FAQ · Should I add a member before removing an unhealthy member?"
  sourceURL="https://etcd.io/docs/v3.6/faq/"
  note="`X buys nothing in terms of Y; Z is still one A away from B.` — **효과가 없다는 판정과 남은 위험을 한 문장에 붙이는** 구조다. `buys nothing`은 '도움이 되지 않는다'보다 강하다. 조치에 값을 치렀다는 전제를 깔고, 그 대가로 산 것이 없다고 말하기 때문이다. `in terms of Y`가 무효 판정의 범위를 한정해 주므로 상대의 조치를 통째로 부정하지 않는다. 세미콜론 뒤의 `still one A away from B`는 위험을 형용사가 아니라 **남은 거리**로 말하는 장치다 — `dangerous`라고 쓰면 감정이지만, '한 번만 더'는 세어 볼 수 있는 사실이다. 장애 중에 나온 임시 조치를 반려할 때 쓴다."
  app1="Since the timeout increased as well, this extra retry buys nothing in terms of availability; the request is still one slow dependency away from failing the whole page."
  app1ko="타임아웃도 함께 늘었으므로, 이 추가 재시도는 가용성 면에서 아무것도 사 주지 못한다. 요청은 여전히 느린 의존성 하나만 걸리면 페이지 전체를 실패시킨다."
  app2="Since the same team holds both keys, the second approver buys nothing in terms of separation of duties; the deploy is still one compromised account away from going out unreviewed."
  app2ko="같은 팀이 두 키를 모두 쥐고 있으므로, 두 번째 승인자는 직무 분리 면에서 아무것도 사 주지 못한다. 배포는 여전히 계정 하나만 탈취되면 검토 없이 나간다."
>}}

{{< sentence
  en="Although it may be tempting to disable quorum checking if there's quorum loss to add a new member, this could lead to full fledged cluster inconsistency."
  ko="정족수를 잃은 상태에서 새 멤버를 넣으려고 정족수 검사를 끄고 싶어질 수 있지만, 그렇게 하면 클러스터 전면 불일치로 이어질 수 있다."
  source="etcd FAQ · Why won't etcd accept my membership changes?"
  sourceURL="https://etcd.io/docs/v3.6/faq/"
  note="`Although it may be tempting to X, this could lead to Y.` — 안전장치를 꺼 버리고 싶은 순간을 **먼저 인정한 뒤** 결과를 붙이는 문형이다. 핵심은 `tempting`이다. 그 조치를 어리석다고 하지 않고 **끌리는 것이 당연하다**고 말해 주므로, 이미 그 버튼에 손을 올린 사람이 방어적으로 변하지 않는다. `this could lead to`도 마찬가지로 `will break`가 아니라 가능성이어서 과장 논쟁을 피한다. 조건절 `if there's quorum loss`가 유혹이 생기는 정확한 상황까지 못 박아 두는 것도 훔칠 만하다 — 언제 이 경고를 떠올려야 하는지가 문장 안에 들어 있다. 런북의 경고 문단, 보안 예외 요청에 대한 회신에 쓴다."
  app1="Although it may be tempting to disable the branch protection if the release is blocked, this could lead to an unreviewed change reaching production."
  app1ko="릴리스가 막혔을 때 브랜치 보호를 끄고 싶어질 수 있지만, 그렇게 하면 검토되지 않은 변경이 프로덕션까지 갈 수 있다."
  app2="Although it may be tempting to widen the role if the job keeps failing on permissions, this could lead to a credential nobody can safely revoke later."
  app2ko="잡이 권한 문제로 계속 실패할 때 역할 범위를 넓히고 싶어질 수 있지만, 그렇게 하면 나중에 누구도 안전하게 회수할 수 없는 자격 증명이 남을 수 있다."
>}}

{{< sentence
  en="This is intentional; disk latency is part of leader liveness. Suppose the cluster leader takes a minute to fsync a raft log update to disk, but the etcd cluster has a one second election timeout."
  ko="이는 의도된 동작이다. 디스크 지연은 리더 생존성의 일부다. 클러스터 리더가 raft 로그 갱신을 디스크에 fsync 하는 데 1분이 걸리는데 etcd 클러스터의 선거 타임아웃은 1초라고 해 보자."
  source="etcd FAQ · Why does etcd lose its leader from disk latency spikes?"
  sourceURL="https://etcd.io/docs/v3.6/faq/"
  note="`This is intentional; X is part of Y.` — 버그 신고로 들어온 동작을 **설계 설명으로 되돌리는** 문형이다. 세미콜론 앞은 판정, 뒤는 근거인데, 근거를 변명이 아니라 **정의**로 준다는 게 핵심이다. '느린 디스크도 장애로 친다'가 아니라 `disk latency is part of leader liveness` — 살아 있다는 말의 뜻 자체에 디스크가 들어 있다고 하므로 더 다툴 것이 없어진다. 이어지는 `Suppose A, but B.`는 숫자 두 개를 나란히 놓아 독자가 스스로 결론에 닿게 하는 장치다. 왜 이렇게 동작하느냐는 문의에 답할 때, 또는 알려진 동작을 문서화할 때 쓴다."
  app1="This is intentional; queue depth is part of the health signal. Suppose the worker answers the probe in five milliseconds, but it has not pulled a job off the queue in ten minutes."
  app1ko="이는 의도된 동작이다. 큐 적체는 헬스 신호의 일부다. 워커가 프로브에는 5밀리초 만에 답하는데 큐에서 잡을 가져간 지는 10분이 됐다고 해 보자."
  app2="This is intentional; review latency is part of the incident timeline. Suppose the fix was written in twenty minutes, but it waited six hours for an approver."
  app2ko="이는 의도된 동작이다. 리뷰 지연은 장애 타임라인의 일부다. 수정은 20분 만에 작성됐는데 승인자를 여섯 시간 기다렸다고 해 보자."
>}}
