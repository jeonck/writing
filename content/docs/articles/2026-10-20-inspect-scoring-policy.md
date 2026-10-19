---
title: 측정 도구의 실패와 대상의 실패를 가르는 표현
description: 부품의 할 일을 변환 사슬로 정의하고, 채점 모델을 측정 장비 쪽으로 귀속시키고, 완료와 오류 사이에 빈칸을 하나 만들고, 경계를 넘은 예외의 이름을 바꾸고, 정상 종료가 자동 처리를 부르지 않는다고 못 박는 문장 5개.
weight: -60
date: 2026-10-20
source: "Inspect · Scoring Policy"
sourceURL: https://inspect.aisi.org.uk/scoring-policy.html
---

# 측정 도구의 실패와 대상의 실패를 가르는 표현

영국 AI 보안연구소(UK AISI)가 만든 LLM 평가 프레임워크 Inspect의 **채점 정책** 페이지다. 한 샘플에서
무슨 일이 벌어질 수 있는지를 셋으로 가른다 — 모델이 틀렸다, 실행 기계가 깨졌다, 그리고 **측정 장치가
판정을 못 냈다**. 이 셋을 지표의 분모에 어떻게 반영하는지가 문서 전체의 주제다. 평가 설정 지식보다
**실패를 누구 몫으로 돌릴지 적는 문장**이 배울 점이라 골랐다 — 채점하는 모델도 모델인데 그것을 평가
대상이 아니라 계측 장비 쪽으로 밀어 넣어야 하고, 오류도 결과도 아닌 상태에 이름을 붙여야 하고, 같은
예외가 어느 층에서 멈췄는지에 따라 다르게 세야 한다. 장애를 분류할 때, 감사 커버리지를 적을 때,
자동 호출 규칙을 정할 때 그대로 틀을 가져다 쓸 수 있다.

