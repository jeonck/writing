---
title: 신뢰를 전제하지 않고 절차를 말하는 표현
description: 정책 이름을 곧바로 풀어 주고, 우리 편의 위험까지 인정하고, 예외를 좁힌 뒤 유보권을 남기는 문장 5개.
weight: -15
date: 2026-09-04
source: "Everything curl — Security"
sourceURL: https://everything.curl.dev/project/security.html
---

# 신뢰를 전제하지 않고 절차를 말하는 표현

curl 프로젝트의 책 *Everything curl* 중 'Security' 장은 취약점 신고를 어떻게 처리하는지,
그리고 수십억 곳에 깔린 라이브러리가 공급망 공격의 표적이 되는 것을 어떻게 막는지를 적어 놓은
문서다. 흥미로운 점은 **자기 편을 믿어 달라고 말하지 않는다**는 것이다. 메인테이너가 악의를
가질 수 있다는 전제를 먼저 적고, 그 위에 2FA·리뷰·재현 가능한 빌드 같은 절차를 쌓는다.
정책을 선언하고, 위험을 인정하고, 기준을 못 박고, 예외를 좁히는 문형을 다섯 개 뽑았다.
보안 감사 소견이나 팀 정책 문서처럼 **사람을 의심하지 않으면서 절차를 요구해야 하는 글**에
그대로 옮겨 쓸 수 있다.

