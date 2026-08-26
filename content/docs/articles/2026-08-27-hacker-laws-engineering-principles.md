---
title: 엔지니어링 법칙 모음의 표현
description: 주장을 요약하면서 과장을 인정하고, 한계를 지적하되 가치는 깎지 않고, 없앨 수 없는 것을 정확히 한정하는 문장 5개.
weight: -7
date: 2026-08-27
source: "hacker-laws"
sourceURL: https://github.com/dwmkerr/hacker-laws
---

# 엔지니어링 법칙 모음의 표현

개발자가 알아 둘 만한 법칙·이론·원칙을 한 문단씩 정리한 오픈 문서. 각 항목이 **인용문을
받아 그 뜻을 다시 풀어 주는** 구조라, 남의 주장을 요약하고 범위를 좁히는 문형이 촘촘하다.
회고나 설계 리뷰에서 "이 원칙이 말하는 건 여기까지"를 말할 때 쓸 틀만 골랐다.

> **원문** — Dave Kerr 외, *hacker-laws — Laws, Theories, Principles and Patterns for developers
> and technologists*, [github.com/dwmkerr/hacker-laws](https://github.com/dwmkerr/hacker-laws),
> [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) 라이선스.
>
> 영어 문장은 원문 그대로 인용했고, 한글 설명과 응용 문장은 이 노트에서 새로 쓴 것이다.

{{< sentence
  en="While hyperbolic, Kernighan's Law makes the argument that simple code is to be preferred over complex code, because debugging any issues that arise in complex code may be costly or even infeasible."
  ko="과장이긴 하지만, 커니핸의 법칙은 복잡한 코드보다 단순한 코드가 낫다고 주장한다. 복잡한 코드에서 생기는 문제를 디버깅하는 일은 비용이 크거나 아예 불가능할 수도 있기 때문이다."
  source="hacker-laws · Kernighan's Law"
  sourceURL="https://github.com/dwmkerr/hacker-laws"
  note="`While hyperbolic, X makes the argument that A, because B.`는 **인용의 과장을 먼저 인정하고 알맹이만 남기는** 문형이다. `While hyperbolic`이 '문자 그대로 받아들이지는 말라'는 안전장치를 걸어 주기 때문에, 뒤에 오는 주장을 방어적으로 굽히지 않고 그대로 말할 수 있다. `makes the argument that`은 `says`나 `proves`보다 한 칸 조심스럽다 — 사실이 아니라 **누군가의 논증**임을 표시한다. 남의 슬로건이나 밈을 근거로 끌어올 때 그 앞에 붙이면 된다."
  app1="While oversimplified, the two-pizza rule makes the argument that smaller teams ship faster, because every extra member adds a communication path that nobody maintains."
  app1ko="지나치게 단순하긴 하지만, 두 판의 피자 규칙은 작은 팀이 더 빨리 낸다고 주장한다. 사람이 하나 늘 때마다 아무도 관리하지 않는 소통 경로가 하나씩 늘기 때문이다."
  app2="While informal, the on-call handover note makes the argument that this alert should be paged rather than ticketed, because the last three occurrences all needed a rollback within ten minutes."
  app2ko="형식을 갖춘 문서는 아니지만, 온콜 인수인계 노트는 이 알림을 티켓이 아니라 호출로 올려야 한다고 주장한다. 최근 세 번 모두 10분 안에 롤백이 필요했기 때문이다."
>}}

{{< sentence
  en="Models can (and do) &quot;hallucinate&quot; - producing plausible sounding output or confidently making statements which are demonstrably wrong. This does not devalue these models, but highlights important characteristics which must be accounted for when using them."
  ko="모델은 환각을 일으킬 수 있고 실제로 일으킨다 — 그럴듯하게 들리는 출력을 만들어 내거나, 명백히 틀린 진술을 자신 있게 내놓는다. 이것이 그 모델들의 가치를 떨어뜨리지는 않는다. 다만 사용할 때 반드시 고려해야 할 중요한 특성을 드러낼 뿐이다."
  source="hacker-laws · The Stochastic Parrot"
  sourceURL="https://github.com/dwmkerr/hacker-laws"
  note="`This does not devalue X, but highlights Y which must be accounted for.` — **한계를 지적하면서 도입 자체를 반대하는 것으로 읽히지 않게 하는** 방어 문형이다. 결함을 말한 직후 `does not devalue`로 상대의 투자를 먼저 지켜 준 다음, `but highlights`로 논점을 '쓸 것이냐'에서 '어떻게 쓸 것이냐'로 옮긴다. `must be accounted for`는 수동태라 책임자를 지목하지 않아, 회의에서 누구를 탓하지 않고 조건만 붙일 수 있다. `can (and do)`는 '이론상 가능'과 '실제로 일어남'을 한 번에 못 박는 삽입구다."
  app1="The cache can (and does) serve stale reads during a failover. This does not devalue the cache, but highlights a consistency window which must be accounted for in the checkout path."
  app1ko="캐시는 페일오버 중에 오래된 값을 내보낼 수 있고 실제로 그런다. 이것이 캐시의 가치를 떨어뜨리지는 않는다. 다만 결제 경로에서 반드시 고려해야 할 정합성 구간을 드러낼 뿐이다."
  app2="The scanner can (and does) report findings that no attacker could reach. This does not devalue the tool, but highlights a triage cost which must be accounted for before we make it a merge gate."
  app2ko="스캐너는 공격자가 도달할 수 없는 항목까지 보고할 수 있고 실제로 그런다. 이것이 도구의 가치를 떨어뜨리지는 않는다. 다만 이걸 머지 게이트로 만들기 전에 반드시 고려해야 할 선별 비용을 드러낼 뿐이다."
>}}

{{< sentence
  en="Chesterton's Fence suggests that one should try to understand the context and meaning of the code fully, before changing or removing it, even if at first glance it seems redundant or incorrect."
  ko="체스터턴의 울타리는 코드를 바꾸거나 지우기 전에 그 맥락과 의미를 온전히 이해하려고 해 보라고 말한다 — 언뜻 보기에 군더더기이거나 잘못된 것처럼 보이더라도."
  source="hacker-laws · Chesterton's Fence"
  sourceURL="https://github.com/dwmkerr/hacker-laws"
  note="`X suggests that one should A, before B, even if at first glance it seems C.` — **삭제를 막는 것이 아니라 순서를 요구하는** 문형이다. 핵심은 `even if at first glance it seems ~`. 상대가 이미 내린 판단('이건 필요 없다')을 틀렸다고 하지 않고 **'첫인상'으로 격하**시켜, 반박이 아니라 확인 요청으로 만든다. `one should`는 `you should`보다 인격을 덜 겨냥한다. 코드 리뷰에서 남의 삭제 커밋에 제동을 걸 때 그대로 쓸 수 있다."
  app1="Our rollback policy suggests that one should reproduce the failure on a canary, before reverting the release, even if at first glance it seems obvious which commit broke it."
  app1ko="우리 롤백 정책은 릴리스를 되돌리기 전에 카나리에서 장애를 재현해 보라고 말한다 — 언뜻 보기에 어느 커밋이 깨뜨렸는지 뻔해 보이더라도."
  app2="The runbook suggests that one should check who last renewed the certificate, before deleting the unused IAM role, even if at first glance it seems attached to nothing."
  app2ko="런북은 쓰이지 않는 IAM 역할을 지우기 전에 그 인증서를 마지막으로 갱신한 사람이 누구인지 확인하라고 말한다 — 언뜻 보기에 아무 데도 붙어 있지 않은 것처럼 보이더라도."
>}}

{{< sentence
  en="However, some complexity is 'intrinsic' as a consequence of the complexity inherent in the problem being solved. This complexity can be moved, but not eliminated."
  ko="그러나 어떤 복잡함은 풀려는 문제 자체에 내재한 복잡함의 결과로서 '본질적'이다. 이 복잡함은 옮길 수는 있어도 없앨 수는 없다."
  source="hacker-laws · The Law of Conservation of Complexity (Tesler's Law)"
  sourceURL="https://github.com/dwmkerr/hacker-laws"
  note="`X can be moved, but not eliminated.` — **없앴다는 착각을 깨는** 한 줄이다. 짧아서 힘이 있다. 앞 문장이 `some complexity is 'intrinsic' as a consequence of ~`로 **왜 없앨 수 없는지**(문제 자체에서 온 것이라서)를 먼저 깔아 주기 때문에, 뒷문장이 단정으로 읽히지 않는다. 같은 골격으로 `absorbed, but not removed`, `deferred, but not avoided`처럼 동사만 갈아 끼우면 된다. 추상화·자동화·리팩터링 제안에 '그래서 이 비용은 어디로 가느냐'를 물을 때 쓴다."
  app1="Some latency is intrinsic as a consequence of the distance between the two regions. This latency can be moved, but not eliminated."
  app1ko="어떤 지연은 두 리전 사이의 거리에서 오는 결과로서 본질적이다. 이 지연은 옮길 수는 있어도 없앨 수는 없다."
  app2="Some review effort is intrinsic as a consequence of the domain knowledge the change requires. This effort can be redistributed, but not eliminated by tooling."
  app2ko="어떤 리뷰 부담은 그 변경이 요구하는 도메인 지식에서 오는 결과로서 본질적이다. 이 부담은 나눠 질 수는 있어도 도구로 없앨 수는 없다."
>}}

{{< sentence
  en="Features that 'surprise' users should be discouraged in favour of features that can be intuitively reasoned about based on existing patterns and practices."
  ko="사용자를 '놀라게' 하는 기능은 지양하고, 기존의 패턴과 관행에 비추어 직관적으로 추론할 수 있는 기능을 택해야 한다."
  source="hacker-laws · The Principle of Least Astonishment"
  sourceURL="https://github.com/dwmkerr/hacker-laws"
  note="`A should be discouraged in favour of B.` — **금지하지 않고 방향만 정하는** 규범 문형이다. `should be banned`나 `must not`이 아니라 `discouraged`라, 예외를 허용하면서도 기본값을 못 박는다. `in favour of B`가 붙어야 완성된다 — 무엇을 하지 말라고만 하면 반발을 사지만, 대체안을 같이 주면 지침이 된다. 컨벤션 문서나 리뷰 가이드에 그대로 넣을 수 있는 골격이고, `'surprise'`처럼 일상어를 따옴표에 넣어 용어로 승격시키는 것도 같이 훔칠 만하다."
  app1="Alerts that fire on causes should be discouraged in favour of alerts that can be traced directly to something a user is currently unable to do."
  app1ko="원인에 대고 울리는 알림은 지양하고, 지금 사용자가 하지 못하는 일로 곧장 추적되는 알림을 택해야 한다."
  app2="Commits that mix a refactor with a behaviour change should be discouraged in favour of commits that can be reverted on their own."
  app2ko="리팩터링과 동작 변경을 섞은 커밋은 지양하고, 단독으로 되돌릴 수 있는 커밋을 택해야 한다."
>}}
