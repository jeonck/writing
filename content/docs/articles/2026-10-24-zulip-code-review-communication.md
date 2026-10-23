---
title: 문턱을 낮추고, 상대가 어떻게 읽을지 미리 적는 표현
description: 자격 조건을 떼어 내 일을 열어 두고, 자동화가 못 덮는 몫을 항구적 사실로 선언하고, 금지 대신 선호의 서열로 적고, 과한 사과를 해석 교체로 풀고, 방치될 가능성을 예측해 보여 주는 문장 5개.
weight: -64
date: 2026-10-24
source: "Zulip Contributor Docs · Reviewing Zulip code"
sourceURL: https://zulip.readthedocs.io/en/latest/contributing/code-reviewing.html
---

# 문턱을 낮추고, 상대가 어떻게 읽을지 미리 적는 표현

Zulip 기여자 문서의 코드 리뷰 장. 체크리스트 부분은 어느 프로젝트에나 있는 내용이지만,
뒤쪽 "Review process and communication" 절은 성격이 다르다. **리뷰라는 행동을 사람들이
어떻게 받아들이는지**를 다루면서, 규칙을 세우는 대신 상대가 지금 무엇을 망설이고 있는지를
짚어 그 망설임을 하나씩 치운다. 경험이 없어도 된다고 말하는 방식, 사과하지 말라고 말하는
방식, 답이 늦으면 어떻게 읽히는지 알려 주는 방식 — 명령문을 쓰지 않고 행동을 바꾸는
문형들이라서 발췌했다.

