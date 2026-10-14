---
title: 하지 않는 일을 범위로 적는 표현
description: 없는 기능을 상대의 선택지로 옮겨 적고, 비교 대상 전부를 인정한 뒤 하나로 못 줄인다는 결론을 끌어내고, 거절과 우회 경로를 한 덩어리로 묶고, 요구가 아니라 구현 계층만 틀렸다고 판정하고, 제약을 메커니즘에서 따라 나오게 적는 문장 5개.
weight: -55
date: 2026-10-15
source: "FoundationDB · Anti-Features"
sourceURL: https://apple.github.io/foundationdb/anti-features.html
---

# 하지 않는 일을 범위로 적는 표현

애플이 공개한 분산 키-값 데이터베이스 FoundationDB의 문서 중 **안티피처(anti-features)** 페이지다.
질의 언어, 분석 프레임워크, 단절 상태 동작, 긴 트랜잭션처럼 **코어가 제공하지 않기로 한 것들**을
한 페이지에 모아, 왜 안 넣었고 그러면 그 일은 어디서 하라는 것인지 적어 둔 문서다. 데이터베이스
내부보다 **거절문의 구조**가 배울 점이라 골랐다 — 요청을 받아 주지 않으면서도 상대를 빈손으로
돌려보내지 않아야 하고, 못 한다와 안 한다를 피해 여기 일이 아니다로 말해야 하고, 숫자로 된
한계를 통보가 아니라 사양으로 읽히게 적어야 하는 글이다. 기능 요청을 돌려보낼 때, 타임아웃이나
보존 기간의 예외 요청을 미리 닫을 때, 플랫폼 팀이 표준을 정하지 않기로 결정한 이유를 적을 때
그대로 틀을 가져다 쓸 수 있다.

