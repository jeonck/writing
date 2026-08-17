---
title: 시스템 설계 글의 표현
description: 트레이드오프, 원인 규명, 가정의 경계를 설명하는 엔지니어링 문장 5개.
weight: 10
date: 2026-08-17
---

# 시스템 설계 글의 표현

엔지니어링 아티클에서 자주 만나는, 설계 판단을 설명하는 문장들.

> [!NOTE]
> 이 페이지는 템플릿을 보여 주기 위해 직접 쓴 **예시 문장**이다.
> 실제 노트는 읽은 아티클에서 발췌하고 `source` / `sourceURL`을 채운다.

{{< sentence
  en="We traded write throughput for read consistency, and for this workload that was the right call."
  ko="쓰기 처리량을 읽기 일관성과 맞바꿨고, 이 워크로드에서는 그게 맞는 판단이었다."
  note="`trade A for B`는 **A를 내주고 B를 얻었다**는 뜻으로, 설계 문서에서 트레이드오프를 한 문장에 담을 때 쓰는 기본형이다. `sacrifice`가 손실을 강조한다면 `trade`는 **의도적인 교환**이라는 뉘앙스가 있다. 뒤의 `that was the right call`은 '그게 옳은 결정이었다'는 구어체 평가로, 딱딱한 `that decision was justified`보다 글의 톤을 낮춰 준다."
  app1="We traded startup time for a smaller memory footprint, which matters more on the edge nodes."
  app1ko="시작 시간을 메모리 사용량과 맞바꿨는데, 엣지 노드에서는 그쪽이 더 중요하다."
  app2="I'd rather not trade readability for a 5% speedup here."
  app2ko="여기서 5% 속도 향상을 위해 가독성을 내주고 싶지는 않다."
>}}

{{< sentence
  en="The bottleneck turned out to be serialization, not the network as we had assumed."
  ko="병목은 우리가 짐작했던 네트워크가 아니라 직렬화였다."
  note="`turn out to be`는 **조사해 보니 실제로는 ~였다**는 반전을 담는 표현이다. 뒤에 `not X as we had assumed`를 붙이면 '기존 가정이 틀렸다'는 사실까지 한 문장에 들어간다. 과거완료 `had assumed`가 '측정하기 이전의 가정'이라는 시점을 분명히 해 준다."
  app1="The slow query turned out to be a missing index, not the ORM as the team had suspected."
  app1ko="느린 쿼리의 원인은 팀이 의심하던 ORM이 아니라 빠진 인덱스였다."
  app2="The flaky test turned out to be a timezone issue, not a race condition."
  app2ko="간헐적으로 실패하던 테스트의 원인은 경쟁 조건이 아니라 타임존 문제였다."
>}}

{{< sentence
  en="Rather than adding another cache layer, we removed the call that made it necessary."
  ko="캐시 레이어를 하나 더 얹는 대신, 그 캐시를 필요하게 만든 호출 자체를 없앴다."
  note="`Rather than -ing, we ...` 구조는 **흔한 해법을 먼저 언급하고 다른 길을 택했다**고 밝히는 도입부다. 독자가 예상할 답을 앞에 놓아 대비를 만든다. `the call that made it necessary`처럼 관계절로 원인을 지목하면 '증상이 아니라 원인을 건드렸다'는 메시지가 선명해진다."
  app1="Rather than retrying the failed job, we made the job idempotent so a retry is safe."
  app1ko="실패한 작업을 재시도하는 대신, 재시도가 안전하도록 작업을 멱등하게 만들었다."
  app2="Rather than documenting the workaround, we fixed the API that required it."
  app2ko="우회 방법을 문서화하는 대신, 그 우회를 필요하게 만든 API를 고쳤다."
>}}

{{< sentence
  en="This assumption holds until the dataset no longer fits in memory."
  ko="이 가정은 데이터셋이 메모리에 들어가지 않는 시점까지만 유효하다."
  note="`hold`는 여기서 '(가정·규칙이) 성립한다'는 자동사다. `until ~`을 붙이면 **유효 범위의 경계**를 명시하게 된다. 설계 문서에서 가정을 적을 때 '언제까지 참인지'를 함께 쓰는 습관이 이 한 문장에 들어 있다."
  app1="The linear scaling holds until you saturate the disk I/O."
  app1ko="선형 확장은 디스크 I/O가 포화되는 지점까지만 성립한다."
  app2="This estimate holds only while traffic stays below 10k requests per second."
  app2ko="이 추정치는 트래픽이 초당 1만 요청 아래에 머무는 동안에만 유효하다."
>}}

{{< sentence
  en="It is easier to reason about a system that fails loudly than one that quietly returns stale data."
  ko="조용히 오래된 데이터를 돌려주는 시스템보다, 요란하게 실패하는 시스템이 이해하기 쉽다."
  note="`reason about ~`은 **머릿속으로 동작을 따라가며 추론하다**라는 뜻으로, `understand`보다 기술 문서에서 훨씬 자주 쓰인다. `fail loudly` / `fail silently`는 짝을 이루는 관용 표현이고, 여기서는 `quietly returns stale data`로 변주해 대비를 만들었다."
  app1="Strict types make the code easier to reason about, even when they add a little ceremony."
  app1ko="엄격한 타입은 약간의 번거로움을 더하더라도 코드를 추론하기 쉽게 만든다."
  app2="A queue that drops messages loudly is safer than one that silently reorders them."
  app2ko="메시지를 조용히 뒤섞는 큐보다, 요란하게 버리는 큐가 더 안전하다."
>}}
