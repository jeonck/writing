---
title: 실패를 분류하고 재발 가능성만 적는 표현
description: 대응을 정답 하나가 아니라 분류의 문제로 넘기고, 우연히 겹친 사고의 재발 가능성만 낮게 적고, 손쉬운 수단을 닫은 뒤 필요한 것을 열거하고, 완료와 기록이 어긋나는 이유를 관측 범위로 돌리고, 하나의 값에 두 축의 요구를 동시에 거는 문장 5개.
weight: -58
date: 2026-10-18
source: "Temporal · Error handling"
sourceURL: https://docs.temporal.io/best-practices/error-handling
---

# 실패를 분류하고 재발 가능성만 적는 표현

내구성 있는 워크플로 실행 엔진 Temporal의 문서 중 **에러 처리 베스트 프랙티스** 페이지다. 실패를
일시적·간헐적·영구적 셋으로 가르고, 재시도로 해결되지 않는 실패를 어떻게 표시하고, 완료된 작업이
왜 다시 실행될 수 있는지를 한 페이지에 적어 둔 글이다. 재시도 설정 지식보다 **아직 원인을 모르는
단계에서 쓰는 문장**이 배울 점이라 골랐다 — 대응을 하나로 못 정할 때 분류로 넘겨야 하고, 재발하지
않는다고 보증할 수 없는데도 추가 조치가 필요 없다고 적어야 하고, 시스템이 뻔히 틀린 동작을 하는
이유를 설계 잘못이 아니라 기록의 공백으로 설명해야 하는 글이다. 장애 보고서를 쓸 때, 지적 사항에
무엇이 필요한지 적을 때, 식별자 규칙을 정할 때 그대로 틀을 가져다 쓸 수 있다.

