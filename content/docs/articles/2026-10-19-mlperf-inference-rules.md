---
title: 결과에 자격을 걸고 입증 책임을 넘기는 표현
description: 재현되지 않는 결과를 정의상 무효로 만들고, 입증 책임의 주소를 한 문장에 박고, 받지 못한 자료를 미해결로 기록하고, 측정 장치의 부산물을 실제 조건과 가르고, 수단의 의도를 한정해 악용을 잘라내는 문장 5개.
weight: -59
date: 2026-10-19
source: "MLCommons · MLPerf Inference Rules"
sourceURL: https://github.com/mlcommons/inference_policies/blob/master/inference_rules.adoc
---

# 결과에 자격을 걸고 입증 책임을 넘기는 표현

MLPerf 추론 벤치마크의 **규칙 문서**다. 어떤 구현이 레퍼런스와 동등한지, 어떤 최적화가 허용되고
어떤 것이 금지되는지, 제출된 수치를 감사할 때 누가 무엇을 내놓아야 하는지를 한 파일에 적어 둔
글이다. 경쟁사끼리 같은 이름을 걸고 숫자를 공개하는 판이라, 이 문서는 **숫자를 믿을 수 있게 만드는
문장**으로 가득하다 — 그래서 벤치마크 지식보다 그 문장 틀이 배울 점이라 골랐다. 결과의 자격을
정의로 박탈하고, 입증 책임의 주소를 먼저 적고, 받지 못한 자료를 비난 대신 기록으로 남기고, 측정
환경에서만 존재하는 것을 실제 조건과 가르고, 편의로 만든 수단이 지표를 올리는 데 쓰이는 것을
의도 한정으로 잘라낸다. 성능 수치를 검토할 때, 보안 감사 자료를 요청할 때, 테스트 전용 장치가
성과로 둔갑할 때 그대로 틀을 가져다 쓸 수 있다.

