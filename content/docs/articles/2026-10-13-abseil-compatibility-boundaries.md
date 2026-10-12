---
title: 의존하지 말라고 선을 긋는 표현
description: 실제 접면이 공식 API보다 넓다고 적고, 금지를 행위별로 쪼개 열거하고, 권고에 예외 경로를 붙이고, 상대가 꺼낼 근거를 미리 적용 범위 밖으로 밀어내고, 놓친 변경은 문서에도 없다고 적는 문장 5개.
weight: -53
date: 2026-10-13
source: "Abseil · Compatibility Guidelines"
sourceURL: https://abseil.io/about/compatibility
---

# 의존하지 말라고 선을 긋는 표현

구글이 만든 C++ 공통 라이브러리 Abseil의 호환성 지침 문서다. 무엇이 공개 API이고 무엇이
구현 세부사항인지, 사용자가 무엇에 의존해도 되고 무엇에 의존하면 안 되는지, 그러면서도
라이브러리 쪽이 지키겠다고 약속하는 것은 어디까지인지를 적어 둔 문서다. C++ 문법보다
**경계를 통보하는 말투**가 배울 점이라 골랐다 — 강제할 수단이 없는 상대에게 하지 말라고
말해야 하고, 권고를 어길 자유는 인정해야 하고, 자기 쪽이 놓칠 수 있다는 것도 같은 문서에
적어야 하는 글이다. API 호환성 공지를 쓸 때, 내부 구현을 건드리는 코드를 리뷰할 때,
점검 결과의 완전성을 약속하지 않고 내보낼 때 그대로 틀을 가져다 쓸 수 있다.

