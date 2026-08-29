---
title: 개발·프로덕션 격차 문서의 표현
description: 상대의 동기를 먼저 인정하고, 사소한 차이가 실패로 이어지는 경로를 그리고, 낡은 전제를 폐기하는 문장 5개.
weight: -10
date: 2026-08-30
source: "The Twelve-Factor App — Dev/prod parity"
sourceURL: https://12factor.net/dev-prod-parity
---

# 개발·프로덕션 격차 문서의 표현

로컬은 가볍게, 프로덕션은 튼튼하게 — 이 흔한 관행을 반박하는 챕터다. 내용보다 **반박하는 방식**이
훔칠 만해서 골랐다. 이 글은 상대가 틀렸다고 말하지 않는다. 대신 끌릴 만한 이유를 먼저 적어 주고,
사소한 차이가 실패로 이어지는 경로를 그리고, 비용을 수명 전체로 합산하고, 그 관행을 떠받치던
전제가 만료됐다고 말한다. 팀에 굳어진 관행을 걷어낼 때 그대로 쓸 문형만 뽑았다.

> **원문** — Adam Wiggins, *The Twelve-Factor App — X. Dev/prod parity*,
> [12factor.net](https://12factor.net/dev-prod-parity)
> ([github.com/heroku/12factor](https://github.com/heroku/12factor/blob/master/content/en/dev-prod-parity.md)),
> [MIT License](https://github.com/heroku/12factor/blob/master/LICENSE).
>
> 영어 문장은 원문 그대로 인용했고, 한글 설명과 응용 문장은 이 노트에서 새로 쓴 것이다.

{{< sentence
  en="Developers sometimes find great appeal in using a lightweight backing service in their local environments, while a more serious and robust backing service will be used in production."
  ko="개발자들은 로컬 환경에서 가벼운 백킹 서비스를 쓰는 데 큰 매력을 느끼곤 한다. 정작 프로덕션에서는 더 진지하고 튼튼한 백킹 서비스가 쓰일 텐데도 그렇다."
  source="The Twelve-Factor App · Dev/prod parity"
  sourceURL="https://12factor.net/dev-prod-parity"
  note="`A sometimes find great appeal in X, while Y.` — **반박하기 전에 상대의 동기를 먼저 적어 주는** 문형이다. `find great appeal in`은 '좋아한다'가 아니라 *끌릴 만한 이유가 있다*로 읽힌다. 그래서 첫 문장부터 상대를 방어 태세로 밀어 넣지 않는다. `sometimes`는 빈도를 재는 말이 아니라 **일반화를 피하는 완충재**다(늘 그렇다고 하면 예외를 든 반박이 곧장 들어온다). 진짜 일은 `while` 절이 한다 — 지적하지 않고 두 상황을 나란히 놓기만 해서, 어긋남은 읽는 사람이 스스로 본다. 굳어진 관행을 문제 삼는 글의 첫 문단에 그대로 쓴다."
  app1="Teams sometimes find great appeal in silencing a noisy alert for a week, while the condition that fires it stays unowned."
  app1ko="팀은 시끄러운 알림을 한 주 동안 꺼 두는 데 큰 매력을 느끼곤 한다. 정작 그 알림을 울리게 만드는 조건은 주인 없이 남아 있는데도 그렇다."
  app2="Reviewers sometimes find great appeal in approving a small diff quickly, while the migration it turns on will run against production data."
  app2ko="리뷰어는 작은 diff를 빨리 승인해 주는 데 큰 매력을 느끼곤 한다. 정작 그 diff가 켜는 마이그레이션은 프로덕션 데이터를 상대로 돌 텐데도 그렇다."
>}}

{{< sentence
  en="Differences between backing services mean that tiny incompatibilities crop up, causing code that worked and passed tests in development or staging to fail in production."
  ko="백킹 서비스 사이의 차이는 사소한 비호환이 불쑥 튀어나온다는 뜻이고, 그 결과 개발이나 스테이징에서 동작하고 테스트까지 통과한 코드가 프로덕션에서 실패한다."
  source="The Twelve-Factor App · Dev/prod parity"
  sourceURL="https://12factor.net/dev-prod-parity"
  note="`X mean that Y crop up, causing Z to fail.` — 원인에서 실패까지를 **한 문장에 두 단으로** 잇는 틀이다. `mean that`은 '~할 수도 있다'가 아니라 정의에 가깝게 읽혀서, 차이를 두면 비호환이 따라온다는 게 우연이 아니라 성질임을 말한다. `crop up`은 계획에 없이 불쑥 나온다는 뜻이라 **예측 불가능성**을 얹는다. 핵심은 관계절 `code that worked and passed tests`다 — 실패한 코드가 부실했던 게 아니라 **우리 검증을 다 통과한 코드**였다고 미리 박아 두기 때문에, '테스트를 더 짜면 되지 않느냐'는 반론이 들어올 자리가 없어진다. 환경 차이나 설정 드리프트를 설명할 때 이 순서로 쓴다."
  app1="Differences between the staging and production IAM policies mean that silent permission denials crop up, causing a job that ran clean in staging to stall in production."
  app1ko="스테이징과 프로덕션 IAM 정책 사이의 차이는 조용한 권한 거부가 불쑥 튀어나온다는 뜻이고, 그 결과 스테이징에서 깔끔하게 돌던 작업이 프로덕션에서 멈춘다."
  app2="Differences between our local and CI toolchains mean that build discrepancies crop up, causing a change that passed review to break the nightly deploy."
  app2ko="로컬과 CI 툴체인 사이의 차이는 빌드 불일치가 불쑥 튀어나온다는 뜻이고, 그 결과 리뷰를 통과한 변경이 야간 배포를 깨뜨린다."
>}}

{{< sentence
  en="The cost of this friction and the subsequent dampening of continuous deployment is extremely high when considered in aggregate over the lifetime of an application."
  ko="이 마찰과 그에 뒤따르는 지속적 배포의 위축이 치르는 비용은, 애플리케이션의 수명 전체에 걸쳐 합산해 놓고 보면 극단적으로 크다."
  source="The Twelve-Factor App · Dev/prod parity"
  sourceURL="https://12factor.net/dev-prod-parity"
  note="`The cost of X is extremely high when considered in aggregate over the lifetime of Y.` — **한 건은 사소하다고 반박당할 때** 꺼내는 문형이다. 두 마디가 일을 나눠 한다. `when considered in aggregate`가 잣대를 건별에서 총량으로 옮기고, `over the lifetime of`가 그 총량을 잴 기간까지 못 박는다. 이 두 마디가 없으면 '그거 5분이면 됩니다'에서 대화가 끝난다. `the subsequent dampening of`도 그냥 수식이 아니다 — 1차 비용(마찰) 뒤에 오는 2차 효과, 즉 **사람들이 아예 그 일을 덜 하게 되는 것**까지 비용에 포함시키는 장치다. 계산이 아니라 계산의 범위를 다시 잡는 문장이라는 점을 기억해 두면 쓸 자리가 보인다."
  app1="The cost of this manual approval step and the subsequent dampening of small releases is extremely high when considered in aggregate over the lifetime of a service."
  app1ko="이 수동 승인 단계와 그에 뒤따르는 작은 릴리스의 위축이 치르는 비용은, 서비스의 수명 전체에 걸쳐 합산해 놓고 보면 극단적으로 크다."
  app2="The cost of one flaky test and the subsequent dampening of trust in CI is extremely high when considered in aggregate over the lifetime of a team."
  app2ko="깜빡거리는 테스트 하나와 그에 뒤따르는 CI 신뢰의 위축이 치르는 비용은, 한 팀의 수명 전체에 걸쳐 합산해 놓고 보면 극단적으로 크다."
>}}

{{< sentence
  en="Lightweight local services are less compelling than they once were."
  ko="가벼운 로컬 서비스는 예전만큼 매력적이지 않다."
  source="The Twelve-Factor App · Dev/prod parity"
  sourceURL="https://12factor.net/dev-prod-parity"
  note="`X is less compelling than it once was.` — 관행을 공격하지 않고 **그 관행을 떠받치던 전제가 만료됐다고** 말하는 문형이다. `wrong`이 아니라 `less compelling`이라서 판정이 아니라 저울질로 남고, 비교급의 기준이 과거의 자기 자신이라 남을 끌어들이지도 않는다. 시제가 결정적이다 — `once were`가 **그때는 그 선택이 옳았음을 인정**하고, 달라진 것은 상황뿐이라고 못 박는다. 그래서 그 관행을 만든 사람이 방 안에 있어도 쓸 수 있다. 대신 이 문장 뒤에는 **무엇이 달라졌는지**가 반드시 와야 한다. 원문도 바로 다음 문장에서 요즘 패키징 도구 이야기를 꺼낸다. 근거 없이 이 문장만 쓰면 취향 표명이 된다."
  app1="The weekly manual access review is less compelling than it once was, now that every grant expires on its own."
  app1ko="주간 수동 접근 권한 검토는 예전만큼 매력적이지 않다. 이제는 모든 권한이 스스로 만료되니까."
  app2="Reading raw logs by hand is less compelling than it once was, now that every request carries a trace id."
  app2ko="로그를 손으로 훑어 읽는 일은 예전만큼 매력적이지 않다. 이제는 모든 요청이 트레이스 아이디를 달고 다니니까."
>}}

{{< sentence
  en="Adapters to different backing services are still useful, because they make porting to new backing services relatively painless. But all deploys of the app (developer environments, staging, production) should be using the same type and version of each of the backing services."
  ko="서로 다른 백킹 서비스에 대한 어댑터는 여전히 쓸모가 있다. 새 백킹 서비스로 옮겨 가는 일을 비교적 수월하게 만들어 주기 때문이다. 하지만 이 앱의 모든 배포(개발자 환경, 스테이징, 프로덕션)는 각 백킹 서비스에 대해 같은 종류와 같은 버전을 쓰고 있어야 한다."
  source="The Twelve-Factor App · Dev/prod parity"
  sourceURL="https://12factor.net/dev-prod-parity"
  note="`X is still useful, because ... But all Y should be Z.` — **도구는 살려 두고 그 도구를 핑계 삼는 것만 막는** 두 문장 세트다. `still useful`이 '그럼 그거 쓰지 말라는 거냐'는 반문을 먼저 닫고, 뒤에 `because` 절까지 붙어서 형식적인 인정이 아님을 보인다. 그 다음에야 `But`이 규칙을 세운다 — 순서가 반대면 규칙이 먼저 나오고 인정은 변명처럼 들린다. 규칙 쪽의 장치는 범위다. `all deploys` 뒤에 괄호로 대상을 **끝까지 열거해서** '우리 개발 환경은 예외 아니냐'가 끼어들 자리를 없앤다. `should be using` 진행형도 의도적이다 — 한 번 맞추는 행위가 아니라 **늘 그렇게 유지돼 있어야 하는 상태**를 가리킨다. 예외 없는 규칙을 공지할 때 이 두 문장 순서를 그대로 쓴다."
  app1="Feature flags are still useful, because they let us turn a bad path off without a deploy. But every flag we keep (ours, the vendor's, the ones nobody claims) should have an owner and a removal date."
  app1ko="기능 플래그는 여전히 쓸모가 있다. 배포 없이도 잘못된 경로를 꺼 버릴 수 있게 해 주기 때문이다. 하지만 우리가 남겨 두는 모든 플래그(우리 것, 벤더 것, 아무도 자기 것이라 하지 않는 것)에는 주인과 제거 예정일이 있어야 한다."
  app2="Break-glass accounts are still useful, because they get us in when SSO is down. But all of them (staging, production, the vendor consoles) should be writing to the same audit trail."
  app2ko="비상용 계정은 여전히 쓸모가 있다. SSO가 죽었을 때 우리를 들여보내 주기 때문이다. 하지만 그 계정 전부(스테이징, 프로덕션, 벤더 콘솔)는 같은 감사 로그에 기록을 남기고 있어야 한다."
>}}
