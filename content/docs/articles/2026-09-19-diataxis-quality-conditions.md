---
title: 조건을 다 채웠는데도 부족하다고 말하는 표현
description: 항목끼리 서로를 보증하지 않는다고 못 박고, 요구 수준을 정의로 환산하고, 필요조건과 충분조건을 한 문장에 담고, 자기 방법론이 못 하는 일을 자기 입으로 긋고, 상대의 평가를 근거에서 빼는 문장 5개.
weight: -30
date: 2026-09-19
source: "Diátaxis — Towards a theory of quality in documentation"
sourceURL: https://diataxis.fr/quality/
---

# 조건을 다 채웠는데도 부족하다고 말하는 표현

문서화 프레임워크 Diátaxis의 *Towards a theory of quality in documentation* 장은 **품질이라는
말을 둘로 쪼개는** 글이다. 측정할 수 있는 쪽(정확성, 완전성, 일관성)을 기능적 품질로 부르고,
측정할 수 없지만 알아볼 수는 있는 쪽(흐름, 사용자를 앞질러 준비해 둔 느낌)을 깊은 품질로
부른다. 이 글이 문장 공부에 쓸모 있는 이유는 주제가 문서라서가 아니라, **체크리스트를 다
통과한 결과물을 앞에 두고 그래도 부족하다고 말해야 하는 상황**을 계속 다루기 때문이다. 코드
리뷰, 장애 회고, 보안 감사, 도구 도입 논의에서 가장 말하기 어려운 자리가 정확히 거기다 —
기준은 다 충족했는데 목적은 이루지 못했다고, 트집으로 들리지 않게 말해야 하는 자리. 그런
말을 성립시키는 다섯 문장을 골랐다.

