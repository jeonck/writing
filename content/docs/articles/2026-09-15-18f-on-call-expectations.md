---
title: 지칠 사람을 전제로 미리 정해 두는 표현
description: 아직 모호할 때 논의를 시작하고, 이상과 현실의 간격을 인정하고, 사람이 잊는다는 사실을 근거로 삼고, 책임이 어디서 끝나는지 못 박고, 무엇부터 연습할지 고르는 문장 5개.
weight: -26
date: 2026-09-15
source: "18F Engineering Practices Guide — On-call recommendations"
sourceURL: https://github.com/18F/guides/blob/main/content/engineering/our-approach/on-call.md
---

# 지칠 사람을 전제로 미리 정해 두는 표현

미국 연방정부 디지털 서비스 조직 18F/TTS의 엔지니어링 가이드 중 *On-call recommendations*는
온콜 당번을 어떻게 세우는지가 아니라, **당번이 서기 훨씬 전에 무엇을 합의해 두어야 하는지**를
인력 배치·개발·지원 단계로 나누어 적은 문서다. 규격서가 아니라 팀에게 건네는 권고문이라
요구를 꺼내는 방식이 조심스럽고, 그래서 **아직 정해지지 않은 것을 인정하면서도 지금 할 일을
꺼내는 문형**이 곳곳에 있다. 모호함을 먼저 인정하고 대화를 시작하자고 하고, 이상적인 배치가
아님을 스스로 말한 뒤 보완책을 붙이고, 사람이 지치면 뻔한 것도 잊는다는 사실을 제도의 근거로
삼고, 책임이 어디서 끝나는지를 선택지로 쪼개 못 박는다. **온콜 합의문, 인수인계, 사후 회고,
훈련 시나리오 선정, 팀 내 제안서**에 그대로 옮겨 쓸 다섯 문장을 골랐다.

