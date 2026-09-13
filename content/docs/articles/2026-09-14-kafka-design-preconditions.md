---
title: 전제가 무너지는 지점을 미리 적는 표현
description: 말의 뜻을 먼저 고정하고, 다루는 실패만 골라 적고, 남의 주장에 조건을 되묻고, 내 보장이 언제 성립하지 않는지 밝히고, 무엇이 먼저 쓰러질지를 설계하는 문장 5개.
weight: -25
date: 2026-09-14
source: "Apache Kafka Documentation — Design"
sourceURL: https://kafka.apache.org/documentation/#design
---

# 전제가 무너지는 지점을 미리 적는 표현

Apache Kafka의 *Design* 문서는 파일시스템을 왜 믿는지, 왜 푸시가 아니라 풀인지, 커밋된 메시지가
어떤 조건에서 유실되지 않는지를 설계자의 1인칭으로 풀어 놓은 긴 글이다. 제품 소개문이 아니라
**자기 시스템의 한계를 스스로 적어 둔 문서**라서, 말의 뜻을 고정하고 범위를 좁히고 전제를 드러내는
문장이 곳곳에 있다. 살아 있다는 말부터 정의하자고 요구하고, 다루지 않는 실패 유형을 따로 떼어
적고, 남들이 내세우는 보장에는 조건을 읽으라고 하고, 자기 보장이 언제 성립하지 않는지를 한 문장
더 써서 못 박는다. **설계 리뷰, 사고 보고서, 런북, 벤더 평가, 온콜 합의문**처럼 내 말이 어디까지
유효한지를 먼저 밝혀야 하는 글에 그대로 옮겨 쓸 다섯 문장을 골랐다.

