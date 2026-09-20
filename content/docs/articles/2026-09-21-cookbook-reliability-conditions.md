---
title: 정답 대신 조건을 말하는 표현
description: 단답을 거부하고 조건을 걸어 권하고, 능력이 맥락과 무관하게 고정돼 있다는 오해에 이름을 붙이고, 한 사례로는 모른다고 유보한 뒤 집계로 뒤집고, 성과가 측정된 벤치마크가 왜 골라졌는지 밝히고, 효과가 0이 되는 경우까지 한 문장에 넣는 문장 5개.
weight: -31
date: 2026-09-21
source: "OpenAI Cookbook — Techniques to improve reliability"
sourceURL: https://cookbook.openai.com/articles/techniques-to-improve-reliability
---

# 정답 대신 조건을 말하는 표현

OpenAI Cookbook의 *Techniques to improve reliability*는 언어 모델이 복잡한 과제에서 틀렸을 때
무엇을 해야 하는지를 정리한 글이다. 2022년에 쓰인 글이라 등장하는 모델 이름은 낡았지만, 이
노트가 여기서 가져오는 것은 기법이 아니라 **기법을 말하는 방식**이다. 이 글은 프롬프트 기법을
하나 소개할 때마다 Method / Results / Implications 세 칸을 붙이고, 마지막 칸에서 거의 매번 방금
자랑한 성과의 조건을 자기 손으로 적는다 — 어떤 벤치마크에서 쟀는지, 그 벤치마크가 왜 골라졌는지,
어떤 과제에서는 효과가 아예 없을 수 있는지. 도구 도입을 제안할 때, 파일럿 결과를 들고 전사 확대를
논의할 때, 한 번의 장애나 한 번의 성공에서 결론을 끌어내야 할 때 필요한 말이 정확히 그 칸에 있다.
정답 하나를 내놓는 대신 조건을 세우는 다섯 문장을 골랐다.

