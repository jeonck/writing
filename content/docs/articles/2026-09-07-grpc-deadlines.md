---
title: 기다림의 한계를 정해 두는 표현
description: 언제까지 기다릴지 정의하고, 기본값이 무엇을 방치하는지 드러내고, 뒷정리 책임을 못 박는 문장 5개.
weight: -18
date: 2026-09-07
source: "gRPC Documentation — Deadlines"
sourceURL: https://grpc.io/docs/guides/deadlines/
---

# 기다림의 한계를 정해 두는 표현

gRPC 공식 문서의 *Deadlines* 페이지는 응답이 언제 올지 모르는 서버를 상대로 클라이언트가
언제까지 기다릴지를 어떻게 정하고, 그 결정이 서버와 중간 서버까지 어떻게 전파되는지를
설명한다. 짧은 문서인데 **경계를 정하는 문장**이 유난히 많다 — 무엇을 데드라인이라 부를지
정의하고, 아무것도 정하지 않은 기본값이 어떤 상태를 낳는지 밝히고, 라이브러리가 대신 해
주지 않는 뒷정리를 누구 책임으로 돌릴지 못 박는다. 타임아웃 설정, 온콜 에스컬레이션 기준,
리뷰 SLA처럼 **사람과 시스템 사이에 한계선을 그어야 하는 글**에 그대로 옮겨 쓸 수 있는
다섯 문장을 골랐다.

