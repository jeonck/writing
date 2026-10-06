---
title: 신고를 가르고 권고의 수위를 조절하는 표현
description: 라벨과 실체를 가르고, 역할을 한 단어로 못 박고, 수단이 막는 것과 못 막는 것을 한 문장에 담고, 금지 대신 기본값에서 내리고, 기한 연장의 조건을 먼저 적는 문장 5개.
weight: -47
date: 2026-10-07
source: "OpenSSF 취약점 공개 가이드 · Maintainer Guide"
sourceURL: https://github.com/ossf/oss-vulnerability-guide/blob/main/maintainer-guide.md
---

# 신고를 가르고 권고의 수위를 조절하는 표현

오픈소스 프로젝트가 외부에서 들어온 취약점 신고를 어떻게 받아 분류하고, 비공개로
고치고, 공개까지 조율하는지 적어 둔 가이드다. 보안 지식이 아니라 **남이 가져온 신고를
다루는 글의 말투**를 골랐다 — 신고를 부정하지 않으면서 분류하고, 역할을 정하고, 쓰는
수단의 한계를 미리 적고, 금지하지 않으면서 권하지 않고, 상대에게 시간을 더 달라고 하는
문장들이다.

> **원문** — OpenSSF Vulnerability Disclosures Working Group, *Guide to implementing a
> coordinated vulnerability disclosure process for open source projects*,
> [ossf/oss-vulnerability-guide](https://github.com/ossf/oss-vulnerability-guide/blob/main/maintainer-guide.md)
> ([발행 사이트](https://oss-vulnerability-guide.openssf.org/)),
> [CC BY 4.0](https://github.com/ossf/oss-vulnerability-guide/blob/main/LICENSE.md).
>
> 영어 문장은 원문 그대로 인용했고, 한글 설명과 응용 문장은 이 노트에서 새로 쓴 것이다.

{{< sentence
  en="Not everything reported as a vulnerability is a vulnerability."
  ko="취약점이라고 신고된 것이 전부 취약점인 것은 아니다."
  source="OpenSSF 취약점 공개 가이드 · Response process"
  sourceURL="https://github.com/ossf/oss-vulnerability-guide/blob/main/maintainer-guide.md#response-process"
  note="`Not everything reported as X is X.` — 같은 명사를 두 번 쓰면서 앞의 것에만 `reported as`를 붙여 **라벨과 실체를 가르는** 부분 부정이다. 부정하는 대상이 신고자가 아니라 라벨이라는 점이 이 문장의 전부다: `Many reports are wrong`이라고 쓰면 사람을 탓하게 되지만, 이 형태는 접수와 판정이 서로 다른 단계라는 사실만 말한다. 그래서 판정 기준(`something is X if ~`)을 꺼내기 **직전**에 놓는 문장이다."
  app1="Not everything reported as an outage is an outage, so the first thing the on-call engineer does is decide which bucket the page belongs in."
  app1ko="장애라고 신고된 것이 전부 장애인 것은 아니다. 그래서 온콜 담당자가 가장 먼저 하는 일은 그 호출이 어느 분류에 들어가는지 정하는 것이다."
  app2="Not everything the scanner reports as a finding is a finding, and the audit trail should record which ones we closed as accepted risk."
  app2ko="스캐너가 지적 사항이라고 보고한 것이 전부 지적 사항인 것은 아니다. 그리고 그중 어떤 것을 위험 수용으로 닫았는지는 감사 기록에 남아야 한다."
>}}

{{< sentence
  en="The VMT's primary responsibility is coordination: they will be the reporters' point of contact throughout the process, keep the reporters informed (if they'd like to be), and keep the security issue moving through the process."
  ko="취약점 관리팀(VMT)의 첫 번째 책임은 조율이다. 과정 내내 신고자의 연락 창구가 되고, (원한다면) 신고자에게 상황을 계속 알리고, 보안 이슈가 과정을 따라 계속 굴러가게 한다."
  source="OpenSSF 취약점 공개 가이드 · Create a vulnerability management team (VMT)"
  sourceURL="https://github.com/ossf/oss-vulnerability-guide/blob/main/maintainer-guide.md#create-a-vulnerability-management-team-vmt"
  note="`X's primary responsibility is Y: they will A, B, and C.` — 역할을 **추상명사 하나로 못 박고**, 콜론 뒤에서 그 단어가 실제로 하는 일을 동사 셋으로 푸는 구조다. `primary`가 일을 줄여 주지는 않는다. 다른 일을 안 한다는 뜻이 아니라 **무엇이 먼저인지**를 정하는 말이라, 역할이 넓은 자리를 적을 때 과장 없이 쓸 수 있다. 서술이 `they will ~`인 것도 의도적이다. `must`로 쓰면 규정이 되고, `will`로 쓰면 팀이 하겠다는 약속으로 읽힌다. 상대 의사에 달린 항목은 `(if they'd like to be)`처럼 괄호로 조용히 표시해 둔다."
  app1="The incident commander's primary responsibility is coordination: they will be the single point of contact for the business side, keep the responders informed, and keep the incident moving toward mitigation."
  app1ko="인시던트 커맨더의 첫 번째 책임은 조율이다. 비즈니스 쪽의 단일 연락 창구가 되고, 대응자들에게 상황을 계속 알리고, 장애가 완화 쪽으로 계속 굴러가게 한다."
  app2="The release shepherd's primary responsibility is coordination: they will collect the sign-offs, keep the on-call team informed (if there is anything to act on), and keep the rollout moving through the stages."
  app2ko="릴리스 담당자의 첫 번째 책임은 조율이다. 승인을 모으고, (대응할 일이 있으면) 온콜 팀에 알리고, 배포가 단계를 따라 계속 굴러가게 한다."
>}}

{{< sentence
  en="STARTTLS attempts to switch to encrypted communication, and thus counters passive monitoring, but because it is opportunistic it is weak against active attacks."
  ko="STARTTLS는 암호화된 통신으로 전환하려 시도하며, 그래서 수동적 감시는 막아 주지만, 기회주의적으로 동작하기 때문에 능동적 공격에는 약하다."
  source="OpenSSF 취약점 공개 가이드 · Accepting vulnerability reports via email"
  sourceURL="https://github.com/ossf/oss-vulnerability-guide/blob/main/maintainer-guide.md#accepting-vulnerability-reports-via-email-with-hop-to-hop-encryption"
  note="`X attempts to A, and thus counters B, but because it is C it is weak against D.` — **한 수단이 막는 것과 못 막는 것을 한 문장에** 담는 틀이다. 시작부터 `attempts to`인 것이 핵심이다. `switches to`라고 썼으면 전환이 보장된다는 뜻이 되는데, 보장되지 않는 동작이라는 사실을 동사에서 이미 밝혀 두고 들어간다. `and thus`는 효과를 동작에서 끌어내고, `but because it is ~`는 한계를 **성질**에서 끌어낸다 — 못 막는 것이 결함이 아니라 설계가 그렇게 생겼다는 말이 된다. 보안 감사에서 '쓰고는 있지만 여기까지는 못 막는다'를 변명처럼 들리지 않게 적을 때."
  app1="Rate limiting at the edge attempts to shed load before it reaches the service, and thus counters accidental retry storms, but because it is per-instance it is weak against a client that spreads the same burst across every pod."
  app1ko="엣지의 요청 제한은 부하가 서비스에 닿기 전에 떨어뜨리려 시도하며, 그래서 실수로 생긴 재시도 폭주는 막아 주지만, 인스턴스 단위로 동작하기 때문에 같은 양을 모든 파드에 흩어 보내는 클라이언트에는 약하다."
  app2="The staging smoke test attempts to exercise the new path end to end, and thus counters obvious regressions, but because it runs on seeded data it is weak against bugs that only appear with production-shaped rows."
  app2ko="스테이징 스모크 테스트는 새 경로를 끝에서 끝까지 한 번 태워 보려 시도하며, 그래서 눈에 띄는 회귀는 막아 주지만, 심어 둔 데이터 위에서 돌기 때문에 운영 데이터 모양에서만 드러나는 버그에는 약하다."
>}}

{{< sentence
  en="Running private mirrors can be done, but we do not recommend this as the default."
  ko="비공개 미러를 운영하는 것도 할 수는 있지만, 우리는 이것을 기본값으로 권하지는 않는다."
  source="OpenSSF 취약점 공개 가이드 · Enable private patch development"
  sourceURL="https://github.com/ossf/oss-vulnerability-guide/blob/main/maintainer-guide.md#enable-private-patch-development"
  note="`X can be done, but we do not recommend this as the default.` — **금지하지 않으면서 선택지를 뒤로 미루는** 문형이다. 앞은 수동태 `can be done`이라 주어가 비어 있다. 누가 하든 가능하다는 허용만 남기고 사람을 지목하지 않는다. 뒤는 반대로 `we`를 드러낸다. 권고에는 출처가 있어야 하기 때문이다. 문장을 결정하는 말은 마지막 `as the default`다. `do not do this`는 금지지만 이것은 **기본값 자리에서 내리는 것**이어서, 사정이 있어 그 길을 택하는 사람을 막지 않는다. 리뷰 코멘트의 수위를 한 칸 낮춰야 할 때 그대로 쓴다."
  app1="Pinning the base image by tag instead of digest can be done, but we do not recommend this as the default."
  app1ko="베이스 이미지를 다이제스트 대신 태그로 고정하는 것도 할 수는 있지만, 우리는 이것을 기본값으로 권하지는 않는다."
  app2="Giving the on-call account standing write access to production can be done, but we do not recommend this as the default; ask for it per incident and let it expire."
  app2ko="온콜 계정에 운영 환경 쓰기 권한을 상시로 주는 것도 할 수는 있지만, 우리는 이것을 기본값으로 권하지는 않는다. 장애마다 따로 요청하고 만료되게 두는 편이 낫다."
>}}

{{< sentence
  en="Most vulnerability reporters are happy to provide some extra time if there is clear ongoing evidence of effort, continuous communication, and a good rationale for that extra time."
  ko="대부분의 취약점 신고자는 노력에 대한 분명하고 지속적인 증거, 끊이지 않는 소통, 그리고 그 추가 시간이 필요한 타당한 근거가 있다면 기꺼이 시간을 더 준다."
  source="OpenSSF 취약점 공개 가이드 · Response process"
  sourceURL="https://github.com/ossf/oss-vulnerability-guide/blob/main/maintainer-guide.md#response-process"
  note="`Most X are happy to Y if there is clear ongoing evidence of A, B, and C.` — 기한을 더 달라고 말하기 전에 **상대가 무엇을 보면 승낙하는지**를 먼저 적어 두는 문형이다. `Most`로 일반화를 한 칸 낮추고, `are happy to`로 '해 줄 의무가 있다'가 아니라 '기꺼이 해 준다'를 전제한다 — 요구가 아니라 부탁의 자리로 문장을 옮겨 놓는 말이다. 조건은 전부 `evidence of`에 묶여 있다. 말이 아니라 **보이는 증거**를 요구한다는 뜻이고, `ongoing`이 붙어서 한 번의 보고가 아니라 계속되는 상태여야 한다고 못 박는다. 연장 요청 메일의 첫 문단으로."
  app1="Most customers are happy to accept a later fix date if there is clear ongoing evidence of progress, a status note at the end of each day, and a good rationale for the delay."
  app1ko="대부분의 고객은 진전에 대한 분명하고 지속적인 증거, 매일 퇴근 전의 상황 공유, 그리고 지연에 대한 타당한 근거가 있다면 기꺼이 수정 기한을 늦춰 준다."
  app2="Most reviewers are happy to take a large refactor in stages if there is clear ongoing evidence of test coverage, a migration plan, and a good rationale for not doing it in one commit."
  app2ko="대부분의 리뷰어는 테스트 커버리지에 대한 분명하고 지속적인 증거, 이행 계획, 그리고 한 커밋에 담지 않는 타당한 근거가 있다면 기꺼이 큰 리팩터링을 나눠서 받아 준다."
>}}
