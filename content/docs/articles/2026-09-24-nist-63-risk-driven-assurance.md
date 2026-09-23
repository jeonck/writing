---
title: 위험 평가가 기술 선택을 이끈다고 말하는 표현
description: 인과의 방향을 되돌리고, 고정된 것과 조정할 수 있는 것을 갈라 놓고, 요구의 최소선만 남기는 문장 5개.
weight: -34
date: 2026-09-24
source: "NIST SP 800-63-3 §5"
sourceURL: https://pages.nist.gov/800-63-3/sp800-63-3.html#sec5
---

# 위험 평가가 기술 선택을 이끈다고 말하는 표현

미국 NIST의 디지털 신원 지침(SP 800-63-3) 중 **위험 관리**를 다루는 5장. 신원 확인·인증·페더레이션의
보증 수준을 각각 따로 평가하라고 요구하면서, 그 판정을 어디까지 조정할 수 있고 어디부터는 손댈 수
없는지를 문장으로 못 박는다. 규정문이라 톤이 딱딱한데, 그 덕에 **의무와 재량을 구분하는 문형**이 선명하게
드러나 발췌했다.

> **원문** — Paul A. Grassi, Michael E. Garcia, James L. Fenton, *Digital Identity Guidelines*,
> [NIST Special Publication 800-63-3](https://pages.nist.gov/800-63-3/sp800-63-3.html) (2017,
> includes updates as of 2020-03-02), 미국 연방정부 간행물로 미국 내 저작권 보호 대상이 아니며
> NIST가 전 세계에 무상·비독점 재수록 권리를 부여한다
> ([NIST Technical Series Publications 라이선스](https://github.com/usnistgov/800-63-3/blob/nist-pages/LICENSE.md)).
> Republished courtesy of the National Institute of Standards and Technology.
>
> 영어 문장은 원문 그대로 인용했고, 한글 설명과 응용 문장은 이 노트에서 새로 쓴 것이다.

{{< sentence
  en="Risk assessments determine the extent to which risk must be mitigated by the identity proofing, authentication, and federation processes. These determinations drive the relevant choices of applicable technologies and mitigation strategies, rather than the desire for any given technology driving risk determinations."
  ko="위험 평가는 신원 확인·인증·페더레이션 절차가 위험을 어느 정도까지 완화해야 하는지를 정한다. 적용할 기술과 완화 전략의 선택을 이끄는 것은 그 판정이며, 특정 기술을 쓰고 싶다는 욕구가 위험 판정을 이끄는 것이 아니다."
  source="NIST SP 800-63-3 · 5.1 Overview"
  sourceURL="https://pages.nist.gov/800-63-3/sp800-63-3.html#5-1-overview"
  note="`A drives B, rather than C driving A.` — **인과의 방향을 되돌려 놓는** 문형이다. `rather than` 뒤에 동명사 절을 통째로 넣어 뒤집힌 순서를 한 번 보여 준 다음 부정하므로, 잘못된 관행을 직접 비난하지 않고 어순만으로 드러낸다. 열쇠는 `the desire for any given technology`다 — 사람을 주어로 세우지 않고 '쓰고 싶은 마음'을 주어로 만들어, 누구도 지목하지 않은 채 문제를 지목한다. 도구를 먼저 정해 놓고 요건을 거기에 맞추는 일을 지적할 때 그대로 쓴다."
  app1="The incident timeline drives which alerts we add, rather than the dashboard we already bought driving the timeline."
  app1ko="어떤 알림을 추가할지 이끄는 것은 장애 타임라인이며, 이미 사 둔 대시보드가 타임라인을 이끄는 것이 아니다."
  app2="The threat model drives the choice of scanner, rather than the scanner we happen to have a license for driving the threat model."
  app2ko="스캐너 선택을 이끄는 것은 위협 모델이며, 마침 라이선스를 가진 스캐너가 위협 모델을 이끄는 것이 아니다."
>}}

{{< sentence
  en="Authentication, proofing, and federation errors with potentially worse consequences require higher levels of assurance."
  ko="결과가 더 나쁠 수 있는 인증·신원 확인·페더레이션 오류에는 더 높은 보증 수준이 필요하다."
  source="NIST SP 800-63-3 · 5.3 Risk and Impacts"
  sourceURL="https://pages.nist.gov/800-63-3/sp800-63-3.html#section5-3"
  note="`X with potentially worse consequences require higher Y.` — 등급 체계의 규칙을 **한 문장으로 못 박는** 비례 진술. 비교급 두 개(`worse` / `higher`)를 짝지어 두면 개별 등급을 설명하지 않고도 등급을 나누는 기준 자체를 말해 버릴 수 있다. 톤을 결정하는 단어는 `potentially`다. 이미 벌어진 결과가 아니라 **벌어질 수 있는 결과**를 재라는 뜻이어서, 이 단어를 빼면 사고가 난 뒤에만 등급을 올릴 수 있다는 말이 된다."
  app1="Changes with a potentially worse blast radius require more reviewers and a longer soak time."
  app1ko="영향 범위가 더 나빠질 수 있는 변경에는 리뷰어를 더 붙이고 관찰 시간을 더 길게 잡아야 한다."
  app2="Findings with potentially worse downstream impact require a named owner and a due date, not just a ticket."
  app2ko="후속 영향이 더 나쁠 수 있는 지적 사항에는 티켓만이 아니라 담당자 이름과 기한이 필요하다."
>}}

{{< sentence
  en="That said, agencies SHALL NOT alter the assessed xAL based on agency capabilities. Rather, the agency MAY adjust their implementation of solutions based on the agency's ability to mitigate risk via means not explicitly addressed by SP 800-63 requirements."
  ko="다만 기관은 자신의 역량을 근거로 평가된 xAL을 바꿔서는 안 된다. 대신 기관은, SP 800-63 요건이 명시적으로 다루지 않은 수단으로 위험을 완화할 수 있는 자신의 능력에 따라 해결책의 구현 방식을 조정할 수 있다."
  source="NIST SP 800-63-3 · 5.4 Risk Acceptance and Compensating Controls"
  sourceURL="https://pages.nist.gov/800-63-3/sp800-63-3.html#risk"
  note="`That said, you SHALL NOT alter A. Rather, you MAY adjust B.` — **고정된 것과 조정할 수 있는 것을 갈라 놓는** 문형이다. `That said`로 시작하는 게 핵심이다: 바로 앞에서 대안을 허용해 놓고, 그 허용이 어디까지인지 곧바로 잘라 낸다. 대비의 축은 조동사 두 개다 — `SHALL NOT`은 **판정**에 붙고 `MAY`는 **구현**에 붙는다. 역량이 부족하다고 기준을 낮추는 일과, 같은 목표를 다른 방법으로 달성하는 일을 구분해 말해야 할 때 쓴다."
  app1="That said, we do not lower the severity because the on-call rotation was short-staffed. Rather, we adjust how the fix is rolled out based on what the team can safely ship this week."
  app1ko="다만 온콜 인원이 부족했다는 이유로 심각도를 낮추지는 않는다. 대신 이번 주에 팀이 안전하게 낼 수 있는 범위에 맞춰 수정 배포 방식을 조정한다."
  app2="That said, reviewers do not relax the merge criteria because a release date is close. Rather, they may reduce the scope of what goes into that release."
  app2ko="다만 릴리스 날짜가 가깝다고 병합 기준을 느슨하게 하지는 않는다. 대신 그 릴리스에 들어갈 범위를 줄일 수 있다."
>}}

{{< sentence
  en="The guidance does not prescribe that any migration needs to occur, only that it be considered as revisions are released."
  ko="이 지침은 마이그레이션이 반드시 일어나야 한다고 규정하지 않는다. 개정판이 나올 때 그것을 검토하라고만 규정한다."
  source="NIST SP 800-63-3 · 5.6 Migrating Identities"
  sourceURL="https://pages.nist.gov/800-63-3/sp800-63-3.html#sec5"
  note="`X does not prescribe that A, only that B.` — 요구 사항의 **최소선만 남기는** 문형. 앞에서 한 번 부정하고 `only that`으로 남길 것만 남기므로, 무엇이 의무가 아니고 무엇이 의무인지가 한 문장에서 동시에 정리된다. `only that it be considered`의 `be`는 `should`가 생략된 가정법이라 규정문 특유의 딱딱한 톤을 만든다. 정책을 쓸 때도, 남의 정책을 인용하면서 과잉 해석을 막을 때도 그대로 쓴다."
  app1="The policy does not prescribe that the key be rotated every quarter, only that the date of the last rotation be recorded."
  app1ko="이 정책은 키를 분기마다 교체하라고 규정하지 않는다. 마지막 교체 날짜를 기록하라고만 규정한다."
  app2="Our review guide does not prescribe that every comment be resolved before merge, only that the unresolved ones be answered."
  app2ko="우리 리뷰 가이드는 병합 전에 모든 코멘트를 해결하라고 규정하지 않는다. 해결되지 않은 코멘트에는 답을 달라고만 규정한다."
>}}

{{< sentence
  en="If an error in the identity system causes no measurable consequences for a category, there is no impact."
  ko="신원 시스템의 오류가 어떤 범주에 측정 가능한 결과를 전혀 일으키지 않는다면, 그 범주에는 영향이 없다."
  source="NIST SP 800-63-3 · 5.3.2 Impacts per Category"
  sourceURL="https://pages.nist.gov/800-63-3/sp800-63-3.html#section5-3"
  note="`If X causes no measurable consequences for A, there is no impact.` — 평가 항목에 **0을 허용한다고 명시하는** 문형이다. 등급표를 만들면 사람들은 모든 칸을 '낮음' 이상으로 채우려 들기 때문에, '없음'이라는 값을 공식적으로 열어 주는 한 줄이 필요하다. 톤을 결정하는 단어는 `measurable`이다. 막연한 불안을 배제하고 **셀 수 있는 결과**만 세라는 뜻이어서, 이 단어 하나가 위험 평가가 무한히 부풀지 않게 막아 준다."
  app1="If a failed job causes no measurable consequences for the customer, it is not an incident; it is a backlog item."
  app1ko="실패한 작업이 고객에게 측정 가능한 결과를 전혀 일으키지 않으면, 그것은 장애가 아니라 백로그 항목이다."
  app2="If the finding causes no measurable consequences for any data we actually store, there is no risk to accept."
  app2ko="그 지적 사항이 우리가 실제로 저장하는 데이터에 측정 가능한 결과를 전혀 일으키지 않는다면, 수용할 위험 자체가 없다."
>}}
