---
title: 장애 회고 가이드의 표현
description: 책임을 시스템으로 옮기고, 과장된 단어를 걷어내고, 리뷰의 목적을 다시 정의하는 문장 5개.
weight: -9
date: 2026-08-29
source: "PagerDuty Incident Response — Effective Postmortems"
sourceURL: https://response.pagerduty.com/after/effective_post_mortems/
---

# 장애 회고 가이드의 표현

장애가 끝난 뒤 포스트모템을 어떻게 써야 실제로 쓸모가 있는지 다룬 문서. 사람을 탓하지 않으면서도
**무엇이 잘못됐는지는 하나도 흐리지 않는** 문형이 많아 발췌했다. 장애 회고뿐 아니라 코드 리뷰,
보안 감사, 상태 공유처럼 남의 실수를 다뤄야 하는 자리에 그대로 옮겨 쓸 틀만 골랐다.

> **원문** — PagerDuty, Inc., *PagerDuty Incident Response Documentation — Effective Postmortems*,
> [response.pagerduty.com](https://response.pagerduty.com/after/effective_post_mortems/)
> ([github.com/PagerDuty/incident-response-docs](https://github.com/PagerDuty/incident-response-docs/blob/master/docs/after/effective_post_mortems.md)),
> [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0).
>
> 영어 문장은 원문 그대로 인용했고, 한글 설명과 응용 문장은 이 노트에서 새로 쓴 것이다.

{{< sentence
  en="We keep our postmortems blameless. If someone deployed a change that broke things, it's not their fault, it's our fault for having a system that allowed them to deploy a breaking change, etc."
  ko="우리는 포스트모템을 무비난(blameless)으로 유지한다. 누군가 배포한 변경이 무언가를 망가뜨렸다면, 그건 그 사람 잘못이 아니라 그런 변경이 배포되도록 놔둔 시스템을 가지고 있던 우리 잘못이다."
  source="PagerDuty Incident Response · Don'ts"
  sourceURL="https://response.pagerduty.com/after/effective_post_mortems/"
  note="`It's not their fault, it's our fault for having X` — **책임의 주어를 사람에서 시스템으로 옮기는** 문형이다. 힘은 `for having`에 있다. 우리 잘못을 '무엇을 했다'가 아니라 **'무엇을 그대로 두고 있었다'**로 규정하기 때문에, 문장이 끝나는 자리에서 개선 항목이 저절로 튀어나온다(그 시스템을 고치면 된다). 순서도 그대로 훔칠 만하다 — 원칙(`blameless`)을 먼저 한 문장으로 못 박고, 바로 다음 문장에서 가장 탓하기 쉬운 상황을 예로 들어 원칙이 실제로 어떻게 적용되는지 보인다. 원칙만 선언하면 사람들은 예외를 상상한다."
  app1="If a regression slipped through review, it's not the reviewer's fault, it's our fault for having a test suite that never covered that path."
  app1ko="회귀 버그가 리뷰를 그냥 통과했다면, 그건 리뷰어 잘못이 아니라 그 경로를 한 번도 커버하지 않은 테스트 스위트를 가지고 있던 우리 잘못이다."
  app2="If a key ended up in the repository, it's not the new hire's fault, it's our fault for having no secret scanning on the default branch."
  app2ko="키가 저장소에 들어갔다면, 그건 새로 온 사람 잘못이 아니라 기본 브랜치에 시크릿 스캐닝조차 두지 않고 있던 우리 잘못이다."
>}}

{{< sentence
  en="We need to be honest in our postmortems, even to ourselves, otherwise they lose their effectiveness."
  ko="우리는 포스트모템에서 정직해야 한다. 우리 자신에게조차 그래야 하고, 그러지 않으면 포스트모템은 효력을 잃는다."
  source="PagerDuty Incident Response · Don'ts"
  sourceURL="https://response.pagerduty.com/after/effective_post_mortems/"
  note="`We need to X, even to ourselves, otherwise Y.` — 요구와 그 요구를 어겼을 때의 대가를 한 문장에 담는 틀이다. 무게중심은 삽입구 `even to ourselves`에 있다. 정직의 대상을 밖(고객·경영진)에서 안(우리)으로 한 번 더 밀어붙이면서, 흔한 자기변호를 미리 막는다. 그리고 `otherwise` 절이 이유를 **도덕이 아니라 비용**으로 댄다 — 정직하지 않으면 나쁜 사람이 되는 게 아니라 그 문서가 쓸모없어진다. 규범을 강요하지 않고 지키게 만들고 싶을 때 이 순서로 쓴다."
  app1="We need to record the real timeline in the incident channel, even when it makes our response look slow, otherwise the review has nothing to work from."
  app1ko="우리는 장애 채널에 실제 타임라인을 남겨야 한다. 우리 대응이 느려 보이게 되더라도 그래야 하고, 그러지 않으면 회고는 근거로 삼을 게 없다."
  app2="We need to write down the risks we accepted, even the ones nobody asked about, otherwise the next audit starts from zero."
  app2ko="우리는 감수하기로 한 리스크를 적어 둬야 한다. 아무도 묻지 않은 것까지 그래야 하고, 그러지 않으면 다음 감사는 맨바닥에서 시작한다."
>}}

{{< sentence
  en="We want to be sure we accurately reflect the impact of an incident, and outage is usually too broad of a term to use. It can lead customers to think we were fully unavailable when that likely was nowhere near the case."
  ko="우리는 장애의 영향을 정확히 반영하고 싶고, outage(전면 중단)는 대개 쓰기에 너무 넓은 말이다. 그 말은 실제로는 전혀 그렇지 않았는데도 고객이 우리가 완전히 멈춰 있었다고 생각하게 만들 수 있다."
  source="PagerDuty Incident Response · Don'ts"
  sourceURL="https://response.pagerduty.com/after/effective_post_mortems/"
  note="단어 하나를 물리는 두 마디 구조다. 먼저 `X is usually too broad of a term to use` — **틀렸다고 하지 않고 넓다고 한다.** 옳고 그름 다툼을 정밀도 문제로 바꾸기 때문에 쓴 사람이 방어할 거리가 없다. 이어서 `It can lead A to think B when that likely was nowhere near the case`가 그 넓이가 만들어 낼 **구체적인 오해**를 적는다. `nowhere near the case`는 '사실과 거리가 멀다'를 세게 말하는 관용구이고, `likely`가 붙어 있어 단정까지 가지는 않는다. 상태 공유, 보고서 제목, 알림 문구에서 부풀려진 단어를 걷어낼 때 꺼내 쓴다."
  app1="We want to be sure we accurately reflect what the alert covers, and critical is usually too broad of a term to use."
  app1ko="우리는 그 알림이 무엇을 가리키는지 정확히 반영하고 싶고, critical은 대개 쓰기에 너무 넓은 말이다."
  app2="Calling it a breach can lead auditors to think customer data left our network when that likely was nowhere near the case."
  app2ko="그걸 침해(breach)라고 부르면, 실제로는 전혀 그렇지 않았는데도 감사자들이 고객 데이터가 우리 네트워크를 빠져나갔다고 생각할 수 있다."
>}}

{{< sentence
  en="Reviewing a postmortem isn't about nit-picking typos (although we should make sure our external message isn't littered with spelling errors). It's about providing constructive feedback on valuable changes to a postmortem so that we get the most benefit from them."
  ko="포스트모템을 리뷰하는 일은 오탈자를 트집 잡는 게 아니다(물론 외부에 나가는 메시지에 맞춤법 오류가 널려 있지 않도록은 해야 한다). 포스트모템에서 최대한을 얻어 내기 위해, 값어치 있는 변경에 건설적인 피드백을 주는 일이다."
  source="PagerDuty Incident Response · Reviewing"
  sourceURL="https://response.pagerduty.com/after/effective_post_mortems/"
  note="`X isn't about A (although ...). It's about B.` — **활동의 목적을 다시 정의하는** 문형이다. 장치는 괄호 안의 양보다. A를 통째로 쳐내면 '그럼 오탈자는 무시해도 되냐'는 반문이 따라오는데, 괄호로 '그건 그거대로 하되 본질은 아니다'를 미리 붙여 두면 그 반문이 막힌다. 그래서 부정문(`isn't about`)이 면제로 읽히지 않는다. 리뷰·회의·문서가 원래 목적을 잃고 형식만 남았을 때, 금지 목록 대신 이 한 쌍으로 방향을 되돌린다."
  app1="Design review isn't about approving the diagram (although the diagram should match what we plan to build). It's about finding the decisions we would regret in six months."
  app1ko="설계 리뷰는 다이어그램을 승인하는 일이 아니다(물론 다이어그램은 우리가 만들려는 것과 맞아야 한다). 여섯 달 뒤에 후회할 결정을 찾아내는 일이다."
  app2="An access review isn't about counting accounts (although we should know how many there are). It's about finding the permissions nobody can explain any more."
  app2ko="접근 권한 검토는 계정 수를 세는 일이 아니다(물론 몇 개인지는 알고 있어야 한다). 이제 아무도 설명하지 못하는 권한을 찾아내는 일이다."
>}}

{{< sentence
  en="Rather than just pointing out what went wrong, does it drill down to the underlying causes of the issue?"
  ko="무엇이 잘못됐는지 짚기만 하는 게 아니라, 문제의 근본 원인까지 파고드는가?"
  source="PagerDuty Incident Response · Reviewing"
  sourceURL="https://response.pagerduty.com/after/effective_post_mortems/"
  note="점검 기준을 **질문으로** 쓰는 문형이다. 골격은 `Rather than just X-ing, does it Y?` — 최소 기준(X)을 먼저 인정해 준 뒤 한 단계 위(Y)를 요구한다. `just`가 이 문장의 안전장치다. 빼면 'X는 하지 말라'로 읽혀 버리는데, `just`가 있으면 X는 했고 거기서 멈췄다는 뜻이 된다. 명령문 `Drill down to the underlying causes`로 쓰면 누가 누구에게 내리는 지시가 되지만, 의문문으로 두면 글쓴이와 리뷰어가 **같이 문서를 놓고 확인하는 기준**이 된다. 체크리스트를 만들 때 항목을 전부 이 꼴로 바꿔 보면 톤이 달라진다."
  app1="Rather than just listing the files it touches, does the pull request description say what changes for the user?"
  app1ko="어떤 파일을 건드렸는지 나열하기만 하는 게 아니라, 그 풀 리퀘스트 설명이 사용자에게 무엇이 달라지는지 말하고 있는가?"
  app2="Rather than just restating the alert, does the runbook tell the on-call engineer what to check first?"
  app2ko="알림 내용을 다시 옮겨 적기만 하는 게 아니라, 그 런북이 온콜 엔지니어에게 무엇부터 확인하라고 말해 주는가?"
>}}
