---
title: 숫자가 어디까지 말이 되는지 적는 표현
description: 기록한 값과 보고 싶은 지표를 가르고, 성립하지 않는 비교를 무의미하다고 닫고, 같은 이름의 두 숫자가 어긋날 것을 미리 적고, 한 사건을 어느 지표에 얹을지 규약으로 정하고, 되살릴 가치를 의심만 올려 두는 문장 5개.
weight: -57
date: 2026-10-17
source: "vLLM · Metrics (design)"
sourceURL: https://docs.vllm.ai/en/latest/design/metrics/
---

# 숫자가 어디까지 말이 되는지 적는 표현

LLM 추론 서버 vLLM의 **메트릭 설계 문서**다. V1 엔진이 어떤 지표를 왜 그렇게 내보내는지, 요청
처리 중의 구간(큐·프리필·디코드)을 어떤 타임스탬프로 재는지, 더 쓰지 않는 지표를 어떻게
걷어내는지를 한 페이지에 적어 둔 글이다. 지표 이름 목록보다 **측정값의 의미를 글로 못 박는
문장**이 배울 점이라 골랐다 — 어떤 비교가 애초에 성립하지 않는지, 이름이 같은 두 숫자가 왜
어긋나는지, 한 사건을 어느 지표에 얹을지, 그리고 되살릴 가치가 없는 지표를 어떻게 접을지를
모두 본문에서 말로 정해 둔다. 대시보드 설명, SLO 문서, 장애 집계 기준, 보고서 각주를 쓸 때
그대로 틀을 가져다 쓸 수 있다.

