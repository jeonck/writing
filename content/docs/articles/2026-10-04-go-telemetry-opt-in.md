---
title: 반발이 예상되는 제안을 글로 적는 표현
description: 거부감을 먼저 인정하고 필요성으로 돌아서는 양보, 담지 않는 것까지 못 박는 범위 한정, 평가어를 검증 가능한 조건으로 바꾸는 정의 — 반대가 예상되는 변경을 설명하는 문장 5개.
weight: -44
date: 2026-10-04
source: "Go Documentation · Go Telemetry"
sourceURL: https://go.dev/doc/telemetry
---

# 반발이 예상되는 제안을 글로 적는 표현

Go 툴체인이 수집하는 텔레메트리의 설계 문서. 오픈소스에서 가장 환영받지 못하는 기능을
설명해야 하는 글이라, 거부감을 먼저 인정하고 수집 범위를 좁히고 승인 조건을 정의로
못 박는 문장이 빽빽하다. 반대가 예상되는 변경을 설명해야 하는 사람에게 그대로 쓸
문형이 많아 발췌했다.

> **원문** — The Go Authors, *Go Telemetry*,
> [Go Documentation](https://go.dev/doc/telemetry)
> ([원본 리포지터리](https://github.com/golang/website/blob/master/_content/doc/telemetry.md)),
> [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) 라이선스
> ([go.dev Copyright](https://go.dev/copyright)에서 선언).
>
> 영어 문장은 원문 그대로 인용했고, 한글 설명과 응용 문장은 이 노트에서 새로 쓴 것이다.

{{< sentence
  en="The word &quot;telemetry&quot; has acquired negative connotations in the world of open source software, in many cases deservedly so. Yet measuring the user experience is an important element of modern software engineering, and data sources such as GitHub issues or annual surveys are coarse and lagging indicators, insufficient for the types of questions the Go team needs to be able to answer."
  ko="telemetry라는 단어는 오픈소스 소프트웨어 세계에서 부정적인 함의를 얻었고, 많은 경우 그럴 만했다. 그러나 사용자 경험을 측정하는 일은 현대 소프트웨어 엔지니어링의 중요한 요소이며, GitHub 이슈나 연간 설문 같은 데이터 출처는 거칠고 뒤늦은 지표여서 Go 팀이 답할 수 있어야 하는 종류의 질문에는 충분하지 않다."
  source="Go Telemetry · Background"
  sourceURL="https://go.dev/doc/telemetry#background"
  note="`X has acquired negative connotations, in many cases deservedly so. Yet Y ...` — 반발이 예상되는 제안을 꺼낼 때, 반발의 **정당성까지** 먼저 인정하고 들어가는 문형이다. 핵심은 `in many cases deservedly so`. '그건 오해다'가 아니라 '많은 경우 그럴 만했다'라고 말하므로 방어적으로 읽히지 않고, 읽는 사람이 경계를 풀 자리가 생긴다. 그다음 `Yet`으로 돌아서면서도 반대 근거를 공격하지 않고 **기존 수단의 한계**를 `coarse and lagging indicators`로 규정한다 — 틀렸다가 아니라 거칠고 뒤늦다는 것이다. 마지막 `insufficient for the types of questions ~ needs to be able to answer`는 '부족하다'의 기준을 내가 답해야 하는 질문에 걸어 둬서, 판단이 취향으로 보이지 않게 한다."
  app1="Adding request tracing has acquired negative connotations on this team, in many cases deservedly so. Yet we still cannot explain last week's latency spike from dashboards alone, and incident timelines reconstructed from chat are coarse and lagging indicators."
  app1ko="요청 트레이싱을 붙이는 일은 우리 팀에서 부정적인 함의를 얻었고, 많은 경우 그럴 만했다. 그러나 우리는 여전히 지난주 지연 급증을 대시보드만으로는 설명하지 못하고, 채팅 기록으로 재구성한 장애 타임라인은 거칠고 뒤늦은 지표다."
  app2="Mandatory review checklists have acquired negative connotations here, in many cases deservedly so. Yet post-release bug reports are coarse and lagging indicators, insufficient for the types of questions a release review needs to be able to answer."
  app2ko="필수 리뷰 체크리스트는 여기서 부정적인 함의를 얻었고, 많은 경우 그럴 만했다. 그러나 릴리스 후 버그 리포트는 거칠고 뒤늦은 지표여서, 릴리스 리뷰가 답할 수 있어야 하는 종류의 질문에는 충분하지 않다."
>}}

{{< sentence
  en="Stack counters include only the names and line numbers of functions within Go toolchain programs. They don't include any information about user inputs, such as the names or contents of a user's source code."
  ko="스택 카운터는 Go 툴체인 프로그램 안에 있는 함수의 이름과 줄 번호만 담는다. 사용자 입력에 대한 정보, 예컨대 사용자 소스 코드의 이름이나 내용은 전혀 담지 않는다."
  source="Go Telemetry · Stack counters"
  sourceURL="https://go.dev/doc/telemetry#stack-counters"
  note="`X include only A. They don't include any information about B, such as b1 or b2.` — 수집 범위를 **담는 것 한 문장, 담지 않는 것 한 문장**으로 끊어 적는 2단 구성. `only`만으로 끝내면 읽는 사람은 '그럼 혹시 ~도 들어가나'를 계속 떠올리므로, 두 번째 문장에서 `don't include any information about`으로 가장 걱정되는 항목에 **이름을 붙여** 차단한다. 요령은 `such as` 뒤에 구체적인 예를 두 개 드는 것이다 — 추상적인 '개인정보'보다 '파일명이나 그 내용'이 훨씬 안심된다. 로그 설계, 수집 고지, 보안 감사 답변에 그대로 쓰는 틀."
  app1="The audit log includes only the actor, the resource ID, and the timestamp. It doesn't include any information about the request body, such as customer names or payment details."
  app1ko="감사 로그는 행위자, 리소스 ID, 타임스탬프만 담는다. 요청 본문에 대한 정보, 예컨대 고객 이름이나 결제 정보는 전혀 담지 않는다."
  app2="Crash reports include only the stack frames of our own packages. They don't include any information about the host environment, such as hostnames or environment variables."
  app2ko="크래시 리포트는 우리 패키지의 스택 프레임만 담는다. 호스트 환경에 대한 정보, 예컨대 호스트명이나 환경 변수는 전혀 담지 않는다."
>}}

{{< sentence
  en="In order to be useful, charts must serve a specific purpose, with actionable outcomes."
  ko="유용하려면, 차트는 구체적인 목적에 쓰여야 하고 실행으로 이어지는 결과를 내야 한다."
  source="Go Telemetry · The telemetry proposal process"
  sourceURL="https://go.dev/doc/telemetry#proposals"
  note="`In order to be <평가어>, X must Y.` — '유용한', '충분한', '안전한'처럼 **사람마다 다르게 읽히는 형용사를 검증 가능한 조건으로 바꿔 적는** 문형. 앞에 `In order to be useful`을 세우면 뒤에 오는 조건이 담당자 취향이 아니라 **그 단어의 정의**로 읽혀서, 반대하려면 조건이 아니라 정의를 반박해야 한다. `serve a specific purpose`와 `with actionable outcomes`처럼 조건을 둘로 끊어 두면 심사할 때 그대로 체크리스트가 된다. 알림 추가, 대시보드 승인, 지표 제안처럼 기준을 글로 남겨야 할 때의 기본형이다."
  app1="In order to be actionable, an alert must name the user-visible symptom, with a documented first response."
  app1ko="실행으로 이어지려면, 알림은 사용자에게 보이는 증상을 가리켜야 하고 문서화된 첫 대응이 있어야 한다."
  app2="In order to be reviewable, a pull request must describe the failure it fixes, with a test that fails without the change."
  app2ko="리뷰할 수 있으려면, PR은 자기가 고치는 실패가 무엇인지 설명해야 하고 변경 없이는 실패하는 테스트가 있어야 한다."
>}}

{{< sentence
  en="Once enough users opt in to uploading telemetry data, the upload process will randomly skip uploading for a fraction of reports, to reduce collection amounts and increase privacy while maintaining statistical significance."
  ko="충분한 수의 사용자가 텔레메트리 데이터 업로드에 동의하면, 업로드 과정은 보고서 일부에 대해 업로드를 무작위로 건너뛰어, 통계적 유의성은 유지하면서 수집량을 줄이고 프라이버시를 높인다."
  source="Go Telemetry · Uploading"
  sourceURL="https://go.dev/doc/telemetry#uploads"
  note="`Once X, Y will Z, to A and B while maintaining C.` — 조건, 동작, 목적, 그리고 **포기하지 않는 것**을 한 문장에 차례로 넣은 구조. 목적까지만 쓰면 읽는 사람 머리에 '그래서 뭘 잃는데?'가 남는데, `while maintaining C`가 그 자리를 미리 막는다. `Once`는 `If`와 달리 그 조건이 언젠가 충족된다는 전제를 깔고 있어서, 아직 오지 않은 상황을 가정이 아니라 **예정된 단계**로 말하게 해 준다. 샘플링을 넣거나 보존 기간·수집량을 줄이는 변경을 설명할 때 쓴다."
  app1="Once the backlog clears, the collector will drop a random share of debug spans, to cut storage cost and shorten queries while maintaining per-endpoint error rates."
  app1ko="백로그가 해소되면, 수집기는 디버그 스팬 일부를 무작위로 버려, 엔드포인트별 오류율은 유지하면서 저장 비용을 줄이고 쿼리 시간을 단축한다."
  app2="Once the rollout reaches every region, the job will sample one request in ten, to reduce log volume and limit exposure of personal data while maintaining enough coverage to catch regressions."
  app2ko="롤아웃이 전 리전에 닿으면, 그 작업은 요청 열 건 중 한 건만 표본으로 남겨, 회귀를 잡을 만큼의 커버리지는 유지하면서 로그 양을 줄이고 개인정보 노출을 제한한다."
>}}

{{< sentence
  en="The use of a memory-mapped file means that even if the program immediately crashes, or several copies of instrumented tools are running simultaneously, the counters are recorded safely."
  ko="메모리 맵 파일을 쓴다는 것은, 프로그램이 즉시 죽거나 계측된 도구가 여러 개 동시에 돌고 있어도 카운터가 안전하게 기록된다는 뜻이다."
  source="Go Telemetry · Counter files"
  sourceURL="https://go.dev/doc/telemetry#counter-files"
  note="`The use of X means that even if A, or B, C.` — 설계 선택을 주어 자리에 올리고, 그것이 **어떤 악조건에서도** 지켜 주는 결과를 `even if` 두 개로 열거하는 문형. `C is safe because we use X`처럼 쓰면 결론이 앞에 와서 근거가 덧붙임처럼 들리지만, 이쪽은 수단 → 견뎌내는 상황 → 결과 순서라 '어디까지 버티는가'가 또렷해진다. 핵심은 `even if A, or B`로 **리뷰어가 떠올릴 반례를 문장 안에 미리 적어 두는** 것이다. 설계 문서나 장애 복기에서 '왜 이렇게 만들었나'를 한 문장으로 답할 때 쓴다."
  app1="The use of an append-only ledger means that even if the worker dies mid-batch, or two schedulers fire the same job, the transfers are recorded exactly once."
  app1ko="추가 전용 원장을 쓴다는 것은, 워커가 배치 중간에 죽거나 스케줄러 두 개가 같은 작업을 띄워도 이체가 정확히 한 번만 기록된다는 뜻이다."
  app2="The use of a separate audit stream means that even if the service is rolled back, or the primary database is restored from a snapshot, the access records survive."
  app2ko="감사 스트림을 따로 둔다는 것은, 서비스가 롤백되거나 주 데이터베이스를 스냅샷에서 복원해도 접근 기록이 남는다는 뜻이다."
>}}
