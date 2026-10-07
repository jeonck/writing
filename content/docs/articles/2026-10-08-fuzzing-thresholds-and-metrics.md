---
title: 숫자로 기준을 세우면서 그 숫자를 규칙으로 굳히지 않는 표현
description: 임계값으로 분류를 정의하고, 보편 기준이 없다고 먼저 밝히고, 지표가 좋은데도 목적이 빗나가는 사례를 세우고, 쓰이지 않는 것의 비용을 말하고, 증상만으로 진단하러 보내는 문장 5개.
weight: -48
date: 2026-10-08
source: "Google Fuzzing Forum · What makes a good fuzz target"
sourceURL: https://github.com/google/fuzzing/blob/master/docs/good-fuzz-target.md
---

# 숫자로 기준을 세우면서 그 숫자를 규칙으로 굳히지 않는 표현

퍼징할 함수(퍼즈 타깃)를 어떻게 써야 퍼저가 제대로 돌아가는지 적어 둔 문서다. 속도,
메모리, 결정성, 시드 코퍼스처럼 전부 **수치로 말해야 하는 항목**들을 다루는데, 퍼징
지식이 아니라 그 수치를 적는 말투를 골랐다 — 임계값으로 분류를 정의하고, 보편 기준이
없다고 먼저 밝히고, 커버리지가 좋은데도 목적은 빗나가는 경우를 사례로 세우고, 쓰이지
않는 것의 비용을 말하고, 원인은 말하지 않고 증상만으로 진단하러 보내는 문장들이다.

