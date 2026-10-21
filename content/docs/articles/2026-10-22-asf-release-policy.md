---
title: 행위로 사실을 판정하고, 항변을 되받는 표현
description: 라벨이 아니라 행위로 사실을 판정하고, 불편하다는 항변을 다른 행동으로 되받고, 모호함을 인정한 뒤 결정권을 귀속시키고, 두 가치의 우선순위를 미리 공개하고, 현실적으로 길이 하나뿐임을 보이는 문장 5개.
weight: -62
date: 2026-10-22
source: "ASF · Release Policy"
sourceURL: https://www.apache.org/legal/release-policy.html
---

# 행위로 사실을 판정하고, 항변을 되받는 표현

아파치 소프트웨어 재단(ASF)이 모든 프로젝트에 적용하는 릴리스 정책. MUST/SHOULD로 요건을
늘어놓는 규범 문서인데, 뒤쪽 FAQ에서 **왜 이 규칙이 필요한지**를 같은 문서 안에서 직접
변호한다. 그래서 규칙을 들이대는 문장보다, 반론을 먼저 품은 뒤 결론을 다시 세우는 문장이
많다. 라벨 대신 실제 행위로 사실을 판정하는 방식과, 불편하다는 항변을 규칙 완화가 아닌
다른 행동으로 되받는 방식이 운영·거버넌스 문서에 그대로 옮겨 쓸 만해서 발췌했다.