> **원문** — Ted Sanders, *Techniques to improve reliability*,
> [OpenAI Cookbook](https://cookbook.openai.com/articles/techniques-to-improve-reliability) (2022-09-12)
> (원본: [`openai/openai-cookbook` · `articles/techniques_to_improve_reliability.md`](https://github.com/openai/openai-cookbook/blob/main/articles/techniques_to_improve_reliability.md)),
> [MIT License](https://github.com/openai/openai-cookbook/blob/main/LICENSE). Copyright (c) OpenAI.
>
> 영어 문장은 원문 그대로 인용했고, 한글 설명과 응용 문장은 이 노트에서 새로 쓴 것이다.

{{< sentence
  en="There is no simple answer - it depends. However, if your task involves logical reasoning or complexity, consider trying the techniques in this article to build more reliable, high-performing prompts."
  ko="간단한 답은 없다 — 상황에 따라 다르다. 다만 당신의 과제가 논리적 추론이나 복잡성을 포함한다면, 더 신뢰할 만하고 성능 좋은 프롬프트를 만들기 위해 이 글의 기법들을 시도해 보라."
  source="OpenAI Cookbook · Techniques to improve reliability"
  sourceURL="https://cookbook.openai.com/articles/techniques-to-improve-reliability"
  note="`There is no simple answer - it depends. However, if your task involves X, consider trying Y.` — 단답을 거부하는 말을 회피가 아니라 분류로 만드는 문형이다. `it depends`만 말하고 끝내면 답을 안 준 것이 되는데, 바로 뒤에 `However` + 조건절이 붙으면 상황에 따라 다르다는 말이 **어떤 상황인지 말해 보라**는 요청으로 바뀐다. 조건절의 모양이 중요하다 — `if your task involves logical reasoning or complexity`처럼 상대가 자기 과제를 대입해 스스로 판정할 수 있어야 한다. 조건이 상대 쪽에 있으니 답을 미룬 것이 아니라 판단 기준을 넘긴 것이 된다. 마무리의 `consider trying`은 지시가 아니라 제안이라, 조건에 맞지 않는 사람이 빠져나갈 자리를 남겨 둔다. 무조건 이걸 쓰라고 말할 수 없는데 그래서 뭘 쓰면 되냐는 질문을 받을 때 쓴다."
  app1="There is no simple answer - it depends. However, if the service still owns user-facing writes during the incident, consider failing closed until the root cause is named."
  app1ko="간단한 답은 없다 — 상황에 따라 다르다. 다만 장애 중에도 그 서비스가 여전히 사용자 쓰기 요청을 담당하고 있다면, 원인이 지목될 때까지 닫힌 쪽으로 실패하도록 두는 방안을 고려해 보라."
  app2="There is no simple answer - it depends. However, if the change touches authentication or data deletion, consider asking for a second reviewer before merging."
  app2ko="간단한 답은 없다 — 상황에 따라 다르다. 다만 그 변경이 인증이나 데이터 삭제를 건드린다면, 머지하기 전에 리뷰어를 한 명 더 요청하는 방안을 고려해 보라."
>}}

{{< sentence
  en="When learning to work with GPT-3, one common conceptual mistake is to believe that its capabilities are fixed across all contexts. E.g., if GPT-3 gets a simple logic question wrong, then it must be incapable of simple logic."
  ko="GPT-3를 다루는 법을 배울 때 흔히 저지르는 개념적 실수 하나는 그 능력이 모든 맥락에서 고정되어 있다고 믿는 것이다. 예컨대 GPT-3가 간단한 논리 문제를 틀리면 그 모델은 간단한 논리를 할 수 없는 게 틀림없다는 식이다."
  source="OpenAI Cookbook · Model capabilities depend on context"
  sourceURL="https://cookbook.openai.com/articles/techniques-to-improve-reliability"
  note="`When learning to work with X, one common conceptual mistake is to believe that its capabilities are fixed across all contexts. E.g., if X gets A wrong, then it must be incapable of A.` — 오해를 반박하기 전에 **이름부터 붙이는** 문형이다. 장치가 둘이다. 첫째, `one common conceptual mistake`는 그것을 개인의 잘못이 아니라 배우는 사람이라면 대개 거치는 단계로 옮겨 놓는다 — `common` 덕분에 지적받은 사람이 자기를 방어할 이유가 사라진다. `conceptual`은 틀린 것의 종류까지 한정한다: 사실을 잘못 안 게 아니라 머릿속 그림이 잘못됐다는 것. 둘째, `E.g.`로 시작하는 뒤 문장은 반박이 아니라 **재현**이다. 그 오해가 굴러가는 추론을 그대로 한 번 소리 내어 읽어 주면, 문장이 끝나기 전에 읽는 사람이 스스로 어색함을 느낀다. 과장을 떠맡는 단어는 `must be`다. 한 번의 관찰에서 고정된 성질을 읽어 내는 말 — 그 팀은 원래 느리다, 그 서비스는 원래 불안정하다 — 에 답할 때 쓴다."
  app1="When onboarding to this system, one common conceptual mistake is to believe that its latency is fixed across all traffic shapes. E.g., if a batch job times out once, then the service must be too slow for batch work."
  app1ko="이 시스템에 새로 들어올 때 흔히 저지르는 개념적 실수 하나는 지연 시간이 모든 트래픽 형태에서 고정되어 있다고 믿는 것이다. 예컨대 배치 작업이 한 번 타임아웃 나면 그 서비스는 배치 작업을 감당하기엔 너무 느린 게 틀림없다는 식이다."
  app2="When reading our incident history, one common conceptual mistake is to believe that a team's response time is fixed across all shifts. E.g., if one page went unanswered for an hour, then the rotation must be understaffed."
  app2ko="우리 장애 이력을 읽을 때 흔히 저지르는 개념적 실수 하나는 한 팀의 대응 시간이 모든 근무조에서 고정되어 있다고 믿는 것이다. 예컨대 호출 하나가 한 시간 동안 응답되지 않았다면 그 당번 편성은 인원이 부족한 게 틀림없다는 식이다."
>}}

{{< sentence
  en="Of course, it's hard to tell from only a single example whether this `Let's think step by step` trick actually works in general or just got lucky on this particular problem. But it really does work. On a benchmark of word math problems, the `Let's think step by step` trick raised GPT-3's solve rate massively, from a worthless 18% to a decent 79%!"
  ko="물론 단 하나의 예시만으로는 이 `Let's think step by step` 요령이 정말 일반적으로 통하는 것인지, 아니면 이 특정 문제에서 운이 좋았을 뿐인지 판단하기 어렵다. 그러나 이것은 정말로 통한다. 수학 문장제 벤치마크에서 이 요령은 GPT-3의 정답률을 쓸모없는 18%에서 쓸 만한 79%로 크게 끌어올렸다."
  source="OpenAI Cookbook · Why GPT-3 fails on complex tasks"
  sourceURL="https://cookbook.openai.com/articles/techniques-to-improve-reliability"
  note="`Of course, it's hard to tell from only a single example whether X actually works in general or just got lucky on this particular case. But it really does work. On <집계>, X raised <지표> from A to B.` — 반론을 상대가 꺼내기 전에 **내가 먼저 꺼내고** 근거로 뒤집는 3박자 문형이다. `Of course`가 신호다: 그건 나도 안다는 뜻이라, 읽는 사람이 준비하던 말을 미리 회수한다. 진짜 장치는 반론을 두 갈래로 정확히 쪼개 놓은 데 있다 — `works in general` 대 `just got lucky on this particular problem`. 이렇게 갈라 두면 다음 문장이 어떤 종류의 증거를 대야 하는지가 정해진다. 사례를 하나 더 드는 것으로는 안 되고, 집계로 가야 한다. 그래서 세 번째 문장이 벤치마크와 두 개의 숫자로 온다. `But it really does work.`를 짧게 끊어 둔 자리도 계산된 것이다. 유보와 근거 사이에 단언을 하나 끼워 넣으면 뒤따르는 숫자가 변명이 아니라 확인으로 읽힌다. 잘 된 사례 하나를 들고 도입을 제안할 때, 반대로 실패 사례 하나로 폐기를 주장하는 말에 답할 때 쓴다."
  app1="Of course, it's hard to tell from only a single incident whether the retry cap actually helps in general or just happened to hold on that particular outage. But it really does help. Across two quarters of paging incidents, the cap cut duplicate writes from one in twelve retries to one in four hundred."
  app1ko="물론 단 한 번의 장애만으로는 그 재시도 상한이 정말 일반적으로 도움이 되는 것인지, 아니면 그 특정 장애에서 우연히 버텨 준 것인지 판단하기 어렵다. 그러나 이것은 정말로 도움이 된다. 두 분기 동안의 호출 장애 전체에서 그 상한은 중복 쓰기를 재시도 열두 번당 한 번에서 사백 번당 한 번으로 줄였다."
  app2="Of course, it's hard to tell from only a single review whether the checklist actually catches defects in general or just got lucky on that particular change. But it really does catch them. Over two hundred merged pull requests, changes reviewed with the checklist needed a follow-up fix half as often."
  app2ko="물론 단 한 번의 리뷰만으로는 그 체크리스트가 정말 일반적으로 결함을 잡아내는 것인지, 아니면 그 특정 변경에서 운이 좋았을 뿐인지 판단하기 어렵다. 그러나 이것은 정말로 잡아낸다. 머지된 풀 리퀘스트 이백 건에 걸쳐, 체크리스트로 리뷰한 변경은 후속 수정이 필요한 일이 절반으로 줄었다."
>}}

{{< sentence
  en="Although the gains on these benchmarks were large, these benchmarks were specifically chosen because they required longer sequences of reasoning. On problems that don't require reasoning with many steps, the gains are likely smaller."
  ko="이 벤치마크들에서의 향상 폭은 컸지만, 이 벤치마크들은 더 긴 추론 단계를 요구한다는 이유로 일부러 선택된 것이었다. 단계가 많은 추론을 요구하지 않는 문제에서는 향상 폭이 더 작을 가능성이 크다."
  source="OpenAI Cookbook · Selection-inference prompting, Implications"
  sourceURL="https://cookbook.openai.com/articles/techniques-to-improve-reliability"
  note="`Although the gains on X were large, X were specifically chosen because they required Y. On problems that don't require Y, the gains are likely smaller.` — 성과를 깎지 않으면서 **그 성과가 측정된 조건**을 드러내는 문형이다. 앞 절에서 크기를 먼저 인정해 두기 때문에 뒤 절이 흠집 내기로 읽히지 않는다. 일하는 표현은 `specifically chosen because`다. 누가 유리하게 조작했다고 말하지 않고 **선택의 기준**만 밝히는데, 기준이 곧 적용 조건이므로 읽는 사람은 자기 환경을 그 기준에 대 볼 수 있게 된다. 마지막 문장은 그 대조를 대신 해 준다 — 조건을 부정형(`don't require Y`)으로 뒤집고 예측을 붙이는 것. `are likely smaller`처럼 **확률로만 말하고 정도는 비워 둔** 것도 일부러다. 얼마나 작아질지 모르면서 숫자를 붙이면 이 문장 자체가 방금 지적한 잘못을 저지르게 된다. 벤치마크·파일럿·PoC 결과를 그대로 우리 환경에 옮기자는 제안에 답할 때 쓴다."
  app1="Although the gains in the pilot were large, the pilot teams were specifically chosen because they already had test coverage above eighty percent. On repositories that don't have that coverage, the gains are likely smaller."
  app1ko="파일럿에서의 향상 폭은 컸지만, 파일럿 팀들은 이미 테스트 커버리지가 80퍼센트를 넘는다는 이유로 일부러 선택된 것이었다. 그 정도 커버리지를 갖추지 못한 리포지터리에서는 향상 폭이 더 작을 가능성이 크다."
  app2="Although the savings in the benchmark were large, those workloads were specifically chosen because they ran with steady, predictable traffic. On services that don't have predictable traffic, the savings are likely smaller."
  app2ko="벤치마크에서의 절감 폭은 컸지만, 그 워크로드들은 트래픽이 꾸준하고 예측 가능하다는 이유로 일부러 선택된 것이었다. 트래픽이 예측 가능하지 않은 서비스에서는 절감 폭이 더 작을 가능성이 크다."
>}}

{{< sentence
  en="Lastly, this technique ought to be most beneficial when there are multiple paths or phrasings to reach an answer; if there's only one path, then the technique may not help at all."
  ko="끝으로, 이 기법은 답에 도달하는 경로나 표현이 여럿일 때 가장 유익할 것이다. 경로가 하나뿐이라면 이 기법은 전혀 도움이 되지 않을 수도 있다."
  source="OpenAI Cookbook · Self-consistency, Implications"
  sourceURL="https://cookbook.openai.com/articles/techniques-to-improve-reliability"
  note="`X ought to be most beneficial when C; if there's only one <조건의 재료>, then X may not help at all.` — 효과가 **무엇에서 나오는지** 말하고, 같은 문장 안에서 그 재료가 없는 경우까지 처리하는 문형이다. 세미콜론이 접속사 노릇을 한다. 마침표로 끊으면 서로 다른 두 주장이 되고 `but`을 쓰면 뒤가 반박이 되는데, 세미콜론은 둘을 **하나의 조건 규칙**으로 묶어 준다. `ought to be`는 예측을 표시하는 조동사다 — `is`라고 쓰면 이미 측정한 사실이 되고 `may be`는 자신 없어 보이는데, `ought to`는 근거에서 따라 나오는 기대라는 뜻이라 아직 재 보지 않았다는 사실을 숨기지 않는다. 뒤쪽에서 진짜 일을 하는 건 `at all`이다. 효과가 줄어든다가 아니라 **0이 될 수 있다**고 적어 두면, 읽는 사람은 도입 여부를 취향이 아니라 조건으로 판단하게 된다. 다양성이 있어야 작동하는 장치(이중 리뷰, 카나리, 다중 신호 알림)를 제안할 때 쓴다."
  app1="Lastly, canary deploys ought to be most beneficial when failures show up in the first minutes of traffic; if the failure only appears after the nightly batch, then the canary may not help at all."
  app1ko="끝으로, 카나리 배포는 장애가 트래픽 초반 몇 분 안에 드러날 때 가장 유익할 것이다. 장애가 야간 배치 이후에야 나타난다면 카나리는 전혀 도움이 되지 않을 수도 있다."
  app2="Lastly, a second reviewer ought to be most beneficial when the two of them read the change in different ways; if both only check the same test output, then the second review may not help at all."
  app2ko="끝으로, 두 번째 리뷰어는 두 사람이 서로 다른 방식으로 그 변경을 읽을 때 가장 유익할 것이다. 둘 다 같은 테스트 결과만 확인한다면 두 번째 리뷰는 전혀 도움이 되지 않을 수도 있다."
>}}