> **원문** — Apache Kafka 기여자, *Design*,
> [Apache Kafka Documentation](https://kafka.apache.org/documentation/#design)
> (원본 마크다운: [`apache/kafka` · `docs/design/design.md`](https://github.com/apache/kafka/blob/trunk/docs/design/design.md)),
> [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0) 라이선스.
>
> 영어 문장은 원문 그대로 인용했고, 한글 설명과 응용 문장은 이 노트에서 새로 쓴 것이다.

{{< sentence
  en="As with most distributed systems, automatically handling failures requires a precise definition of what it means for a node to be &quot;alive.&quot;"
  ko="대부분의 분산 시스템이 그렇듯, 장애를 자동으로 처리하려면 노드가 살아 있다는 것이 무엇을 뜻하는지에 대한 정확한 정의가 필요하다."
  source="Apache Kafka Design · Replication"
  sourceURL="https://kafka.apache.org/documentation/#design"
  note="`Doing X requires a precise definition of what it means for Y to be Z.` — 자동화나 판정을 시작하기 전에 **말의 뜻부터 고정하자**고 요구하는 문형이다. 요구를 사람이 아니라 **작업**에 건다는 점이 핵심: '당신 기준이 모호하다'가 아니라 '이 일을 하려면 정의가 있어야 한다'가 된다. 앞에 붙은 `As with most X`는 이게 우리만의 유난이 아니라 이런 일에 으레 따라오는 절차임을 알려 주어 요구의 날을 눌러 준다. 알림 기준, SLO 문구, 완료 조건을 합의할 때 첫 문장으로 쓴다."
  app1="As with most on-call rotations, automating the escalation requires a precise definition of what it means for an incident to be &quot;acknowledged.&quot;"
  app1ko="대부분의 온콜 체계가 그렇듯, 에스컬레이션을 자동화하려면 장애가 확인되었다는 말이 무엇을 뜻하는지 정확히 정의해야 한다."
  app2="Automatically blocking a deploy requires a precise definition of what it means for a test to be &quot;flaky.&quot;"
  app2ko="배포를 자동으로 막으려면 테스트가 불안정하다는 말이 무엇을 뜻하는지 정확히 정의해야 한다."
>}}

{{< sentence
  en="In distributed systems terminology we only attempt to handle a &quot;fail/recover&quot; model of failures where nodes suddenly cease working and then later recover (perhaps without knowing that they have died). Kafka does not handle so-called &quot;Byzantine&quot; failures in which nodes produce arbitrary or malicious responses (perhaps due to bugs or foul play)."
  ko="분산 시스템 용어로 말하면 우리는 노드가 갑자기 동작을 멈췄다가 나중에 (자신이 죽었다는 사실을 모른 채) 복구되는 실패/복구 모델만 다루려 한다. Kafka는 노드가 (버그나 나쁜 짓 때문에) 임의의 응답이나 악의적인 응답을 내놓는 이른바 비잔틴 실패는 다루지 않는다."
  source="Apache Kafka Design · Replication"
  sourceURL="https://kafka.apache.org/documentation/#design"
  note="`We only attempt to handle X. It does not handle Y.` — **다루는 실패에 이름을 붙여 범위를 긋고, 다루지 않는 실패를 따로 한 문장으로 떼어 내는** 구조다. `only attempt to`는 몸을 두 번 낮춘다. 범위는 X뿐이고, 그 안에서도 완벽을 약속하지는 않는다. `so-called`는 업계에서 통용되는 용어를 빌려 쓰되 그 말에 기대지는 않겠다는 거리 두기다. 위협 모델이나 설계 문서의 범위 절에서, 빠뜨린 게 아니라 **의도적으로 밖에 둔 것**임을 밝힐 때 쓴다."
  app1="We only attempt to handle operator error and hardware loss in this runbook. It does not cover a compromised credential, which belongs to the security incident process."
  app1ko="이 런북은 운영자 실수와 하드웨어 유실만 다루려 한다. 자격 증명 탈취는 다루지 않으며, 그것은 보안 사고 절차가 맡는다."
  app2="This review only attempts to check that the migration is reversible. It does not check whether the new indexes are the right ones."
  app2ko="이 리뷰는 마이그레이션을 되돌릴 수 있는지만 확인하려 한다. 새 인덱스가 적절한지는 확인하지 않는다."
>}}

{{< sentence
  en="Many systems claim to provide &quot;exactly-once&quot; delivery semantics, but it is important to read the fine print, because sometimes these claims are misleading (i.e. they don't translate to the case where consumers or producers can fail, cases where there are multiple consumer processes, or cases where data written to disk can be lost)."
  ko="많은 시스템이 정확히 한 번 전달 시맨틱을 제공한다고 주장하지만, 그런 주장이 때로 오해를 부르기 때문에 세부 조항을 읽는 것이 중요하다(즉, 소비자나 생산자가 실패할 수 있는 경우, 소비자 프로세스가 여럿인 경우, 디스크에 쓴 데이터가 유실될 수 있는 경우에는 그 주장이 그대로 적용되지 않는다)."
  source="Apache Kafka Design · Message Delivery Semantics"
  sourceURL="https://kafka.apache.org/documentation/#design"
  note="`Many X claim to provide Y, but it is important to read the fine print, because ...` — 상대의 주장을 거짓이라 하지 않으면서 **그 주장이 성립하는 범위를 되묻는** 문형이다. `read the fine print`는 약관 아래쪽 작은 글씨를 읽으라는 비유라서 '속인다'가 아니라 '조건이 붙어 있다'로 들린다. `misleading`도 `false`보다 한 칸 약해 선의를 남겨 둔다. 실제 무게는 괄호 안 `they don't translate to the case where ~`에 실린다 — **어떤 조건에서 그 주장이 무너지는지**를 나열해 주면 반박이 아니라 검증 항목이 된다. 벤더 평가, 아키텍처 리뷰, 보안 심사에 그대로 쓴다."
  app1="Several vendors claim to provide zero-downtime upgrades, but it is important to read the fine print, because those claims usually assume that every client retries and that no schema change is involved."
  app1ko="여러 벤더가 무중단 업그레이드를 제공한다고 주장하지만, 그 주장은 대개 모든 클라이언트가 재시도하고 스키마 변경이 없다는 것을 전제하므로 세부 조건을 읽어야 한다."
  app2="The dashboard claims full coverage of the request path, but it is important to read the fine print, because the number does not translate to requests that fail before they reach the gateway."
  app2ko="대시보드는 요청 경로 전체를 커버한다고 하지만, 그 수치는 게이트웨이에 닿기 전에 실패한 요청에는 적용되지 않으니 세부 조건을 읽어야 한다."
>}}

{{< sentence
  en="Note that Kafka's guarantee with respect to data loss is predicated on at least one replica remaining in sync. If all the nodes replicating a partition die, this guarantee no longer holds."
  ko="데이터 유실에 관한 Kafka의 보장은 적어도 하나의 복제본이 동기 상태로 남아 있다는 것을 전제로 한다는 점에 유의하라. 파티션을 복제하는 노드가 모두 죽으면 이 보장은 더 이상 성립하지 않는다."
  source="Apache Kafka Design · Unclean leader election"
  sourceURL="https://kafka.apache.org/documentation/#design"
  note="`X is predicated on Y. If Z, this guarantee no longer holds.` — 보장을 말한 뒤 그것이 **무엇 위에 얹혀 있는지**를 밝히고, 그 받침이 빠지는 조건을 한 문장 더 써서 못 박는 구조다. `predicated on`은 `assumes`보다 형식적이고, 전제가 결론을 떠받치고 있다는 그림을 준다. `no longer holds`는 보장을 취소하는 말이 아니라 **성립 구간이 끝나는 지점**을 표시하는 말이라, 물러서는 것처럼 보이지 않는다. 사고 보고서나 SLO 문서에서 '이 조건에서는 보장이 없다'를 각 세우지 않고 적을 때 쓴다."
  app1="Note that our recovery time objective is predicated on the standby region staying warm. If the standby has been scaled to zero overnight, this guarantee no longer holds."
  app1ko="우리의 복구 목표 시간은 대기 리전이 웜 상태로 유지된다는 것을 전제로 한다. 대기 리전을 밤사이 0으로 줄여 두었다면 이 보장은 더 이상 성립하지 않는다."
  app2="Note that the idempotency of this handler is predicated on the request carrying a client-generated key. If the key is absent, this guarantee no longer holds."
  app2ko="이 핸들러의 멱등성은 요청이 클라이언트가 만든 키를 실어 보낸다는 것을 전제로 한다. 그 키가 없으면 이 보장은 더 이상 성립하지 않는다."
>}}

{{< sentence
  en="By being very fast we help ensure that the application will tip over under load before the infrastructure."
  ko="아주 빠르게 만들어 둠으로써, 부하가 걸렸을 때 인프라보다 애플리케이션이 먼저 쓰러지도록 하는 데 도움을 준다."
  source="Apache Kafka Design · Efficiency"
  sourceURL="https://kafka.apache.org/documentation/#design"
  note="`By doing X we help ensure that A will fail before B.` — 목표를 '무너지지 않는다'가 아니라 **무너지는 순서**로 적는 문형이다. 공유 인프라에서는 누가 먼저 한계에 닿느냐가 곧 설계 목표가 되는데, 이 문장은 그 순서를 그대로 목적어 자리에 넣는다. `tip over`는 한계를 넘겨 옆으로 기우는 그림이라 `crash`보다 덜 파국적이어서 부하 이야기에 어울린다. `help ensure`는 보장을 한 칸 낮춰 잡는 완충어다 — 이 조치 하나로 책임지지는 않는다는 뜻. 용량 계획, 멀티테넌시 설계, 가드레일을 왜 그 값으로 잡았는지 설명할 때 쓴다."
  app1="By keeping the rate limiter well under the database's capacity, we help ensure that a single tenant will be throttled before the cluster degrades."
  app1ko="레이트 리미터를 데이터베이스 용량보다 충분히 낮게 잡아 둠으로써, 클러스터가 나빠지기 전에 한 테넌트가 먼저 제한되도록 하는 데 도움을 준다."
  app2="By failing the build on a missing migration, we help ensure that the pipeline breaks before production does."
  app2ko="마이그레이션이 빠졌을 때 빌드를 실패시킴으로써, 운영이 깨지기 전에 파이프라인이 먼저 깨지도록 하는 데 도움을 준다."
>}}
