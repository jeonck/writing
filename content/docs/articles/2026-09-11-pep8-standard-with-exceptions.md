---
title: 기준을 세우면서 그 한계까지 같이 적는 표현
description: 우선순위를 점층으로 쌓고, 예외 판단을 읽는 사람에게 넘기고, 보장 범위를 좁힌 자리에서 의무를 끌어내고, 되돌리는 비용으로 기본값을 정하는 문장 5개.
weight: -22
date: 2026-09-11
source: "PEP 8 — Style Guide for Python Code"
sourceURL: https://peps.python.org/pep-0008/
---

# 기준을 세우면서 그 한계까지 같이 적는 표현

파이썬의 코딩 표준 문서인 *PEP 8*은 규칙 목록처럼 보이지만, 읽어 보면 **규칙을 제시하는
문장보다 그 규칙이 어디까지 적용되는지 말하는 문장**이 더 인상적이다. 원칙들이 충돌할 때 어느
쪽이 이기는지 미리 적어 두고, 어길 때를 판별할 책임을 읽는 사람에게 넘기고, 보장의 범위를
좁히는 동시에 그 경계를 알아볼 수 있게 만드는 것을 자기 의무로 받고, 판단이 서지 않을 때
무엇을 고를지를 되돌리는 비용으로 정당화한다. 코딩 표준 제안서, 코드 리뷰 코멘트, 온콜 수칙,
지원 범위 고지처럼 **내가 만든 기준을 남이 지키게 해야 하는 글**에 그대로 옮겨 쓸 다섯 문장을
골랐다.

