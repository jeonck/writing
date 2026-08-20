---
title: 커널 패치 제출 가이드의 표현
description: 리뷰어를 설득하고, 주장에 수치를 붙이고, 지금은 괜찮다는 말을 미래까지 늘려 반박하는 문장 5개.
weight: -1
date: 2026-08-21
source: "Linux kernel docs · Submitting patches"
sourceURL: https://docs.kernel.org/process/submitting-patches.html
---

# 커널 패치 제출 가이드의 표현

리눅스 커널에 코드를 보낼 때 패치를 어떻게 나누고, 설명을 어떻게 쓰고, 리뷰 코멘트에
어떻게 답해야 하는지를 정리한 문서. 사람에게 요구하면서도 비난처럼 들리지 않는 문형이
많아 발췌했다 — 코드 리뷰와 장애 보고에 그대로 옮겨 쓸 수 있다.

> **원문** — Linux kernel contributors, *Submitting patches: the essential guide to getting
> your code into the kernel*,
> [Linux kernel documentation](https://docs.kernel.org/process/submitting-patches.html),
> [GPL-2.0](https://github.com/torvalds/linux/blob/master/COPYING) 라이선스.
> 원본 파일: [Documentation/process/submitting-patches.rst](https://github.com/torvalds/linux/blob/master/Documentation/process/submitting-patches.rst).
>
> 영어 문장은 원문 그대로 인용했고, 한글 설명과 응용 문장은 이 노트에서 새로 쓴 것이다.

{{< sentence
  en="Convince the reviewer that there is a problem worth fixing and that it makes sense for them to read past the first paragraph."
  ko="고칠 만한 문제가 있다는 것, 그리고 첫 문단 너머까지 읽을 가치가 있다는 것을 리뷰어에게 납득시켜라."
  source="Linux kernel docs · Describe your changes"
  sourceURL="https://docs.kernel.org/process/submitting-patches.html"
  note="`Convince X that A and that B.` — 설득해야 할 것을 **두 겹으로 못 박는** 문형이다. 첫째는 문제가 존재한다는 것, 둘째는 계속 읽을 이유가 있다는 것. `that`을 두 번 반복하는 게 핵심이다. 두 번째를 생략하면 뒷부분이 앞 절에 딸린 조건처럼 읽혀 요구가 하나로 뭉개진다. `worth fixing`은 가치 판단을 두 단어로 압축하고, `read past the first paragraph`는 '관심을 유지시킨다'는 추상적인 목표를 **독자의 물리적 행동**으로 바꿔 말한 표현이다."
  app1="Convince the on-call team that there is a failure worth paging for and that it makes sense for them to read past the alert title."
  app1ko="호출할 만한 장애가 있다는 것, 그리고 알림 제목 너머까지 읽을 가치가 있다는 것을 온콜 팀에게 납득시켜라."
  app2="Convince the security reviewer that there is a risk worth blocking the release for and that it makes sense for them to read the full audit trail."
  app2ko="릴리스를 막을 만한 위험이 있다는 것, 그리고 감사 기록 전체를 읽을 가치가 있다는 것을 보안 리뷰어에게 납득시켜라."
>}}

{{< sentence
  en="If you claim improvements in performance, memory consumption, stack footprint, or binary size, include numbers that back them up."
  ko="성능, 메모리 사용량, 스택 점유, 바이너리 크기에서 개선을 주장한다면 그것을 뒷받침하는 수치를 함께 넣어라."
  source="Linux kernel docs · Describe your changes"
  sourceURL="https://docs.kernel.org/process/submitting-patches.html"
  note="`If you claim X, include Y that backs it up.` — 주장과 근거를 **조건과 의무로 묶는** 문형이다. 규칙처럼 들리고 지적처럼 들리지 않는 게 장점이다. `you`에 조건절을 걸어 두면 특정한 사람을 지목하지 않고도 요구가 성립한다. `back up`은 `substantiate` 같은 격식체 대신 쓰는 가장 평범한 구어 동사라 문서 톤을 딱딱하게 만들지 않는다. 앞에 항목을 나열해 두면 **어디까지가 근거를 요구하는 범위인지**가 함께 정해진다."
  app1="If you claim the new index improved query latency, include the numbers that back it up."
  app1ko="새 인덱스가 쿼리 지연을 줄였다고 주장한다면 그것을 뒷받침하는 수치를 함께 넣어라."
  app2="If you claim the incident had no customer impact, include the dashboards and log queries that back that up."
  app2ko="이번 장애가 고객에게 영향이 없었다고 주장한다면 그것을 뒷받침하는 대시보드와 로그 쿼리를 함께 넣어라."
>}}

{{< sentence
  en="Solve only one problem per patch. If your description starts to get long, that's a sign that you probably need to split up your patch."
  ko="패치 하나에 문제 하나만 해결하라. 설명이 길어지기 시작한다면, 그건 아마 패치를 쪼개야 한다는 신호다."
  source="Linux kernel docs · Describe your changes"
  sourceURL="https://docs.kernel.org/process/submitting-patches.html"
  note="규칙을 한 문장으로 못 박고, 그 규칙을 어겼는지 **스스로 알아채는 방법**을 뒤에 붙였다. `that's a sign that you probably need to ~`는 징후를 진단으로 바꾸는 골격이다. `starts to get long`은 이미 길다는 상태가 아니라 **길어지는 초기**를 가리켜서 아직 늦지 않았다는 여지를 남긴다. `probably`는 단정을 피하면서도 뒤따르는 지시는 그대로 유지한다 — 판단은 상대에게 넘기되 할 일은 알려 주는 방식이다."
  app1="Fix only one root cause per pull request. If the title starts to need an 'and', that's a sign that you probably need to split it up."
  app1ko="풀 리퀘스트 하나에 근본 원인 하나만 고쳐라. 제목에 and가 필요해지기 시작한다면, 그건 아마 쪼개야 한다는 신호다."
  app2="If your incident timeline starts to get long, that's a sign that you probably need to separate the outage itself from the follow-up work."
  app2ko="장애 타임라인이 길어지기 시작한다면, 그건 아마 장애 자체와 후속 작업을 분리해야 한다는 신호다."
>}}

{{< sentence
  en="You must respond to those comments; ignoring reviewers is a good way to get ignored in return."
  ko="그 코멘트들에는 반드시 답해야 한다. 리뷰어를 무시하는 것은 자기도 무시당하는 좋은 방법이다."
  source="Linux kernel docs · Respond to review comments"
  sourceURL="https://docs.kernel.org/process/submitting-patches.html"
  note="세미콜론 앞은 의무(`You must ~`), 뒤는 그 의무를 어겼을 때 벌어지는 일을 **반어로** 말한다. `a good way to get X`는 '~하는 지름길'이라는 뜻의 비꼬는 관용 표현이라, 제재를 예고하지 않고도 경고가 된다. `in return`이 결정적이다. 인과를 규정이 아니라 **사람 사이의 되갚음**으로 돌려서, 강제할 수 없는 팀 규범을 강제하지 않고 전달한다."
  app1="You must answer the questions left on your pull request; ignoring reviewers is a good way to get your next one queued behind everyone else's."
  app1ko="풀 리퀘스트에 남은 질문에는 반드시 답해야 한다. 리뷰어를 무시하는 것은 다음 리뷰가 남들 뒤로 밀리는 좋은 방법이다."
  app2="You must reply to the audit findings; leaving them open is a good way to get the same finding reopened next quarter."
  app2ko="감사 지적 사항에는 반드시 답해야 한다. 열어 둔 채 두는 것은 다음 분기에 같은 지적을 다시 받는 좋은 방법이다."
>}}

{{< sentence
  en="Bear in mind that, even if there is no collision with your six-character ID now, that condition may change five years from now."
  ko="지금은 여섯 자리 ID로 충돌이 나지 않더라도 그 조건은 5년 뒤에 달라질 수 있다는 점을 염두에 두라."
  source="Linux kernel docs · Describe your changes"
  sourceURL="https://docs.kernel.org/process/submitting-patches.html"
  note="`Bear in mind that, even if X now, that condition may change ~.` — **지금 괜찮다는 관찰을 미래까지 늘려 반박하는** 양보 구문이다. 핵심은 `that condition`이다. 상대가 든 근거를 '조건'이라는 한 단어로 되받아, 사실 자체가 아니라 **그 사실이 성립하는 전제**를 문제 삼는다. `may change`로 단정을 피하고 `five years from now`처럼 기간을 명시하면 막연한 불안이 아니라 따져 볼 수 있는 주장이 된다. 용량 산정, 키 길이, 보존 기간처럼 '지금은 충분하다'로 끝나는 논의에 그대로 꺼내 쓴다."
  app1="Bear in mind that, even if the current quota is enough now, that condition may change once the batch jobs move to this cluster."
  app1ko="지금은 현재 쿼터로 충분하더라도 배치 작업이 이 클러스터로 옮겨 오면 그 조건은 달라질 수 있다는 점을 염두에 두라."
  app2="Bear in mind that, even if no one outside the team can reach this endpoint now, that condition may change the first time we open a VPC peering."
  app2ko="지금은 팀 밖에서 이 엔드포인트에 닿을 수 없더라도 VPC 피어링을 한 번 열면 그 조건은 달라질 수 있다는 점을 염두에 두라."
>}}