> **원문** — Daniele Procida, *Towards a theory of quality in documentation*,
> [Diátaxis](https://diataxis.fr/quality/)
> (원본: [`evildmp/diataxis-documentation-framework` · `source/quality.rst`](https://github.com/evildmp/diataxis-documentation-framework/blob/main/source/quality.rst)),
> [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).
> Copyright Daniele Procida.
>
> 영어 문장은 원문 그대로 인용했고, 한글 설명과 응용 문장은 이 노트에서 새로 쓴 것이다.

{{< sentence
  en="Documentation can be accurate without being complete. It can be complete, but inaccurate and inconsistent. It can be accurate, complete, consistent and also useless."
  ko="문서는 완전하지 않으면서도 정확할 수 있다. 완전하되 부정확하고 일관되지 않을 수도 있다. 정확하고 완전하고 일관되면서 동시에 쓸모없을 수도 있다."
  source="Diátaxis · Functional quality"
  sourceURL="https://diataxis.fr/quality/"
  note="`X can be A without being B. It can be B, but not A and not C. It can be A, B, C and also useless.` — 항목들이 서로를 보증하지 않는다는 말을 세 번 고쳐 쓰면서 못 박는 문형이다. 한 번만 말하면 반례로 들리지만, 조합을 바꿔 세 번 늘어놓으면 **이 목록의 성질**에 대한 진술이 된다. 진짜 장치는 마지막 문장의 `and also useless`다. 앞의 세 기준을 모두 통과한 상태를 먼저 인정해 준 다음 그 위에 얹기 때문에, 부정이 아니라 관찰로 읽힌다. 순서를 뒤집어 쓸모없으면 소용없다고 먼저 말했다면 같은 내용이 트집이 된다. 접속사도 일을 나눠 맡는다 — `but`은 같은 층위의 항목끼리 어긋남을 표시하고, `and also`는 층위를 한 칸 올려 목적 자체를 꺼낸다. 체크리스트를 다 통과한 산출물을 앞에 두고 그래도 목적을 못 이뤘다고 말해야 할 때 쓴다."
  app1="A runbook can be current without being executable. It can be executable, but untested and ambiguous. It can be current, executable, unambiguous and also useless at three in the morning."
  app1ko="런북은 실행 가능하지 않으면서도 최신일 수 있다. 실행 가능하되 검증되지 않고 모호할 수도 있다. 최신이고 실행 가능하고 모호하지 않으면서 동시에 새벽 세 시에는 쓸모없을 수도 있다."
  app2="An alert can be accurate without being actionable. It can be actionable, but late and noisy. It can be accurate, timely, actionable and also ignored."
  app2ko="알림은 대응 가능하지 않으면서도 정확할 수 있다. 대응 가능하되 늦고 시끄러울 수도 있다. 정확하고 제때 오고 대응 가능하면서 동시에 무시당할 수도 있다."
>}}

{{< sentence
  en="Attaining functional quality means meeting high, objectively-measurable standards in multiple independent dimensions, consistently. It requires discipline and attention to detail, and high levels of technical skill."
  ko="기능적 품질에 도달한다는 것은 서로 독립적인 여러 차원에서 높고 객관적으로 측정 가능한 기준을 일관되게 충족한다는 뜻이다. 그것은 규율과 세부에 대한 주의, 그리고 높은 수준의 기술적 숙련을 요구한다."
  source="Diátaxis · Functional quality"
  sourceURL="https://diataxis.fr/quality/"
  note="`Attaining X means meeting high, objectively-measurable standards in multiple independent dimensions, consistently.` — 구호로 떠다니는 목표를 **정의로 환산하는** 문형이다. `means`가 하는 일이 핵심이다. 목표를 칭찬 대상에서 조건 목록으로 옮겨 놓아서, 이제부터 그 목표를 말하는 사람은 조건을 말해야 한다. 수식어 셋이 각각 다른 도망길을 막는 것도 눈여겨볼 만하다 — `objectively-measurable`은 자기 평가로 때우는 길, `multiple independent dimensions`는 한 항목을 잘해서 다른 항목을 상쇄하는 길, 문장 맨 끝에 쉼표로 떼어 놓은 `consistently`는 한 번 잘하고 끝내는 길. 마지막 단어를 굳이 분리해 둔 자리 자체가 강조다. 두 번째 문장은 곧바로 **대가**를 붙인다. 요구 수준만 적고 멈추면 그러면 그냥 하면 되지 않느냐는 반응이 돌아오는데, 필요한 것이 의지가 아니라 규율·주의·숙련이라고 적어 두면 그 반응이 닫힌다. 팀 기준을 문서로 굳힐 때, 준비됨의 정의를 합의할 때 쓴다."
  app1="Attaining production readiness means meeting high, objectively-measurable standards in multiple independent dimensions, consistently. It requires named ownership, rehearsed failure, and high levels of operational discipline."
  app1ko="운영 준비 상태에 도달한다는 것은 서로 독립적인 여러 차원에서 높고 객관적으로 측정 가능한 기준을 일관되게 충족한다는 뜻이다. 그것은 이름이 붙은 담당자, 미리 연습해 본 장애, 그리고 높은 수준의 운영 규율을 요구한다."
  app2="Attaining audit readiness means meeting high, objectively-measurable standards in multiple independent dimensions, consistently. It requires evidence collected as we go, and high levels of agreement on what counts as proof."
  app2ko="감사 준비 상태에 도달한다는 것은 서로 독립적인 여러 차원에서 높고 객관적으로 측정 가능한 기준을 일관되게 충족한다는 뜻이다. 그것은 진행하면서 그때그때 모아 둔 증거, 그리고 무엇을 증거로 칠지에 대한 높은 수준의 합의를 요구한다."
>}}

{{< sentence
  en="Documentation can be accurate and complete and consistent without being truly excellent - but it will never have deep quality without being accurate and complete and consistent."
  ko="문서는 진정으로 탁월하지 않으면서도 정확하고 완전하고 일관될 수 있다. 그러나 정확하고 완전하고 일관되지 않고서는 결코 깊은 품질을 갖지 못한다."
  source="Diátaxis · What's the difference?"
  sourceURL="https://diataxis.fr/quality/"
  note="`X can be A and B and C without being D - but it will never be D without being A and B and C.` — 필요조건과 충분조건을 한 문장에 나란히 놓는 문형이다. 장치는 같은 목록(`accurate and complete and consistent`)을 **줄이지 않고 그대로 뒤에 다시 쓰는** 데 있다. 대명사나 요약어로 받으면 두 주장이 서로 다른 얘기처럼 보이는데, 통째로 반복하면 하나의 대상을 두고 방향만 뒤집었다는 것이 눈으로 보인다. `and`를 세 번 반복한 것도 의도된 리듬이다 — 쉼표로 묶으면 한 덩어리로 읽히지만, `and`로 이으면 항목이 하나씩 얹히면서 각각이 따로 요구된다는 느낌이 남는다. 뒤 절의 `never ... without`은 이중 부정이라 예외를 허용하지 않는다. 기본을 지키라는 요구가 형식주의라고 반박당할 때 쓴다: 기본이 목표가 아님을 먼저 인정해 주고, 그다음 기본 없이는 목표에 닿지 못한다고 닫는 순서다."
  app1="A change can be small and tested and documented without being a good change - but it will never be a good change without being small and tested and documented."
  app1ko="변경은 좋은 변경이 아니면서도 작고 테스트되고 문서화될 수 있다. 그러나 작고 테스트되고 문서화되지 않고서는 결코 좋은 변경이 되지 못한다."
  app2="An incident review can be prompt and detailed and blameless without changing anything - but it will never change anything without being prompt and detailed and blameless."
  app2ko="장애 회고는 아무것도 바꾸지 못하면서도 신속하고 상세하고 책임을 묻지 않는 방식일 수 있다. 그러나 신속하고 상세하고 책임을 묻지 않는 방식이 아니고서는 결코 아무것도 바꾸지 못한다."
>}}

{{< sentence
  en="Diátaxis offers a set of principles - it doesn't offer a formula. It certainly cannot offer a short-cut to success, bypassing the skills and insights of disciplines such as user experience or user interaction design, or even visual design."
  ko="Diátaxis는 원칙의 묶음을 제공한다. 공식을 제공하지는 않는다. 사용자 경험이나 사용자 인터랙션 디자인, 심지어 시각 디자인 같은 분야의 기술과 통찰을 건너뛴 채 성공으로 가는 지름길을 제공하는 일은 분명히 할 수 없다."
  source="Diátaxis · Understanding the limits"
  sourceURL="https://diataxis.fr/quality/"
  note="`X offers A - it doesn't offer B. It certainly cannot offer a short-cut to C, bypassing the skills and insights of disciplines such as D or E.` — 자기가 내놓은 물건의 한계를 **자기 입으로 긋는** 문형이다. 대시 하나를 사이에 두고 준 것과 주지 않은 것을 붙여 놓아서, 기대가 자라기 전에 그 자리에서 잘린다. `certainly`는 강조가 아니라 **양보의 거부**로 일한다 — 그래도 잘 쓰면 되지 않느냐는 예외 요청을 미리 닫는다. 이 문장을 겸손이 아니라 경계 설정으로 만드는 것은 마지막의 `bypassing` 분사구다. 못 하는 일을 그냥 지름길이 아니라 **무엇을 건너뛴 지름길**로 정의하기 때문에, 읽는 사람은 여전히 자기가 해야 할 몫이 무엇인지 목록으로 받게 된다. 도구 도입을 제안할 때, 자동화의 사정거리를 공지할 때, 이걸 넣으면 그 문제가 해결되느냐는 질문에 답할 때 쓴다."
  app1="The linter offers a set of guardrails - it doesn't offer a verdict. It certainly cannot offer a short-cut to a reviewed change, bypassing the skills and judgement of someone who knows what the code is for."
  app1ko="린터는 가드레일의 묶음을 제공한다. 판정을 제공하지는 않는다. 그 코드가 무엇을 위한 것인지 아는 사람의 기술과 판단을 건너뛴 채 리뷰를 마친 변경으로 가는 지름길을 제공하는 일은 분명히 할 수 없다."
  app2="The scanner offers a set of signals - it doesn't offer assurance. It certainly cannot offer a short-cut to a security sign-off, bypassing the skills and insights of work such as threat modelling or manual review."
  app2ko="스캐너는 신호의 묶음을 제공한다. 보증을 제공하지는 않는다. 위협 모델링이나 수동 검토 같은 작업의 기술과 통찰을 건너뛴 채 보안 승인으로 가는 지름길을 제공하는 일은 분명히 할 수 없다."
>}}

{{< sentence
  en="The users of our documentation may or may not have the understanding to say why it's good, or where its quality lapses. They might recognise only the more obvious aspects of functional quality in it, mistaking those for its deeper excellence."
  ko="우리 문서의 사용자들은 그것이 왜 좋은지, 또는 품질이 어디서 무너지는지 말할 만한 이해를 가지고 있을 수도 있고 아닐 수도 있다. 그들은 문서에서 기능적 품질의 더 눈에 띄는 측면만 알아보고, 그것을 더 깊은 탁월함으로 착각할 수도 있다."
  source="Diátaxis · How we recognise deep quality"
  sourceURL="https://diataxis.fr/quality/"
  note="`X may or may not have the understanding to say why A, or where B. They might recognise only C, mistaking those for D.` — 상대의 판단력을 깎지 않으면서 **상대의 평가를 근거에서 빼는** 문형이다. `may or may not`은 얼버무림처럼 보이지만 기능은 반대다. 아는지 모르는지를 확정하지 않음으로써 그 질문 자체를 논점에서 들어내고, 그래서 이 문장은 사용자를 평가하지 않는다. 뒤 문장은 오해의 **방향**까지 특정한다 — 아무것도 못 본다가 아니라 `recognise only`, 즉 보이는 것은 정확히 보되 그것을 전부로 여긴다는 것이다. `mistaking those for`라는 분사구는 그 착각을 사람의 잘못이 아니라 상황의 구조로 돌려 놓는다. 만족도 점수는 높은데 실제 품질이 나쁠 때, 대시보드는 초록인데 사용자 경험은 나쁠 때, 승인 개수를 품질의 근거로 들이밀 때 꺼내 쓴다."
  app1="The people who approve our changes may or may not have the context to say why a design holds, or where it will break first. They might recognise only the checks that went green on the diff, mistaking those for evidence that the change is safe."
  app1ko="우리 변경을 승인하는 사람들은 그 설계가 왜 버티는지, 또는 어디서 먼저 깨질지 말할 만한 맥락을 가지고 있을 수도 있고 아닐 수도 있다. 그들은 그 디프에서 초록으로 바뀐 검사만 알아보고, 그것을 변경이 안전하다는 증거로 착각할 수도 있다."
  app2="Our stakeholders may or may not have the background to say why the incident happened, or where the risk still sits. They might recognise only the graphs that came back to normal, mistaking those for a resolved root cause."
  app2ko="우리 이해관계자들은 그 장애가 왜 일어났는지, 또는 위험이 아직 어디에 남아 있는지 말할 만한 배경지식을 가지고 있을 수도 있고 아닐 수도 있다. 그들은 정상으로 돌아온 그래프만 알아보고, 그것을 원인이 해결되었다는 뜻으로 착각할 수도 있다."
>}}