> **원문** — Google Fuzzing Forum 기여자들, *What makes a good fuzz target*,
> [google/fuzzing](https://github.com/google/fuzzing/blob/master/docs/good-fuzz-target.md),
> [Apache-2.0](https://github.com/google/fuzzing/blob/master/LICENSE).
>
> 영어 문장은 원문 그대로 인용했고, 한글 설명과 응용 문장은 이 노트에서 새로 쓴 것이다.

{{< sentence
  en="Any API with more than 20000-30000 reachable control flow edges should probably be considered large."
  ko="도달 가능한 제어 흐름 간선이 20000~30000개를 넘는 API는 아마도 크다고 봐야 한다."
  source="Google Fuzzing Forum · Large APIs"
  sourceURL="https://github.com/google/fuzzing/blob/master/docs/good-fuzz-target.md#large-apis"
  note="`Any X with more than <N> Y should probably be considered Z.` — '크다', '위험하다'처럼 사람마다 다르게 읽는 형용사를 **숫자로 정의하는** 문형이다. 세 가지가 동시에 일어난다. `Any X with more than ~`이 대상을 조건으로 묶고, 수동태 `be considered`가 판정의 주체를 지우고, `should probably`가 단언을 한 칸 내린다. 주체를 지운 것이 핵심이다. `we consider ~`라고 쓰면 우리 팀의 관행이 되어 남이 따를 이유가 없지만, `should be considered`는 누가 보든 그렇게 분류하라는 뜻이 된다. 그러면서 `probably`가 경계선이 딱 떨어지지 않는다는 사실을 인정해 둔다. 숫자를 하나로 박지 않고 `20000-30000` 범위로 쓴 것도 같은 일을 한다 — 숫자 하나를 박으면 그 숫자를 방어해야 한다. 운영 문서에서 '대형', '고위험', '중대'를 처음 정의할 때."
  app1="Any incident with more than 30-40 minutes of customer-visible impact should probably be considered a major incident, whatever the final root cause turns out to be."
  app1ko="고객에게 보이는 영향이 30~40분을 넘은 장애는, 최종 원인이 무엇으로 밝혀지든 아마도 중대 장애로 봐야 한다."
  app2="Any pull request touching more than 15-20 files should probably be considered too large to review in one sitting, and we ask the author to split it."
  app2ko="15~20개를 넘는 파일을 건드리는 풀 리퀘스트는 아마도 한 번에 리뷰하기에 너무 크다고 봐야 한다. 그래서 작성자에게 나눠 달라고 요청한다."
>}}

{{< sentence
  en="There is no one-size-fits-all RAM threshold, but as of 2019 a typical good fuzz target would consume less than 1.5Gb."
  ko="모든 경우에 맞는 단일 메모리 기준선은 없지만, 2019년 기준으로 괜찮은 퍼즈 타깃은 보통 1.5GB 미만을 쓴다."
  source="Google Fuzzing Forum · Memory consumption"
  sourceURL="https://github.com/google/fuzzing/blob/master/docs/good-fuzz-target.md#memory-consumption"
  note="`There is no one-size-fits-all X, but as of <연도> a typical Y would Z.` — 숫자를 주면서 **그 숫자가 규칙이 아니라고 먼저 못 박는** 문형이다. 앞 절이 기준의 존재 자체를 부정하기 때문에, 뒤에 나오는 수치는 규칙이 아니라 관측값의 자격으로 들어온다. 톤을 정하는 말은 두 개다. `as of 2019`는 숫자에 유통기한을 붙인다 — 나중에 틀려도 문서가 틀린 것이 아니라 시점이 지난 것이 된다. 그리고 `would`다. `consumes`로 쓰면 사실 보고가 되지만 `would consume`은 '그런 경우라면 대체로 그렇다'는 전형의 서술이 되어, 예외 하나로 무너지지 않는다. 감사 답변이나 용량 산정 문서에서 수치를 요구받았는데 그 수치가 상한으로 굳어 버리는 것을 막고 싶을 때."
  app1="There is no one-size-fits-all retention period, but as of this quarter a typical application log in our stack would be kept for less than 30 days."
  app1ko="모든 경우에 맞는 단일 보관 기간은 없지만, 이번 분기 기준으로 우리 스택의 일반적인 애플리케이션 로그는 보통 30일 미만 보관된다."
  app2="There is no one-size-fits-all error budget, but as of the last review a typical user-facing API here would burn less than 20% of it in a quiet month."
  app2ko="모든 경우에 맞는 단일 에러 예산은 없지만, 지난 검토 기준으로 여기서 사용자에게 노출되는 API는 조용한 달에 보통 예산의 20% 미만을 태운다."
>}}

{{< sentence
  en="For example, imagine we are fuzzing an API that consumes an encrypted input, and we have a comprehensive seed corpus with such encrypted inputs. This seed corpus will provide good code coverage, but any mutation of the inputs will be rejected early as broken."
  ko="예를 들어 암호화된 입력을 받는 API를 퍼징하고 있고, 그런 암호화된 입력으로 된 충실한 시드 코퍼스를 갖고 있다고 해 보자. 이 시드 코퍼스는 좋은 코드 커버리지를 내주겠지만, 입력에 가해진 어떤 변형이든 깨진 것으로 보고 앞단에서 거부될 것이다."
  source="Google Fuzzing Forum · Coverage discoverability"
  sourceURL="https://github.com/google/fuzzing/blob/master/docs/good-fuzz-target.md#coverage-discoverability"
  note="`imagine we are ~, and we have ~. This X will provide good A, but B will be rejected early as C.` — **지표는 통과하는데 목적은 빗나가는 상황**을 설명하는 틀이다. 반론을 추상적으로 적지 않고 `imagine we are ~`로 가상의 사례를 세운 뒤, 다음 문장에서 그 사례를 뒤집는다. 앞 문장이 일부러 **좋은 조건**인 것이 중요하다. `comprehensive`라고까지 써서 상대가 자랑할 만한 설정을 만들어 주고 그 설정에서도 안 된다고 말하기 때문에, '설정이 부실했던 것 아니냐'는 반박이 미리 막힌다. 뒤 문장의 `will provide good ~, but`은 지표를 부정하지 않는다 — 커버리지는 진짜로 좋다고 인정하고, 그 지표가 **대신 보증하지 못하는 것**만 떼어 낸다. `early`도 한몫한다. 거부가 앞단에서 일어나므로 그 뒤의 코드는 시도조차 되지 않는다는 뜻이다. 커버리지·SLO·스캔 통과율처럼 숫자는 좋은데 실제로는 지켜지지 않는다고 말해야 할 때."
  app1="For example, imagine we are testing a payment service that only accepts signed requests, and we have a comprehensive fixture set of valid signed requests. This fixture set will provide good line coverage, but any mutated payload will be rejected early as malformed."
  app1ko="예를 들어 서명된 요청만 받는 결제 서비스를 테스트하고 있고, 유효한 서명 요청으로 된 충실한 픽스처 집합을 갖고 있다고 해 보자. 이 픽스처 집합은 좋은 라인 커버리지를 내주겠지만, 변형된 페이로드는 어떤 것이든 형식이 틀린 것으로 보고 앞단에서 거부될 것이다."
  app2="For example, imagine we are load-testing a queue consumer that only pulls messages it can deserialize, and we have a comprehensive sample of production-shaped messages. This sample will provide good throughput numbers, but any message from the newer producer will be rejected early as unreadable."
  app2ko="예를 들어 역직렬화할 수 있는 메시지만 꺼내 가는 큐 컨슈머에 부하 테스트를 돌리고 있고, 운영 데이터 모양의 샘플을 충실히 갖고 있다고 해 보자. 이 샘플은 좋은 처리량 수치를 내주겠지만, 더 새 버전 프로듀서가 보낸 메시지는 어떤 것이든 읽을 수 없는 것으로 보고 앞단에서 거부될 것이다."
>}}

{{< sentence
  en="Even if some code linked to the fuzzer binary is never executed, it may still slow down fuzzing."
  ko="퍼저 바이너리에 링크된 코드가 한 번도 실행되지 않더라도, 그 코드는 여전히 퍼징을 느리게 만들 수 있다."
  source="Google Fuzzing Forum · Unreachable Code"
  sourceURL="https://github.com/google/fuzzing/blob/master/docs/good-fuzz-target.md#unreachable-code"
  note="`Even if X is never Y, it may still Z.` — **쓰이지 않는 것에도 비용이 남는다**고 말하는 양보 구문이다. `Even if`가 상대의 반박을 대신 말해 준다 — '그 코드는 실행도 안 되는데요'를 문장 앞쪽에 넣어 두고 시작하니, 읽는 사람이 꺼낼 말이 이미 처리되어 있다. 결론은 `still`에 걸려 있다. `still`은 조건이 바뀌어도 결과는 안 바뀐다는 신호여서, 실행 여부와 비용이 **서로 다른 축**이라는 말이 된다. 그리고 `may`로 닫는다. `will slow down`으로 쓰면 매번 느려진다는 주장이 되어 반례 하나로 무너지지만, `may`는 '그럴 수 있으니 치워 두자'까지만 요구한다. 안 쓰는 의존성, 꺼 둔 기능 플래그, 죽은 설정을 왜 걷어내야 하는지 적을 때."
  app1="Even if a feature flag has been off in every environment for a year, it may still cost us on every deploy, because both branches have to keep compiling and both paths have to keep passing tests."
  app1ko="기능 플래그가 1년 동안 모든 환경에서 꺼져 있었더라도, 그 플래그는 여전히 배포마다 비용을 물릴 수 있다. 양쪽 분기가 계속 컴파일되어야 하고 양쪽 경로가 계속 테스트를 통과해야 하기 때문이다."
  app2="Even if a dependency is never imported at runtime, it may still widen the surface we have to answer for in an audit, since the scanner reports its advisories against our service."
  app2ko="어떤 의존성이 런타임에 한 번도 임포트되지 않더라도, 그 의존성은 여전히 감사에서 우리가 해명해야 할 범위를 넓힐 수 있다. 스캐너가 그 의존성의 권고를 우리 서비스 앞으로 보고하기 때문이다."
>}}

{{< sentence
  en="If your fuzz target has less than 10 exec/s you are probably doing something wrong."
  ko="퍼즈 타깃이 초당 10회 미만으로 실행되고 있다면, 아마 무언가를 잘못하고 있는 것이다."
  source="Google Fuzzing Forum · Speed"
  sourceURL="https://github.com/google/fuzzing/blob/master/docs/good-fuzz-target.md#speed"
  note="`If your X has less than <N> Y you are probably doing something wrong.` — 증상에서 **진단으로 거꾸로 올라가는** 문형이다. 무엇이 잘못인지는 말하지 않는다. 그게 이 문장의 쓸모다 — 원인은 상황마다 다르니 숫자만 주고, 그 아래면 원인을 찾으러 가라는 신호만 보낸다. 톤은 `probably`와 `something`이 함께 만든다. `you are doing something wrong`은 단정이고 `something is wrong`은 주체가 없는데, 이 문장은 그 중간을 골랐다 — 책임은 상대 쪽에 두면서(`you are`) 확정하지는 않는다(`probably`). 쉼표가 없는 것까지 의도로 읽힌다. 한 호흡에 읽고 지나가는 짧은 경고문이다. 런북이나 리뷰 체크리스트에서 '이 수치 아래면 멈추고 들여다봐라'를 적을 때."
  app1="If your build goes from a failing test to green in less than 10 seconds you are probably doing something wrong, and the most likely cause is that the test is not running at all."
  app1ko="실패하던 테스트가 10초도 안 되어 초록으로 바뀐다면 아마 무언가를 잘못하고 있는 것이고, 가장 그럴듯한 원인은 그 테스트가 아예 돌지 않고 있다는 것이다."
  app2="If your quarterly access review has less than 5 minutes of actual work per reviewer you are probably doing something wrong."
  app2ko="분기 권한 검토에 검토자 한 사람당 실제로 들인 시간이 5분도 안 된다면, 아마 무언가를 잘못하고 있는 것이다."
>}}