> **원문** — The Abseil Authors, *Abseil Compatibility Guidelines*,
> [abseil/abseil.github.io](https://github.com/abseil/abseil.github.io/blob/master/about/compatibility.md)
> (문서 사이트: [abseil.io — Abseil Compatibility Guidelines](https://abseil.io/about/compatibility)),
> [Apache-2.0](https://github.com/abseil/abseil.github.io/blob/master/LICENSE) 라이선스.
>
> 영어 문장은 원문 그대로 인용했고, 한글 설명과 응용 문장은 이 노트에서 새로 쓴 것이다.

{{< sentence
  en="Applications developers interact with a C++ library through more than just the C++ symbols and headers. They also need to reference the name of the library in their build scripts."
  ko="애플리케이션 개발자가 C++ 라이브러리와 만나는 접면은 C++ 심벌과 헤더만이 아니다. 빌드 스크립트에서 라이브러리 이름을 가리켜야 하기도 한다."
  source="Abseil · What we mean by API"
  sourceURL="https://abseil.io/about/compatibility"
  note="`X interacts with Y through more than just A. They also need to B.` — 계약의 면적을 공식 인터페이스 **밖으로 넓히는** 문장이다. `more than just`가 핵심 — 앞에서 세운 정의(공개 헤더가 API다)를 틀렸다고 하지 않고 좁다고만 말한다. 그래서 정의를 철회하지 않고도 그 위에 얹을 수 있고, 읽는 쪽도 반박할 지점을 못 찾는다. 둘째 문장의 `also need to`는 추가분을 취향이 아니라 **의무**로 적는다 — 빌드 스크립트에 이름을 적는 일은 선택이 아니니, 그 이름이 바뀌면 사용자가 깨진다는 결론이 저절로 따라온다. 주어가 산출물이 아니라 사람(`Applications developers`)이라는 점도 의도적이다. 심벌과 헤더를 주어로 쓰면 범위 이야기가 되지만, 사람을 주어로 쓰면 깨지는 대상이 사람이 된다 — 공식 API는 안 건드렸다는 답이 막힌다. 로그 포맷, 메트릭 이름, 종료 코드, 큐 이름처럼 **문서에 없는데 이미 계약인 것들**을 적어 둘 때 쓴다."
  app1="Downstream teams interact with our service through more than just the REST endpoints. They also need to match on the error codes we put in the response body."
  app1ko="다른 팀이 우리 서비스와 만나는 접면은 REST 엔드포인트만이 아니다. 응답 본문에 담아 보내는 에러 코드에도 맞춰 분기해야 한다."
  app2="On-call engineers interact with this job through more than just its dashboard. They also need to read the log lines that the retry loop prints."
  app2ko="온콜 담당자가 이 잡과 만나는 접면은 대시보드만이 아니다. 재시도 루프가 찍는 로그 줄도 읽어야 한다."
>}}

{{< sentence
  en="It's an implementation detail. You cannot friend it, you cannot include it, you cannot mention it or refer to it in any way."
  ko="그것은 구현 세부사항이다. friend로 지정할 수도, include할 수도, 언급하거나 어떤 방식으로든 참조할 수도 없다."
  source="Abseil · C++ Symbols and Files"
  sourceURL="https://abseil.io/about/compatibility"
  note="`It's an X. You cannot A, you cannot B, you cannot C or D in any way.` — 금지를 한 덩어리로 묶지 않고 **행위별로 끊어 반복하는** 문장이다. `You cannot depend on it` 한 줄로 적으면 직접 의존은 아니라는 해석의 틈이 남는다. 쪼개 열거하면 그 틈이 사라진다 — 열거가 길어질수록 내가 한 일은 저 중에 없다고 말하기 어려워지기 때문이다. 마지막 `or refer to it in any way`가 울타리를 닫는다. 앞의 셋을 예시로 만들어 두고 남은 전부를 한 번에 덮으니, 더 열거하지 않아도 빠짐이 없다. 주어를 규칙이 아니라 `You`로 둔 것도 세다 — `Internal headers must not be included`는 규정집의 문장이고, `you cannot include it`은 눈앞의 상대에게 하는 말이다. 앞에 분류를 선언하는 `It's an implementation detail.` 한 문장을 세워 둔 2단 구성이 이 문형의 뼈대다. 금지를 먼저 적으면 왜 안 되냐는 질문을 받고, 분류를 먼저 적으면 금지가 그 분류에서 따라 나온다."
  app1="That table is an implementation detail. You cannot query it, you cannot join against it, you cannot copy its schema or depend on its column names in any way."
  app1ko="그 테이블은 구현 세부사항이다. 조회할 수도, 조인할 수도, 스키마를 복사하거나 컬럼 이름에 어떤 방식으로든 의존할 수도 없다."
  app2="The staging credential is a debugging aid. You cannot commit it, you cannot paste it into a ticket, you cannot forward it or keep it on disk in any way."
  app2ko="스테이징 자격 증명은 디버깅 보조 수단이다. 커밋할 수도, 티켓에 붙여넣을 수도, 전달하거나 어떤 방식으로든 디스크에 남겨 둘 수도 없다."
>}}

{{< sentence
  en="We generally do not recommend you use the global namespace for anything. If you must, please qualify any call that accepts a type provided by Abseil."
  ko="우리는 전역 네임스페이스를 어떤 용도로든 쓰는 것을 일반적으로 권하지 않는다. 그래도 써야 한다면, Abseil이 제공하는 타입을 받는 호출은 모두 한정해서 적어 달라."
  source="Abseil · C++ Symbols and Files"
  sourceURL="https://abseil.io/about/compatibility"
  note="`We generally do not recommend X. If you must, please Y.` — 강제할 수단이 없는 일을 두고 **권고와 최소 조건을 두 문장으로 나누는** 문장이다. 첫 문장은 금지가 아니라 권고라는 걸 숨기지 않는다 — `generally`가 예외의 존재를 미리 인정해 두기 때문에, 상대가 반례를 들고 와도 문장이 깨지지 않는다. 핵심은 둘째 문장의 `If you must`다. 권고를 어길 자유를 먼저 인정해 버리고, 대신 어길 때 지킬 것 **한 가지만** 받아낸다. 이 문장을 빼면 권고는 조용히 무시되고, 반대로 `you must never`로 조이면 그 자리에서 예외 협상이 시작된다. 톤을 정하는 단어는 `please`다 — 명령이 아니라 부탁이라서, 권한이 없는 자리에서 쓸 수 있는 가장 강한 문형이 된다. 코드 리뷰에서 내가 바꿀 권한이 없는 코드에 의견을 달 때, 운영 규칙에 예외를 허용하면서 최소 조건을 붙일 때 쓴다."
  app1="We generally do not recommend running migrations by hand for anything. If you must, please paste the exact statements into the incident channel before you run them."
  app1ko="우리는 마이그레이션을 손으로 돌리는 것을 어떤 경우에도 권하지 않는다. 그래도 해야 한다면, 실행 전에 돌릴 문장을 그대로 장애 채널에 붙여 달라."
  app2="We generally do not recommend reading another team's database directly for anything. If you must, please go through a read replica and write down which columns you touched."
  app2ko="우리는 다른 팀 데이터베이스를 직접 읽는 것을 어떤 용도로든 권하지 않는다. 그래도 읽어야 한다면, 읽기 복제본을 거치고 어떤 컬럼을 건드렸는지 적어 달라."
>}}

{{< sentence
  en="We will try to be clear about which libraries are OK for dynamic loading. However we don't generally deploy code in this fashion, mistakes are possible, and the normal argument of &quot;This code is production hardened&quot; does not apply in such usage."
  ko="어떤 라이브러리가 동적 로딩에 괜찮은지는 분명히 적어 보려 한다. 다만 우리는 보통 그런 방식으로 코드를 배포하지 않으므로, 실수가 있을 수 있고 &quot;이 코드는 프로덕션에서 검증됐다&quot;는 평소의 근거가 그런 용법에는 적용되지 않는다."
  source="Abseil · C++ Symbols and Files"
  sourceURL="https://abseil.io/about/compatibility"
  note="`However we don't generally X, mistakes are possible, and the normal argument of &quot;Y&quot; does not apply in such usage.` — 상대가 꺼낼 **익숙한 근거를 미리 지목해 무력화하는** 문장이다. 훔칠 자리는 `the normal argument of &quot;...&quot;` — 반론을 요약하지 않고 따옴표로 그대로 인용해 이름을 붙인다. 그래야 반박할 대상이 생기고, 나중에 그 말이 실제로 나왔을 때 이미 다뤄 둔 것이 된다. 그 뒤가 더 중요하다. `does not apply in such usage`는 그 근거가 **틀렸다고 하지 않는다** — 적용 범위 밖이라고만 한다. 근거 자체를 부정하면 그걸 믿는 사람들과 싸워야 하지만, 범위를 끊으면 싸울 일이 없다. 순서도 의도적이다. 신뢰의 출처(많이 돌려 봤다)가 왜 여기서 안 통하는지를 `we don't generally deploy code in this fashion`로 먼저 깔고, `mistakes are possible`로 결과를 적은 다음에야 결론을 낸다. 리뷰나 회고에서 이 경로는 원래 잘 돌던 코드라는 말을 받아낼 때 쓴다."
  app1="We will try to be clear about which endpoints are safe to retry. However we don't generally see this traffic pattern outside incidents, mistakes are possible, and the normal argument of &quot;this path has run for two years&quot; does not apply in such usage."
  app1ko="어떤 엔드포인트가 재시도해도 안전한지는 분명히 적어 보려 한다. 다만 우리는 보통 장애 상황 밖에서는 이런 트래픽 패턴을 보지 못하므로, 실수가 있을 수 있고 &quot;이 경로는 2년을 돌았다&quot;는 평소의 근거가 그런 용법에는 적용되지 않는다."
  app2="We will try to be clear about which jobs can be replayed without harm. However we don't generally re-send events by hand, mistakes are possible, and the normal argument of &quot;the pipeline is idempotent&quot; does not apply in such usage."
  app2ko="어떤 잡을 다시 돌려도 해가 없는지는 분명히 적어 보려 한다. 다만 우리는 보통 이벤트를 손으로 다시 보내지 않으므로, 실수가 있을 수 있고 &quot;이 파이프라인은 멱등이다&quot;는 평소의 근거가 그런 용법에는 적용되지 않는다."
>}}

{{< sentence
  en="Though we take reasonable efforts to prevent this, it is possible that backwards incompatible changes go undetected and, therefore, undocumented."
  ko="이를 막으려 합당한 노력을 들이지만, 하위 호환을 깨는 변경이 탐지되지 않고 그래서 문서에도 남지 않는 일이 있을 수 있다."
  source="Abseil · Compatibility Guidelines"
  sourceURL="https://abseil.io/about/compatibility"
  note="`Though we take reasonable efforts to prevent this, it is possible that X go undetected and, therefore, undocumented.` — 노력과 한계를 한 문장에 담고, 한계의 **2차 결과까지 적는** 문장이다. 노력을 `Though` 종속절로 처리한 순서가 이 문장의 성격을 정한다 — 주절 자리에 한계가 와야 한계가 결론이 된다. 뒤집어 `It is possible that ..., though we take reasonable efforts to prevent it`로 쓰면 같은 내용이 변명으로 읽힌다. `reasonable efforts`는 계약서에서 온 표현이다. 최선을 다했다(`best efforts`)고 하지 않고 합당한 수준까지라고 적어, 놓친 사례가 드러나도 약속을 깬 것이 되지 않게 범위를 미리 잡아 둔다. 가장 배울 부분은 `and, therefore, undocumented` — 놓친 변경은 **문서에도 없다**는, 당연한데 아무도 적지 않는 귀결이다. 이 한 조각이 문서에 없으니 안 바뀐 것이라는 추론을 막는다. `therefore`를 콤마로 양쪽에서 끊어 그 귀결에 눈이 걸리게 만든 것도 의도적이다. 여기서 `this`는 앞 문단의 호환성 파괴를 가리킨다. 릴리스 노트, 점검 결과, 감사 보고서에서 **목록의 완전성**을 약속하지 않고 내보낼 때 쓴다."
  app1="Though we take reasonable efforts to prevent this, it is possible that permission changes go unreviewed and, therefore, unlogged."
  app1ko="이를 막으려 합당한 노력을 들이지만, 권한 변경이 리뷰를 거치지 않고 그래서 기록에도 남지 않는 일이 있을 수 있다."
  app2="Though we take reasonable efforts to prevent this, it is possible that a failed retry goes unalerted and, therefore, unreported in the weekly summary."
  app2ko="이를 막으려 합당한 노력을 들이지만, 실패한 재시도가 알림을 내지 않고 그래서 주간 요약에도 빠지는 일이 있을 수 있다."
>}}