> **원문** — FoundationDB 프로젝트 (Apple Inc.), *Anti-Features*,
> [apple/foundationdb](https://github.com/apple/foundationdb/blob/main/documentation/sphinx/source/anti-features.rst)
> (문서 사이트: [apple.github.io/foundationdb — Anti-Features](https://apple.github.io/foundationdb/anti-features.html)),
> [Apache-2.0](https://github.com/apple/foundationdb/blob/main/LICENSE) 라이선스.
>
> 영어 문장은 원문 그대로 인용했고, 한글 설명과 응용 문장은 이 노트에서 새로 쓴 것이다.

{{< sentence
  en="The FoundationDB core exposes a robust and powerful API but includes no separate query language. FoundationDB empowers developers to employ a broad range of data models and use the query languages best suited to their applications, implemented as layers."
  ko="FoundationDB 코어는 견고하고 강력한 API를 제공하지만 별도의 질의 언어는 포함하지 않는다. FoundationDB는 개발자가 넓은 범위의 데이터 모델을 쓰고, 각자의 애플리케이션에 가장 맞는 질의 언어를 레이어로 구현해 쓰게 해 준다."
  source="FoundationDB · Query languages"
  sourceURL="https://apple.github.io/foundationdb/anti-features.html"
  note="`X exposes A but includes no B. X empowers developers to C.` — 없는 기능을 결함이 아니라 **상대의 선택지**로 옮겨 적는 2단 문장이다. 첫 문장의 `but includes no B`가 핵심 — 없다는 사실을 뒤로 미루지 않고 자랑(`robust and powerful`)과 같은 문장에 붙여 적는다. 그래서 변명을 끼워 넣을 자리가 애초에 생기지 않고, 상대가 캐묻기 전에 내 쪽에서 먼저 말한 것이 된다. 둘째 문장은 주어를 바꾸지 않고 **동사를 바꿔** 같은 사실을 다시 적는다 — `empowers developers to`. 없음을 공백으로 두면 미완성으로 읽히지만, 그 자리를 누가 채우는지 적으면 설계로 읽힌다. `does not provide Y yet`은 약속처럼 들려 나중에 독촉을 받고, `Y is not supported`는 대화를 끝내 버린다. `best suited to their applications`도 계산된 표현이다 — 내가 고르지 않은 이유를 상대가 더 잘 안다는 쪽에 둔다. 기능 요청을 거절하면서 우회 경로를 상대 손에 남길 때, 플랫폼 팀이 표준을 정하지 않기로 할 때 쓴다."
  app1="The deploy pipeline exposes a single promote step but includes no environment-specific hooks. It empowers each team to run the checks best suited to their service, implemented in their own repository."
  app1ko="배포 파이프라인은 승격 단계 하나를 제공하지만 환경별 훅은 포함하지 않는다. 각 팀이 자기 서비스에 가장 맞는 검사를 자기 리포지터리에 구현해 돌리게 해 준다."
  app2="The audit log API exposes raw events but includes no built-in report templates. It empowers each reviewer to assemble the views best suited to their scope, built on top of the same export."
  app2ko="감사 로그 API는 원본 이벤트를 제공하지만 보고서 템플릿은 포함하지 않는다. 같은 추출물 위에서 각 검토자가 자기 범위에 가장 맞는 화면을 직접 구성하게 해 준다."
>}}

{{< sentence
  en="Each of these data models is useful and appropriate for different use cases. An application that is even moderately complex may have distinct data sets that best fit different models."
  ko="이 데이터 모델들은 각각 서로 다른 용례에서 유용하고 적절하다. 조금만 복잡한 애플리케이션이라도 서로 다른 모델이 가장 잘 맞는 데이터 집합을 여러 개 갖고 있을 수 있다."
  source="FoundationDB · Data models"
  sourceURL="https://apple.github.io/foundationdb/anti-features.html"
  note="`Each of these X is useful and appropriate for different Y. A Z that is even moderately complex may have distinct ... that best fit different X.` — 비교 대상 **전부를 인정해 두고**, 그 인정에서 하나로 줄일 수 없다는 결론을 끌어내는 2단 문장이다. 첫 문장은 우열을 가리지 않는다. `useful and appropriate for different use cases`는 어느 쪽도 틀리지 않았다고 먼저 적어 두는 말이고, 그래서 각 모델을 쓰는 사람들과 싸우지 않고도 다음 문장으로 넘어갈 수 있다. 결론을 밀어 넣는 단어는 둘째 문장의 `even moderately complex`다 — 아주 복잡한 시스템이 아니라 **조금만 복잡해도**라고 기준을 낮게 잡아, 여러 모델이 섞이는 상황을 예외가 아니라 기본값으로 만든다. `may have`로 약하게 적은 것도 계산이다. 반드시 그렇다고 하면 반례 하나로 무너지지만, 있을 수 있다고 하면 반례가 문장을 깨지 못한다. 도구나 표준을 하나로 통일하자는 압박을 받을 때, 왜 단일 해법을 고르지 않았냐는 질문에 답할 때 쓴다."
  app1="Each of these alerting rules is useful and appropriate for different failure modes. A service that is even moderately complex may have distinct symptoms that best fit different rules."
  app1ko="이 알림 규칙들은 각각 서로 다른 장애 양상에서 유용하고 적절하다. 조금만 복잡한 서비스라도 서로 다른 규칙이 가장 잘 맞는 증상을 여러 개 갖고 있을 수 있다."
  app2="Each of these review checklists is useful and appropriate for different kinds of change. A pull request that is even moderately large may have distinct files that best fit different checklists."
  app2ko="이 리뷰 체크리스트들은 각각 서로 다른 종류의 변경에서 유용하고 적절하다. 조금만 큰 풀 리퀘스트라도 서로 다른 체크리스트가 가장 잘 맞는 파일을 여러 개 갖고 있을 수 있다."
>}}

{{< sentence
  en="Analytic frameworks are outside the scope of the FoundationDB core. However, because the core can use range reads to efficiently scan large swaths of data, analytics can be implemented within a layer, possibly as part of a query language."
  ko="분석 프레임워크는 FoundationDB 코어의 범위 밖이다. 다만 코어가 범위 읽기로 넓은 구간의 데이터를 효율적으로 훑을 수 있으므로, 분석은 레이어 안에서 구현할 수 있고 질의 언어의 일부로 둘 수도 있다."
  source="FoundationDB · Analytic frameworks"
  sourceURL="https://apple.github.io/foundationdb/anti-features.html"
  note="`X is outside the scope of Y. However, because Y can A, X can be implemented within Z, possibly as B.` — 거절과 **우회 경로**를 한 덩어리로 묶는 문형이다. 거절의 성격을 정하는 말은 `outside the scope` — 못 한다(능력)도, 안 한다(의지)도 아니라 **여기 일이 아니다**(범위)라고 적는다. 능력으로 적으면 할 수 있다는 반박을 받고, 의지로 적으면 왜 안 하느냐는 설득을 받는데, 범위로 적으면 둘 다 과녁을 벗어난다. 뒤의 `However, because Y can A`는 길을 열면서도 보증을 하지 않는다 — 근거를 내가 이미 가진 기능 하나(`range reads`)로 한정했기 때문에, 열어 준 것은 가능성이고 책임은 넘어가지 않는다. 마지막 `possibly as part of ...`는 제안의 **온도를 낮추는** 장치다. 설계까지 지정하면 그 설계를 떠안게 되지만, 가능성만 적으면 결정은 상대 쪽에 남는다. 범위 밖 요청을 돌려보내면서 상대를 빈손으로 두지 않을 때 쓴다."
  app1="Capacity forecasting is outside the scope of this dashboard. However, because the exporter already keeps per-hour maximums, forecasting can be built in a separate job, possibly as part of the weekly report."
  app1ko="용량 예측은 이 대시보드의 범위 밖이다. 다만 익스포터가 이미 시간별 최댓값을 보관하고 있으므로, 예측은 별도 잡으로 만들 수 있고 주간 리포트의 일부로 둘 수도 있다."
  app2="Access recertification is outside the scope of the audit script. However, because the script records who approved each grant, recertification can be done on top of its output, possibly as part of the quarterly review."
  app2ko="접근 권한 재승인은 이 감사 스크립트의 범위 밖이다. 다만 스크립트가 각 권한을 누가 승인했는지 기록해 두므로, 재승인은 그 출력 위에서 할 수 있고 분기 점검의 일부로 둘 수도 있다."
>}}

{{< sentence
  en="Because it would sacrifice ACID properties, we believe that in those applications where disconnected operation is needed, the database is the wrong tier to implement it."
  ko="ACID 속성을 희생해야 하므로, 단절 상태 동작이 필요한 애플리케이션이라면 그것을 구현할 계층으로 데이터베이스는 맞지 않다고 우리는 본다."
  source="FoundationDB · Disconnected operation"
  sourceURL="https://apple.github.io/foundationdb/anti-features.html"
  note="`Because it would sacrifice X, we believe that in those applications where Y is needed, Z is the wrong tier to implement it.` — 요구 자체는 건드리지 않고 **구현 위치만 틀렸다고** 판정하는 문장이다. 훔칠 자리는 `the wrong tier to implement it` — 필요 없다거나 안 된다고 하지 않는다. `in those applications where Y is needed`로 **필요하다는 전제를 그대로 받아 놓고** 자리만 옮기기 때문에, 요청한 사람과의 싸움이 설계 논의로 바뀐다. 앞에 `Because it would sacrifice X`를 먼저 세운 순서도 중요하다. 대가를 먼저 적어 두면 결론이 취향이 아니라 비용 계산으로 읽힌다 — 뒤집어 쓰면 거절이 먼저 오고 이유가 변명처럼 따라붙는다. 약해 보이는 `we believe`도 의도적이다. 사실이 아니라 판단임을 밝혀, 다른 계층에서 해 보겠다는 반론이 들어올 틈을 일부러 남긴다. 어떤 기능을 우리 서비스나 레이어에 넣어 달라는 요청을 돌려보낼 때 쓴다."
  app1="Because it would sacrifice replay safety, we believe that in those pipelines where deduplication is needed, the consumer is the wrong tier to implement it."
  app1ko="재처리 안전성을 희생해야 하므로, 중복 제거가 필요한 파이프라인이라면 그것을 구현할 계층으로 컨슈머는 맞지 않다고 우리는 본다."
  app2="Because it would sacrifice a clean audit trail, we believe that in those workflows where emergency access is needed, the on-call script is the wrong tier to implement it."
  app2ko="깔끔한 감사 추적을 희생해야 하므로, 긴급 접근이 필요한 업무 흐름이라면 그것을 구현할 계층으로 온콜 스크립트는 맞지 않다고 우리는 본다."
>}}

{{< sentence
  en="The system employs multiversion concurrency control and maintains conflict information for a five second period. A transaction that is kept open longer will not be able to commit."
  ko="이 시스템은 다중 버전 동시성 제어를 쓰고 충돌 정보를 5초 동안 유지한다. 그보다 오래 열어 둔 트랜잭션은 커밋할 수 없다."
  source="FoundationDB · Long-running read/write transactions"
  sourceURL="https://apple.github.io/foundationdb/anti-features.html"
  note="`The system employs A and maintains B for <기간>. A X that is kept open longer will not be able to Y.` — 제약을 규칙으로 통보하지 않고 **메커니즘에서 따라 나오게** 적는 2단 문장이다. 첫 문장은 금지를 한 마디도 하지 않는다. 쓰는 기법과 보관 기간만 적는다. 둘째 문장은 거기서 저절로 나오는 결과다. 그래서 왜 5초냐는 질문이 정책 협상이 아니라 구조 설명으로 돌아간다 — 숫자를 한계 쪽이 아니라 **메커니즘 쪽**에 둔 것이 이 효과의 전부다. 톤을 정하는 말은 `will not be able to`다. `is not allowed to`는 허가의 문제라서 예외를 줄 사람을 찾게 되고, `must not`은 규정이라서 어길 수 있다. 능력의 부재로 적으면 협상할 상대가 없어진다. 숫자를 `a five second period`처럼 기간으로 적고 `longer`로 비교만 한 것도 포인트다. 경계값을 다투지 않아도 결론이 선다. 타임아웃, 보존 기간, 재시도 한도를 설명하면서 예외 요청을 미리 닫을 때 쓴다."
  app1="The collector batches events in memory and keeps them for a sixty second window. An event that arrives later will not be able to join that batch."
  app1ko="수집기는 이벤트를 메모리에 모으고 60초 구간 동안 보관한다. 그보다 늦게 도착한 이벤트는 그 배치에 들어갈 수 없다."
  app2="The audit store indexes requests by actor and keeps raw request bodies for a thirty day period. A review that starts later will not be able to show what was sent."
  app2ko="감사 저장소는 요청을 행위자 기준으로 색인하고 원본 요청 본문을 30일 동안 보관한다. 그보다 늦게 시작한 점검은 무엇이 전송됐는지 보여 줄 수 없다."
>}}
