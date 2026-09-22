---
title: 위험의 크기를 재서 적는 표현
description: 일반론을 대표 사례로 좁히고, 기능을 위험으로 다시 정의하고, 위협의 한계를 긋고, 옳은 권고에 현실을 덧붙이고, 보장 수준을 미리 낮춰 두는 문장 5개.
weight: -33
date: 2026-09-23
source: "Hugging Face Hub Docs — Pickle Scanning"
sourceURL: https://huggingface.co/docs/hub/security-pickle
---

# 위험의 크기를 재서 적는 표현

허깅페이스 Hub 문서의 *Pickle Scanning*은 파이썬 pickle 형식이 왜 임의 코드 실행으로
이어지는지, 그리고 Hub의 보안 스캐너가 무엇을 잡고 무엇을 못 잡는지를 설명한다. 위험을
겁주지도 축소하지도 않고 **크기를 재서 적는** 문장이 많아 발췌했다 — 보안 감사 결과나
장애 리포트를 쓸 때 그대로 가져다 쓸 수 있는 틀이다.

> **원문** — Hugging Face, *Pickle Scanning*,
> [huggingface.co/docs/hub/security-pickle](https://huggingface.co/docs/hub/security-pickle),
> [Apache-2.0](https://www.apache.org/licenses/LICENSE-2.0) 라이선스.
> 원본 마크다운은 [huggingface/hub-docs](https://github.com/huggingface/hub-docs/blob/main/docs/hub/security-pickle.md).
>
> 영어 문장은 원문 그대로 인용했고, 한글 설명과 응용 문장은 이 노트에서 새로 쓴 것이다.

{{< sentence
  en="Pickle is a widely used serialization format in ML. Most notably, it is the default format for PyTorch model weights."
  ko="pickle은 머신러닝에서 널리 쓰이는 직렬화 형식이다. 무엇보다도, 파이토치 모델 가중치의 기본 형식이다."
  source="Pickle Scanning · 도입부"
  sourceURL="https://huggingface.co/docs/hub/security-pickle"
  note="`X is a widely used A. Most notably, it is the default B.` — 넓은 진술을 먼저 놓고 **가장 아픈 사례 하나로 좁히는** 두 문장 짝이다. 첫 문장만 있으면 '많이 쓰인다' 정도로 흘러가지만, `Most notably`가 뒤따르면서 범위가 급히 좁아지고 독자는 '그럼 내 얘기네'로 넘어간다. 힘은 `default`에 있다 — 누가 고른 게 아니라 **아무도 고르지 않았을 때 그렇게 된다**는 뜻이라, 뒤에 이어질 위험 설명이 '일부 사용자'가 아니라 전부에게 걸린다. 영향 범위를 산정해 보고할 때 첫 두 줄로 쓴다."
  app1="Shared service accounts are a widely used shortcut in our deploy scripts. Most notably, they are the default path for anything that touches the staging database."
  app1ko="공용 서비스 계정은 우리 배포 스크립트에서 널리 쓰이는 지름길이다. 무엇보다도, 스테이징 데이터베이스를 건드리는 모든 작업의 기본 경로다."
  app2="Retries are a widely used remedy for flaky upstream calls. Most notably, they are the default behavior of every client we ship."
  app2ko="재시도는 불안정한 상위 호출에 널리 쓰이는 처방이다. 무엇보다도, 우리가 배포하는 모든 클라이언트의 기본 동작이다."
>}}

{{< sentence
  en="Pickle is not simply a serialization protocol, it allows more flexibility by giving the ability to users to run python code at de-serialization time."
  ko="pickle은 단순한 직렬화 프로토콜이 아니다. 역직렬화 시점에 사용자가 파이썬 코드를 실행할 수 있게 해 주어 더 많은 유연성을 허용한다."
  source="Pickle Scanning · What is a pickle?"
  sourceURL="https://huggingface.co/docs/hub/security-pickle"
  note="`X is not simply A, it allows more flexibility by giving the ability to users to B.` — **기능을 칭찬하는 문장 형태 그대로 위험을 고발하는** 문형이다. `not simply A`로 상대가 갖고 있던 정의를 먼저 깨고, 그 자리에 `more flexibility`라는 좋은 말을 넣는다. 그런데 뒤에 붙은 `to run python code at de-serialization time`이 그 유연성의 정체를 밝히면서 칭찬이 그대로 경고로 뒤집힌다. 비난하는 단어를 하나도 쓰지 않고 위험을 전달하기 때문에, 그 기능을 만든 사람 앞에서도 쓸 수 있다. 감사 보고서에서 설정 하나가 왜 문제인지 적을 때 특히 잘 듣는다."
  app1="The admin token is not simply a deploy credential, it allows more flexibility by giving the ability to any workflow to rewrite branch protection rules."
  app1ko="그 관리자 토큰은 단순한 배포 자격 증명이 아니다. 어떤 워크플로든 브랜치 보호 규칙을 다시 쓸 수 있게 해 주어 더 많은 유연성을 허용한다."
  app2="A feature flag is not simply a switch, it allows more flexibility by giving the ability to on-call engineers to change production behavior without a review."
  app2ko="피처 플래그는 단순한 스위치가 아니다. 온콜 엔지니어가 리뷰 없이 운영 동작을 바꿀 수 있게 해 주어 더 많은 유연성을 허용한다."
>}}

{{< sentence
  en="As we've stated above, de-serializing pickle means that code can be executed. But this comes with certain limitations: you can only reference functions and classes from the top level module; you cannot embed them in the pickle file itself."
  ko="위에서 말했듯 pickle을 역직렬화한다는 것은 코드가 실행될 수 있다는 뜻이다. 다만 여기에는 몇 가지 제약이 따른다. 최상위 모듈의 함수와 클래스를 참조할 수만 있고, 그것들을 pickle 파일 안에 담아 넣을 수는 없다."
  source="Pickle Scanning · Why is it dangerous?"
  sourceURL="https://huggingface.co/docs/hub/security-pickle"
  note="`But this comes with certain limitations: you can only X; you cannot Y.` — 위험을 말한 **바로 다음 문장에서 그 위험의 경계를 스스로 긋는** 문형이다. 콜론 뒤를 `can only` / `cannot` 한 쌍으로 짜는 것이 핵심이다. 할 수 있는 것을 먼저 좁혀 놓고, 할 수 없는 것을 세미콜론 뒤에 붙여 반대쪽 벽을 세운다. 이렇게 두 벽을 같이 보여 주면 읽는 사람이 위험을 과대평가하지도 무시하지도 못한다. `certain limitations`의 `certain`은 '확실한'이 아니라 **'몇 가지 정해진'**이라는 뜻이라, 제약이 임시방편이 아니라 구조에서 나온다는 인상을 준다. 취약점의 실제 영향 범위를 보고할 때 이 짝을 쓰면 '그래서 얼마나 위험한 건데'라는 되물음이 줄어든다."
  app1="Leaking this key means that the bucket can be read by anyone who finds it. But this comes with certain limitations: you can only list the prefixes the key was scoped to; you cannot write objects or delete anything already there."
  app1ko="이 키가 유출됐다는 것은 그것을 손에 넣은 누구든 버킷을 읽을 수 있다는 뜻이다. 다만 여기에는 몇 가지 제약이 따른다. 키에 허용된 경로만 나열할 수 있을 뿐, 객체를 쓰거나 이미 있는 것을 지울 수는 없다."
  app2="A stolen session cookie means that the account can be impersonated. But this comes with certain limitations: you can only act within one region; you cannot change the password or register a new MFA device."
  app2ko="세션 쿠키를 빼앗겼다는 것은 그 계정을 사칭할 수 있다는 뜻이다. 다만 여기에는 몇 가지 제약이 따른다. 한 리전 안에서만 행동할 수 있을 뿐, 비밀번호를 바꾸거나 새 MFA 기기를 등록할 수는 없다."
>}}

{{< sentence
  en="Sound advice Luc, but pickle is used profusely and isn't going anywhere soon: finding a new format everyone is happy with and initiating the change will take some time."
  ko="좋은 지적이야 뤽, 그런데 pickle은 워낙 많이 쓰이고 있어서 금방 사라지지 않는다. 모두가 만족할 새 형식을 찾고 그 전환을 시작하는 데는 시간이 걸린다."
  source="Pickle Scanning · Mitigation Strategies"
  sourceURL="https://huggingface.co/docs/hub/security-pickle"
  note="`Sound advice, but X is used profusely and isn't going anywhere soon: Y and Z will take some time.` — 앞에서 자기가 내놓은 정답(&quot;pickle을 쓰지 마라&quot;)을 **스스로 받아치는** 문형이다. `Sound advice`로 그 조언이 틀렸다고 말하지 않고 먼저 인정해 버리기 때문에, 뒤에 오는 반론이 변명이 아니라 현실 보고가 된다. `isn't going anywhere soon`은 '없앨 수 없다'가 아니라 **당분간은 그대로 있다**는 시간 표현이라 포기 선언으로 읽히지 않는다. 콜론 뒤에서 남은 일을 동명사로 나열해 '시간이 걸린다'의 근거를 붙이는 것까지가 한 세트다. 리뷰에서 받은 옳은 지적을 이번 PR에서는 못 고칠 때 그대로 쓸 수 있다."
  app1="Sound advice, but the legacy scheduler is used profusely and isn't going anywhere soon: finding a replacement everyone is happy with and migrating the jobs will take some time."
  app1ko="좋은 지적입니다. 그런데 예전 스케줄러는 워낙 많이 쓰이고 있어서 금방 사라지지 않습니다. 모두가 만족할 대체재를 찾고 작업들을 옮기는 데는 시간이 걸립니다."
  app2="Sound advice, but this helper is used profusely across the codebase and isn't going anywhere soon: agreeing on a new interface and updating the call sites will take some time."
  app2ko="좋은 지적입니다. 그런데 이 헬퍼는 코드베이스 전반에서 워낙 많이 쓰이고 있어서 금방 사라지지 않습니다. 새 인터페이스에 합의하고 호출부를 고치는 데는 시간이 걸립니다."
>}}

{{< sentence
  en="It is your responsibility as a user to check if something is safe or not. We are not actively auditing python packages for safety, the safe/unsafe imports lists we have are maintained in a best-effort manner."
  ko="무언가가 안전한지 아닌지 확인하는 것은 사용자인 당신의 책임이다. 우리는 파이썬 패키지의 안전성을 능동적으로 감사하지 않으며, 우리가 가진 안전/위험 임포트 목록은 최선을 다하는 수준으로 관리된다."
  source="Pickle Scanning · Hub's Security Scanner"
  sourceURL="https://huggingface.co/docs/hub/security-pickle"
  note="`It is your responsibility as a user to X. We are not actively Y, the Z we have are maintained in a best-effort manner.` — 도구를 제공하면서 **그 도구가 대신해 주지 않는 것을 같은 자리에서 못 박는** 문형이다. 순서가 중요하다. 책임을 먼저 상대에게 놓고(`It is your responsibility as a user`), 그다음에야 자기 쪽이 하지 않는 일을 `We are not actively ~`로 밝힌다. 거꾸로 쓰면 발뺌처럼 들린다. `best-effort manner`는 이 바닥에서 **보장 수준을 가장 낮게 잡는 관용 표현**이라, 목록이 틀렸을 때 책임 소재를 두고 다툴 일을 미리 없앤다. 사내 스캐너나 대시보드를 팀에 넘길 때, 안내문 맨 아래에 이 두 문장을 붙여 둔다."
  app1="It is your responsibility as a service owner to check if an alert still means anything or not. We are not actively reviewing every rule for accuracy, the default thresholds we ship are maintained in a best-effort manner."
  app1ko="알림이 아직 의미가 있는지 아닌지 확인하는 것은 서비스 소유자인 당신의 책임입니다. 우리는 모든 규칙의 정확성을 능동적으로 검토하지 않으며, 우리가 배포하는 기본 임계값은 최선을 다하는 수준으로 관리됩니다."
  app2="It is your responsibility as a reviewer to check if a dependency bump is safe or not. We are not actively auditing upstream releases for regressions, the version pins we keep are maintained in a best-effort manner."
  app2ko="의존성 버전 올리기가 안전한지 아닌지 확인하는 것은 리뷰어인 당신의 책임입니다. 우리는 상위 릴리스의 회귀를 능동적으로 감사하지 않으며, 우리가 유지하는 버전 고정값은 최선을 다하는 수준으로 관리됩니다."
>}}