> **원문** — Zulip contributors, *Reviewing Zulip code*,
> [Zulip Contributor Documentation](https://zulip.readthedocs.io/en/latest/contributing/code-reviewing.html)
> ([원본 리포지터리](https://github.com/zulip/zulip/blob/main/docs/contributing/code-reviewing.md)),
> [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0).
>
> 영어 문장은 원문 그대로 인용했고, 한글 설명과 응용 문장은 이 노트에서 새로 쓴 것이다.

{{< sentence
  en="Anyone can do a code review -- you don't have to have a ton of experience, and you don't have to have the power to ultimately merge the PR."
  ko="누구나 코드 리뷰를 할 수 있다 — 경험이 아주 많아야 할 필요도 없고, 그 PR을 최종적으로 머지할 권한이 있어야 할 필요도 없다."
  source="Zulip Contributor Docs · Reviewing Zulip code"
  sourceURL="https://zulip.readthedocs.io/en/latest/contributing/code-reviewing.html"
  note="`Anyone can X -- you don't have to A, and you don't have to B.` — 선언을 먼저 하고 대시 뒤에서 **사람들이 스스로 붙여 둔 자격 조건을 하나씩 떼어 내는** 문형이다. 방향이 중요하다. `Even if you're inexperienced, you can still help`처럼 조건을 인정한 뒤 면제해 주는 게 아니라, `you don't have to have ...`로 **그 조건이 애초에 없다**고 적는다. 전자는 예외를 만들어 주는 말이고 후자는 오해를 정정하는 말이어서, 받는 쪽이 자기를 예외로 느끼지 않는다. 두 번째 항목이 특히 계산된 자리다. 경험이 없다는 것보다 `the power to ultimately merge the PR`이 없다는 것이 더 그럴듯한 핑계인데, 그걸 지목해서 먼저 치워 버린다. 리뷰·당직 섀도잉·점검처럼 **권한이 없어서 안 하고 있는 일**을 열 때 쓴다."
  app1="Anyone can join the incident review -- you don't have to have been on call that night, and you don't have to have write access to the service that broke."
  app1ko="누구나 장애 회고에 들어올 수 있다 — 그날 밤 당직이었어야 할 필요도 없고, 문제가 난 서비스에 쓰기 권한이 있어야 할 필요도 없다."
  app2="Anyone can file a finding in the audit tracker -- you don't have to be on the security team, and you don't have to have confirmed that the issue is exploitable."
  app2ko="누구나 감사 트래커에 발견 사항을 올릴 수 있다 — 보안팀 소속이어야 할 필요도 없고, 그 문제가 실제로 악용 가능한지 확인해 두었어야 할 필요도 없다."
>}}

{{< sentence
  en="Our goal is to have as much of this as possible verified via the linters and tests, but there will always be unusual forms of Python/JavaScript style that our tools don't check for."
  ko="우리의 목표는 이 가운데 가능한 만큼을 린터와 테스트로 검증하는 것이지만, 우리 도구가 검사하지 못하는 특이한 파이썬·자바스크립트 스타일은 언제나 있을 것이다."
  source="Zulip Contributor Docs · Reviewing Zulip code"
  sourceURL="https://zulip.readthedocs.io/en/latest/contributing/code-reviewing.html"
  note="`Our goal is to have as much of this as possible verified via X, but there will always be Y that our tools don't check for.` — 자동화의 목표와 **자동화가 끝내 덮지 못하는 몫**을 한 문장에 함께 두는 문형이다(`this`는 앞 문장의 코딩 스타일 규약을 받는다). 앞쪽 `as much of this as possible`은 목표를 수치가 아니라 방향으로 적는다. 커버리지를 숫자로 박으면 미달이 곧 실패가 되는데, 이렇게 쓰면 진행 중인 상태가 정상이 된다. 뒤쪽 `there will always be`가 더 중요한 장치다. 현재 상태(`아직 못 했다`)가 아니라 **항구적 사실**로 선언하기 때문에, 남는 수작업 검토가 치워야 할 부채가 아니라 처음부터 설계된 몫이 된다. 린터·정책 엔진의 적용 범위를 합의할 때, 체크리스트에 사람이 판단하는 항목을 남겨 두는 이유를 적을 때."
  app1="Our goal is to have as much of this as possible verified via the policy engine in CI, but there will always be privilege escalations that come from how two roles combine, which our rules don't check for."
  app1ko="우리의 목표는 이 가운데 가능한 만큼을 CI의 정책 엔진으로 검증하는 것이지만, 역할 두 개가 겹치는 방식에서 생기는 권한 상승은 언제나 있을 것이고 우리 규칙은 그것을 검사하지 못한다."
  app2="Our goal is to have as much of this as possible verified via automated alerts, but there will always be slow degradations that stay inside every threshold and that our monitors don't check for."
  app2ko="우리의 목표는 이 가운데 가능한 만큼을 자동 알림으로 검증하는 것이지만, 모든 임계값 안에 머무르면서 천천히 나빠지는 상태는 언제나 있을 것이고 우리 모니터는 그것을 검사하지 못한다."
>}}

{{< sentence
  en="But it's better yet if verbose explanation isn't needed. We prefer writing code that is readable without explanation over a heavily commented codebase using lots of clever tricks."
  ko="하지만 긴 설명이 아예 필요 없다면 그게 더 낫다. 우리는 설명 없이도 읽히는 코드를 쓰는 편을, 영리한 기법을 잔뜩 쓰고 주석을 빼곡히 붙인 코드베이스보다 선호한다."
  source="Zulip Contributor Docs · Reviewing Zulip code"
  sourceURL="https://zulip.readthedocs.io/en/latest/contributing/code-reviewing.html"
  note="`But it's better yet if X isn't needed. We prefer A over B.` — 두 문장이 한 조로 움직인다. 앞 문장 `it's better yet if`는 방금 권한 좋은 방법(주석을 잘 달기)을 부정하지 않으면서 **그보다 한 단 위에 다른 선택지를 올려놓는다**. `better`가 아니라 `better yet`인 이유가 여기 있다 — 비교가 아니라 층을 하나 더 쌓는 말이다. 뒤 문장은 그 선택을 `We prefer A over B`, 즉 금지가 아니라 **선호의 서열**로 적는다. 규칙으로 적으면 예외마다 허락을 받아야 하지만 선호로 적으면 기본값이 되고, 벗어날 때 이유를 대면 된다. B를 `a heavily commented codebase using lots of clever tricks`처럼 길게 묘사한 것도 장치다. 피하고 싶은 쪽을 구체적인 그림으로 보여 주면 서열이 취향이 아니라 판단으로 읽힌다."
  app1="But it's better yet if the runbook isn't needed. We prefer a deploy that rolls itself back over a well-written page of manual recovery steps that someone has to find at 3am."
  app1ko="하지만 런북이 아예 필요 없다면 그게 더 낫다. 우리는 스스로 롤백되는 배포를, 누군가 새벽 3시에 찾아내야 하는 잘 쓰인 수동 복구 절차 한 장보다 선호한다."
  app2="But it's better yet if the exception isn't needed. We prefer a default that teams can live with over a documented approval path that half the organization walks through every quarter."
  app2ko="하지만 예외 신청이 아예 필요 없다면 그게 더 낫다. 우리는 팀들이 그대로 받아들일 수 있는 기본값을, 조직의 절반이 분기마다 통과하는 잘 문서화된 승인 절차보다 선호한다."
>}}

{{< sentence
  en="There is no need to apologize when asking for a change; you're collaborating with the author to make the PR as good as you can together."
  ko="변경을 요청할 때 사과할 필요는 없다. 당신은 그 PR을 함께 할 수 있는 만큼 좋게 만들려고 작성자와 협업하고 있는 것이다."
  source="Zulip Contributor Docs · Reviewing Zulip code"
  sourceURL="https://zulip.readthedocs.io/en/latest/contributing/code-reviewing.html"
  note="`There is no need to apologize when X; you're Y.` — 상대의 과한 조심을 **금지가 아니라 해석 교체로** 푸는 문형이다. 세미콜론 앞만 떼어 놓으면 `사과하지 마라`라는 또 하나의 지시가 된다. 일을 하는 쪽은 뒤쪽이다. `you're collaborating with the author to ...`가 그 행동이 실제로 무엇인지 다시 규정해 주기 때문에, 앞 문장이 지시가 아니라 **그 규정에서 따라 나오는 결론**이 된다. 요구는 사과할 일이 아니고 협업의 일부이므로 사과할 필요가 없다는 순서다. 마지막 `together`가 작은 단어치고 많은 일을 한다. 이것이 없으면 `as good as you can`의 주체가 리뷰어 한 사람이 되어 요구가 다시 일방적인 것으로 돌아간다. 리뷰 코멘트 쓰는 법을 가르칠 때, 질문이나 거절을 앞두고 과하게 몸을 낮추는 사람에게."
  app1="There is no need to apologize when paging the database on-call at night; you're giving them the one piece of context they'll want before the backlog gets any longer."
  app1ko="밤중에 데이터베이스 당직을 호출할 때 사과할 필요는 없다. 당신은 밀린 처리가 더 쌓이기 전에 그들이 알고 싶어 할 단 하나의 맥락을 건네주고 있는 것이다."
  app2="There is no need to apologize when sending the audit evidence request back; you're saving the team a second round with the auditor by getting the scope right the first time."
  app2ko="감사 증빙 요청을 돌려보낼 때 사과할 필요는 없다. 당신은 범위를 처음에 제대로 잡아서 팀이 감사인과 두 번 씨름하는 일을 덜어 주고 있는 것이다."
>}}

{{< sentence
  en="If you resolve the feedback, but the PR has merge conflicts, CI failures, or the most recent comment is the reviewer asking you to fix something, it's very likely that a potential reviewer skimming your PR will assume it isn't ready for review and move on to other work."
  ko="피드백을 해결했더라도 그 PR에 머지 충돌이나 CI 실패가 있거나, 가장 최근 코멘트가 리뷰어가 뭔가 고쳐 달라고 한 것이라면, 당신의 PR을 훑어본 잠재적 리뷰어는 아직 리뷰할 준비가 안 됐다고 판단하고 다른 일로 넘어갈 가능성이 매우 높다."
  source="Zulip Contributor Docs · Reviewing Zulip code"
  sourceURL="https://zulip.readthedocs.io/en/latest/contributing/code-reviewing.html"
  note="`If you do A, but B, C, or D, it's very likely that X will assume Y and move on.` — 규칙을 들이대지 않고 **상대가 당신 것을 어떻게 읽을지 예측해서** 행동을 바꾸는 문형이다. 주어가 `you`가 아니라 `a potential reviewer skimming your PR`이라는 점이 핵심이다. 요구가 아니라 제3자의 반응 예보가 되기 때문에 비난할 자리가 없고, 받는 쪽은 자기 평판을 자기가 관리하게 된다. `skimming`이 결정적인 단어다. 상대가 꼼꼼히 읽지 않는다는 전제를 미리 깔아 두므로 `읽어 보면 다 되어 있는데`라는 반박이 통하지 않는다. 끝의 `move on to other work`도 세게 고른 말이다. 결과를 거절이나 반대가 아니라 **조용한 방치**로 적어서, 싸울 상대조차 없다는 쪽이 더 무섭게 들린다. 티켓·PR·보안 이슈가 왜 그대로 멈춰 있는지 설명할 때 쓴다."
  app1="If you post the fix in the incident channel, but the alert is still firing, the status page says investigating, or the last update is an hour old, it's very likely that someone skimming the channel will assume nobody is on it and start a second investigation."
  app1ko="장애 채널에 수정 사항을 올렸더라도 알림이 아직 울리고 있거나, 상태 페이지가 여전히 조사 중이라고 적혀 있거나, 마지막 업데이트가 한 시간 전이라면, 채널을 훑어본 누군가는 아무도 붙어 있지 않다고 판단하고 조사를 하나 더 시작할 가능성이 매우 높다."
  app2="If you answer the finding, but the ticket is still open, the risk rating hasn't changed, or the latest note is the auditor asking for evidence, it's very likely that a reviewer skimming the register will assume the item is unresolved and carry it into the next quarter."
  app2ko="발견 사항에 답을 달았더라도 티켓이 아직 열려 있거나, 위험 등급이 그대로이거나, 최신 메모가 감사인이 증빙을 요청한 것이라면, 대장을 훑어본 검토자는 그 항목이 미해결이라고 판단하고 다음 분기로 넘길 가능성이 매우 높다."
>}}
