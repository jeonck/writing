---
title: 알림 운영 지침의 표현
description: 원칙을 한 줄로 요약하고, 하지 않아도 되는 이유를 대고, 급하지 않은 위험을 끼워 넣는 문장 5개.
weight: -3
date: 2026-08-23
source: "Prometheus Docs — Alerting"
sourceURL: https://prometheus.io/docs/practices/alerting/
---

# 알림 운영 지침의 표현

무엇에 페이지를 울리고 무엇을 넘길지, 알림 규칙을 세우는 원칙을 정리한 Prometheus 공식 운영 문서.
지침을 쓸 때 필요한 문형 — 여러 원칙을 한 줄로 압축하기, 목표와 그 달성 방법을 한 문장에 붙이기,
**행동하지 않아도 되는 조건**을 명시하기 — 이 고루 들어 있어 발췌했다.

> **원문** — The Prometheus Authors, *Alerting*, [Prometheus Documentation](https://prometheus.io/docs/practices/alerting/)
> ([원본 마크다운](https://github.com/prometheus/docs/blob/main/docs/practices/alerting.md)),
> [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0) 라이선스.
>
> 영어 문장은 원문 그대로 인용했고, 한글 설명과 응용 문장은 이 노트에서 새로 쓴 것이다.

{{< sentence
  en="To summarize: keep alerting simple, alert on symptoms, have good consoles to allow pinpointing causes, and avoid having pages where there is nothing to do."
  ko="요약하면 이렇다. 알림은 단순하게 유지하고, 증상에 대해 알리고, 원인을 짚어낼 수 있는 좋은 콘솔을 갖추고, 할 일이 없는 페이지는 만들지 않는다."
  source="Prometheus Docs · Alerting"
  sourceURL="https://prometheus.io/docs/practices/alerting/"
  note="`To summarize:` 뒤에 **동사원형 명령절을 콤마로 나열**하는 요약 문형이다. 긴 문서를 읽힌 뒤 '결국 이것만 지키면 된다'로 좁힐 때 쓴다. 핵심은 나열된 항목의 **품사를 맞추는 것** — `keep / alert / have / avoid` 넷 다 동사원형이라 한 호흡으로 읽힌다. 마지막 항목만 `avoid`로 부정을 두어 '하지 말 것'을 끝에 배치한 것도 의도적이다. 회의록 맨 위나 설계 문서의 TL;DR에 그대로 옮겨 쓸 수 있다."
  app1="To summarize: keep the runbook short, link the dashboard, name the owner, and avoid steps that require guessing."
  app1ko="요약하면 이렇다. 런북은 짧게 유지하고, 대시보드를 링크하고, 담당자를 명시하고, 추측이 필요한 단계는 만들지 않는다."
  app2="To summarize: log the decision, keep the diff small, review before merge, and avoid changes that cannot be rolled back."
  app2ko="요약하면 이렇다. 결정을 기록하고, 변경은 작게 유지하고, 병합 전에 리뷰하고, 되돌릴 수 없는 변경은 만들지 않는다."
>}}

{{< sentence
  en="Aim to have as few alerts as possible, by alerting on symptoms that are associated with end-user pain rather than trying to catch every possible way that pain could be caused."
  ko="최종 사용자의 고통과 직결된 증상에 대해 알림으로써, 알림 개수를 가능한 한 적게 유지하는 것을 목표로 하라. 그 고통을 일으킬 수 있는 모든 경로를 잡아내려 하지 말고."
  source="Prometheus Docs · Alerting"
  sourceURL="https://prometheus.io/docs/practices/alerting/"
  note="`Aim to X, by doing A rather than doing B` — **목표와 그 달성 방법, 그리고 버려야 할 방법까지** 한 문장에 담는 지침 문형이다. `Aim to`는 `Must`보다 부드러워서 예외를 허용하는 원칙에 어울리고, `by -ing`가 '어떻게'를 붙이며, `rather than -ing`가 흔히 빠지는 오답을 미리 쳐낸다. `as few X as possible`은 '최소화하라'를 수치 없이 말하는 표준 표현. 무엇을 줄이자고 제안할 때, 줄이는 **방법**까지 같은 문장에 넣는 습관을 이 틀로 들일 수 있다."
  app1="Aim to have as few required approvers as possible, by routing reviews to the people who own the code rather than adding everyone who might have an opinion."
  app1ko="코드를 소유한 사람에게 리뷰를 보냄으로써 필수 승인자 수를 가능한 한 적게 유지하는 것을 목표로 하라. 의견이 있을 법한 사람을 전부 넣지 말고."
  app2="Aim to have as few manual steps as possible, by scripting the parts that never change rather than documenting them in more detail."
  app2ko="바뀌지 않는 부분을 스크립트로 만듦으로써 수작업 단계를 가능한 한 적게 유지하는 것을 목표로 하라. 그 단계를 더 자세히 문서화하지 말고."
>}}

{{< sentence
  en="If a lower-level component is slower than it should be, but the overall user latency is fine, then there is no need to page."
  ko="하위 컴포넌트가 마땅한 속도보다 느리더라도 전체 사용자 지연 시간이 괜찮다면, 호출할 필요가 없다."
  source="Prometheus Docs · Alerting"
  sourceURL="https://prometheus.io/docs/practices/alerting/"
  note="`If X, but Y, then there is no need to Z` — **행동하지 않아도 되는 조건**을 명시하는 문형이다. 지침은 보통 '언제 하라'만 적지만, 대응 문서에서 정작 다툼이 나는 지점은 '언제 안 해도 되는가'다. `but` 절이 '나쁜 신호는 맞지만'을 인정하고 들어가므로 문제를 무시한다는 인상을 주지 않는다. `slower than it should be`는 절대 기준 없이 '기대보다 느리다'를 말하는 표현이고, `there is no need to`는 `you should not`보다 약해서 **금지가 아니라 면제**로 읽힌다."
  app1="If a retry is failing but the request eventually succeeds within the SLO, then there is no need to escalate."
  app1ko="재시도가 실패하고 있더라도 요청이 결국 SLO 안에서 성공한다면, 에스컬레이션할 필요가 없다."
  app2="If the finding is real but the affected path is unreachable from the internet, then there is no need to hotfix it this week."
  app2ko="발견된 문제가 실재하더라도 해당 경로가 인터넷에서 도달 불가능하다면, 이번 주에 긴급 패치할 필요가 없다."
>}}

{{< sentence
  en="While not a problem causing immediate user impact, being close to capacity often requires human intervention to avoid an outage in the near future."
  ko="당장 사용자 영향을 일으키는 문제는 아니지만, 용량 한계에 가까워지는 것은 가까운 미래의 장애를 피하기 위해 사람의 개입을 필요로 하는 경우가 많다."
  source="Prometheus Docs · Alerting"
  sourceURL="https://prometheus.io/docs/practices/alerting/"
  note="`While not X, Y` — 주어와 be동사를 생략한 **양보 축약절**이다. `Although it is not a problem that causes...`를 세 단어로 줄인 형태라 지침 문서의 밀도에 맞는다. 이 문형의 쓸모는 '급하지 않은 항목을 그럼에도 목록에 넣는' 자리다: 앞 절에서 심각성을 스스로 낮춰 두고, 뒤 절에서 `often requires`로 다시 끌어올린다. `often`이 없으면 예외 없는 규칙이 되어 반박당하기 쉽다. `to avoid an outage in the near future`처럼 **시점을 붙인 목적구**가 '지금은 아니지만 곧'이라는 온도를 만든다."
  app1="While not a blocker for this release, the missing index will often require a migration before the table grows past a few million rows."
  app1ko="이번 릴리스의 차단 요인은 아니지만, 빠진 인덱스는 테이블이 수백만 행을 넘기 전에 마이그레이션을 요구하는 경우가 많다."
  app2="While not a violation of the current policy, storing the token in the build log often requires a rotation before the next audit."
  app2ko="현재 정책 위반은 아니지만, 빌드 로그에 토큰을 남기는 것은 다음 감사 전에 키 교체를 요구하는 경우가 많다."
>}}

{{< sentence
  en="Supplementing the whitebox monitoring of Prometheus with external blackbox monitoring can catch problems that are otherwise invisible, and also serves as a fallback in case internal systems completely fail."
  ko="Prometheus의 화이트박스 모니터링을 외부 블랙박스 모니터링으로 보완하면 다른 방법으로는 보이지 않는 문제를 잡을 수 있고, 내부 시스템이 완전히 죽는 경우의 대비책 역할도 한다."
  source="Prometheus Docs · Alerting"
  sourceURL="https://prometheus.io/docs/practices/alerting/"
  note="`Supplementing A with B can X, and also serves as Y` — 동명사구를 주어로 세워 **하나의 조치에 이득 두 개를 매다는** 문형이다. 제안을 팔 때 쓴다. `Supplement A with B`는 'A를 버리고 B로 간다'가 아니라 **A는 그대로 두고 B를 덧댄다**는 뜻이라, 기존 체계를 부정하지 않고 추가를 설득할 수 있다. `that are otherwise invisible`의 `otherwise`는 '그렇게 하지 않으면'을 한 단어로 처리하는 장치이고, `serves as a fallback in case ~`는 평소 쓸모가 아니라 **최악의 경우의 쓸모**를 말한다."
  app1="Supplementing the automated checks with a short manual review can catch mistakes that are otherwise invisible, and also serves as a fallback in case the pipeline silently skips a stage."
  app1ko="자동 검사를 짧은 수동 리뷰로 보완하면 다른 방법으로는 보이지 않는 실수를 잡을 수 있고, 파이프라인이 조용히 한 단계를 건너뛰는 경우의 대비책 역할도 한다."
  app2="Supplementing the on-call rotation with a written handover can catch context that is otherwise invisible, and also serves as a fallback in case the previous responder is unreachable."
  app2ko="온콜 로테이션을 문서화된 인수인계로 보완하면 다른 방법으로는 보이지 않는 맥락을 잡을 수 있고, 직전 대응자와 연락이 닿지 않는 경우의 대비책 역할도 한다."
>}}
