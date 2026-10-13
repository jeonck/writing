---
title: 반대를 절차에 올리는 표현
description: 승인의 뜻을 책임으로 정의하고, 어디에 적어야 효력이 있는지 끊고, 반대할 권리에 유지 조건을 붙이고, 새 절차를 덧셈이라고 못 박고, 사고를 정상 범위에 넣은 뒤 바로 할 일을 적는 문장 5개.
weight: -54
date: 2026-10-14
source: "Node.js · Collaborator Guide"
sourceURL: https://github.com/nodejs/node/blob/main/doc/contributing/collaborator-guide.md
---

# 반대를 절차에 올리는 표현

Node.js 코어 저장소의 커미터 운영 문서다. 누가 몇 명 승인하면 PR이 들어갈 수 있는지,
반대는 어떻게 해야 효력이 있는지, 반대가 풀리지 않으면 어디로 올라가는지, 그러고도
잘못 머지됐을 때는 무엇을 하는지를 적어 둔 글이다. Node.js 내부 사정보다
**의견 불일치를 절차로 다루는 말투**가 배울 점이라 골랐다 — 아무에게도 명령할 수 없는
자원봉사자들 사이에서 거부권을 나눠 주면서도 그 거부권이 남용되지 않게 조건을 붙여야
하고, 반대한 사람을 적으로 만들지 않으면서 그 반대가 집계되는 조건을 좁혀야 하는 글이다.
리뷰 규칙을 적을 때, 승인 권한의 무게를 분명히 할 때, 반대 의견을 받아 적을 때
그대로 틀을 가져다 쓸 수 있다.