> **원문** — Temporal Technologies, *Error handling*,
> [Temporal Documentation](https://docs.temporal.io/best-practices/error-handling),
> [MIT License](https://github.com/temporalio/documentation/blob/main/LICENSE.md)
> (문서 파일까지 복제·배포를 명시적으로 허용).
> 원문 마크다운은 [`temporalio/documentation`](https://github.com/temporalio/documentation/blob/main/docs/best-practices/error-handling.mdx)에 있다.
>
> 영어 문장은 원문 그대로 인용했고, 한글 설명과 응용 문장은 이 노트에서 새로 쓴 것이다.

{{< sentence
  en="When an operation fails, the appropriate response depends on the nature of the failure."
  ko="어떤 동작이 실패했을 때 적절한 대응은 그 실패의 성질에 따라 달라진다."
  source="Temporal · Error handling → Categorize failures"
  sourceURL="https://docs.temporal.io/best-practices/error-handling"
  note="`the appropriate X depends on the nature of Y` — **정답 하나를 요구하는 질문을 분류의 문제로 넘기는** 구문이다. `the appropriate response`는 '옳은 대응'이 아니라 '그 상황에 맞는 대응'이라서, 보편적인 정답이 있다는 전제를 문장에서 빼 버린다. `the nature of`는 원인이 아니라 성질을 가리키므로 **원인을 아직 모르는 단계에서도 쓸 수 있다**. 이 문형의 용도는 뒤에 분류 기준을 꺼내는 것이다 — 원문도 이 문장 바로 뒤에 실패 유형 셋을 세운다. 반대로 분류를 이어서 제시할 생각이 없다면 이 문장은 책임 회피로 읽힌다."
  app1="When an alert fires at night, the appropriate response depends on the nature of the degradation, not on who is on call."
  app1ko="밤에 알림이 울렸을 때 적절한 대응은 누가 당직이냐가 아니라 성능 저하의 성질에 따라 달라진다."
  app2="When a review finds a defect, the appropriate response depends on the nature of the defect. A typo and a race condition do not belong in the same queue."
  app2ko="리뷰에서 결함이 나왔을 때 적절한 대응은 그 결함의 성질에 따라 달라진다. 오타와 경쟁 상태를 같은 대기열에 넣을 수는 없다."
>}}

{{< sentence
  en="For example, a Worker happens to make a network request at the exact moment an administrator replaces a network cable. The cause is unlikely to affect future requests."
  ko="예를 들어 워커가 하필 관리자가 네트워크 케이블을 교체하는 바로 그 순간에 네트워크 요청을 보내는 경우다. 그 원인이 이후 요청에 영향을 줄 가능성은 낮다."
  source="Temporal · Error handling → Transient failures"
  sourceURL="https://docs.temporal.io/best-practices/error-handling"
  note="일회성 장애를 적는 두 단계다. 먼저 `happens to V at the exact moment ~`로 우연을 그린다 — `happens to`가 '하필', `at the exact moment`가 '바로 그 순간'을 맡아, 둘이 합쳐 **겹칠 이유가 없는 두 사건이 겹쳤다**는 뜻이 된다. 그다음 `The cause is unlikely to affect future requests.`로 **재발 가능성만** 낮게 적는다. `will not affect`가 아니라 `is unlikely to affect`인 것이 핵심이다 — 재발하지 않는다고 보증하지 않으면서 추가 조치가 필요 없다는 판단은 전달한다. 장애 보고서에서 '일시적 현상으로 보인다'를 쓸 자리이고, 보증할 수 없는 것을 보증하지 않고 넘어가는 방법이다."
  app1="The job happened to write its checkpoint at the exact moment the volume was being resized. The cause is unlikely to affect future runs."
  app1ko="그 작업은 하필 볼륨 크기가 조정되는 바로 그 순간에 체크포인트를 기록했다. 그 원인이 이후 실행에 영향을 줄 가능성은 낮다."
  app2="The access check failed because the service happened to refresh its token at the exact moment the policy was being reloaded. The cause is unlikely to affect future audits."
  app2ko="그 접근 검사가 실패한 것은 서비스가 하필 정책이 다시 로드되는 바로 그 순간에 토큰을 갱신했기 때문이다. 그 원인이 이후 감사에 영향을 줄 가능성은 낮다."
>}}

{{< sentence
  en="Permanent failures cannot be resolved through retries. They require different input data, a code fix, or some external intervention."
  ko="영구적 실패는 재시도로 해결되지 않는다. 다른 입력 데이터, 코드 수정, 또는 외부의 어떤 개입이 필요하다."
  source="Temporal · Error handling → Permanent failures"
  sourceURL="https://docs.temporal.io/best-practices/error-handling"
  note="`X cannot be resolved through Y. They require A, B, or C.` — 손쉬운 수단을 먼저 못으로 박아 닫고, 그다음 실제로 필요한 것을 열거하는 두 문장 구조다. `cannot be resolved through`는 **안 되는 이유를 수단에 한정**하므로 누가 잘못했다는 말이 섞이지 않는다. 열거를 `or some external intervention`처럼 **범위가 가장 넓은 항목으로 닫는 것**도 그대로 훔칠 만하다 — 구체적인 항목 둘을 앞에 세워 두되 마지막 자리를 열어 놓아, 빠진 경우가 있어도 문장이 틀리지 않는다. 재시도·재배포·재시작으로 덮고 넘어가려는 자리에서 꺼낸다."
  app1="This alert cannot be resolved through a restart. It requires a schema migration, a client upgrade, or some change on the provider side."
  app1ko="이 알림은 재시작으로 해결되지 않는다. 스키마 마이그레이션, 클라이언트 업그레이드, 또는 제공자 측의 어떤 변경이 필요하다."
  app2="The finding cannot be resolved through configuration. It requires a credential rotation, a code change in the handler, or some exception approved by the security owner."
  app2ko="그 지적은 설정 변경으로 해결되지 않는다. 자격 증명 교체, 핸들러 코드 수정, 또는 보안 담당자가 승인한 어떤 예외가 필요하다."
>}}

{{< sentence
  en="A Worker can execute an Activity, complete it, and then crash before reporting the result to the Temporal Service. The Activity is retried even though it completed, because the Service has no record of the completion."
  ko="워커가 액티비티를 실행해 완료한 다음, 그 결과를 Temporal 서비스에 보고하기 전에 죽을 수 있다. 액티비티는 완료되었는데도 재시도된다. 서비스에 완료 기록이 없기 때문이다."
  source="Temporal · Error handling → Design Activities for idempotence"
  sourceURL="https://docs.temporal.io/best-practices/error-handling"
  note="`X is V-ed even though Y, because Z.` — 사실과 어긋나 보이는 동작을 변호하지 않고 **관측 범위의 문제로** 설명하는 구문이다. `even though it completed`가 모순을 먼저 인정해 버리고, `because ~ has no record of ~`가 그 모순을 **시스템이 아는 것과 실제로 일어난 것의 차이**로 돌린다. 앞 문장의 `can V, V, and then V before -ing`는 사고가 끼어드는 지점을 시간 순서로 늘어놓는 틀이다 — 세 동작을 나열한 뒤 `before -ing`로 **빠진 마지막 단계**를 지목한다. 동작이 틀린 게 아니라 기록이 없었던 것이라고 쓸 때 그대로 쓴다."
  app1="The deploy is marked failed even though it succeeded, because the health probe timed out before the first response arrived."
  app1ko="그 배포는 성공했는데도 실패로 기록된다. 첫 응답이 도착하기 전에 헬스 프로브가 타임아웃됐기 때문이다."
  app2="The change is listed as unreviewed even though two engineers read it, because the approval was given in the incident channel and never recorded on the pull request."
  app2ko="그 변경은 두 사람이 읽었는데도 미리뷰 상태로 남아 있다. 승인이 장애 대응 채널에서 이뤄져 PR에는 전혀 기록되지 않았기 때문이다."
>}}

{{< sentence
  en="Combine the Workflow Run ID and Activity ID for a value that is consistent across retries but unique across Workflow Executions."
  ko="워크플로 실행 ID와 액티비티 ID를 합쳐, 재시도 사이에서는 같고 워크플로 실행 사이에서는 유일한 값을 만든다."
  source="Temporal · Error handling → Design Activities for idempotence"
  sourceURL="https://docs.temporal.io/best-practices/error-handling"
  note="`a value that is consistent across A but unique across B` — 하나의 값에 **두 축의 요구를 동시에** 거는 구문이다. `consistent across`와 `unique across`가 같은 전치사로 대칭을 이루고, `but`이 두 요구가 서로 당긴다는 걸 표시한다. 같은 내용을 '재시도해도 같아야 한다'와 '실행마다 달라야 한다' 두 문장으로 쪼개 쓰면 각 조건을 따로 만족시키는 답이 나오는데, 한 문장에 묶으면 **둘 다 동시에 만족하는 값**이라는 조건이 된다. `Combine A and B for ~`는 요구를 먼저 말하지 않고 **만드는 방법부터** 주는 형태라 규칙 문서에 어울린다. 식별자·중복 제거 키·라벨 규칙을 정할 때 꺼낸다."
  app1="Combine the alert name and the instance label for a key that is consistent across repeated firings but unique across hosts."
  app1ko="알림 이름과 인스턴스 라벨을 합쳐, 반복 발생 사이에서는 같고 호스트 사이에서는 유일한 키를 만든다."
  app2="Combine the release tag and the file path for an audit reference that is consistent across re-runs of the scan but unique across findings."
  app2ko="릴리스 태그와 파일 경로를 합쳐, 스캔을 다시 돌려도 같고 지적 사항 사이에서는 유일한 감사 참조값을 만든다."
>}}
