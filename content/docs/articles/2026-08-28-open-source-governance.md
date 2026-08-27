---
title: 오픈소스 거버넌스 가이드의 표현
description: 요건을 조건부로 면제하고, 오해를 미리 없애고, 예외를 막으면서 판단 기준을 세우는 문장 5개.
weight: -8
date: 2026-08-28
source: "Open Source Guides — Leadership and Governance"
sourceURL: https://opensource.guide/leadership-and-governance/
---

# 오픈소스 거버넌스 가이드의 표현

프로젝트가 커진 뒤 역할·의사결정·문서화를 어떻게 정할지 다룬 가이드. 규칙을 강제하지 않으면서도
**무엇이 필요하고 무엇은 필요 없는지를 딱 잘라 말하는** 문형이 많아 발췌했다. 팀 규칙을 정하거나
운영 원칙을 문서로 남길 때 그대로 쓸 틀만 골랐다.

> **원문** — GitHub 외, *Open Source Guides — Leadership and Governance*,
> [opensource.guide](https://opensource.guide/leadership-and-governance/)
> ([github.com/github/opensource.guide](https://github.com/github/opensource.guide/blob/main/_articles/leadership-and-governance.md)),
> [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) 라이선스.
>
> 영어 문장은 원문 그대로 인용했고, 한글 설명과 응용 문장은 이 노트에서 새로 쓴 것이다.

{{< sentence
  en="You don't need a legal entity to support your open source project unless you're handling money."
  ko="돈을 다루는 게 아니라면, 오픈소스 프로젝트를 운영하는 데 법인이 필요하지는 않다."
  source="Open Source Guides · Do I need a legal entity to support my project?"
  sourceURL="https://opensource.guide/leadership-and-governance/"
  note="`You don't need X unless Y` — **요건을 조건부로 면제하는** 문형이다. 핵심은 순서다. 먼저 '필요 없다'로 부담을 걷어 내고, `unless` 절에서 **딱 하나의 예외**만 붙인다. 반대로 쓴 `You need X only if Y`는 요건 쪽에 무게가 실려 여전히 겁을 준다. 과잉 절차를 걷어 낼 때 — 승인, 문서, 회의가 정말 언제부터 필요한지 못 박을 때 — 꺼내 쓴다."
  app1="You don't need a formal change request to deploy this unless it touches the payment path."
  app1ko="결제 경로를 건드리는 게 아니라면, 이걸 배포하는 데 정식 변경 요청서가 필요하지는 않다."
  app2="You don't need to page the on-call engineer for this alert unless the error rate stays above one percent for ten minutes."
  app2ko="오류율이 10분 넘게 1퍼센트를 웃도는 게 아니라면, 이 알림 때문에 온콜 엔지니어를 호출할 필요는 없다."
>}}

{{< sentence
  en="Documenting this information avoids the community perception that maintainers are a clique that makes its decisions privately."
  ko="이 정보를 문서로 남기면, 메인테이너가 자기들끼리 비공개로 결정하는 패거리라는 커뮤니티의 인식을 피할 수 있다."
  source="Open Source Guides · How do I formalize these leadership roles?"
  sourceURL="https://opensource.guide/leadership-and-governance/"
  note="어떤 행동의 이유를 **막게 되는 오해**로 설명하는 문형이다. 골격은 `Doing X avoids the perception that Y`. '문서화하면 투명해진다' 같은 좋은 말 대신, 문서화가 없을 때 사람들이 갖게 될 **구체적인 나쁜 인식**을 그대로 문장에 넣는 게 힘의 근원이다. `avoids the perception that ~`은 '사실이 아니다'라고 다투지 않고 인식 자체를 관리 대상으로 놓기 때문에, 실제로 억울한 상황에서도 각이 서지 않는다."
  app1="Publishing the on-call rotation avoids the perception that incidents are handled by whoever happens to be awake."
  app1ko="온콜 순번을 공개해 두면, 장애를 그때 깨어 있는 사람이 알아서 처리한다는 인식을 피할 수 있다."
  app2="Recording the rejected options in the design doc avoids the perception that the decision was made before the review even started."
  app2ko="검토에서 탈락한 선택지를 설계 문서에 남겨 두면, 리뷰가 시작되기도 전에 결론이 나 있었다는 인식을 피할 수 있다."
>}}

{{< sentence
  en="Paid developers shouldn't get special treatment over unpaid ones, of course; each contribution must be evaluated on its technical merits."
  ko="물론 보수를 받는 개발자가 그렇지 않은 개발자보다 특별 대우를 받아서는 안 된다. 기여는 하나하나 기술적 가치로 평가되어야 한다."
  source="Open Source Guides · What happens if corporate employees start submitting contributions?"
  sourceURL="https://opensource.guide/leadership-and-governance/"
  note="`A shouldn't get special treatment over B, of course; each C must be evaluated on its D` — **예외를 막고 곧바로 판단 기준을 세우는** 두 마디 구조다. 삽입된 `of course`가 '이건 굳이 다툴 일도 아니다'라는 뜻이라, 상대를 의심하지 않으면서도 선은 긋는다. 세미콜론 뒤가 진짜 알맹이다: 무엇을 하지 말라는 말로 끝내지 않고 **대신 무엇으로 판단할지**를 같은 문장 안에 넣는다. 금지만 남기면 다음 사람이 또 묻는다."
  app1="Changes from the platform team shouldn't get special treatment over anyone else's, of course; each pull request must be evaluated on the tests it ships with."
  app1ko="물론 플랫폼 팀이 올린 변경이 다른 사람의 변경보다 특별 대우를 받아서는 안 된다. 풀 리퀘스트는 하나하나 함께 올라온 테스트로 평가되어야 한다."
  app2="Findings raised by the vendor shouldn't get special treatment over ours, of course; each item must be evaluated on the evidence attached to it."
  app2ko="물론 외부 업체가 올린 지적이 우리 쪽 지적보다 특별 대우를 받아서는 안 된다. 항목은 하나하나 첨부된 근거로 평가되어야 한다."
>}}

{{< sentence
  en="There is no right time to write down your project's governance, but it's much easier to define once you've seen your community dynamics play out."
  ko="프로젝트의 거버넌스를 문서로 남기기에 옳은 시점이란 없다. 다만 커뮤니티가 실제로 어떻게 굴러가는지 본 뒤라면 정의하기가 훨씬 쉽다."
  source="Open Source Guides · Do I need governance docs when I launch my project?"
  sourceURL="https://opensource.guide/leadership-and-governance/"
  note="`There is no right time to X, but it's much easier to Y once Z` — **'언제 해야 하냐'는 질문에 시점을 정해 주지 않으면서 답하는** 문형이다. 앞마디가 정답이 없음을 인정해 미루는 사람을 몰아세우지 않고, `but` 뒤가 조건을 하나 얹어 실질적인 권고로 바뀐다. `play out`은 '계획대로 되다'가 아니라 **상황이 저절로 전개되어 드러나다**라는 뜻이라, 관찰이 필요하다는 뉘앙스를 정확히 만든다."
  app1="There is no right time to write the runbook, but it's much easier to write once you've watched the same alert fire three times."
  app1ko="런북을 쓰기에 옳은 시점이란 없다. 다만 같은 알림이 세 번 울리는 걸 본 뒤라면 쓰기가 훨씬 쉽다."
  app2="There is no right time to freeze the API, but it's much easier to freeze once you've seen how the first two integrations actually use it."
  app2ko="API를 고정하기에 옳은 시점이란 없다. 다만 처음 두 연동이 실제로 그걸 어떻게 쓰는지 본 뒤라면 고정하기가 훨씬 쉽다."
>}}

{{< sentence
  en="Keep your project discussions focused on the contributions, not on the external factors that enable people to make those contributions."
  ko="프로젝트 논의는 기여 자체에 초점을 맞춰라. 사람들이 그 기여를 할 수 있게 해 준 외부 요인이 아니라."
  source="Open Source Guides · What happens if corporate employees start submitting contributions?"
  sourceURL="https://opensource.guide/leadership-and-governance/"
  note="`Keep X focused on A, not on B` — **논의가 새려 할 때 초점을 되돌리는** 명령형이다. `Keep`은 `Focus on`과 달리 '지금 맞춰라'가 아니라 **'계속 그 자리에 두어라'**여서, 이미 옳은 방향에 있었다는 전제를 깔고 시작한다. 그래서 참견이 아니라 진행으로 들린다. `not on B`를 뒤에 붙여 무엇이 논외인지까지 못 박아 두면, 같은 곁가지가 다시 올라올 때 이 문장 하나로 끊을 수 있다."
  app1="Keep the postmortem focused on the sequence of events, not on who was holding the pager that night."
  app1ko="장애 회고는 사건의 순서에 초점을 맞춰라. 그날 밤 누가 호출기를 들고 있었느냐가 아니라."
  app2="Keep the review focused on what the code does, not on how long the author spent writing it."
  app2ko="리뷰는 코드가 무엇을 하는지에 초점을 맞춰라. 작성자가 그걸 쓰는 데 얼마나 오래 걸렸는지가 아니라."
>}}