> **원문** — Daniel Stenberg, *Everything curl — Security*,
> [everything.curl.dev](https://everything.curl.dev/project/security.html)
> ([github.com/curl/everything-curl](https://github.com/curl/everything-curl/blob/master/project/security.md)),
> [CC BY 4.0](https://github.com/curl/everything-curl/blob/master/LICENSE).
>
> 영어 문장은 원문 그대로 인용했고, 한글 설명과 응용 문장은 이 노트에서 새로 쓴 것이다.

{{< sentence
  en="We use a responsible disclosure policy, meaning that we prefer to discuss and work on security fixes out of the public eye and we alert the vendors on the openwall.org list a few days before we announce the problem and fix to the world."
  ko="우리는 책임 있는 공개 정책을 쓴다. 즉 보안 수정은 공개된 자리 밖에서 논의하고 작업하는 편을 택하며, 문제와 수정을 세상에 알리기 며칠 전에 openwall.org 목록으로 벤더들에게 먼저 알린다는 뜻이다."
  source="Everything curl · Security"
  sourceURL="https://everything.curl.dev/project/security.html"
  note="`We use X, meaning that A and B.` — 정책의 **이름을 먼저 던지고 곧바로 풀어 주는** 구조다. 이름만 적으면 읽는 사람마다 다르게 이해하므로, `meaning that` 뒤에 실제로 무슨 일이 벌어지는지를 동사로 적어 준다. 이때 `we prefer to`가 톤을 정한다 — 금지 규칙이 아니라 기본값이라고 말해 예외의 여지를 남긴다. `out of the public eye`처럼 관용구 하나로 '비공개'를 은근하게 표현하는 것도 같은 계산이다. 팀 정책·운영 원칙을 문서에 적을 때, 한 문장 안에서 선언과 해설을 끝내는 틀."
  app1="We use a staged rollout policy, meaning that we ship to one region first and we watch error rates for a full business day before we open it to everyone."
  app1ko="우리는 단계적 배포 정책을 쓴다. 즉 한 리전에 먼저 내보내고, 전체에 열기 전에 영업일 하루 동안 오류율을 지켜본다는 뜻이다."
  app2="We use a two-person rule for schema changes, meaning that the author never merges their own migration and we replay it on a restored snapshot before it touches production."
  app2ko="스키마 변경에는 2인 규칙을 쓴다. 즉 작성자가 자기 마이그레이션을 직접 머지하지 않으며, 운영에 닿기 전에 복원한 스냅샷에서 한 번 돌려 본다는 뜻이다."
>}}

{{< sentence
  en="With libcurl being installed and running in billions of installations all over the world and in countless different environments, we recognize that it is an ideal target for someone who wants a backdoor somewhere."
  ko="libcurl이 전 세계 수십억 곳에서, 그리고 헤아릴 수 없이 다양한 환경에서 설치되어 돌아가고 있는 만큼, 우리는 그것이 어딘가에 백도어를 심고 싶어 하는 누군가에게 이상적인 표적임을 인정한다."
  source="Everything curl · Backdoors and supply chain risks"
  sourceURL="https://everything.curl.dev/project/security.html"
  note="`With X being ~, we recognize that X is an ideal target for ~.` — 부대상황 `With` 절로 **규모라는 사실을 먼저 깔고**, 주절에서 그 사실의 필연적 결과로 자기가 표적임을 인정하는 순서다. 자랑(수십억 설치)이 그대로 위협의 근거가 되도록 뒤집는 것이 이 문장의 기술이다. `we recognize that`은 '알고는 있다'가 아니라 **인정했으니 대응하겠다**는 신호라서, 바로 뒤에 대책 목록이 따라올 때만 쓴다. 위협 모델링 문서나 감사 대응의 첫 문단."
  app1="With the deploy key being shared across every service in the cluster, we recognize that it is a single point of compromise for the whole platform."
  app1ko="그 배포 키가 클러스터의 모든 서비스에 공유되어 쓰이고 있는 만큼, 우리는 그것이 플랫폼 전체를 한 번에 무너뜨릴 수 있는 지점임을 인정한다."
  app2="With this dashboard being the only place on-call looks during an incident, we recognize that a stale panel here is worse than no panel at all."
  app2ko="장애 중에 온콜이 들여다보는 곳이 이 대시보드뿐인 만큼, 우리는 여기 남아 있는 낡은 패널이 차라리 패널이 없느니만 못하다는 것을 인정한다."
>}}

{{< sentence
  en="A new or old maintainer might at any point propose a change that sounds innocent and well-meaning but has a disguised malicious intent."
  ko="새로 온 메인테이너든 오래된 메인테이너든, 언제든 악의를 감춘 채 순수하고 선의로 들리는 변경을 제안할 수 있다."
  source="Everything curl · Backdoors and supply chain risks"
  sourceURL="https://everything.curl.dev/project/security.html"
  note="`A new or old X might at any point propose Y that sounds A but has B.` — 내부자 위험을 **아무도 지목하지 않고** 적는 문형이다. `A new or old`가 신참과 고참을 함께 묶어 '경력이 면제 사유가 아니다'라고 말하고, `at any point`가 시점 조건까지 지워 버린다. 남는 것은 사람이 아니라 그런 일이 가능한 구조다. `sounds ~ but has ~`는 겉과 속의 대조인데, 앞쪽에 `innocent and well-meaning`처럼 좋은 말을 일부러 얹어 둘수록 뒤의 반전이 선명해진다. 리뷰 절차나 권한 분리를 왜 두느냐고 물을 때 답으로 쓴다."
  app1="Anyone with merge rights might at any point land a dependency bump that looks routine but pulls in a package no one on the team has read."
  app1ko="머지 권한이 있는 사람은 누구든 언제든, 팀의 아무도 읽어 본 적 없는 패키지를 끌어오면서도 겉보기에는 일상적인 의존성 업데이트를 넣을 수 있다."
  app2="A trusted script might at any point ask for one more permission that reads as a convenience but grants standing access to the audit bucket."
  app2ko="믿고 쓰던 스크립트도 언제든, 편의를 위한 것처럼 읽히지만 실은 감사 로그 버킷에 상시 접근권을 주는 권한을 하나 더 요구할 수 있다."
>}}

{{< sentence
  en="If code is hard to read it should be improved until it gets easy to read."
  ko="코드가 읽기 어렵다면, 읽기 쉬워질 때까지 개선되어야 한다."
  source="Everything curl · Readable code"
  sourceURL="https://everything.curl.dev/project/security.html"
  note="`If X is hard to A, it should be improved until it gets easy to A.` — 짧지만 **완료 기준까지 박아 넣은** 처방문이다. '읽기 쉽게 고쳐라'로 끝나면 어디까지 해야 하는지 매번 다투게 되는데, `until it gets easy to read`가 그 끝점을 문장 안에 넣는다. 수동태 `it should be improved`는 누가 고칠지를 지목하지 않아 개인에 대한 요구가 아니라 규칙처럼 읽히게 만든다. 리뷰 기준, 문서화 원칙, 알림 정리처럼 **주관적인 품질을 규칙으로 적어야 할 때** 그대로 쓴다."
  app1="If an alert is not actionable it should be rewritten until the first line tells the responder what to do."
  app1ko="알림을 받고 할 일이 떠오르지 않는다면, 첫 줄만 읽고도 대응자가 무엇을 해야 할지 알 수 있을 때까지 다시 쓰여야 한다."
  app2="If a runbook step cannot be followed by someone outside the team it should be revised until it can."
  app2ko="런북의 어떤 단계를 팀 밖의 사람이 따라 할 수 없다면, 따라 할 수 있게 될 때까지 손봐야 한다."
>}}

{{< sentence
  en="Whenever we receive a security vulnerability report, we create and ship a fix in the next pending release. Sometimes sooner than previously planned. Only in extremely rare cases does it take longer than a release cycle, but in the name of accuracy and correctness we do reserve the right to spend time on research to get it right."
  ko="보안 취약점 신고를 받으면 우리는 다음 예정 릴리스에서 수정을 만들어 내보낸다. 때로는 원래 계획보다 더 일찍 내기도 한다. 릴리스 주기보다 오래 걸리는 것은 극히 드문 경우뿐이지만, 정확성과 올바름을 위해 제대로 고치는 데 필요한 조사 시간을 쓸 권리는 남겨 둔다."
  source="Everything curl · Fix all vulnerabilities quickly"
  sourceURL="https://everything.curl.dev/project/security.html"
  note="약속을 적는 세 박자다. ① `Whenever A, we B.`로 조건과 기본 대응을 건다. ② 동사 없는 조각 `Sometimes sooner than previously planned.`로 더 나은 경우를 덧붙인다 — 문장을 짧게 끊을수록 생색이 덜 난다. ③ `Only in extremely rare cases does it ~, but we do reserve the right to ~`로 예외를 **먼저 좁혀 놓고** 유보권을 밝힌다. `Only`가 문두에 오면 `does it take`로 도치되는 것이 규칙이고, 이 도치가 '드물다'를 강조한다. `we do reserve`의 `do`도 같은 강조. 예외를 빠져나갈 구멍이 아니라 정직한 유보로 읽히게 하는 것은, 그 앞에 범위를 이미 좁혀 두었기 때문이다. SLA, 대응 시간 약속, 감사 답변에 쓴다."
  app1="Whenever a page fires, we acknowledge it within five minutes. Only in extremely rare cases does triage take longer than an hour, but we do reserve the right to hold the all-clear until we understand the root cause."
  app1ko="호출이 울리면 우리는 5분 안에 확인 응답을 보낸다. 분류가 한 시간을 넘기는 것은 극히 드문 경우뿐이지만, 근본 원인을 이해할 때까지 상황 종료 선언을 미룰 권리는 남겨 둔다."
  app2="Whenever an access review flags an account, we revoke it in the same cycle. Only in extremely rare cases does the revocation wait, but we do reserve the right to keep an account alive while a customer migration is still running."
  app2ko="접근 권한 검토에서 걸린 계정은 같은 주기 안에 회수한다. 회수가 미뤄지는 것은 극히 드문 경우뿐이지만, 고객 마이그레이션이 진행 중인 동안에는 계정을 살려 둘 권리는 남겨 둔다."
>}}