> **원문** — gRPC Authors, *Deadlines*,
> [grpc.io](https://grpc.io/docs/guides/deadlines/) (gRPC Documentation), 문서 라이선스
> [CC BY 4.0](https://github.com/grpc/grpc.io/blob/main/LICENSE)
> ([원본 마크다운](https://github.com/grpc/grpc.io/blob/main/content/en/docs/guides/deadlines.md)).
>
> 영어 문장은 원문 그대로 인용했고, 한글 설명과 응용 문장은 이 노트에서 새로 쓴 것이다.

{{< sentence
  en="A deadline is used to specify a point in time past which a client is unwilling to wait for a response from a server."
  ko="데드라인은 클라이언트가 그 시점을 넘어서까지는 서버의 응답을 기다릴 뜻이 없는, 시간상의 한 점을 지정하는 데 쓰인다."
  source="gRPC Documentation · Deadlines — Overview"
  sourceURL="https://grpc.io/docs/guides/deadlines/"
  note="`X is used to specify a point in time past which A is unwilling to B.` — 용어를 **동작이 아니라 의사로** 정의하는 문형이다. 톤을 정하는 단어는 `unwilling`이다. `cannot`이나 `must not`이 아니라 '기다릴 뜻이 없다'이므로, 기술적 한계가 아니라 **우리가 내린 결정**이라는 사실이 문장에 남는다. `past which` 관계절은 경계 뒤쪽을 통째로 잘라내는 장치라서, 값 하나(30초)를 적는 대신 그 값이 무엇을 뜻하는지를 정의할 수 있다. 용어집, 설계 문서의 첫 문단, 합의가 필요한 기준을 세울 때 꺼내 쓴다."
  app1="An escalation window is used to specify a point in time past which the on-call engineer is unwilling to keep debugging alone."
  app1ko="에스컬레이션 기준 시각은 온콜 담당자가 그 시점을 넘어서까지는 혼자 디버깅을 계속할 뜻이 없는, 시간상의 한 점을 지정하는 데 쓰인다."
  app2="A review SLA is used to specify a point in time past which the author is unwilling to keep a branch open waiting for comments."
  app2ko="리뷰 SLA는 작성자가 그 시점을 넘어서까지는 코멘트를 기다리며 브랜치를 열어 둘 뜻이 없는, 시간상의 한 점을 지정하는 데 쓰인다."
>}}

{{< sentence
  en="Clients that do not wait around unnecessarily and servers that know when to give up processing requests will improve the resource utilization and latency of your system."
  ko="불필요하게 마냥 기다리지 않는 클라이언트와 언제 요청 처리를 포기해야 하는지 아는 서버는 시스템의 자원 사용률과 지연을 개선한다."
  source="gRPC Documentation · Deadlines — Overview"
  sourceURL="https://grpc.io/docs/guides/deadlines/"
  note="`A that do not X and B that know when to Y will improve Z.` — 규칙을 명령형으로 늘어놓는 대신 **바람직한 상태를 주어 자리에 세우는** 문형이다. 양쪽 주체에 관계절을 하나씩 붙여 각자 할 일을 담고, 동사는 `will improve` 하나로 받는다. 그래서 지시가 아니라 원칙으로 읽히고, 누구를 지목하지 않고도 양쪽 모두에게 숙제를 남긴다. 핵심 표현은 `know when to give up`이다 — 포기를 실패가 아니라 판단력으로 바꿔 놓기 때문에, 중단·철회를 권해야 하는 자리에서 특히 쓸모 있다."
  app1="Pipelines that do not retry unnecessarily and jobs that know when to give up fetching artifacts will improve the queue time and cost of your CI."
  app1ko="불필요하게 재시도하지 않는 파이프라인과 언제 아티팩트 내려받기를 포기해야 하는지 아는 잡은 CI의 대기 시간과 비용을 개선한다."
  app2="Reviewers that do not block on style nits and authors that know when to split a change will improve the review latency of your team."
  app2ko="사소한 스타일 지적으로 붙잡아 두지 않는 리뷰어와 언제 변경을 쪼개야 하는지 아는 작성자는 팀의 리뷰 지연을 개선한다."
>}}

{{< sentence
  en="By default, gRPC does not set a deadline which means it is possible for a client to end up waiting for a response effectively forever."
  ko="기본적으로 gRPC는 데드라인을 설정하지 않는다. 이는 클라이언트가 사실상 영원히 응답을 기다리는 상태에 빠질 수 있다는 뜻이다."
  source="gRPC Documentation · Deadlines — Deadlines on the Client"
  sourceURL="https://grpc.io/docs/guides/deadlines/"
  note="`By default, X does not Y, which means it is possible for A to end up Z-ing.` — 기본값을 비난하지 않고 **기본값이 데려가는 최악의 상태**를 이어 붙이는 문형이다. `which means`가 사실과 해석을 갈라 놓아서, 앞절은 반박할 수 없는 관찰로 남고 뒷절만 논의 대상이 된다. `it is possible for ... to end up ...`은 '이미 그렇다'가 아니라 '그렇게 끝날 수 있다'이므로 과장이 아니고, `effectively forever` 역시 `effectively` 덕분에 감정이 아니라 관측으로 내려온다. 보안 감사나 설정 리뷰에서 위험한 기본값을 지적할 때 그대로 쓴다."
  app1="By default, the bucket policy does not expire old objects which means it is possible for a retention violation to sit in the account effectively forever."
  app1ko="기본적으로 이 버킷 정책은 오래된 객체를 만료시키지 않는다. 이는 보존 규정 위반이 계정 안에 사실상 영원히 남아 있을 수 있다는 뜻이다."
  app2="By default, the workflow does not pin action versions which means it is possible for a build to end up running code nobody on the team has ever reviewed."
  app2ko="기본적으로 이 워크플로는 액션 버전을 고정하지 않는다. 이는 빌드가 팀의 누구도 검토한 적 없는 코드를 실행하게 될 수 있다는 뜻이다."
>}}

{{< sentence
  en="Please note that the server application is responsible for stopping any activity it has spawned to service the RPC."
  ko="서버 애플리케이션은 그 RPC를 처리하려고 자기가 띄운 모든 작업을 멈출 책임이 있다는 점에 유의하라."
  source="gRPC Documentation · Deadlines — Deadlines on the Server"
  sourceURL="https://grpc.io/docs/guides/deadlines/"
  note="`Please note that A is responsible for stopping any B it has spawned to C.` — 자동으로 처리되지 않는 지점을 **책임의 소재로** 못 박는 문형이다. `Please note that`은 새로운 정보라는 신호가 아니라 '놓치기 쉬우니 여기서 한 번 멈추라'는 신호다. 진짜 일은 `any ... it has spawned`가 한다 — 항목을 나열하지 않고도 범위를 '네가 만든 것 전부'로 닫아 버려서, 목록에 없었다는 변명이 통하지 않는다. 인수인계 문서, 운영 가이드, 설계 문서의 책임 경계 절에서."
  app1="Please note that the calling team is responsible for cleaning up any test data it has created to exercise the staging environment."
  app1ko="호출하는 팀은 스테이징 환경을 시험하려고 자기가 만든 모든 테스트 데이터를 정리할 책임이 있다는 점에 유의하라."
  app2="Please note that the service owner is responsible for revoking any credential it has issued to run the migration."
  app2ko="서비스 소유자는 마이그레이션을 돌리려고 자기가 발급한 모든 자격 증명을 폐기할 책임이 있다는 점에 유의하라."
>}}

{{< sentence
  en="Using this capability lets you avoid the error-prone approach of manually including the deadline for each outgoing RPC."
  ko="이 기능을 쓰면 나가는 RPC마다 데드라인을 손으로 넣어 주는, 실수하기 쉬운 방식을 피할 수 있다."
  source="gRPC Documentation · Deadlines — Deadline Propagation"
  sourceURL="https://grpc.io/docs/guides/deadlines/"
  note="`Using X lets you avoid the error-prone approach of manually ...ing.` — 도입을 권할 때 **얻는 것이 아니라 피하는 것**으로 말하는 문형이다. '이게 더 낫다'는 취향 싸움이 되지만, '사람이 매번 기억해야 하는 방식을 안 써도 된다'는 반박하기 어렵다. `error-prone`은 사람이 아니라 방식에 붙는 형용사여서 누구의 실수도 들추지 않고, `manually`가 그 방식이 무엇인지 정확히 지목한다. 코드 리뷰에서 헬퍼·린트 규칙·자동화 도입을 제안할 때 그대로 옮겨 쓴다."
  app1="Using the shared client factory lets you avoid the error-prone approach of manually setting the retry policy in each service."
  app1ko="공용 클라이언트 팩토리를 쓰면 서비스마다 재시도 정책을 손으로 설정해 주는, 실수하기 쉬운 방식을 피할 수 있다."
  app2="Using a templated runbook lets you avoid the error-prone approach of manually recalling every rollback step during an incident."
  app2ko="템플릿 런북을 쓰면 장애 중에 롤백 단계를 하나하나 기억해 내는, 실수하기 쉬운 방식을 피할 수 있다."
>}}
