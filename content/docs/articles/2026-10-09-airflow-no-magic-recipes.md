---
title: 지름길이 없다고 먼저 말하고 할 일은 분명히 남기는 표현
description: 유추로 기준을 세우고, 뻔한 해법의 비용을 짚고, 무엇의 대체가 아닌지 분류로 밝히고, 걸리는 시간을 하나의 숫자 대신 범위로 답하고, 비법이 없다고 말한 뒤 책임을 지목하는 문장 5개.
weight: -49
date: 2026-10-09
source: "Apache Airflow · Best Practices"
sourceURL: https://airflow.apache.org/docs/apache-airflow/stable/best-practices.html
---

# 지름길이 없다고 먼저 말하고 할 일은 분명히 남기는 표현

데이터 파이프라인을 Airflow로 쓸 때의 권고를 모아 둔 공식 문서다. 태스크를 어떻게
나눌지, 어디에 코드를 두면 안 되는지, 무엇을 테스트로 덮을 수 있고 무엇은 못 덮는지를
다룬다. 파이프라인 지식이 아니라 **지름길을 거절하는 말투**를 골랐다 — 이미 아는 개념에
올려 규칙을 세우고, 상대가 떠올릴 답을 먼저 말해 준 뒤 비용을 붙이고, 어떤 수단이 무엇의
대체가 아닌지 분류로 밝히고, 소요 시간을 숫자 하나 대신 범위로 답하고, 비법이 없다고
말한 다음 그 일을 누가 하는지 지목하는 문장들이다.

