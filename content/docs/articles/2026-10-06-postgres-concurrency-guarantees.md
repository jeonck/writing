---
title: 보장하지 않는 것을 먼저 적는 표현
description: 부분적으로만 보이는 상태를 콜론으로 가르고, 유효 판정을 커밋 뒤로 미루고, 세부에 의존하지 말라고 못 박고, 사건의 정체와 탐지 결과를 분리하고, 보장할 수 없으니 기능을 만들지 않았다고 적는 문장 5개.
weight: -46
date: 2026-10-06
source: "PostgreSQL 문서 · Concurrency Control"
sourceURL: https://www.postgresql.org/docs/current/mvcc.html
---

# 보장하지 않는 것을 먼저 적는 표현

여러 세션이 같은 데이터를 동시에 건드릴 때 PostgreSQL이 무엇을 보장하고 무엇을
보장하지 않는지 설명하는 장(章)이다. 기능을 자랑하는 문장이 아니라 **보장의 바깥쪽을
먼저 적어 두는** 문장들을 골랐다 — 어디까지 보이는지, 언제부터 유효한지, 무엇에
의존해서는 안 되는지.

> **원문** — PostgreSQL Global Development Group, *PostgreSQL Documentation — Chapter
> Concurrency Control*, [postgresql.org](https://www.postgresql.org/docs/current/mvcc.html)
> ([원본 `doc/src/sgml/mvcc.sgml`](https://github.com/postgres/postgres/blob/master/doc/src/sgml/mvcc.sgml)),
> [PostgreSQL License](https://github.com/postgres/postgres/blob/master/COPYRIGHT) —
> 소프트웨어와 **그 문서**의 복제·배포를 명시적으로 허용한다.
>
> 영어 문장은 원문 그대로 인용했고, 한글 설명과 응용 문장은 이 노트에서 새로 쓴 것이다.

{{< sentence
  en="Because of the above rules, it is possible for an updating command to see an inconsistent snapshot: it can see the effects of concurrent updating commands on the same rows it is trying to update, but it does not see effects of those commands on other rows in the database."
  ko="위의 규칙 때문에, 갱신 명령이 일관되지 않은 스냅숏을 보는 일이 가능하다. 자신이 갱신하려는 바로 그 행들에 대해서는 동시에 실행된 갱신 명령의 효과를 볼 수 있지만, 그 명령들이 데이터베이스의 다른 행들에 미친 효과는 보지 못한다."
  source="PostgreSQL 문서 · Read Committed Isolation Level"
  sourceURL="https://www.postgresql.org/docs/current/transaction-iso.html#XACT-READ-COMMITTED"
  note="`it is possible for X to see an inconsistent view: it can see A, but it does not see B.` — 콜론 뒤에서 **어디까지 보이고 어디부터 안 보이는지** 경계를 가르는 문형이다. 핵심은 같은 동사를 두 번 쓴 것: `can see` / `does not see`로 대비가 또렷해지고, 무엇이 다른지가 목적어에만 남는다. 앞머리의 `it is possible for ~ to ~`는 '항상 그렇다'가 아니라 **가능성만 열어 두는** 완곡한 선언이라, 재현이 조건부인 현상을 적을 때 과장을 피하게 해 준다."
  app1="Because of how the cache is invalidated, it is possible for the dashboard to show an inconsistent view: it can see the new error rate for the pods it queried, but it does not see the rollback that already happened on the other clusters."
  app1ko="캐시가 무효화되는 방식 때문에, 대시보드가 일관되지 않은 화면을 보여 주는 일이 가능하다. 조회한 파드의 새 에러율은 보이지만, 다른 클러스터에서 이미 일어난 롤백은 보이지 않는다."
  app2="It is possible for a reviewer to read an inconsistent diff: they can see the changes in the files they opened, but they do not see the generated files the same commit rewrote."
  app2ko="리뷰어가 일관되지 않은 diff를 읽는 일이 가능하다. 열어 본 파일의 변경은 보이지만, 같은 커밋이 다시 생성해 버린 파일은 보이지 않는다."
>}}

{{< sentence
  en="When relying on Serializable transactions to prevent anomalies, it is important that any data read from a permanent user table not be considered valid until the transaction which read it has successfully committed."
  ko="이상 현상을 막기 위해 직렬화 가능 트랜잭션에 의존한다면, 영구 사용자 테이블에서 읽은 데이터는 그것을 읽은 트랜잭션이 성공적으로 커밋될 때까지는 유효한 것으로 간주하지 않는 것이 중요하다."
  source="PostgreSQL 문서 · Serializable Isolation Level"
  sourceURL="https://www.postgresql.org/docs/current/transaction-iso.html#XACT-SERIALIZABLE"
  note="`When relying on X to prevent Y, it is important that Z not be considered valid until W.` — **어떤 보장에 기대려면 이쪽에서 지켜야 하는 조건**을 적는 문형이다. `is not considered`가 아니라 `not be considered`인 이유는 `it is important that` 뒤라서 동사가 원형으로 가는 가정법이기 때문이다(should가 생략된 자리). 명령문보다 톤이 낮아 규범 문서에 맞는다. `until ~ has committed`로 **유효해지는 시점**을 못 박는 것이 이 문장의 일이다."
  app1="When relying on the retry queue to prevent data loss, it is important that a message not be considered delivered until the consumer has acknowledged it."
  app1ko="데이터 유실을 막기 위해 재시도 큐에 의존한다면, 메시지는 컨슈머가 확인 응답을 보낼 때까지는 전달된 것으로 간주하지 않는 것이 중요하다."
  app2="When relying on the scanner to prevent leaked credentials, it is important that a clean result not be considered trustworthy until the full history, not just the latest commit, has been scanned."
  app2ko="자격 증명 유출을 막기 위해 스캐너에 의존한다면, 최신 커밋만이 아니라 전체 이력을 다 훑기 전까지는 깨끗하다는 결과를 믿을 만한 것으로 간주하지 않는 것이 중요하다."
>}}

{{< sentence
  en="PostgreSQL automatically detects deadlock situations and resolves them by aborting one of the transactions involved, allowing the other(s) to complete. (Exactly which transaction will be aborted is difficult to predict and should not be relied upon.)"
  ko="PostgreSQL은 교착 상태를 자동으로 감지하고, 관련된 트랜잭션 중 하나를 중단시켜 나머지가 끝날 수 있게 함으로써 해소한다. (정확히 어느 트랜잭션이 중단될지는 예측하기 어렵고, 그것에 의존해서는 안 된다.)"
  source="PostgreSQL 문서 · Explicit Locking — Deadlocks"
  sourceURL="https://www.postgresql.org/docs/current/explicit-locking.html#LOCKING-DEADLOCKS"
  note="**보장하는 것을 말한 바로 다음 괄호에서 보장하지 않는 세부를 잘라 내는** 구조다. `X is difficult to predict and should not be relied upon.`은 두 가지를 한 번에 한다: 예측 불가라는 사실 진술과, 그에 기대지 말라는 지침. 수동태 `should not be relied upon`은 주체를 비워 둬서 특정 독자를 지목하지 않고, 금지보다 설계 지침처럼 읽힌다. 괄호에 넣은 덕에 본문의 '해소된다'는 약속을 흐리지 않으면서 덧붙는다."
  app1="The scheduler retries the failed job on a healthy node. (Exactly which node picks it up is difficult to predict and should not be relied upon.)"
  app1ko="스케줄러는 실패한 작업을 정상 노드에서 재시도한다. (정확히 어느 노드가 집어 갈지는 예측하기 어렵고, 그것에 의존해서는 안 된다.)"
  app2="Both replicas write to the same log stream, so the interleaving of their lines is difficult to predict and should not be relied upon when reconstructing the incident timeline."
  app2ko="두 레플리카가 같은 로그 스트림에 쓰기 때문에, 줄이 섞이는 순서는 예측하기 어렵고 장애 타임라인을 재구성할 때 그것에 의존해서는 안 된다."
>}}

{{< sentence
  en="This is effectively a serialization failure, but the server will not detect it as such because it cannot see the connection between the inserted value and the previous reads."
  ko="이것은 사실상 직렬화 실패이지만, 서버는 그것을 직렬화 실패로 탐지하지 못한다. 삽입된 값과 앞선 읽기 사이의 연결을 볼 수 없기 때문이다."
  source="PostgreSQL 문서 · Serialization Failure Handling"
  sourceURL="https://www.postgresql.org/docs/current/mvcc-serialization-failure-handling.html"
  note="`This is effectively X, but Y will not detect it as such because it cannot see the connection between A and B.` — **사건의 정체와 탐지 결과를 분리**하는 문형이다. `effectively`는 '공식 분류는 아니지만 실질적으로는'이라는 뜻이고, `as such`는 '방금 말한 바로 그것으로'를 받아 같은 말을 되풀이하지 않게 해 준다. 탐지 실패의 이유를 `cannot see the connection between A and B`로 적으면 도구를 탓하지 않고 **정보의 한계**로 돌릴 수 있다. 모니터링·감사의 사각지대를 설명할 때 그대로 쓴다."
  app1="This is effectively a privilege escalation, but the audit log will not record it as such because it cannot see the connection between the role grant and the token refresh that followed."
  app1ko="이것은 사실상 권한 상승이지만, 감사 로그는 그것을 권한 상승으로 기록하지 못한다. 역할 부여와 그 뒤에 일어난 토큰 갱신 사이의 연결을 볼 수 없기 때문이다."
  app2="These are effectively one incident, but the alerting rule will not group them as such because it cannot see the connection between the queue backlog and the deploy that preceded it."
  app2ko="이것들은 사실상 하나의 장애이지만, 알림 규칙은 그것을 하나로 묶지 못한다. 큐 적체와 그에 앞선 배포 사이의 연결을 볼 수 없기 때문이다."
>}}

{{< sentence
  en="Therefore, PostgreSQL does not offer an automatic retry facility, since it cannot do so with any guarantee of correctness."
  ko="그러므로 PostgreSQL은 자동 재시도 기능을 제공하지 않는다. 정확성을 보장하면서 그렇게 할 수는 없기 때문이다."
  source="PostgreSQL 문서 · Serialization Failure Handling"
  sourceURL="https://www.postgresql.org/docs/current/mvcc-serialization-failure-handling.html"
  note="`X does not offer Y, since it cannot do so with any guarantee of Z.` — **만들지 않은 이유를 한 문장으로 적는 거절문**이다. `does not offer`는 `is not supported`보다 주체가 분명해서 '못 한다'가 아니라 '안 한다'로 읽힌다. `with any guarantee of correctness`의 `any`가 부정을 강화해 '어느 수준의 보장도 못 한다'가 되고, 그래서 '아직 못 만들었다'가 아니라 **보장 없이는 만들지 않는다**는 선택으로 들린다. 바로 앞 문장이 근거이고 `Therefore`가 그 근거를 결론으로 끌어온다 — 기능 요청을 돌려보낼 때 핑계처럼 들리지 않게 하는 순서다."
  app1="Therefore, the runbook does not offer a one-click rollback for schema changes, since we cannot do so with any guarantee of data safety."
  app1ko="그러므로 런북은 스키마 변경에 대한 원클릭 롤백을 제공하지 않는다. 데이터 안전성을 보장하면서 그렇게 할 수는 없기 때문이다."
  app2="Therefore, we do not auto-close stale alerts, since we cannot do so with any guarantee that the underlying condition is gone."
  app2ko="그러므로 우리는 오래된 알림을 자동으로 닫지 않는다. 원인이 되는 상태가 사라졌다고 보장하면서 그렇게 할 수는 없기 때문이다."
>}}
