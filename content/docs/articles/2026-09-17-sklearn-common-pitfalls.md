---
title: 그 숫자를 믿어도 되는지 묻는 표현
description: 잘못을 사람이 아니라 정보의 시점으로 정의하고, 빠져나갈 구멍을 먼저 막고, 분리가 무너진 자리를 짚고, 뻔한 지적을 잔소리가 아니게 만들고, 좋아 보이는 결과를 반박 없이 무력화하는 문장 5개.
weight: -28
date: 2026-09-17
source: "scikit-learn — Common pitfalls and recommended practices"
sourceURL: https://scikit-learn.org/stable/common_pitfalls.html
---

# 그 숫자를 믿어도 되는지 묻는 표현

scikit-learn 공식 문서의 *Common pitfalls and recommended practices* 장은 전처리 불일치,
데이터 누수, 난수 제어를 차례로 다루면서 매번 **틀린 예와 맞는 예를 나란히** 놓는다. 눈에
띄는 것은 실수를 다루는 방식이다. 누가 무엇을 잘못했다고 하지 않고, **왜 그 숫자가 그렇게
나왔는지**를 설명한 다음 규칙을 꺼낸다. 그래서 이 문서에는 좋아 보이는 결과를 깎아내리지
않으면서 못 믿겠다고 말하는 문형, 당연한 이야기를 다시 하면서 상대를 가르치지 않는 문형이
모여 있다. 장애 회고, 벤치마크 반박, 감사 회신, 코드 리뷰에 그대로 옮겨 쓸 다섯 문장을 골랐다.