> **원문** — vLLM 프로젝트 기여자들, *Metrics* (design 문서),
> [docs.vllm.ai](https://docs.vllm.ai/en/latest/design/metrics/) · 원본
> [vllm-project/vllm `docs/design/metrics.md`](https://github.com/vllm-project/vllm/blob/main/docs/design/metrics.md)
> (main 브랜치, 2026-10-17 확인), [Apache-2.0](https://github.com/vllm-project/vllm/blob/main/LICENSE).
>
> 영어 문장은 원문 그대로 인용했고, 한글 설명과 응용 문장은 이 노트에서 새로 쓴 것이다.

{{< sentence
  en="Every time the prefix cache is queried, we record the number of tokens queried and the number of queried tokens present in the cache (i.e. hits). However, the metric of interest is the hit rate - i.e. the number of hits per query."
  ko="프리픽스 캐시에 질의가 들어올 때마다 우리는 질의된 토큰 수와 그중 캐시에 있던 토큰 수(즉 히트)를 기록한다. 그러나 관심 있는 지표는 히트율 — 즉 질의당 히트 수 — 이다."
  source="vLLM · Prefix Cache metrics"
  sourceURL="https://docs.vllm.ai/en/latest/design/metrics/"
  note="`Every time X happens, we record A and B. However, the metric of interest is C.` — **기록하는 값**과 **보고 싶은 값**을 한 묶음으로 적고 그 둘을 가르는 문형이다. 전체를 결정하는 말은 `the metric of interest` — 우리가 보는 숫자가 아니라 **관심의 대상**이라고 적어서, 누가 열어 보든 판단 기준은 저쪽이라는 뜻이 된다. `However`는 앞 문장을 반박하지 않는다. 하는 일은 **층을 나누는 것**이다 — 앞은 원자료, 뒤는 그걸로 계산하는 지표. 이 두 줄을 먼저 적어 두면 뒤따르는 설계 결정(원자료를 카운터로 쌓고 비율 계산은 보는 쪽에 넘긴다)이 따로 설명할 것 없이 따라온다. `i.e.`로 정의를 바로 붙인 것도 장치다. 히트율 같은 말은 사람마다 분모를 다르게 잡으므로, 한 번 적어 두면 나중에 수치가 안 맞는 이유를 찾느라 시간을 쓰지 않는다. 대시보드 설명이나 SLO 문서 첫 줄, 로그에 남는 값과 보고서에 올리는 값이 다를 때 쓴다."
  app1="Every time a deploy finishes, we record the number of pods replaced and the number of them that passed the readiness probe. However, the metric of interest is the rollout success rate - i.e. the number of healthy pods per replaced pod."
  app1ko="배포가 끝날 때마다 우리는 교체된 파드 수와 그중 레디니스 프로브를 통과한 파드 수를 기록한다. 그러나 관심 있는 지표는 롤아웃 성공률 — 즉 교체된 파드당 정상 파드 수 — 이다."
  app2="Every time the scanner runs, we record the number of findings opened and the number of them closed within the SLA. However, the metric of interest is the remediation rate - i.e. the number of closures per finding."
  app2ko="스캐너가 돌 때마다 우리는 새로 열린 발견 사항 수와 그중 SLA 안에 닫힌 수를 기록한다. 그러나 관심 있는 지표는 조치율 — 즉 발견 사항당 종료 수 — 이다."
>}}

{{< sentence
  en="It's also important to note that monotonic clocks differ between processes - each process has its own reference point. So it is meaningless to compare monotonic timestamps from different processes."
  ko="또한 모노토닉 시계는 프로세스마다 다르다는 점을 짚어 둘 필요가 있다 — 프로세스마다 자기만의 기준점을 갖는다. 그래서 서로 다른 프로세스의 모노토닉 타임스탬프를 비교하는 것은 무의미하다."
  source="vLLM · Interval Calculations"
  sourceURL="https://docs.vllm.ai/en/latest/design/metrics/"
  note="`It's also important to note that X - <이유>. So it is meaningless to compare A and B.` — 잘못된 비교를 틀렸다고 하지 않고 **의미가 없다**고 적는 문형이다. 이 단어 선택이 전부다. `wrong`이라고 하면 그러면 어느 쪽이 맞느냐는 질문이 남지만, `meaningless`는 그 질문 자체를 없앤다 — 답이 틀린 게 아니라 **애초에 성립하지 않는 연산**이라는 뜻이다. 세게 들리면서도 공격이 되지 않는 이유는 대상이 사람의 판단이 아니라 **값의 성질**이기 때문이다. 순서를 바꾸면 깨진다. 대시 뒤의 `each process has its own reference point`가 먼저 와야 `meaningless`가 단정이 아니라 결론으로 읽힌다. 근거 없이 결론만 적으면 같은 말인데도 반발을 산다. `It's also important to note that`은 새 주장을 꺼내는 말이 아니라 **빠뜨리면 사고가 나는 전제**를 끼워 넣는 연결어다. 두 시스템에서 뽑은 숫자를 나란히 놓고 차이를 따지려는 사람에게, 차이를 설명하기 전에 비교를 멈추게 할 때 꺼낸다."
  app1="It's also important to note that the two services log in different time zones - each writes its own local time without an offset. So it is meaningless to compare raw timestamps from the two logs."
  app1ko="또한 두 서비스가 서로 다른 시간대로 로그를 남긴다는 점을 짚어 둘 필요가 있다 — 각자 오프셋 없이 자기 지역 시간을 적는다. 그래서 두 로그의 원본 타임스탬프를 비교하는 것은 무의미하다."
  app2="It's also important to note that the two latency reports were produced on different instance types - each run had its own hardware. So it is meaningless to compare the p99 figures across the two reports."
  app2ko="또한 두 지연 보고서가 서로 다른 인스턴스 타입에서 나왔다는 점을 짚어 둘 필요가 있다 — 각 실행이 자기 하드웨어를 썼다. 그래서 두 보고서의 p99 수치를 비교하는 것은 무의미하다."
>}}

{{< sentence
  en="Requests that generate no more than one token are recorded with a TPOT of zero, while `vllm bench serve` excludes them from its TPOT statistics. Therefore, the Prometheus histogram and benchmark TPOT statistics can differ."
  ko="토큰을 하나 이하로 생성하는 요청은 TPOT이 0으로 기록되지만, `vllm bench serve`는 그런 요청을 TPOT 통계에서 제외한다. 따라서 프로메테우스 히스토그램과 벤치마크 TPOT 통계는 다를 수 있다."
  source="vLLM · Grafana Dashboard"
  sourceURL="https://docs.vllm.ai/en/latest/design/metrics/"
  note="`A are recorded with <처리 1>, while B excludes them. Therefore, A and B can differ.` — 이름이 같은 두 숫자가 어긋날 것을 **어긋나기 전에** 적어 두는 문형이다. 칸이 둘이다. `while`로 양쪽의 처리 방식 차이를 한 줄에 붙이고, `Therefore ... can differ`로 그 차이가 수치에 드러난다고 못 박는다. 둘 다 채워야 작동한다 — 차이만 적으면 독자가 결과를 스스로 계산해야 하고, 결과만 적으면 어느 쪽이 버그냐는 티켓이 올라온다. 톤을 만드는 말은 `can differ`다. `are different`가 아니라 조동사를 쓴 덕분에, 항상 어긋난다는 뜻이 아니라 **어긋나도 정상**이라는 뜻이 된다. 오해를 막는 문장은 대개 이 한 단어에 걸려 있다. 처리 규칙을 숫자로 적어 둔 것(`a TPOT of zero`)도 계산이다 — 어긋남의 **방향과 크기**를 독자가 가늠할 수 있다. 같은 이름의 지표를 두 곳에서 내보낼 때, 주간 보고서 숫자와 대시보드 숫자가 다를 때 각주로 쓴다."
  app1="Cancelled jobs are recorded with a duration of zero, while the weekly report excludes them from its duration statistics. Therefore, the dashboard median and the report median can differ."
  app1ko="취소된 작업은 수행 시간이 0으로 기록되지만, 주간 보고서는 그런 작업을 수행 시간 통계에서 제외한다. 따라서 대시보드의 중앙값과 보고서의 중앙값은 다를 수 있다."
  app2="Findings marked as accepted risk are recorded with an age of zero, while the audit export excludes them from its age statistics. Therefore, the internal backlog age and the audited figure can differ."
  app2ko="위험 수용으로 표시된 발견 사항은 경과일이 0으로 기록되지만, 감사 산출물은 그런 항목을 경과일 통계에서 제외한다. 따라서 내부 백로그 경과일과 감사에 제출된 수치는 다를 수 있다."
>}}

{{< sentence
  en="When a preemption occurs during decode, since any already generated tokens are reused, we consider the preemption as affecting the inter-token, decode, and inference intervals."
  ko="디코드 중에 선점이 일어나면, 이미 생성된 토큰은 재사용되므로, 우리는 그 선점이 토큰 간 간격과 디코드 구간, 추론 구간에 영향을 준 것으로 본다."
  source="vLLM · Interval Calculations vs Preemptions"
  sourceURL="https://docs.vllm.ai/en/latest/design/metrics/"
  note="`When X occurs, since <이유>, we consider X as affecting A, B, and C.` — 한 사건이 **어느 지표에 얹히는지**를 미리 정해 두는 문형이다. 핵심은 `we consider ... as affecting ...`이다. 사실을 서술하는 것이 아니라 **규약을 선언**한다. 측정에는 정답이 없는 경계가 있다 — 이 지연을 누구 몫으로 셀 것인가 같은 것이다. 그 경계를 사실인 척 적어 두면 사람이 바뀔 때마다 처음부터 다시 다투게 되지만, `we consider`라고 적으면 그것이 선택이었음이 드러나고 바꿀 때도 합의로 바꿀 수 있다. `since` 절을 주절 **안쪽**에 끼워 넣은 것도 장치다. 규약과 그 근거를 한 문장에 묶어 두면 나중에 근거만 잘려 전해지지 않는다. 영향받는 지표를 셋 다 나열한 것도 계산이다 — 하나만 적으면 나머지는 영향이 없다고 읽힌다. 장애 시간을 어느 SLO에 넣을지, 재시도 지연을 누구 지표로 셀지, 리뷰 대기 시간을 리드타임에 포함할지 정할 때 쓴다."
  app1="When a rollback occurs during an incident, since the failed requests have already been counted, we consider the rollback as affecting the error budget, the availability SLO, and the time-to-recovery figure."
  app1ko="장애 중에 롤백이 일어나면, 실패한 요청은 이미 집계되어 있으므로, 우리는 그 롤백이 오류 예산과 가용성 SLO, 복구 시간 수치에 영향을 준 것으로 본다."
  app2="When a reviewer goes on leave mid-review, since the change stays open in the queue, we consider the leave as affecting the review wait time, the cycle time, and the weekly throughput."
  app2ko="리뷰 도중에 리뷰어가 휴가를 가면, 그 변경은 큐에 열린 상태로 남으므로, 우리는 그 휴가가 리뷰 대기 시간과 사이클 타임, 주간 처리량에 영향을 준 것으로 본다."
>}}

{{< sentence
  en="Therefore, these metrics are unavailable when `--api-server-count > 1`. It's questionable how relevant these are since they do not aggregate these stats for all processes that make up a vLLM instance."
  ko="따라서 `--api-server-count > 1`일 때 이 지표들은 제공되지 않는다. 이 지표들이 얼마나 유의미한지는 의문인데, vLLM 인스턴스를 구성하는 모든 프로세스에 대해 이 통계를 합산해 주지는 않기 때문이다."
  source="vLLM · Built in Python/Process Metrics"
  sourceURL="https://docs.vllm.ai/en/latest/design/metrics/"
  note="`<사라진 것>. It's questionable how relevant these are since they do not <결정적 결함>.` — 없어진 기능을 **아쉬워하지 않기로 결정하는** 문장이다. 보통 이 자리에는 알려진 한계라거나 추후 개선이라고 적는데, 그렇게 적으면 영원히 할 일 목록에 남는다. 대신 `It's questionable how relevant these are`는 **되살릴 가치가 있는지**를 묻는 쪽으로 질문을 옮긴다. 어조를 만드는 말은 `questionable` — 쓸모없다고 단정하지 않고 의심만 올려 두므로, 반대하는 사람이 근거를 들고 올 여지가 남는다. `how relevant`라는 정도 표현도 같은 역할이다. 있다/없다가 아니라 정도를 묻기 때문에 문이 닫히지 않는다. 그러면서 뒤의 `since they do not ...`가 의심의 **근거를 하나로 특정**한다. 그래서 논의가 다시 열리는 조건이 분명해진다 — 그 근거가 깨질 때만이다. 복구하지 않기로 한 알림, 아무도 안 보는 리포트, 지우려는 대시보드 패널의 사유를 한 줄로 남길 때 쓴다."
  app1="The host-level panels have been empty since the agent moved into a sidecar. It's questionable how relevant these are since they do not roll the numbers up to the service that owns the host."
  app1ko="에이전트가 사이드카로 옮겨 간 뒤로 호스트 단위 패널은 비어 있다. 이 패널들이 얼마나 유의미한지는 의문인데, 그 호스트를 소유한 서비스 단위로 숫자를 합산해 주지는 않기 때문이다."
  app2="The nightly permission diff has not run since the account was split in two. It's questionable how relevant it is since it does not cover the roles that were moved to the new account."
  app2ko="계정이 둘로 갈린 뒤로 야간 권한 비교 작업은 돌지 않았다. 이 작업이 얼마나 유의미한지는 의문인데, 새 계정으로 옮겨 간 역할들은 다루지 않기 때문이다."
>}}