> **원문** — Node.js contributors, *Node.js collaborator guide*,
> [nodejs/node](https://github.com/nodejs/node/blob/main/doc/contributing/collaborator-guide.md)
> (`doc/contributing/collaborator-guide.md`),
> [MIT](https://github.com/nodejs/node/blob/main/LICENSE) 라이선스.
>
> 영어 문장은 원문 그대로 인용했고, 한글 설명과 응용 문장은 이 노트에서 새로 쓴 것이다.

{{< sentence
  en="Approving a pull request indicates that the collaborator accepts responsibility for the change."
  ko="PR을 승인한다는 것은 그 커미터가 해당 변경에 대한 책임을 받아들인다는 뜻이다."
  source="Node.js collaborator guide · Code reviews"
  sourceURL="https://github.com/nodejs/node/blob/main/doc/contributing/collaborator-guide.md#code-reviews"
  note="`Doing X indicates that the actor accepts responsibility for Y.` — 규칙을 새로 만드는 대신 **이미 하고 있는 동작의 뜻을 정의하는** 문장이다. 훔칠 자리는 주어 — 사람이 아니라 동작(`Approving a pull request`)이 주어다. `Collaborators must take responsibility for what they approve`로 쓰면 새 의무를 부과하는 말이 되어 왜 그래야 하냐는 질문을 받지만, 동작을 주어로 두면 승인 버튼의 **의미를 알려 주는** 말이 되어 반박할 지점이 없다. 동사 `indicates`가 톤을 정한다 — `means`는 단정적이고 `implies`는 추론처럼 들리는데, `indicates`는 그 사이에서 공표하는 느낌이다. `you` 대신 역할 이름 `the collaborator`를 쓴 것도 장치다. 특정인을 겨누지 않으니 비난이 아니고, 대신 그 역할을 맡은 모두에게 걸린다. 승인·결재의 **가격을 올려야 할 때** 쓴다 — 도장 찍는 일이 가볍게 취급되는 자리에서 그 행위가 무엇을 떠안는 일인지 한 줄로 적어 둔다."
  app1="Approving a production deploy indicates that the reviewer accepts responsibility for the rollback."
  app1ko="프로덕션 배포를 승인한다는 것은 그 리뷰어가 롤백에 대한 책임을 받아들인다는 뜻이다."
  app2="Signing off on the quarterly access review indicates that the system owner accepts responsibility for every account left enabled."
  app2ko="분기 권한 점검에 서명한다는 것은 그 시스템 담당자가 살려 둔 모든 계정에 대한 책임을 받아들인다는 뜻이다."
>}}

{{< sentence
  en="Dissent comments alone don't constitute an objection, nor do dissenting comments made in any associated issue."
  ko="반대하는 댓글만으로는 정식 반대가 되지 않고, 연관된 이슈에 적은 반대 의견도 마찬가지다."
  source="Node.js collaborator guide · Objections"
  sourceURL="https://github.com/nodejs/node/blob/main/doc/contributing/collaborator-guide.md#objections"
  note="`X alone doesn't constitute Y, nor does Z.` — 어떤 행동이 **절차로 집계되는지**를 깎아내는 문장이다. 핵심은 `alone` — 반대 의견이 쓸모없다고 하지 않고, 그것만으로는 효력이 없다고만 한다. 그래서 반대한 사람을 부정하지 않고도 절차의 입구를 좁힐 수 있다. 동사 `constitute`는 법률 어휘다. 의견이 세다/약하다는 평가를 피하고 **요건 충족 여부**로 화제를 옮긴다 — 설득의 문제가 아니라 형식의 문제로 만들어 버린다. 뒷절의 도치 `nor do ...`가 두 번째 구멍을 닫는다. `and comments in the issue don't either`로 쓰면 덧붙인 예외처럼 읽히지만, `nor`는 같은 판정이 한 번 더 적용되는 것으로 읽혀서 **장소를 옮겨도 결과가 같다**는 뜻이 선명해진다. 어디에 적어야 효력이 있는지 정해 둘 때 쓴다 — 장애 채널의 말과 티켓, 복도 합의와 변경 기록을 구분해야 하는 자리."
  app1="A thumbs-up in the incident channel alone doesn't constitute an approval, nor do messages sent in any related thread."
  app1ko="장애 채널의 좋아요 반응만으로는 승인이 되지 않고, 관련 스레드에 보낸 메시지도 마찬가지다."
  app2="A note from the team lead alone doesn't constitute an access grant, nor does a request made in any chat room."
  app2ko="팀 리드의 메모만으로는 권한 부여가 되지 않고, 채팅방에서 한 요청도 마찬가지다."
>}}

{{< sentence
  en="Any pull request objection must include a clear reason for that objection, and the objector must remain responsive for further discussion towards consensus about the direction of the pull request."
  ko="PR에 대한 반대는 그 반대의 분명한 이유를 담아야 하고, 반대한 사람은 PR의 방향에 대한 합의를 향한 이후 논의에도 계속 응해야 한다."
  source="Node.js collaborator guide · Objections"
  sourceURL="https://github.com/nodejs/node/blob/main/doc/contributing/collaborator-guide.md#objections"
  note="`Any X must include A, and the one who raised it must remain responsive for B.` — 거부권을 인정하면서 **그 권한의 유지 조건**을 같은 문장에 붙인다. 두 의무의 성격이 다른 것이 이 문형의 뼈대다. 앞의 `must include a clear reason`은 한 번 하면 끝나는 일이고, 뒤의 `must remain responsive`는 **계속 지켜야 하는 상태**다. `must be responsive`가 아니라 `must remain`인 덕에 시작 시점의 조건이 아니라 지속 조건이 되고, 반대만 던져 놓고 사라지는 경우를 이 한 단어가 막는다. 그래서 뒤에 이어지는 규정(7일 무응답이면 기각할 수 있다)이 새 규칙처럼 보이지 않고 이 문장에서 따라 나오는 결과처럼 읽힌다. `the objector`라고 역할에 이름을 붙인 것도 의도적이다 — 반대한 사람을 한 단어로 부를 수 있어야 그 사람에게 의무를 걸 수 있다. 보류·블로킹 권한을 주면서 조건을 붙일 때 쓴다."
  app1="Any objection to this release must include a clear reason for that hold, and the objector must remain responsive for further discussion towards a ship date the team can commit to."
  app1ko="이번 릴리스에 대한 반대는 그 보류의 분명한 이유를 담아야 하고, 반대한 사람은 팀이 약속할 수 있는 배포 날짜를 향한 이후 논의에도 계속 응해야 한다."
  app2="Any security objection to the design must include a clear reason for that objection, and the objector must remain responsive for further discussion towards a mitigation we can actually ship."
  app2ko="이 설계에 대한 보안 반대는 그 반대의 분명한 이유를 담아야 하고, 반대한 사람은 우리가 실제로 내보낼 수 있는 완화책을 향한 이후 논의에도 계속 응해야 한다."
>}}

{{< sentence
  en="Fast-track approval is additional to code-review approval, not a replacement for it."
  ko="패스트트랙 승인은 코드 리뷰 승인에 더해지는 것이고, 그것을 대신하는 것이 아니다."
  source="Node.js collaborator guide · Waiting for approvals"
  sourceURL="https://github.com/nodejs/node/blob/main/doc/contributing/collaborator-guide.md#waiting-for-approvals"
  note="`A is additional to B, not a replacement for it.` — 새로 들인 절차가 기존 절차를 **덜어 주는 것으로 읽히는 오해**를 한 줄로 끊는다. `additional to`가 덧셈이라고 못 박고 나면 뒷부분은 사실 없어도 뜻이 통하는데, 그래도 `not a replacement for it`을 붙인다. 사람들이 실제로 할 오해를 **이름 붙여 미리 부정해 두는 것**이 이 문장의 거의 전부다. 짧은 것도 설계다. 이유를 덧붙이면 예외를 찾을 여지가 생기고, 한 줄이면 인용하기 쉬워 규칙으로 돌아다닌다 — 리뷰 스레드에 그대로 붙일 수 있는 길이다. 마지막 `for it`의 `it`이 B를 한 번 더 가리켜 두 절을 하나로 묶는 것도 눈여겨볼 부분이다. `not a replacement`로 끊으면 무엇을 대신하지 않는지가 흐려진다. 자동화를 들이면서 사람 손을 남겨야 할 때 쓴다 — 정적 분석, 자동 리뷰, 자동 점검 도구를 도입하는 공지."
  app1="The automated scan is additional to the manual security review, not a replacement for it."
  app1ko="자동 스캔은 사람이 하는 보안 리뷰에 더해지는 것이고, 그것을 대신하는 것이 아니다."
  app2="The alert dashboard is additional to the written on-call handover, not a replacement for it."
  app2ko="알림 대시보드는 글로 남기는 온콜 인수인계에 더해지는 것이고, 그것을 대신하는 것이 아니다."
>}}

{{< sentence
  en="Mistakes do happen. If a pull request is merged with an unresolved objection, submit a fix."
  ko="실수는 일어난다. 반대가 해소되지 않은 PR이 머지됐다면, 수정을 올려라."
  source="Node.js collaborator guide · Objections"
  sourceURL="https://github.com/nodejs/node/blob/main/doc/contributing/collaborator-guide.md#objections"
  note="`Mistakes do happen. If X, do Y.` — 사고를 **미리 정상 범위에 넣어 두고** 곧바로 할 일로 넘어가는 두 문장이다. 강조형 `do`가 여기서 하는 일이 크다. `Mistakes happen`은 세상 돌아가는 이야기로 읽히고 `Mistakes can happen`은 가능성 진술이지만, `do happen`은 **여기서도 일어나는 일임을 인정하는 선언**이 된다 — 이 한 글자가 뒤에 올 지시를 질책이 아니게 만든다. 구성이 핵심이다. 첫 문장이 책임 추궁의 자리를 미리 치워 버리고, 둘째 문장이 조건과 행동만 적는다. 그래서 누가 그랬냐는 대화가 설 자리가 없다. 명령형 `submit a fix`에 주어가 없는 것도 그래서다 — 지목하지 않으니, 발견한 사람이 하면 된다는 뜻이 된다. 회고를 열 때, 롤백 절차의 첫 줄에, 실수한 사람에게 처음 말을 걸 때 쓴다."
  app1="Mistakes do happen. If a secret is pushed to a public branch, rotate it first and tell the channel after."
  app1ko="실수는 일어난다. 비밀값이 공개 브랜치에 푸시됐다면, 먼저 교체하고 알리는 것은 그다음에 해라."
  app2="Mistakes do happen. If a migration ran against the wrong database, stop the job and post the exact statements you ran."
  app2ko="실수는 일어난다. 마이그레이션이 엉뚱한 데이터베이스에 돌았다면, 잡을 멈추고 돌린 문장을 그대로 올려라."
>}}
