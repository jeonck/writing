---
title: 확신의 크기를 재서 말하는 표현
description: 의심할 조건을 규칙으로 적고, 근거가 미치는 범위를 자르고, 확신을 요구하지도 과장하지도 않는 문장 5개.
weight: -17
date: 2026-09-06
source: "Deep Learning Tuning Playbook"
sourceURL: https://github.com/google-research/tuning_playbook
---

# 확신의 크기를 재서 말하는 표현

구글 리서치 팀이 쓴 *Deep Learning Tuning Playbook*은 딥러닝 모델의 하이퍼파라미터를
어떤 순서로 실험하고 무엇을 근거로 채택할지를 정리한 문서다. 결과를 자랑하는 글이 아니라
**어디까지가 근거이고 어디부터가 운인지**를 계속 가려내는 글이라서, 확신의 크기를 문장
안에서 조절하는 표현이 많다. 의심할 조건을 규칙으로 적는 문장, 자기 경험의 사정거리를
스스로 자르는 문장, 확신을 요구하지도 과장하지도 않는 문장을 다섯 개 뽑았다. 장애 원인
분석, 성능 개선 리뷰, A/B 결과 보고처럼 **아직 결론이 덜 선 것을 말해야 하는 글**에 그대로
옮겨 쓸 수 있다.