> **원문** — The Apache Software Foundation, *Release Policy*,
> [apache.org/legal](https://www.apache.org/legal/release-policy.html)
> ([원본 리포지터리](https://github.com/apache/www-site/blob/main/content/legal/release-policy.md)),
> [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0).
>
> 영어 문장은 원문 그대로 인용했고, 한글 설명과 응용 문장은 이 노트에서 새로 쓴 것이다.

{{< sentence
  en="If the general public is being instructed to download a package, then that package has been released."
  ko="일반 대중에게 어떤 패키지를 내려받으라고 안내하고 있다면, 그 패키지는 이미 릴리스된 것이다."
  source="ASF Release Policy · What is a release?"
  sourceURL="https://www.apache.org/legal/release-policy.html#what"
  note="`If X is being instructed to ..., then Y has been Z.` — 선언이나 라벨이 아니라 **지금 실제로 벌어지고 있는 행위**로 사실을 판정하는 문형이다. 현재진행 수동 `is being instructed`가 '누가 의도했든 현재 그렇게 돌아가고 있다'를 가리키고, 뒤의 현재완료 `has been released`가 그 결과를 **이미 끝난 일**로 못 박는다. 그래서 우리는 릴리스라고 부르지 않았다는 항변이 끼어들 틈이 없다. 베타·내부 공개·프리뷰처럼 이름으로 책임을 비켜 가려는 상황에서 쓴다."
  app1="If on-call is being paged for it, then it is a production dependency, whatever the service tier says."
  app1ko="그것 때문에 온콜이 호출되고 있다면, 서비스 등급에 뭐라고 적혀 있든 그건 운영 의존성이다."
  app2="If customers are being told to use this endpoint, then it is a public API and it is now under our compatibility promise."
  app2ko="고객에게 이 엔드포인트를 쓰라고 안내하고 있다면, 그건 공개 API이고 이제 우리 호환성 약속의 대상이다."
>}}

{{< sentence
  en="Under no circumstances are unapproved builds a substitute for releases. If this policy seems inconvenient, then release more often."
  ko="어떤 경우에도 승인되지 않은 빌드가 릴리스를 대신할 수는 없다. 이 정책이 불편하게 느껴진다면, 더 자주 릴리스하라."
  source="ASF Release Policy · What is a release?"
  sourceURL="https://www.apache.org/legal/release-policy.html#what"
  note="앞 문장은 `Under no circumstances are A a substitute for B`로 **도치**를 써서 예외의 여지를 먼저 닫는다. `Under no circumstances`를 문장 머리로 올리면 조동사가 주어 앞으로 당겨 오고(`are unapproved builds`), 그 어순 자체가 '여기에 조건을 붙여 볼 생각은 하지 말라'는 신호가 된다. 뒤 문장 `If this policy seems inconvenient, then <더 자주 하라>`는 불편하다는 항변을 **규칙 완화가 아니라 빈도 조정**으로 되받는다. `seems`가 핵심인데, 불편함을 사실로 확정하지 않고 느낌으로 받아 두는 덕에 규칙 쪽은 한 치도 흔들리지 않는다."
  app1="Under no circumstances is a manual hotfix a substitute for a reviewed change. If the review queue seems slow, then split the change into smaller ones."
  app1ko="어떤 경우에도 수동 핫픽스가 리뷰를 거친 변경을 대신할 수는 없다. 리뷰 대기가 느리게 느껴진다면, 변경을 더 작게 쪼개라."
  app2="Under no circumstances is a screenshot a substitute for an exported audit log. If pulling the log seems tedious, then ask us to automate the export."
  app2ko="어떤 경우에도 스크린샷이 내보낸 감사 로그를 대신할 수는 없다. 로그를 뽑는 일이 번거롭게 느껴진다면, 내보내기를 자동화해 달라고 우리에게 요청하라."
>}}

{{< sentence
  en="Everyone will probably have a different definition of what an exceptional circumstance is, but ultimately it is down to individual PMCs to decide for their project."
  ko="예외적인 상황이 무엇인지에 대한 정의는 아마 사람마다 다를 것이다. 하지만 결국 자기 프로젝트에 대해 판단하는 것은 개별 PMC의 몫이다."
  source="ASF Release Policy · Expedited Releases"
  sourceURL="https://www.apache.org/legal/release-policy.html#expedited-releases"
  note="`Everyone will probably have a different definition of X, but ultimately it is down to Y to decide.` — 정의를 끝까지 좁히려 들지 않고 **모호함을 인정한 채 결정권만 분명히 귀속시키는** 문형이다. `will probably`가 다른 의견을 미리 품어 주어 '내 기준은 다르다'는 반박을 무력화하고, `ultimately`가 '그 논쟁이 끝나지 않아도 결론은 여기서 난다'로 넘긴다. `it is down to Y to decide`는 `Y decides`보다 결정의 **책임 소재**에 무게가 실린다. 기준을 문서로 다 적을 수 없는 판단, 가령 심각도 등급이나 긴급 배포 여부를 규정할 때 쓴다."
  app1="Everyone will probably have a different definition of what counts as a sev-1, but ultimately it is down to the on-call engineer to decide at the time."
  app1ko="무엇을 sev-1로 볼지에 대한 정의는 아마 사람마다 다를 것이다. 하지만 결국 그 순간에 판단하는 것은 온콜 담당자의 몫이다."
  app2="Everyone will probably have a different definition of what a blocking review comment is, but ultimately it is down to the code owner to decide for their area."
  app2ko="무엇이 머지를 막는 리뷰 코멘트인지에 대한 정의는 아마 사람마다 다를 것이다. 하지만 결국 자기 영역에 대해 판단하는 것은 코드 오너의 몫이다."
>}}

{{< sentence
  en="Do note however that organizationally we prefer robust, reviewable decision-making over efficient decision-making, so if you are thinking of proposing an alternative process for the board to consider, be sure your targets reflect this."
  ko="다만 조직 차원에서 우리는 효율적인 의사결정보다 견고하고 검토 가능한 의사결정을 선호한다는 점을 유념하라. 그러니 이사회가 검토할 다른 절차를 제안할 생각이라면, 목표가 이 점을 반영하게 하라."
  source="ASF Release Policy · Why do we need a Foundation-wide policy?"
  sourceURL="https://www.apache.org/legal/release-policy.html#why"
  note="`we prefer A over B, so if you are thinking of proposing ..., be sure your targets reflect this.` — **두 가치의 우선순위를 미리 공개해 상대 제안의 전제를 깔아 주는** 문형이다. B(효율)를 나쁘다고 깎지 않고 순위만 매기는 것이 핵심이고, `Do note however that`은 바로 앞에서 인정한 불편함을 받아 단서를 다는 공손한 전환이다. 끝이 반대 표명이 아니라 `be sure your targets reflect this`, 즉 **제안서를 다시 쓰라는 지시**라서 문을 닫지 않고도 기준을 강제한다. 설계 리뷰에서 제안 자체를 막지 않으면서 평가 축을 먼저 못 박을 때 쓴다."
  app1="Do note however that as a team we prefer reversible changes over fast ones, so if you are thinking of proposing a big-bang migration, be sure your plan reflects this."
  app1ko="다만 팀 차원에서 우리는 빠른 변경보다 되돌릴 수 있는 변경을 선호한다는 점을 유념하라. 그러니 한 번에 전환하는 마이그레이션을 제안할 생각이라면, 계획이 이 점을 반영하게 하라."
  app2="Do note however that we prefer explicit configuration over inferred defaults, so if you are thinking of proposing auto-detection here, be sure the design reflects this."
  app2ko="다만 우리는 추론된 기본값보다 명시적인 설정을 선호한다는 점을 유념하라. 그러니 여기에 자동 탐지를 제안할 생각이라면, 설계가 이 점을 반영하게 하라."
>}}

{{< sentence
  en="Practically speaking, when a release consists of anything beyond an archive (e.g., tarball or zip file) of a source control tag, the only practical way to validate that archive is to build it locally; manually inspecting generated files (especially binary files) is not feasible."
  ko="현실적으로 말하면, 릴리스가 소스 관리 태그의 아카이브(예: tarball이나 zip 파일)를 넘는 무언가를 담는 순간, 그 아카이브를 검증할 유일한 현실적 방법은 로컬에서 직접 빌드해 보는 것이다. 생성된 파일(특히 바이너리 파일)을 수동으로 들여다보는 것은 가능한 일이 아니다."
  note="원칙론(`Strictly speaking`)을 먼저 적고 현실의 답을 `Practically speaking`으로 따로 적는 짝 구조의 뒷짝이다. `the only practical way to X is to Y`로 길을 하나로 좁히고, 세미콜론 뒤에서 **배제한 대안이 왜 불가능한지**를 곧바로 붙인다. 여기서 `is not feasible`은 금지가 아니라 **해 봐도 안 된다는 실행 가능성의 부정**이어서, 상대의 성의를 깎지 않고도 그 방법을 접게 만든다. 수동 점검으로 버티는 관행을 두고 자동화나 재현 빌드가 왜 필요한지 설명할 때 쓴다."
  source="ASF Release Policy · Must releases be built on hardware owned and controlled by the committer?"
  sourceURL="https://www.apache.org/legal/release-policy.html#owned-controlled-hardware"
  app1="Practically speaking, when a dashboard pulls from more than one data source, the only practical way to trust a number is to recompute it from the raw events; eyeballing the panels is not feasible."
  app1ko="현실적으로 말하면, 대시보드가 두 개 이상의 데이터 소스에서 값을 끌어오는 순간, 어떤 수치를 신뢰할 유일한 현실적 방법은 원시 이벤트에서 다시 계산해 보는 것이다. 패널을 눈으로 훑는 것은 가능한 일이 아니다."
  app2="Practically speaking, when a change touches generated code, the only practical way to review it is to regenerate and diff; reading the generated lines by hand is not feasible."
  app2ko="현실적으로 말하면, 변경이 생성된 코드를 건드리는 순간, 그것을 리뷰할 유일한 현실적 방법은 다시 생성해서 차이를 보는 것이다. 생성된 줄들을 손으로 읽는 것은 가능한 일이 아니다."
>}}