> **원문** — UK AI Security Institute, *Scoring Policy*,
> [Inspect Documentation](https://inspect.aisi.org.uk/scoring-policy.html),
> [MIT License](https://github.com/UKGovernmentBEIS/inspect_ai/blob/main/LICENSE)
> (소프트웨어와 그에 딸린 문서 파일의 복제·배포를 명시적으로 허용).
> 원문 마크다운은 [`UKGovernmentBEIS/inspect_ai`](https://github.com/UKGovernmentBEIS/inspect_ai/blob/main/docs/scoring-policy.qmd)에 있다.
>
> 영어 문장은 원문 그대로 인용했고, 한글 설명과 응용 문장은 이 노트에서 새로 쓴 것이다.

{{< sentence
  en="A scorer's job is to turn what a model did on a sample into a verdict about the model's capability on the task, which Inspect then aggregates into the metrics that summarise the evaluation."
  ko="채점기가 할 일은 모델이 한 샘플에서 한 행동을 그 과제에 대한 모델 능력의 판정으로 바꾸는 것이고, Inspect는 그 판정을 모아 평가를 요약하는 지표로 집계한다."
  source="Inspect · Scoring Policy · Overview"
  sourceURL="https://inspect.aisi.org.uk/scoring-policy.html"
  note="`X's job is to turn A into B, which C then aggregates into D` — 부품 하나의 **책임을 변환으로 정의하는** 문형이다. `job is to`는 '이런 기능이 있다'가 아니라 '이 일을 맡았다'는 말이라, 그 일이 안 됐을 때 누구를 봐야 하는지까지 같이 정해 준다. 뒤에 붙은 `which ... then aggregates into`가 **그 산출물이 어디로 흘러가는지**를 같은 문장에 매달아, 부품 하나를 정의하면서 파이프라인 전체를 보여 준다. 역할·모듈·직무를 규정하는 글의 첫 문장으로 그대로 쓴다."
  app1="An on-call engineer's job is to turn a page into a decision about user impact, which the incident review then aggregates into the reliability report."
  app1ko="온콜 엔지니어가 할 일은 호출 하나를 사용자 영향에 대한 판단으로 바꾸는 것이고, 장애 리뷰는 그 판단을 모아 신뢰성 보고서로 집계한다."
  app2="A reviewer's job is to turn a diff into a judgement about whether it is safe to ship, which the release checklist then aggregates into a go or no-go."
  app2ko="리뷰어가 할 일은 디프를 배포해도 되는지에 대한 판단으로 바꾸는 것이고, 릴리스 체크리스트는 그 판단을 모아 배포 여부로 집계한다."
>}}

{{< sentence
  en="A grader model is part of the measurement instrument; its output determines whether the evaluated response receives a verdict."
  ko="채점 모델은 측정 장치의 일부다. 그 출력이 평가 대상 응답에 판정이 내려지는지를 결정한다."
  source="Inspect · Scoring Policy · Overview"
  sourceURL="https://inspect.aisi.org.uk/scoring-policy.html"
  note="`A is part of B; its output determines whether C` — 어떤 구성 요소를 **어느 쪽으로 귀속시킬지 선언하는** 문형이다. 힘은 `is part of`에 있다. 채점 모델도 모델이지만 평가 **대상**이 아니라 **계측 장비** 쪽이라고 못 박아, 그쪽이 삐끗한 것을 대상의 실패로 세지 못하게 만든다. 세미콜론 뒤의 `its output determines whether ~`는 그 귀속이 왜 중요한지를 근거로 붙인다 — 이 부품이 멈추면 판정 자체가 나오지 않는다. 측정·감사·심사에서 '이건 평가 대상이 아니라 우리 쪽 장비다'를 가를 때 쓴다."
  app1="The log pipeline is part of the monitoring instrument; its gaps determine whether an incident gets a timeline at all."
  app1ko="로그 파이프라인은 모니터링 장치의 일부다. 그 공백이 장애에 타임라인이 남는지 자체를 결정한다."
  app2="The scanner is part of the audit instrument; its coverage determines whether a repository can be called reviewed."
  app2ko="스캐너는 감사 장치의 일부다. 그 커버리지가 어떤 리포지터리를 검토 완료라고 부를 수 있는지를 결정한다."
>}}

{{< sentence
  en="A scorer can complete without obtaining a verdict. For example, a grader model may return output from which the scorer cannot extract a grade."
  ko="채점기는 판정을 얻지 못한 채로 완료될 수 있다. 예를 들어 채점 모델이, 채점기가 등급을 뽑아낼 수 없는 출력을 돌려줄 수 있다."
  source="Inspect · Scoring Policy · Unscoreable samples"
  sourceURL="https://inspect.aisi.org.uk/scoring-policy.html"
  note="`X can complete without -ing. For example, ...` — 성공/실패 이분법에 **세 번째 칸을 내는** 문형이다. `complete`와 `without obtaining`을 한 문장에 넣어 '오류도 아니고 결과도 아닌' 상태를 만들어 낸다. `can`은 가능성만 열어 두고, 뒤의 `For example`이 그 가능성이 실제로 어떻게 생기는지 **경로 하나만** 보여 준다 — 전부 열거하지 않는 것이 요령이다. 상태를 정의하거나 집계 규칙을 세울 때, 정상과 오류 사이의 빈칸을 명시할 때 쓴다."
  app1="A health check can pass without proving the dependency is reachable. For example, the probe may hit a cached response that outlives the database connection."
  app1ko="헬스 체크는 의존성에 닿는다는 것을 입증하지 않고도 통과할 수 있다. 예를 들어 프로브가 데이터베이스 연결보다 오래 남은 캐시 응답을 맞출 수 있다."
  app2="A migration can finish without leaving the data in the shape we expected. For example, a row may be dropped by a filter that nobody re-read after the schema changed."
  app2ko="마이그레이션은 데이터를 우리가 기대한 모양으로 남기지 않고도 끝날 수 있다. 예를 들어 스키마가 바뀐 뒤 아무도 다시 읽지 않은 필터 때문에 어떤 행이 버려질 수 있다."
>}}

{{< sentence
  en="Grader API requests follow the model's retry policy. An API exception that propagates to the scorer becomes a scoring error."
  ko="채점 모델의 API 요청은 그 모델의 재시도 정책을 따른다. 채점기까지 올라온 API 예외는 채점 오류가 된다."
  source="Inspect · Scoring Policy · Model-graded scorers"
  sourceURL="https://inspect.aisi.org.uk/scoring-policy.html"
  note="`An X that propagates to Y becomes a Z` — **경계를 넘는 순간 이름이 바뀐다**고 적는 문형이다. 앞 문장이 먼저 재시도 계층을 세워 두고, 뒷 문장이 그 계층을 **빠져나온 것만** 집어 새 분류를 붙인다. `propagates to`는 '발생했다'가 아니라 '어디까지 올라왔다'를 말하므로, 같은 예외라도 어느 층에서 멈췄는지에 따라 다르게 집계된다는 뜻이 된다. 장애 분류 기준이나 에러 예산 규칙을 적을 때, 재시도로 흡수된 실패와 사용자까지 간 실패를 가르는 문장으로 쓴다."
  app1="Transient writes are retried inside the client. A timeout that propagates to the request handler becomes a user-visible failure."
  app1ko="일시적인 쓰기 실패는 클라이언트 안에서 재시도된다. 요청 핸들러까지 올라온 타임아웃은 사용자에게 보이는 실패가 된다."
  app2="Lint findings are fixed in the pre-commit hook. A violation that propagates to CI becomes a blocked merge."
  app2ko="린트 지적은 프리커밋 훅에서 고쳐진다. CI까지 올라온 위반은 머지 차단이 된다."
>}}

{{< sentence
  en="An unscored result completes scoring normally and does not trigger a sample retry."
  ko="판정 없는 결과는 채점을 정상적으로 완료하며, 샘플 재시도를 유발하지 않는다."
  source="Inspect · Scoring Policy · Model-graded scorers"
  sourceURL="https://inspect.aisi.org.uk/scoring-policy.html"
  note="`X completes A normally and does not trigger B` — 어떤 상태를 **정상 경로에 두면서 후속 동작만 떼어 내는** 문형이다. `and`로 묶인 두 절이 각각 다른 일을 한다. 앞 절은 그 상태가 오류가 아니라고 승인하고, 뒷 절은 그래서 오류에 딸린 자동 처리가 돌지 않는다고 못 박는다. `does not trigger`가 핵심인데, 단순한 부정이 아니라 **방아쇠가 당겨지지 않는다**는 말이라 자동화의 작동 조건을 설명하는 데 맞는다. 운영 규칙에서 '이건 사고가 아니니 호출하지 않는다'를 적을 때 쓴다."
  app1="A planned failover completes the drill normally and does not trigger an incident review."
  app1ko="계획된 페일오버는 훈련을 정상적으로 완료하며, 장애 리뷰를 유발하지 않는다."
  app2="A deprecation warning completes the build normally and does not trigger a release block."
  app2ko="지원 중단 경고는 빌드를 정상적으로 완료하며, 릴리스 차단을 유발하지 않는다."
>}}