> **원문** — The scikit-learn developers, *Common pitfalls and recommended practices*,
> [scikit-learn documentation](https://scikit-learn.org/stable/common_pitfalls.html)
> (원본: [`scikit-learn/scikit-learn` · `doc/common_pitfalls.rst`](https://github.com/scikit-learn/scikit-learn/blob/main/doc/common_pitfalls.rst)),
> [BSD 3-Clause](https://github.com/scikit-learn/scikit-learn/blob/main/COPYING).
> Copyright (c) 2007-2026 The scikit-learn developers. All rights reserved.
>
> 영어 문장은 원문 그대로 인용했고, 한글 설명과 응용 문장은 이 노트에서 새로 쓴 것이다.

{{< sentence
  en="Data leakage occurs when information that would not be available at prediction time is used when building the model."
  ko="데이터 누수는 예측 시점에는 확보할 수 없는 정보가 모델을 만들 때 쓰이는 경우에 일어난다."
  source="Common pitfalls and recommended practices · Data leakage"
  sourceURL="https://scikit-learn.org/stable/common_pitfalls.html#data-leakage"
  note="`X occurs when information that would not be available at A time is used when doing B.` — 잘못을 사람이 아니라 **정보의 시점**으로 정의하는 문형이다. `occurs when`은 정의를 조건문처럼 쓰는 장치라, 누가 그랬는지가 문장에서 통째로 빠지고 조건만 남는다. 그래서 같은 지적이 비난이 아니라 판정 기준이 된다. 무게는 `would not be available at ~ time`에 실린다 — 지금 그 정보를 가지고 있느냐가 아니라 **판단해야 하는 그 순간에 가지고 있었겠느냐**로 기준을 옮기기 때문에, 이미 알아 버린 사람도 자기 판단을 검사할 수 있다. 회고에서 사후에 알게 된 사실로 당시 대응을 평가할 때, 실험이나 벤치마크가 운영에서는 못 얻는 정보를 쓰고 있을 때 꺼내 쓴다."
  app1="Hindsight bias occurs when information that would not be available at decision time is used when judging the responder who was paged."
  app1ko="사후 확신 편향은 판단해야 했던 시점에는 확보할 수 없는 정보가 호출을 받은 담당자를 평가할 때 쓰이는 경우에 일어난다."
  app2="Optimistic capacity planning occurs when headroom that would not be available at peak time is used when sizing the cluster."
  app2ko="낙관적인 용량 산정은 피크 시점에는 확보할 수 없는 여유 용량이 클러스터 크기를 정할 때 쓰이는 경우에 일어난다."
>}}

{{< sentence
  en="If these data transforms are used when training a model, they also must be used on subsequent datasets, whether it's test data or data in a production system. Otherwise, the feature space will change, and the model will not be able to perform effectively."
  ko="이 데이터 변환들을 모델 학습에 썼다면, 그 뒤에 오는 데이터셋에도 반드시 써야 한다. 그것이 테스트 데이터든 운영 시스템의 데이터든 마찬가지다. 그러지 않으면 특징 공간이 달라지고, 모델은 제대로 성능을 낼 수 없게 된다."
  source="Common pitfalls and recommended practices · Inconsistent preprocessing"
  sourceURL="https://scikit-learn.org/stable/common_pitfalls.html#inconsistent-preprocessing"
  note="`If X is used when A, it also must be used on B, whether it's C or D. Otherwise, ...` — 한쪽에만 적용된 처리를 양쪽에 맞추라고 요구하는 문형이다. 세 부분이 각자 일한다. `also must`는 새 규칙을 얹는 게 아니라 **이미 한 일의 짝을 요구**하는 표현이라 추가 부담처럼 들리지 않는다. `whether it's C or D`는 예외로 빠져나갈 만한 후보를 **먼저 세어 두는** 자리다 — 나중에 테스트는 예외 아니냐는 말이 나오기 전에 그 둘을 이름으로 못 박아 둔다. `Otherwise` 뒤에는 벌칙이 아니라 **메커니즘**이 온다: 성능이 나빠진다가 아니라 특징 공간이 달라진다를 먼저 말하고 거기서 결과를 끌어내기 때문에, 명령이 아니라 인과로 읽힌다. 스테이징에만 켜 둔 설정, 테스트 하네스에만 있는 전처리, 리허설에만 있는 단계를 지적할 때 쓴다."
  app1="If a feature flag is used when we run the load test, it also must be used on every later environment, whether it's staging or the production rollout. Otherwise, the request path will change, and the numbers we measured will not describe what users get."
  app1ko="부하 테스트를 돌릴 때 기능 플래그를 켰다면, 그 뒤의 모든 환경에서도 반드시 켜야 한다. 그것이 스테이징이든 운영 배포든 마찬가지다. 그러지 않으면 요청 경로가 달라지고, 우리가 측정한 숫자는 사용자가 실제로 겪는 것을 설명하지 못한다."
  app2="If a sanitizer is used when we accept input in the public API, it also must be used on every other entry point, whether it's the batch importer or the admin console. Otherwise, the trust boundary will move, and the audit will not be able to rely on a single check."
  app2ko="공개 API에서 입력을 받을 때 정화 처리를 했다면, 다른 모든 진입점에도 반드시 써야 한다. 그것이 일괄 임포터든 관리자 콘솔이든 마찬가지다. 그러지 않으면 신뢰 경계가 옮겨 가고, 감사는 한 군데의 점검에 기댈 수 없게 된다."
>}}

{{< sentence
  en="A common cause is not keeping the test and train data subsets separate. Test data should never be used to make choices about the model."
  ko="흔한 원인은 테스트 데이터와 학습 데이터를 분리된 상태로 유지하지 않는 것이다. 테스트 데이터는 모델에 관한 선택을 하는 데 절대 쓰여서는 안 된다."
  source="Common pitfalls and recommended practices · Data leakage"
  sourceURL="https://scikit-learn.org/stable/common_pitfalls.html#data-leakage"
  note="`A common cause is not keeping X and Y separate. X should never be used to make choices about Y.` — 원인을 한 줄로 짚고 곧바로 금지선을 긋는 문형이다. 앞 문장의 핵심은 `not keeping ~ separate`다. 무엇을 했다가 아니라 **분리를 유지하지 못했다**는 부정형이라, 원인이 누군가의 실수가 아니라 **그 상태를 지켜 주는 장치가 없었다**는 쪽을 가리킨다. 그래서 대책도 주의하자가 아니라 장치를 만들자로 이어진다. 뒤 문장의 `to make choices about`은 금지의 범위를 정하는 자리다 — 보지 마라나 열지 마라처럼 행위를 막는 대신 **그것을 근거로 무언가를 고르는 일 전부**를 막기 때문에, 슬쩍 참고만 했다는 변명이 들어올 틈이 없다. 권한 분리를 요구할 때, 튜닝에 쓴 데이터로 성능을 주장할 때, 배포자와 승인자가 같을 때 쓴다."
  app1="A common cause is not keeping the tuning incidents and the holdout incidents separate. The outages we tuned the alerts on should never be used to make choices about whether the alerts work."
  app1ko="흔한 원인은 튜닝에 쓴 장애 사례와 평가용으로 남겨 둔 장애 사례를 분리된 상태로 유지하지 않는 것이다. 알림을 맞출 때 쓴 장애는 그 알림이 제대로 동작하는지에 관한 선택을 하는 데 절대 쓰여서는 안 된다."
  app2="A common cause is not keeping the deploy and the approval paths separate. The account that ships a change should never be used to make choices about whether that change is allowed."
  app2ko="흔한 원인은 배포 경로와 승인 경로를 분리된 상태로 유지하지 않는 것이다. 변경을 내보내는 계정은 그 변경이 허용되는지에 관한 선택을 하는 데 절대 쓰여서는 안 된다."
>}}

{{< sentence
  en="While this may sound obvious, this is easy to miss in some cases, for example when applying certain pre-processing steps."
  ko="이 말이 당연하게 들릴 수 있지만, 예를 들어 특정 전처리 단계를 적용할 때처럼 어떤 경우에는 놓치기 쉽다."
  source="Common pitfalls and recommended practices · Data leakage"
  sourceURL="https://scikit-learn.org/stable/common_pitfalls.html#data-leakage"
  note="`While this may sound obvious, this is easy to miss in some cases, for example when X.` — 누구나 아는 원칙을 다시 말해야 할 때 **가르치는 모양이 되지 않게** 하는 완충 문형이다. `While this may sound obvious`가 상대도 이미 안다는 것을 먼저 인정해 버리기 때문에, 지적의 무게가 아는가 모르는가에서 **놓치기 쉬운가**로 옮겨 간다. 즉 사람을 평가하는 문장이 아니라 상황을 평가하는 문장이 된다. 진짜 일을 하는 부분은 뒤의 `for example when ~`이다. 이것이 없으면 조심하자는 잔소리로 끝나지만, 놓치는 **구체적인 지점 하나**가 붙는 순간 확인해 볼 자리가 생긴다. 그래서 이 문형을 쓸 때는 예시를 반드시 채운다. 코드 리뷰에서 기본기를 짚을 때, 런북에 당연해 보이는 단계를 남기는 이유를 적을 때, 나보다 경력이 긴 사람에게 기본 점검을 요청할 때 쓴다."
  app1="While this may sound obvious, this is easy to miss in some cases, for example when the retry wrapper swallows the original error and logs only the last attempt."
  app1ko="이 말이 당연하게 들릴 수 있지만, 예를 들어 재시도 래퍼가 원래 오류를 삼키고 마지막 시도만 로그에 남길 때처럼 어떤 경우에는 놓치기 쉽다."
  app2="While this may sound obvious, this is easy to miss in some cases, for example when the same limit is set in two places and only one of them shows up in the diff."
  app2ko="이 말이 당연하게 들릴 수 있지만, 예를 들어 같은 제한값이 두 군데에 설정되어 있는데 그중 하나만 diff에 나타날 때처럼 어떤 경우에는 놓치기 쉽다."
>}}

{{< sentence
  en="Using all the data to perform feature selection results in an accuracy score much higher than chance, even though our targets are completely random."
  ko="특징 선택에 데이터 전체를 쓰면 정확도 점수가 우연 수준보다 훨씬 높게 나오는데, 우리의 정답 값이 완전히 무작위인데도 그렇다."
  source="Common pitfalls and recommended practices · Data leakage during pre-processing"
  sourceURL="https://scikit-learn.org/stable/common_pitfalls.html#data-leakage-during-pre-processing"
  note="`Doing X results in Y much higher than chance, even though Z.` — 좋아 보이는 결과를 **반박하지 않고 무력화**하는 문형이다. 앞 절에서 숫자를 그대로 인정해 주기 때문에 다툴 거리가 생기지 않고, `even though` 뒤에 그 숫자로는 설명할 수 없는 사실을 하나 붙인다. 그러면 쟁점이 숫자가 맞느냐 틀리느냐에서 **이 숫자로 무엇을 결정할 수 있느냐**로 옮겨 간다. 상대의 측정을 의심한다고 말하지 않고도 그 측정을 근거에서 빼내는 것이다. 또 하나 훔칠 것은 `much higher than chance` — **비교 기준을 문장 안에 미리 박아 두는 습관**이다. 기준 없이 높다고 하면 체감 싸움이 되지만, 무엇보다 높은지를 정해 두면 반박하는 쪽도 같은 자를 들고 와야 한다. 벤치마크 결과를 되돌려 줄 때, 캐시가 데워진 채 잰 지연 시간을 지적할 때, 통과했지만 사실상 아무것도 검사하지 않는 테스트를 짚을 때 쓴다."
  app1="Running the benchmark against a warmed cache results in a p99 much lower than the SLO, even though the slow query is still on the request path."
  app1ko="캐시가 데워진 상태에서 벤치마크를 돌리면 p99가 SLO보다 훨씬 낮게 나오는데, 느린 쿼리가 여전히 요청 경로에 있는데도 그렇다."
  app2="Counting only the tickets we closed results in a resolution rate much higher than last quarter, even though the backlog grew every single week."
  app2ko="우리가 닫은 티켓만 세면 해결률이 지난 분기보다 훨씬 높게 나오는데, 밀린 일감이 매주 빠짐없이 늘었는데도 그렇다."
>}}