> **원문** — Guido van Rossum, Barry Warsaw, Alyssa Coghlan, *PEP 8 – Style Guide for Python
> Code*, [peps.python.org](https://peps.python.org/pep-0008/) (2001-07-05 최초 공개, 현재도
> Active 상태), 문서가 직접 선언한 **Public Domain**
> ([원본 reStructuredText](https://github.com/python/peps/blob/main/peps/pep-0008.rst) —
> Copyright 절: This document has been placed in the public domain.).
>
> 영어 문장은 원문 그대로 인용했고, 한글 설명과 응용 문장은 이 노트에서 새로 쓴 것이다.

{{< sentence
  en="A style guide is about consistency. Consistency with this style guide is important. Consistency within a project is more important. Consistency within one module or function is the most important."
  ko="스타일 가이드는 일관성에 관한 것이다. 이 스타일 가이드와의 일관성은 중요하다. 한 프로젝트 안에서의 일관성은 더 중요하다. 한 모듈이나 함수 안에서의 일관성은 가장 중요하다."
  source="PEP 8 · A Foolish Consistency is the Hobgoblin of Little Minds"
  sourceURL="https://peps.python.org/pep-0008/#a-foolish-consistency-is-the-hobgoblin-of-little-minds"
  note="`A is important. B is more important. C is the most important.` — 같은 골격의 문장을 세 번 반복하면서 형용사만 한 칸씩 올리는 점층 사다리다. 구조가 똑같기 때문에 **범위가 좁아질수록 우선순위가 올라간다**는 규칙을 따로 설명하지 않아도 읽는 사람이 스스로 읽어 낸다. 순서가 생명이어서 가장 중요한 것을 맨 뒤에 둬야 하고, 항목마다 비교급·최상급만 갈아 끼우면 되므로 넷, 다섯으로 늘려도 문형이 버틴다. 원칙 여러 개가 충돌할 때 무엇이 이기는지 **미리** 적어 두는 문서(코딩 표준, 리뷰 기준, 온콜 수칙)에 그대로 쓴다."
  app1="Consistency with the language style guide is important. Consistency within this repository is more important. Consistency within the file you are editing is the most important."
  app1ko="언어의 스타일 가이드와의 일관성은 중요하다. 이 리포지터리 안에서의 일관성은 더 중요하다. 지금 고치고 있는 파일 안에서의 일관성은 가장 중요하다."
  app2="Following the org-wide on-call policy is important. Following your service's runbook is more important. Following the instruction in the alert you were paged for is the most important."
  app2ko="조직 공통 온콜 정책을 따르는 것은 중요하다. 담당 서비스의 런북을 따르는 것은 더 중요하다. 지금 호출된 그 알림에 적힌 지시를 따르는 것은 가장 중요하다."
>}}

{{< sentence
  en="However, know when to be inconsistent -- sometimes style guide recommendations just aren't applicable."
  ko="하지만, 언제 일관성을 깨야 하는지도 알아라 — 스타일 가이드의 권고가 그냥 적용되지 않는 경우도 있다."
  source="PEP 8 · A Foolish Consistency is the Hobgoblin of Little Minds"
  sourceURL="https://peps.python.org/pep-0008/#a-foolish-consistency-is-the-hobgoblin-of-little-minds"
  note="`know when to be <규칙과 반대되는 상태> -- sometimes X just aren't applicable.` — 규칙을 쓴 사람이 같은 문서 안에서 **예외 판단을 읽는 사람에게 넘기는** 문형이다. 명령형 `know when to ~`가 핵심인데, '어겨도 된다'는 허락이 아니라 **'어길 때를 판별할 책임을 져라'** 는 요구라서 규칙의 권위를 깎지 않고도 예외가 열린다. 톤을 정하는 단어는 `just`다 — 권고가 '그냥' 맞지 않는 경우가 있다고 말해 두면, 예외를 쓸 때마다 정당화 문서를 받아 내지는 않겠다는 신호가 된다. 체크리스트·코딩 표준·리뷰 기준을 배포할 때 맨 앞이나 맨 뒤에 한 줄로 붙이기 좋다."
  app1="Follow the runbook, but know when to deviate -- sometimes the steps just aren't applicable to the failure in front of you."
  app1ko="런북을 따르되, 언제 벗어나야 하는지도 알아라 — 눈앞의 장애에는 그 단계들이 그냥 맞지 않는 경우도 있다."
  app2="Know when to approve anyway -- sometimes a checklist item just isn't applicable to the change under review."
  app2ko="그래도 승인할 때를 알아라 — 지금 보고 있는 변경에는 체크리스트 항목 하나가 그냥 해당되지 않는 경우도 있다."
>}}

{{< sentence
  en="Any backwards compatibility guarantees apply only to public interfaces. Accordingly, it is important that users be able to clearly distinguish between public and internal interfaces."
  ko="어떤 하위 호환성 보장이든 공개 인터페이스에만 적용된다. 따라서 사용자가 공개 인터페이스와 내부 인터페이스를 분명히 구별할 수 있어야 한다는 점이 중요하다."
  source="PEP 8 · Public and Internal Interfaces"
  sourceURL="https://peps.python.org/pep-0008/#public-and-internal-interfaces"
  note="`Any X guarantees apply only to Y. Accordingly, it is important that users be able to clearly distinguish between Y and Z.` — 두 문장이 한 덩어리로 움직인다. 앞은 보장의 **범위를 좁히고**(`apply only to`), 뒤는 그 좁힘에서 곧바로 **내 쪽 의무를 끌어낸다**(`Accordingly`). 범위만 좁혀 놓으면 책임 회피로 읽히는데, 경계를 알아볼 수 있게 만드는 일이 내 몫이라고 이어 붙이기 때문에 그렇게 읽히지 않는다. `Any ~ guarantees`의 `Any`가 '어떤 보장이든 예외 없이'로 빠져나갈 틈을 막고, `be able to`는 결과가 아니라 **가능성**을 요구한다 — 사용자가 실제로 구별했는지가 아니라 구별할 수 있게 해 두었는지가 기준이다. 지원 범위 고지, API 버전 정책, 내부 도구의 공개 경계를 적을 때 그대로 쓴다."
  app1="Our uptime commitment applies only to the endpoints listed in this document. Accordingly, it is important that callers be able to clearly distinguish between supported and best-effort endpoints."
  app1ko="우리의 가동률 약속은 이 문서에 적힌 엔드포인트에만 적용된다. 따라서 호출하는 쪽이 지원 대상 엔드포인트와 최선 노력 엔드포인트를 분명히 구별할 수 있어야 한다는 점이 중요하다."
  app2="Any sign-off from this audit applies only to the configuration we reviewed. Accordingly, it is important that the team be able to clearly distinguish between the audited setup and every change made after it."
  app2ko="이번 감사의 승인은 우리가 검토한 구성에만 적용된다. 따라서 팀이 감사를 받은 설정과 그 뒤에 이루어진 모든 변경을 분명히 구별할 수 있어야 한다는 점이 중요하다."
>}}

{{< sentence
  en="Always decide whether a class's methods and instance variables (collectively: &quot;attributes&quot;) should be public or non-public. If in doubt, choose non-public; it's easier to make it public later than to make a public attribute non-public."
  ko="클래스의 메서드와 인스턴스 변수(묶어서 '속성')를 공개할지 비공개로 둘지를 항상 결정하라. 판단이 서지 않으면 비공개를 골라라. 나중에 공개로 바꾸는 것이, 이미 공개된 속성을 비공개로 되돌리는 것보다 쉽다."
  source="PEP 8 · Designing for Inheritance"
  sourceURL="https://peps.python.org/pep-0008/#designing-for-inheritance"
  note="`If in doubt, choose X; it's easier to A later than to B.` — 기본값을 취향이나 권위가 아니라 **되돌리는 비용의 비대칭**으로 정당화하는 문형이다. 어느 쪽이 옳은지는 아예 다투지 않는다 — `If in doubt`가 모른다고 먼저 인정해 버리고, 대신 틀렸을 때 어느 실수가 싼지만 비교한다. 그래서 상대의 판단력을 부정하지 않고도 기본값에 합의할 수 있다. 세미콜론 뒤 절 전체가 근거이고, `easier ... later than to ...`가 시간축을 끌어들여 '지금 편한 쪽'과 '나중에 싼 쪽'을 갈라 놓는다. 한번 열면 닫기 어려운 결정(권한 부여, 공개 API 노출, 기능 플래그 기본값)을 설득할 때 그대로 쓴다."
  app1="If in doubt, keep the endpoint internal; it's easier to expose it later than to take a public endpoint away from callers who already depend on it."
  app1ko="판단이 서지 않으면 그 엔드포인트를 내부용으로 두어라. 나중에 공개하는 것이, 이미 그것에 의존하고 있는 호출자들에게서 공개 엔드포인트를 거두는 것보다 쉽다."
  app2="If in doubt, grant read-only; it's easier to add write access later than to take write access back from a team that has already built a workflow on it."
  app2ko="판단이 서지 않으면 읽기 권한만 부여하라. 나중에 쓰기 권한을 더하는 것이, 이미 그 권한으로 업무 흐름을 만들어 둔 팀에게서 쓰기 권한을 거두는 것보다 쉽다."
>}}

{{< sentence
  en="Avoid using properties for computationally expensive operations; the attribute notation makes the caller believe that access is (relatively) cheap."
  ko="계산 비용이 큰 연산에는 프로퍼티를 쓰지 마라. 속성 표기법은 호출하는 쪽에게 그 접근이 (비교적) 싸다고 믿게 만든다."
  source="PEP 8 · Designing for Inheritance"
  sourceURL="https://peps.python.org/pep-0008/#designing-for-inheritance"
  note="`Avoid X; the Y makes the caller believe that Z.` — 금지의 근거를 성능 수치가 아니라 **표기가 만들어 내는 오해**에 두는 문형이다. 주어가 사람이 아니라 `the attribute notation`이라서, 호출하는 쪽이 부주의하다는 말을 하지 않고도 '설계가 잘못된 신호를 보낸다'고 지적할 수 있다. `makes the caller believe`는 '오해를 일으킬 수 있다'보다 세다 — 가능성이 아니라 **기본적으로 그렇게 읽힌다**는 뜻이라, 문서에 주석 한 줄 달아 두자는 타협을 막는다. 괄호 속 `(relatively)`는 단정을 한 칸 낮추는 장치다. 인터페이스가 비용이나 위험을 숨기고 있을 때(필드처럼 보이는 네트워크 호출, 안전해 보이는 이름의 재시도 플래그) 코드 리뷰 코멘트에 그대로 쓴다."
  app1="Avoid putting a remote lookup behind a plain getter; the field access makes the caller believe that no network is involved."
  app1ko="원격 조회를 평범한 getter 뒤에 숨기지 마라. 필드에 접근하는 모양새는 호출하는 쪽에게 네트워크가 끼어들지 않는다고 믿게 만든다."
  app2="Avoid naming the retry flag safe_retry; the name makes the caller believe that a second attempt cannot charge the customer twice."
  app2ko="재시도 플래그에 safe_retry라는 이름을 붙이지 마라. 그 이름은 호출하는 쪽에게 두 번째 시도가 고객에게 두 번 청구할 수는 없다고 믿게 만든다."
>}}