> **원문** — Varun Godbole, George E. Dahl, Justin Gilmer, Christopher J. Shallue, Zachary Nado,
> *Deep Learning Tuning Playbook*,
> [github.com/google-research/tuning_playbook](https://github.com/google-research/tuning_playbook)
> (2023), 문서 라이선스
> [CC BY 4.0](https://github.com/google-research/tuning_playbook/blob/main/LICENSE).
>
> 영어 문장은 원문 그대로 인용했고, 한글 설명과 응용 문장은 이 노트에서 새로 쓴 것이다.

{{< sentence
  en="A search space is suspicious if the best point sampled from it is close to its boundary. We might find an even better point if we expanded the search range in that direction."
  ko="탐색 공간에서 뽑아낸 최적점이 그 경계에 가깝다면 그 탐색 공간은 의심스럽다. 그 방향으로 탐색 범위를 넓혔다면 더 나은 점을 찾았을지도 모른다."
  source="Deep Learning Tuning Playbook · Identifying bad search space boundaries"
  sourceURL="https://github.com/google-research/tuning_playbook"
  note="`X is suspicious if Y.` — 무엇이 잘못이라고 단정하는 대신 **의심할 조건을 규칙으로 적어 두는** 문형이다. `is suspicious`는 판정이 아니라 신호다. 아직 확인하지 않았지만 그냥 넘기지도 않겠다는 자리에 놓기 때문에, 남의 작업을 지적할 때도 공격으로 읽히지 않는다. 이어지는 `We might find ... if we expanded ...`는 가정법으로 **놓쳤을 가능성**만 제시하고 상대에게 확인을 넘긴다. 리뷰 코멘트나 조사 메모에서 '이건 틀렸다' 대신 '이 조건이면 다시 봐야 한다'를 남길 때 쓴다."
  app1="A load test is suspicious if the best throughput we measured is close to the highest concurrency we tried. We might see a higher ceiling if we pushed the concurrency further."
  app1ko="부하 테스트에서 측정한 최고 처리량이 우리가 시도한 최대 동시성 근처에 있다면 그 테스트는 의심스럽다. 동시성을 더 밀어 봤다면 더 높은 한계를 봤을지도 모른다."
  app2="A timeout value is suspicious if the p99 latency sits right under it. We might be dropping healthy requests if the upstream ever gets slightly slower."
  app2ko="p99 지연이 타임아웃 값 바로 아래에 붙어 있다면 그 타임아웃 값은 의심스럽다. 업스트림이 조금만 더 느려지면 정상 요청까지 버리고 있을지도 모른다."
>}}

{{< sentence
  en="The study variance depends on the number of trials and the search space and we have seen cases where it is larger than the trial variance as well as cases where it is much smaller."
  ko="스터디 분산은 시도 횟수와 탐색 공간에 따라 달라진다. 우리는 그것이 시행 분산보다 큰 경우도 봤고 훨씬 작은 경우도 봤다."
  source="Deep Learning Tuning Playbook · Determining whether to adopt a training pipeline change"
  sourceURL="https://github.com/google-research/tuning_playbook"
  note="`X depends on A and B, and we have seen cases where ... as well as cases where ...` — 일반화를 요구받는 자리에서 **일반화를 거부하되 침묵하지도 않는** 방식이다. 앞절이 무엇에 의존하는지 변수를 먼저 밝혀서, 뒤의 '경우에 따라 다르다'가 회피로 들리지 않게 만든다. 핵심은 `we have seen cases`다. 이론적 가능성이 아니라 **자기가 관찰한 범위**로 말하기 때문에 반박당해도 무너지지 않고, 동시에 상대가 자기 상황을 대입해 볼 여지를 남긴다. 양쪽 극단을 다 봤다고 적는 `as well as cases where it is much smaller`가 없으면 은근한 편들기로 읽힌다는 점도 훔칠 만하다."
  app1="The cost of a retry storm depends on the timeout budget and the fan-out depth, and we have seen incidents where it dwarfed the original failure as well as incidents where it was barely visible."
  app1ko="재시도 폭주의 비용은 타임아웃 예산과 팬아웃 깊이에 따라 달라진다. 우리는 그것이 원래 장애보다 훨씬 커진 사례도 봤고 거의 눈에 띄지 않은 사례도 봤다."
  app2="Review turnaround depends on the size of the diff and how many teams own the touched files, and we have seen changes that landed in an hour as well as changes of the same size that sat for a week."
  app2ko="리뷰 소요 시간은 디프 크기와 건드린 파일을 소유한 팀 수에 따라 달라진다. 우리는 한 시간 만에 머지된 변경도 봤고 같은 크기인데 일주일을 기다린 변경도 봤다."
>}}

{{< sentence
  en="At the end of the day, although we only want to adopt changes (including new hyperparameter configurations) that produce real improvements, demanding complete certainty that something helps isn't the right answer either."
  ko="결국, 우리는 실제로 개선을 만들어 내는 변경(새 하이퍼파라미터 설정을 포함해)만 채택하고 싶지만, 그렇다고 무언가가 도움이 된다는 완전한 확신을 요구하는 것도 정답은 아니다."
  source="Deep Learning Tuning Playbook · Determining whether to adopt a training pipeline change"
  sourceURL="https://github.com/google-research/tuning_playbook"
  note="`Although we only want A, demanding B isn't the right answer either.` — 원칙을 세워 놓고 **그 원칙을 극단까지 밀면 안 된다**고 같은 문장 안에서 덧붙이는 구조다. 문장 끝의 `either`가 저울추다. 앞에서 이미 한쪽(근거 없는 채택)을 부정했으니, `either`는 '반대쪽도 마찬가지로 아니다'를 한 단어로 처리한다. `demanding complete certainty`처럼 반대 극단을 동명사로 이름 붙여 주어 자리에 세우면, 사람을 지목하지 않고 **태도만** 반박할 수 있다. 기준을 세우는 문서에서 그 기준이 무기로 쓰이는 걸 미리 막을 때."
  app1="Although we only want to merge changes that come with a regression test, demanding a test for every one-line config fix isn't the right answer either."
  app1ko="회귀 테스트가 붙은 변경만 머지하고 싶은 것은 맞지만, 한 줄짜리 설정 수정까지 테스트를 요구하는 것도 정답은 아니다."
  app2="Although we only want to page on-call for user-visible failures, demanding proof of user impact before anyone is woken up isn't the right answer either."
  app2ko="사용자에게 드러난 장애에만 온콜을 호출하고 싶은 것은 맞지만, 누군가를 깨우기 전에 사용자 영향의 증거부터 요구하는 것도 정답은 아니다."
>}}

{{< sentence
  en="However, the difference in validation set performance between two batch sizes typically goes away if the training pipeline is optimized independently for each batch size."
  ko="다만 두 배치 크기 사이의 검증 세트 성능 차이는, 각 배치 크기마다 학습 파이프라인을 따로 최적화하면 대개 사라진다."
  source="Deep Learning Tuning Playbook · Why the batch size should not be tuned for validation performance"
  sourceURL="https://github.com/google-research/tuning_playbook"
  note="`The difference between A and B typically goes away if C.` — 관찰된 차이를 부정하지 않으면서 **그 차이가 무엇 때문이었는지 자리를 옮겨 놓는** 문형이다. 상대의 측정을 틀렸다고 하지 않는다. 조건 `C`를 맞추면 없어지는 차이라고만 말하므로, 결론은 뒤집히는데 상대의 관찰은 그대로 살아 있다. `goes away`는 `is not real`보다 훨씬 부드럽고, `typically`는 예외를 미리 인정해 준다. 벤치마크 논쟁이나 '언어/프레임워크를 바꾸니 빨라졌다' 류의 주장에 답할 때 그대로 쓴다."
  app1="However, the difference in p95 latency between the two runtimes typically goes away if the connection pool is sized independently for each one."
  app1ko="다만 두 런타임 사이의 p95 지연 차이는, 각각에 맞게 커넥션 풀 크기를 따로 잡아 주면 대개 사라진다."
  app2="However, the gap in build times between the two CI providers typically goes away if the cache is warmed the same way on both."
  app2ko="다만 두 CI 제공자 사이의 빌드 시간 차이는, 양쪽에서 캐시를 같은 방식으로 데워 주면 대개 사라진다."
>}}

{{< sentence
  en="This type of validation-error-sensitive schedule is fine to use if it can be fully automated, but human-in-the-loop schedules that are a function of validation error are brittle and not easily reproducible, so we recommend avoiding them."
  ko="이런 식으로 검증 오차에 반응하는 스케줄은 완전히 자동화할 수 있다면 써도 괜찮다. 하지만 검증 오차에 따라 사람이 개입하는 스케줄은 깨지기 쉽고 재현하기도 어려우므로, 쓰지 않기를 권한다."
  source="Deep Learning Tuning Playbook · Why do some papers have complicated learning rate schedules?"
  sourceURL="https://github.com/google-research/tuning_playbook"
  note="`X is fine to use if C, but Y are brittle and not easily reproducible, so we recommend avoiding them.` — 금지 대신 **조건을 걸어 허용하고, 조건을 못 맞추는 쪽만 잘라 내는** 3단 구조다. `is fine to use if`로 먼저 문을 열어 두기 때문에 뒤의 `we recommend avoiding`이 일방적 금지로 읽히지 않는다. 이유 자리에 결과(느리다, 나쁘다)가 아니라 성질(`brittle`, `not easily reproducible`)을 놓는 것이 핵심이다 — 이번에 잘 돌아갔다는 반례로는 반박되지 않기 때문이다. `we recommend`는 규칙이 아니라 권고라서 예외를 만들 사람에게 책임을 넘긴다. 코딩 컨벤션, 운영 가이드, 리뷰 기준을 쓸 때."
  app1="This type of manual hotfix is fine to use if it can be replayed from the pipeline afterwards, but patches applied straight to a running instance are brittle and not easily reproducible, so we recommend avoiding them."
  app1ko="이런 식의 수동 핫픽스는 나중에 파이프라인에서 다시 재생할 수 있다면 써도 괜찮다. 하지만 돌고 있는 인스턴스에 곧바로 적용하는 패치는 깨지기 쉽고 재현하기도 어려우므로, 쓰지 않기를 권한다."
  app2="This type of environment-specific override is fine to use if it lives in version control, but values typed into the console during an incident are brittle and not easily reproducible, so we recommend avoiding them."
  app2ko="이런 식의 환경별 오버라이드는 버전 관리 안에 들어 있다면 써도 괜찮다. 하지만 장애 중에 콘솔에서 직접 입력한 값은 깨지기 쉽고 재현하기도 어려우므로, 쓰지 않기를 권한다."
>}}
