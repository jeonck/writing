---
title: 코드 리뷰 기준을 세우는 문장
description: 규칙을 선언하고, 우선순위를 못 박고, 갈등을 다른 채널로 옮기는 문장 5개.
weight: -2
date: 2026-08-22
source: "Google Eng Practices"
sourceURL: https://google.github.io/eng-practices/review/reviewer/standard.html
---

# 코드 리뷰 기준을 세우는 문장

구글이 사내 코드 리뷰의 **합격 기준을 어디에 둘 것인가**를 정리한 문서. 리뷰어가 어디까지 요구해도 되는지,
의견이 갈릴 때 무엇이 이기는지를 다룬다. 팀 규칙을 문서로 써야 할 때 골격째 가져다 쓸 수 있는 문장이 많아 발췌했다.

> **원문** — Google, *The Standard of Code Review*,
> [google/eng-practices](https://google.github.io/eng-practices/review/reviewer/standard.html)
> ([리포지터리](https://github.com/google/eng-practices/blob/master/review/reviewer/standard.md)),
> [CC BY 3.0](https://creativecommons.org/licenses/by/3.0/) 라이선스.
>
> 영어 문장은 원문 그대로 인용했고, 한글 설명과 응용 문장은 이 노트에서 새로 쓴 것이다.

{{< sentence
  en="If you never submit an improvement to the codebase, then the codebase never improves."
  ko="코드베이스에 개선을 한 번도 반영하지 않는다면, 코드베이스는 결코 개선되지 않는다."
  source="Google eng-practices · The Standard of Code Review"
  sourceURL="https://google.github.io/eng-practices/review/reviewer/standard.html"
  note="`If you never X, then Y never Z.` — 새 정보를 주는 문장이 아니라, 상대가 붙들고 있는 전제를 끝까지 밀어붙여 **반대편 극단이 왜 말이 안 되는지** 한 줄로 보여 주는 문장이다. 동어반복처럼 들리는 게 약점이 아니라 무기다. 반박할 거리가 없으니까. `never ~ never` 반복이 리듬을 만들고 `then`이 결론을 못 박는다. 완벽주의나 과잉 게이트를 지적할 때, 근거를 늘어놓기 전에 먼저 던져 판을 정리한다."
  app1="If you never merge a partial fix, then the incident never gets shorter."
  app1ko="부분 수정을 한 번도 머지하지 않는다면, 장애 시간은 결코 짧아지지 않는다."
  app2="If we never practice a rollback, then we never find out whether the rollback works."
  app2ko="롤백을 한 번도 연습해 보지 않으면, 롤백이 동작하는지 영영 알 수 없다."
>}}

{{< sentence
  en="On the other hand, it is the duty of the reviewer to make sure that each CL is of such a quality that the overall code health of their codebase is not decreasing as time goes on."
  ko="다른 한편으로, 각 변경이 코드베이스 전체의 코드 건강도를 시간이 흐르면서 떨어뜨리지 않을 만한 품질인지 확인하는 것은 리뷰어의 의무다."
  source="Google eng-practices · The Standard of Code Review"
  sourceURL="https://google.github.io/eng-practices/review/reviewer/standard.html"
  note="`it is the duty of X to make sure that Y`는 역할을 **권한이 아니라 의무**로 못 박는 문형이다. 진짜 기술은 기준을 잡은 방식에 있다. '좋아져야 한다'가 아니라 `is not decreasing as time goes on`, 즉 **시간축 위의 부정형**으로 잡았다. 한 건씩 합격·불합격을 따지는 대신 추세가 나빠지지 않는지를 묻기 때문에, 개별 예외를 허용하면서도 방향은 잃지 않는다. `of such a quality that ~`은 '~할 정도의 품질'이라는 결과 구문이고, `On the other hand`는 바로 앞에 반대편 논거를 세워 둔 다음에만 쓴다."
  app1="It is the duty of the on-call engineer to make sure that each mitigation is of such a quality that the error budget is not shrinking week over week."
  app1ko="각 임시 조치가 오류 예산을 주 단위로 갉아먹지 않을 만한 품질인지 확인하는 것은 온콜 엔지니어의 의무다."
  app2="It is the duty of the approver to make sure that each exception is narrow enough that the number of standing waivers is not growing over time."
  app2ko="각 예외 승인이 상시 면제 건수를 시간이 갈수록 늘리지 않을 만큼 좁은지 확인하는 것은 승인자의 의무다."
>}}

{{< sentence
  en="In general, reviewers should favor approving a CL once it is in a state where it definitely improves the overall code health of the system being worked on, even if the CL isn't perfect."
  ko="일반적으로 리뷰어는, 변경이 완벽하지 않더라도 작업 중인 시스템의 전체 코드 건강도를 확실히 개선하는 상태에 이르렀다면 승인하는 쪽으로 기울어야 한다."
  source="Google eng-practices · The Standard of Code Review"
  sourceURL="https://google.github.io/eng-practices/review/reviewer/standard.html"
  note="규칙을 선언하는 문장의 표준 골격 — `In general, A should favor X once Y, even if Z.` 부품 네 개가 각자 일한다. `In general`은 예외의 여지를 미리 남기고, `favor -ing`은 '무조건 하라'가 아니라 **판단이 갈릴 때 어느 쪽으로 기울지**만 정해 주고, `once ~`는 승인 가능한 최소 조건을 못 박고, `even if ~`는 사람들이 실제로 걸고 넘어질 반론을 미리 인정한 채 지나간다. 규칙을 짧게 쓰면 예외 논쟁이 뒤따르는데, 이 틀은 그 논쟁을 문장 안에 미리 접어 넣는다."
  app1="In general, on-call should favor rolling back once the error rate is clearly lower on the previous build, even if the root cause isn't understood yet."
  app1ko="일반적으로 온콜은, 근본 원인이 아직 밝혀지지 않았더라도 이전 빌드에서 오류율이 확실히 낮다면 롤백하는 쪽으로 기울어야 한다."
  app2="In general, auditors should favor closing a finding once the control is in a state where it demonstrably reduces the risk, even if the documentation isn't complete."
  app2ko="일반적으로 감사자는, 문서가 아직 완전하지 않더라도 통제가 위험을 눈에 띄게 줄이는 상태에 이르렀다면 지적 사항을 종결하는 쪽으로 기울어야 한다."
>}}

{{< sentence
  en="Technical facts and data overrule opinions and personal preferences."
  ko="기술적 사실과 데이터는 의견과 개인적 선호를 무효화한다."
  source="Google eng-practices · Principles"
  sourceURL="https://google.github.io/eng-practices/review/reviewer/standard.html"
  note="주어·동사·목적어만 남긴 여섯 단어짜리 **우선순위 선언**. 힘은 전부 `overrule`에서 나온다. '더 낫다'도 '우선한다'도 아니고 앞선 판결을 뒤집는다는 법정 어휘라서, 둘이 부딪히면 한쪽이 그냥 진다는 뜻이 된다. 조건절도 완충어도 없는 것이 실수가 아니라 설계다 — 원칙 목록의 첫 줄은 논쟁의 대상이 아니라 논쟁의 바깥에 서 있어야 해서, 길어지면 오히려 약해진다. 취향 싸움이 길어질 때 반박 대신 이 줄을 가리킨다."
  app1="Reproduction steps overrule severity labels."
  app1ko="재현 절차는 심각도 라벨을 무효화한다."
  app2="Measured latency overrules architectural intuition."
  app2ko="측정된 지연 시간은 아키텍처적 직관을 무효화한다."
>}}

{{< sentence
  en="When coming to consensus becomes especially difficult, it can help to have a face-to-face meeting or a video conference between the reviewer and the author, instead of just trying to resolve the conflict through code review comments."
  ko="합의에 이르기가 특히 어려워지면, 코드 리뷰 코멘트만으로 갈등을 풀려고 하는 대신 리뷰어와 작성자가 대면 회의나 화상 회의를 하는 편이 도움이 될 수 있다."
  source="Google eng-practices · Resolving Conflicts"
  sourceURL="https://google.github.io/eng-practices/review/reviewer/standard.html"
  note="`When X becomes especially difficult, it can help to Y, instead of just Z.` — **명령이 아니라 제안**으로 대화 채널을 바꾸자고 말하는 문형이다. 이미 감정이 상한 자리에 새 규칙을 얹으면 갈등이 하나 더 늘 뿐이라서, `it can help to ~`로 힘을 뺀다. `especially difficult`가 발동 조건을 평소가 아닌 예외 상황으로 좁혀 주고, `instead of just ~ing`의 `just`는 지금 하고 있는 방식을 '틀렸다'가 아니라 '그것만으로는 부족하다'로만 깎는다. 이 `just` 하나를 빼면 문장이 곧바로 비난이 된다."
  app1="When a review thread becomes especially long, it can help to get the two of you on a call, instead of just adding another round of comments."
  app1ko="리뷰 스레드가 특히 길어지면, 코멘트를 한 번 더 주고받는 대신 두 사람이 통화를 하는 편이 도움이 될 수 있다."
  app2="When an incident review becomes especially tense, it can help to walk through the timeline together, instead of just exchanging findings in the doc."
  app2ko="장애 리뷰가 특히 껄끄러워지면, 문서에서 발견 사항만 주고받는 대신 타임라인을 함께 짚어 보는 편이 도움이 될 수 있다."
>}}