> **원문** — Apache Airflow 기여자들, *Best Practices*,
> [apache/airflow](https://github.com/apache/airflow/blob/main/airflow-core/docs/best-practices.rst),
> [Apache-2.0](https://github.com/apache/airflow/blob/main/LICENSE).
>
> 영어 문장은 원문 그대로 인용했고, 한글 설명과 응용 문장은 이 노트에서 새로 쓴 것이다.

{{< sentence
  en="You should treat tasks in Airflow equivalent to transactions in a database. This implies that you should never produce incomplete results from your tasks."
  ko="Airflow의 태스크는 데이터베이스의 트랜잭션과 동등하게 다뤄야 한다. 이는 태스크가 절대 불완전한 결과를 내놓아서는 안 된다는 뜻이다."
  source="Apache Airflow · Creating a task"
  sourceURL="https://airflow.apache.org/docs/apache-airflow/stable/best-practices.html#creating-a-task"
  note="`You should treat X equivalent to Y. This implies that you should never Z.` — 이미 합의된 개념에 올려 규칙을 세우는 **유추** 문형이다. 설명이 아니라 빌려오기다. 트랜잭션이 무엇인지는 상대가 이미 아니까, 거기 붙어 있던 성질(전부 아니면 전무)을 태스크 쪽으로 옮겨 온다. 톤을 정하는 말은 `equivalent to`다. `like`나 `similar to`로 쓰면 비유에 그쳐 '어디까지 비슷한가'를 두고 다툴 여지가 남지만, `equivalent to`는 같은 등급으로 취급하라는 요구가 된다. 그리고 두 번째 문장의 `This implies that`이 유추를 규칙으로 환전한다 — 비유를 던져 놓고 알아서 해석하라고 두지 않고, 거기서 나오는 금지 하나를 직접 못 박는다. 그 금지를 예외 없이 만드는 것은 `never`다. 새 규칙을 설득할 때, 근거를 처음부터 쌓는 대신 상대가 이미 받아들인 규칙에 올려붙이고 싶을 때."
  app1="You should treat a feature flag flip equivalent to a deploy. This implies that you should never flip one without an owner watching the dashboards."
  app1ko="기능 플래그를 켜고 끄는 일은 배포와 동등하게 다뤄야 한다. 이는 대시보드를 지켜보는 담당자 없이 절대 플래그를 건드려서는 안 된다는 뜻이다."
  app2="You should treat an access review equivalent to a change request. This implies that you should never close one without a record of who approved it."
  app2ko="권한 검토는 변경 요청과 동등하게 다뤄야 한다. 이는 누가 승인했는지에 대한 기록 없이 절대 검토를 종료해서는 안 된다는 뜻이다."
>}}

{{< sentence
  en="The obvious solution is to save these objects to the database so they can be read while your code is executing. However, reading and writing objects to the database are burdened with additional time overhead."
  ko="뻔한 해법은 이 객체들을 데이터베이스에 저장해 두어, 코드가 실행되는 동안 읽히게 하는 것이다. 하지만 객체를 데이터베이스에서 읽고 쓰는 일에는 추가 시간 비용이 따라붙는다."
  source="Apache Airflow · Mocking variables and connections"
  sourceURL="https://airflow.apache.org/docs/apache-airflow/stable/best-practices.html#mocking-variables-and-connections"
  note="`The obvious solution is to X. However, X is burdened with Y.` — 상대가 떠올릴 답을 **내가 먼저 말해 주고** 그 답의 비용을 붙이는 문형이다. 반대 의견을 낼 때 가장 많이 막히는 지점이 '그럼 그냥 이렇게 하면 되잖아요'인데, 그 말을 상대가 꺼내기 전에 내 문장 안에 넣어 둔다. 그 일을 하는 말이 `obvious`다. 그 해법이 안이하다고 하지 않고, 누구나 먼저 떠올리는 것이 당연하다고 인정해 준다. 그래서 뒤에 오는 `However`가 사람을 깎는 말이 되지 않는다. `burdened with`도 세기를 고른 결과다. `is slower`는 못 쓴다는 판정이지만 `burdened with additional overhead`는 비용이 붙는다고만 말한다 — 그 비용을 지불할지는 읽는 사람이 정한다. 리뷰 코멘트나 설계 문서에서 남의 안을 깎지 않으면서 다른 안을 올리고 싶을 때."
  app1="The obvious solution is to add a retry around the failing call so the alert stops firing. However, retries against a saturated downstream are burdened with additional load at exactly the wrong moment."
  app1ko="뻔한 해법은 실패하는 호출에 재시도를 감아 알림이 더 울리지 않게 하는 것이다. 하지만 이미 포화된 하위 서비스를 향한 재시도에는 가장 안 좋은 시점에 부하가 더 얹히는 비용이 따라붙는다."
  app2="The obvious solution is to give the on-call group standing write access to the production database. However, permissions that nobody has to request are burdened with a justification we owe at every audit from then on."
  app2ko="뻔한 해법은 온콜 그룹에게 운영 데이터베이스 쓰기 권한을 상시로 주는 것이다. 하지만 아무도 요청할 필요가 없는 권한에는 그 뒤로 감사마다 우리가 해명해야 할 몫이 따라붙는다."
>}}

{{< sentence
  en="That is an integration test: it needs a metadata database and a Dag that Airflow can serialize, so it is not a substitute for the unit tests above."
  ko="그것은 통합 테스트다. 메타데이터 데이터베이스와 Airflow가 직렬화할 수 있는 Dag가 있어야 돌아가므로, 위의 단위 테스트를 대신하지는 못한다."
  source="Apache Airflow · Unit tests"
  sourceURL="https://airflow.apache.org/docs/apache-airflow/stable/best-practices.html#unit-tests"
  note="`That is an X: it needs A and B, so it is not a substitute for Y.` — 어떤 수단의 **이름을 먼저 정하고, 그 이름에서 한계를 끌어내는** 문형이다. 순서가 핵심이다. '이걸로는 부족하다'를 먼저 말하면 평가가 되지만, 분류(`That is an integration test`)를 앞에 두면 뒤에 오는 한계가 평가가 아니라 분류의 결과로 읽힌다. 그 연결을 콜론이 맡는다 — 근거를 `because`로 달지 않고 콜론으로 이어 붙이니, 덧붙인 설명이 아니라 정의의 일부처럼 들어온다. `it needs A and B`는 한계의 근거를 **요구 조건**으로 적은 것이다. 느리다거나 불안정하다는 성질이 아니라 무엇이 있어야 돌아가는지를 적었으므로, 반박하려면 그 조건을 치워야 한다. 닫는 말은 `not a substitute for`다. 쓸모없다는 뜻이 아니라 교체되지 않는다는 뜻이어서, 둘 다 있어야 한다는 결론으로 간다. 테스트 전략, 모니터링 계층, 감사 증거의 종류를 구분해 적을 때."
  app1="That is a synthetic probe: it needs a dedicated test account and a path we keep exempt from rate limits, so it is not a substitute for the real-user metrics above."
  app1ko="그것은 합성 모니터링이다. 전용 테스트 계정과 우리가 속도 제한에서 계속 빼 두는 경로가 있어야 돌아가므로, 위의 실제 사용자 지표를 대신하지는 못한다."
  app2="That is a quarterly access review: it needs a frozen snapshot and a reviewer with time to read it, so it is not a substitute for the automated checks that run on every grant."
  app2ko="그것은 분기 권한 검토다. 멈춰 세운 스냅숏과 그것을 읽을 시간이 있는 검토자가 있어야 돌아가므로, 권한을 부여할 때마다 돌아가는 자동 점검을 대신하지는 못한다."
>}}

{{< sentence
  en="Depending on your configuration, speed of your distributed filesystem, number of files, number of Dags, number of changes in the files, sizes of the files, number of Dag processors, speed of CPUS, this can take from seconds to minutes, in extreme cases many minutes."
  ko="설정, 분산 파일시스템의 속도, 파일 개수, Dag 개수, 파일의 변경 개수, 파일 크기, Dag 프로세서 개수, CPU 속도에 따라 이 일은 수 초에서 수 분까지, 극단적인 경우 여러 분이 걸릴 수 있다."
  source="Apache Airflow · Triggering Dags after changes"
  sourceURL="https://airflow.apache.org/docs/apache-airflow/stable/best-practices.html#triggering-dags-after-changes"
  note="`Depending on A, B, C, ..., this can take from X to Y, in extreme cases Z.` — '얼마나 걸리나요'에 **숫자 하나를 주지 않으면서 답하는** 문형이다. 거절이 아니다. `Depending on ~` 뒤에 변수를 길게 늘어놓는 것 자체가 답의 일부다 — 목록이 길수록 왜 단일 숫자가 나올 수 없는지가 설명되고, 동시에 '무엇에 좌우되는지는 우리가 알고 있다'는 증거가 된다. 그래서 모른다는 말이 아니라 **구조를 안다**는 말로 읽힌다. 뒤쪽은 둘로 나뉜다. `from X to Y`가 실제로 쓸 수 있는 범위를 주고, `in extreme cases Z`가 꼬리를 따로 떼어 놓는다. 꼬리를 범위에 섞지 않은 것이 중요하다 — 섞으면 범위가 넓어져 쓸모가 없어지지만, 떼어 놓으면 평소 기대값과 최악의 경우를 한 문장에서 둘 다 말할 수 있다. 용량 산정, 복구 시간 질문, 마이그레이션 일정 추정처럼 숫자를 요구받지만 하나로 답하면 거짓이 되는 자리에서."
  app1="Depending on the size of the backlog, the number of partitions, how far the consumer has fallen behind, and whether the downstream is still rate-limiting us, a full replay can take from minutes to hours, in extreme cases most of a working day."
  app1ko="적체된 양, 파티션 개수, 컨슈머가 얼마나 뒤처져 있는지, 하위 서비스가 아직 우리를 속도 제한하고 있는지에 따라 전체 재처리는 수 분에서 수 시간까지, 극단적인 경우 근무일 대부분이 걸릴 수 있다."
  app2="Depending on how many services still hold the old key, how each of them reloads configuration, and how many need a restart to pick up the new one, a full credential rotation can take from hours to days, in extreme cases a whole release cycle."
  app2ko="아직 옛 키를 들고 있는 서비스가 몇 개인지, 각 서비스가 설정을 어떻게 다시 읽는지, 새 키를 집어 가려면 몇 개를 재시작해야 하는지에 따라 자격 증명 전체 교체는 수 시간에서 수 일까지, 극단적인 경우 릴리스 주기 하나가 걸릴 수 있다."
>}}

{{< sentence
  en="There are no magic recipes for making your Dag &quot;less complex&quot; - since this is a Python code, it's the Dag writer who controls the complexity of their code."
  ko="Dag를 '덜 복잡하게' 만드는 마법 같은 비법은 없다 — 이것은 파이썬 코드이므로, 자기 코드의 복잡도를 통제하는 사람은 Dag를 쓰는 바로 그 사람이다."
  source="Apache Airflow · Reducing Dag complexity"
  sourceURL="https://airflow.apache.org/docs/apache-airflow/stable/best-practices.html#reducing-dag-complexity"
  note="`There are no magic recipes for X - since ..., it's Y who controls Z.` — 비법을 달라는 요청을 거절하면서 **그 일을 누가 하는지 지목하는** 문형이다. 두 동작이 붙어 있다. 앞은 비법의 존재를 부정하고(`There are no magic recipes`), 뒤는 그렇다면 누구의 일인지를 짚는다. 지목에 쓰인 것이 `it's Y who ~` 분열문이다. `the Dag writer controls the complexity`로 써도 뜻은 같지만, `it's ~ who`로 쪼개면 '다른 누구도 아니라 바로 그 사람'이라는 대조가 생긴다. 도구나 플랫폼이 대신 해 주지 않는다는 말을 직접 하지 않고 이 대조 하나로 처리한다. 근거는 `since this is a Python code`다. 평범한 사실 하나를 깔아 두는 것인데, 이것이 거절을 개인적인 것이 아니게 만든다 — 비법이 없는 이유가 내 판단이 아니라 대상의 성질이 되기 때문이다. 체크리스트를 달라는 요청에 체크리스트로 답할 수 없을 때, 또는 '자동화로 해결되는 문제가 아니다'를 적어야 할 때."
  app1="There are no magic recipes for making an incident review blameless - since this is a conversation, it's the facilitator who controls whether people can say what actually happened."
  app1ko="장애 회고를 비난 없는 자리로 만드는 마법 같은 비법은 없다 — 이것은 대화이므로, 사람들이 실제로 무슨 일이 있었는지 말할 수 있는지를 통제하는 사람은 진행자 바로 그 사람이다."
  app2="There are no magic recipes for making a pull request easy to review - since this is a series of commits, it's the author who controls how much the reviewer has to hold in their head at once."
  app2ko="풀 리퀘스트를 리뷰하기 쉽게 만드는 마법 같은 비법은 없다 — 이것은 커밋의 연속이므로, 리뷰어가 한 번에 머릿속에 담아야 할 양을 통제하는 사람은 작성자 바로 그 사람이다."
>}}