> **원문** — 18F/TTS Engineering Practices Guild, *On-call recommendations*,
> [`18F/guides` · `content/engineering/our-approach/on-call.md`](https://github.com/18F/guides/blob/main/content/engineering/our-approach/on-call.md)
> (게시본 경로: `guides.18f.gov/engineering/our-approach/on-call/`).
> 미국 연방정부의 저작물로 퍼블릭 도메인이며,
> [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/)으로도 권리를 포기해 두었다.
>
> 영어 문장은 원문 그대로 인용했고, 한글 설명과 응용 문장은 이 노트에서 새로 쓴 것이다.

{{< sentence
  en="The shape of support may not be clear this early in the product life cycle, but starting those conversations now will guide what kind of documentation and telemetry needs to be built into the project."
  ko="제품 생애주기의 이렇게 이른 시점에는 지원의 모습이 아직 분명하지 않을 수 있지만, 지금 그 대화를 시작해 두면 프로젝트에 어떤 문서와 텔레메트리를 넣어야 하는지가 정해진다."
  source="18F Engineering Practices Guide · On-call recommendations"
  sourceURL="https://github.com/18F/guides/blob/main/content/engineering/our-approach/on-call.md"
  note="`X may not be clear this early, but starting those conversations now will guide Y.` — '아직 결론이 안 났으니 나중에 이야기하자'에 대응하는 문형이다. 앞 절에서 **모호함을 먼저 인정해** 상대의 반박을 미리 흡수하고, 뒤 절에서 대화의 결과를 '결정'이 아니라 `guide`(방향을 잡아 준다)로 한 칸 낮춰 잡는다. 그래서 '지금 정하자'가 아니라 '지금 이야기해 두면 나중 작업이 덜 흔들린다'로 들려 거절하기 어렵다. `this early`가 붙어 있어 영구적인 유보가 아니라 **지금 단계의 한계**라는 뜻도 살아난다. 설계 착수, 온콜 도입, 관측 체계 논의처럼 요구사항이 덜 여문 상태에서 첫 회의를 잡을 때 쓴다."
  app1="The exact SLO may not be clear this early in the migration, but agreeing on what counts as an error now will guide which metrics we emit."
  app1ko="마이그레이션 초기라 정확한 SLO는 아직 분명하지 않을 수 있지만, 무엇을 오류로 볼지 지금 합의해 두면 어떤 지표를 내보낼지가 정해진다."
  app2="The final approval process may not be clear this early, but deciding now who has to sign off on a schema change will guide how we split the pull requests."
  app2ko="최종 승인 절차는 지금 단계에서 분명하지 않을 수 있지만, 스키마 변경을 누가 승인해야 하는지 지금 정해 두면 PR을 어떻게 쪼갤지가 정해진다."
>}}

{{< sentence
  en="In an ideal world, the folks providing support will be the same folks who have been working on the product. While we don't often live in an ideal world, doing the work to make support seamless for team members will also set external support people up for success!"
  ko="이상적인 세상이라면 지원을 맡는 사람은 그 제품을 만들어 온 사람과 같을 것이다. 우리가 이상적인 세상에 사는 일은 드물지만, 팀원에게 지원이 매끄럽도록 공들여 두면 외부 지원 인력에게도 성공할 발판이 된다."
  source="18F Engineering Practices Guide · Support phase"
  sourceURL="https://github.com/18F/guides/blob/main/content/engineering/our-approach/on-call.md"
  note="`In an ideal world, X. While we don't often live in an ideal world, doing Y will also Z.` — 이상적인 전제를 먼저 말해 두고, **그 전제가 대개 맞지 않는다는 것을 스스로 인정한 뒤**, 그래도 해 둘 일을 제안하는 3단 구조다. `In an ideal world`는 '원래 이래야 한다'를 누구를 탓하지 않고 꺼내는 장치이고, `While we don't often live in ~`가 현실을 인정하며 논쟁을 닫아 버린다. 무게는 마지막 `also`에 실린다 — 원래 목적(팀원이 편하도록)에 **부수 효과가 하나 더 붙는다**는 뜻이라, 차선책이 손해가 아니라 이득으로 읽힌다. 내부 문서라 느낌표까지 붙은 구어체지만 구조는 그대로 격식 있는 제안서에 들어간다. 인수인계, 외주 전환, 당직 확대처럼 **최선이 아닌 배치를 받아들이며 보완책을 붙일 때** 쓴다."
  app1="In an ideal world, the engineer who wrote the migration would be the one to run it. While we don't often live in an ideal world, writing the rollback steps down will also make the review easier."
  app1ko="이상적인 세상이라면 마이그레이션을 작성한 엔지니어가 직접 실행할 것이다. 현실이 그렇지 못한 경우가 많지만, 롤백 절차를 적어 두면 리뷰까지 쉬워진다."
  app2="In an ideal world, every alert would be reviewed by the team that owns the service. While we don't often live in an ideal world, naming a fallback owner for each alert will also show us which services have no owner at all."
  app2ko="이상적인 세상이라면 모든 알림은 그 서비스를 맡은 팀이 검토할 것이다. 현실은 그렇지 않은 경우가 많지만, 알림마다 대리 담당자를 지정해 두면 아예 주인이 없는 서비스가 어디인지도 드러난다."
>}}

{{< sentence
  en="Even developers deeply knowledgeable about the product may forget obvious things to check if they are tired or stressed about a highly visible incident."
  ko="제품을 깊이 아는 개발자라도 지쳐 있거나 눈에 띄는 장애로 긴장한 상태라면 확인해야 할 뻔한 것들을 잊을 수 있다."
  source="18F Engineering Practices Guide · Support phase"
  sourceURL="https://github.com/18F/guides/blob/main/content/engineering/our-approach/on-call.md"
  note="`Even X may forget obvious things if they are tired or stressed.` — 체크리스트나 런북이 왜 필요하냐는 물음에 **역량이 아니라 조건으로** 답하는 문형이다. 주어를 일부러 `developers deeply knowledgeable about the product`처럼 **가장 잘하는 사람**으로 잡는 것이 이 문장의 기술이다. 제일 잘 아는 사람도 그렇다면 나머지는 말할 것도 없고, 동시에 누구를 지목한 것도 아니게 된다. `obvious things`는 '기본적인 것조차'라는 대비를 키우고, `may`는 단정 대신 가능성으로 남겨 반박할 거리를 없앤다. 사후 회고에서 **사람 탓을 피하면서 제도를 요구할 때**, 자동화·체크리스트·2인 확인을 제안할 때 쓴다."
  app1="Even reviewers who know this service well may miss a dropped index if the pull request lands at the end of a long day."
  app1ko="이 서비스를 잘 아는 리뷰어라도 긴 하루의 끝에 올라온 PR이라면 인덱스가 빠진 것을 놓칠 수 있다."
  app2="Even an experienced operator may skip a verification step if the runbook is long and the pager is still going off."
  app2ko="경험 많은 운영자라도 런북이 길고 호출이 계속 울리는 상황이라면 확인 절차를 건너뛸 수 있다."
>}}

{{< sentence
  en="The person on-call should know definitively what is expected of them in different types of scenarios, and whether they are in charge of troubleshooting, fully resolving or escalating an incident."
  ko="온콜을 맡은 사람은 상황 유형별로 자신에게 무엇이 기대되는지, 그리고 자신이 맡은 것이 원인 파악인지 완전한 해결인지 아니면 에스컬레이션인지를 확실하게 알고 있어야 한다."
  source="18F Engineering Practices Guide · Establish scope of support"
  sourceURL="https://github.com/18F/guides/blob/main/content/engineering/our-approach/on-call.md"
  note="`A should know definitively what is expected of them, and whether they are in charge of X, Y or Z.` — 책임을 '맡는다 / 안 맡는다'가 아니라 **어디까지 맡는지**로 쪼개 적는 문형이다. `definitively`는 '알고는 있다'와 '확실히 안다'를 가르는 단어로, 구두 합의 정도로는 부족하다는 요구가 부사 하나에 담긴다. 진짜 일은 뒤쪽 `whether ... X, Y or Z`가 한다 — 단계를 셋 나란히 놓으면 읽는 사람이 **자기 위치를 하나 골라야** 하므로 '알아서 잘 하기'라는 답이 불가능해진다. 온콜 합의문, 위임 문서, 인수인계, 리뷰어 역할 정의에 그대로 옮겨 쓴다."
  app1="Whoever takes the alert should know definitively what is expected of them at 3 a.m., and whether they are in charge of restarting the service, rolling back the release or waking the service owner."
  app1ko="알림을 받는 사람은 새벽 3시에 자신에게 무엇이 기대되는지, 그리고 맡은 것이 서비스 재시작인지 릴리스 롤백인지 아니면 서비스 담당자를 깨우는 일인지를 확실하게 알고 있어야 한다."
  app2="A reviewer should know definitively what is expected of them on a security-sensitive change, and whether they are in charge of checking the logic, approving the new dependency or requesting a formal audit."
  app2ko="리뷰어는 보안에 민감한 변경에서 자신에게 무엇이 기대되는지, 그리고 맡은 것이 로직 확인인지 새 의존성 승인인지 아니면 정식 감사 요청인지를 확실하게 알고 있어야 한다."
>}}

{{< sentence
  en="Prioritize events that are likely to happen within the context of your system and have outsized impacts."
  ko="당신의 시스템이라는 맥락 안에서 일어날 법하고, 영향이 유난히 큰 사건을 우선하라."
  source="18F Engineering Practices Guide · Test and iterate your support guides with simulations"
  sourceURL="https://github.com/18F/guides/blob/main/content/engineering/our-approach/on-call.md"
  note="`Prioritize X that are likely to happen within the context of your system and have outsized impacts.` — 우선순위를 **두 축의 교집합**으로 정의하는 문형이다. 가능성만 기준으로 삼으면 사소한 일이 목록 위로 올라오고, 영향만 기준으로 삼으면 일어나지도 않을 종말 시나리오가 올라온다. `and`로 묶어 둘 다 만족하는 것만 남기는 것이 이 문장이 하는 일이다. `within the context of your system`은 남의 사고 목록을 그대로 베끼지 말라는 제한이고, `outsized`는 `large`와 달리 **규모에 어울리지 않게 크다**는 불균형을 가리켜 '큰 사고'가 아니라 '작은 원인에 비해 큰 사고'를 집어낸다. 훈련 시나리오 선정, 위협 모델, 테스트 항목, 백로그 정리처럼 **목록이 길어져 고르지 못할 때** 기준 문장으로 쓴다."
  app1="Prioritize failure modes that are likely to happen within the context of our deployment and have outsized impacts on checkout."
  app1ko="우리 배포 환경이라는 맥락 안에서 일어날 법하고, 결제에 유난히 큰 영향을 주는 실패 유형을 우선하라."
  app2="Prioritize the audit findings that are likely to be reachable within the context of this service and have outsized impacts on customer data."
  app2ko="이 서비스라는 맥락 안에서 실제로 닿을 수 있고, 고객 데이터에 유난히 큰 영향을 주는 감사 지적 사항을 우선하라."
>}}