> **원문** — MLCommons, *MLPerf Inference Rules*,
> [mlcommons/inference_policies](https://github.com/mlcommons/inference_policies/blob/master/inference_rules.adoc),
> [Apache License 2.0](https://github.com/mlcommons/inference_policies/blob/master/LICENSE.md)
> (리포지터리 루트 LICENSE.md — 복제·배포 허용).
>
> 영어 문장은 원문 그대로 인용했고, 한글 설명과 응용 문장은 이 노트에서 새로 쓴 것이다.

{{< sentence
  en="Results that cannot be replicated are not valid results."
  ko="재현할 수 없는 결과는 유효한 결과가 아니다."
  source="MLPerf Inference Rules → General rules → Replicability is mandatory"
  sourceURL="https://github.com/mlcommons/inference_policies/blob/master/inference_rules.adoc"
  note="`X that cannot be V-ed are not valid X.` — 같은 명사를 주어와 서술어에 두 번 써서 **자격을 정의로 박탈하는** 구문이다. 틀렸다고 하지 않고 `are not valid results`라고 하는 것이 핵심 — 내용의 참·거짓을 다투지 않고 **받아들여질 수 있는 것의 범위**만 정한다. `valid`는 사람이 내리는 평가가 아니라 규칙이 내리는 판정이라서, 책임이 판정자에서 규칙으로 옮겨간다. 같은 명사를 반복하는 형태 자체가 '그건 결과가 아니라 일화다'라는 톤을 만든다. 재현 절차 없는 성능 수치, 로그 없는 원인 주장, 테스트 없는 개선 보고 앞에서 꺼낸다."
  app1="A latency number that cannot be reproduced on a quiet environment is not a performance result."
  app1ko="조용한 환경에서 재현되지 않는 지연 수치는 성능 측정 결과가 아니다."
  app2="A root cause that cannot be traced to a line in the logs is not a root cause."
  app2ko="로그의 어느 줄로도 짚어낼 수 없는 근본 원인은 근본 원인이 아니다."
>}}

{{< sentence
  en="The burden is on the submitter to provide sufficient materials to demonstrate that the submission is compliant with the rules."
  ko="규칙을 지켰음을 보여 줄 충분한 자료를 내놓을 책임은 제출자에게 있다."
  source="MLPerf Inference Rules → General rules → Audit Process"
  sourceURL="https://github.com/mlcommons/inference_policies/blob/master/inference_rules.adoc"
  note="`The burden is on X to provide sufficient materials to demonstrate that Y.` — 입증 책임을 한 문장에 배분하는 구문이다. `The burden is on X`가 먼저 **책임의 주소**를 박고, 뒤의 to부정사가 그 책임의 내용을 적는다. `sufficient`는 분량을 숫자로 못 박지 않으면서 **충분한지 판단할 권한을 받는 쪽에 남기는** 단어다 — 무엇을 내라가 아니라 납득시킬 만큼 내라는 뜻이 된다. `demonstrate`도 고른 말이다: `prove`보다 약하고 `explain`보다 강해서, 말로 설명하는 게 아니라 자료로 보여 주는 수준을 가리킨다. 감사나 승인 자리에서 '안 된다는 걸 내가 증명해야 하느냐'가 쟁점이 될 때 방향을 되돌리는 문장."
  app1="The burden is on the requesting team to provide sufficient evidence to demonstrate that the exception is still needed."
  app1ko="그 예외가 아직도 필요하다는 것을 보여 줄 충분한 근거를 내놓을 책임은 요청한 팀에 있다."
  app2="The burden is on the author to provide sufficient context to demonstrate that the migration can be rolled back."
  app2ko="그 마이그레이션을 되돌릴 수 있다는 것을 보여 줄 충분한 맥락을 적을 책임은 작성자에게 있다."
>}}

{{< sentence
  en="Where information or access is not provided, the auditor's report will list the issues that could not be resolved."
  ko="자료나 접근 권한을 받지 못한 경우, 감사자의 보고서는 해소되지 못한 쟁점을 열거한다."
  source="MLPerf Inference Rules → FAQ → Audit"
  sourceURL="https://github.com/mlcommons/inference_policies/blob/master/inference_rules.adoc"
  note="`Where X is not provided, the report will list the issues that could not be resolved.` — 비협조에 벌칙을 걸지 않고 **기록으로 남긴다고만** 적는 구문이다. 조건절을 `If`가 아니라 `Where`로 여는 것이 톤을 정한다 — 특정 상대를 가정하지 않고 '그런 경우에는'이라는 규정문 어투가 되어 추궁이 섞이지 않는다. 미해결을 `refused`나 `withheld` 같은 능동태로 쓰지 않고 `could not be resolved`로 적는 것도 같은 방향이다: 누가 막았는지 쓰지 않는다. 그런데도 압력은 세다 — 자료를 주지 않으면 보고서에 빈칸이 남고, **그 빈칸 자체가 결론이 된다**. 자료 요청이 계속 미뤄질 때 쓰는 가장 깔끔한 문장이다."
  app1="Where logs or dashboard access is not provided, the incident review will list the questions that could not be answered."
  app1ko="로그나 대시보드 접근 권한을 받지 못한 경우, 장애 리뷰는 답하지 못한 질문을 열거한다."
  app2="Where a reason for the change is not provided, the review summary will list the hunks that could not be evaluated."
  app2ko="변경 이유를 받지 못한 경우, 리뷰 요약은 판단하지 못한 변경 덩어리를 열거한다."
>}}

{{< sentence
  en="Query indices are an artifact of using a finite set of samples to represent an infinite set, and would have no counterpart in production scenarios. As such, the system under test should not cache any information associated with query indices."
  ko="쿼리 인덱스는 무한한 집합을 유한한 표본으로 대신하느라 생긴 부산물이며, 실제 운영 환경에는 대응하는 것이 없다. 따라서 테스트 대상 시스템은 쿼리 인덱스에 딸린 어떤 정보도 캐시해서는 안 된다."
  source="MLPerf Inference Rules → FAQ"
  sourceURL="https://github.com/mlcommons/inference_policies/blob/master/inference_rules.adoc"
  note="`X is an artifact of A, and would have no counterpart in B. As such, ...` — 금지의 근거를 규칙이 아니라 **대상의 출처**에서 끌어오는 구문이다. `artifact`는 측정하느라 생겨 버린 것을 가리키는 말이라, 이 한 단어로 그것이 시스템의 성질이 아니라 **실험 장치의 흔적**이라는 판정이 끝난다. `would have no counterpart`의 가정법 `would`도 일부러 고른 것이다 — 운영 환경에 그런 게 없다고 단정하는 대신 '있다 해도 대응물이 없을 것'이라고 적어 반례 시비를 피한다. 그다음 `As such`가 출처에서 금지로 건너가는 다리를 놓는다. 테스트에만 존재하는 값에 기대어 숫자가 좋아질 때 그 숫자를 무효로 만드는 방법이다."
  app1="The retry counter in the fixture is an artifact of replaying a recorded trace, and would have no counterpart in production traffic. As such, the handler should not branch on it."
  app1ko="픽스처의 재시도 카운터는 녹화된 트레이스를 다시 재생하느라 생긴 부산물이며, 실제 트래픽에는 대응하는 것이 없다. 따라서 핸들러가 그 값으로 분기해서는 안 된다."
  app2="The order of findings in the scanner output is an artifact of how the files are walked, and would have no counterpart in how urgent the findings are. As such, the report should not present it as a priority list."
  app2ko="스캐너 출력에서 지적 사항이 놓인 순서는 파일을 훑는 방식 때문에 생긴 부산물이며, 지적의 시급함과는 대응하는 것이 없다. 따라서 보고서가 그 순서를 우선순위 목록처럼 내보여서는 안 된다."
>}}

{{< sentence
  en="The performance test mode's response caching is specifically designed to replay the same workload for performance comparisons, not to avoid computation."
  ko="성능 테스트 모드의 응답 캐싱은 성능을 비교하려고 같은 작업을 다시 재생하기 위한 것이며, 계산을 건너뛰기 위한 것이 아니다."
  source="MLPerf Inference Rules → FAQ → E2E-RAG"
  sourceURL="https://github.com/mlcommons/inference_policies/blob/master/inference_rules.adoc"
  note="`X is specifically designed to A, not to B.` — 같은 수단이 두 목적에 쓰일 수 있을 때, **허용된 목적을 먼저 적고 금지된 목적을 바로 잘라내는** 구문이다. `specifically`가 '그 목적에 한정해서'를 맡기 때문에, 뒤의 `not to B`는 새로 추가하는 금지 조항이 아니라 **처음부터 범위 밖**이라는 뜻이 된다 — 규칙을 늘리지 않고 악용을 막는다. `designed to`는 의도를 만든 쪽에 돌리므로 '내가 금지한다'가 아니라 '그렇게 쓰려고 만든 물건이 아니다'가 되어, 상대를 추궁하지 않고도 선이 그어진다. 편의로 만들어 둔 플래그나 예외 경로가 지표를 올리는 데 쓰이기 시작할 때 꺼낸다."
  app1="The maintenance window flag is specifically designed to silence alerts during a planned change, not to keep a failing service out of the error budget."
  app1ko="점검 창 플래그는 예정된 변경 중에 알림을 줄이기 위한 것이며, 고장 난 서비스를 오류 예산에서 빼기 위한 것이 아니다."
  app2="The fast-track review path is specifically designed to unblock an urgent fix, not to move a large refactor past review."
  app2ko="신속 리뷰 경로는 급한 수정을 막히지 않게 하려는 것이며, 큰 리팩터링을 리뷰 없이 통과시키기 위한 것이 아니다."
>}}
