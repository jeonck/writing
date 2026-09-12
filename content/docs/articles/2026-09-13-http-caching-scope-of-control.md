---
title: 어디까지 손이 닿는지 적는 표현
description: 신호 하나로 단정하지 않고, 전제가 바뀌었음을 밝히고, 재량과 권고를 갈라 적고, 손쓸 수 없는 시점을 못 박는 문장 5개.
weight: -24
date: 2026-09-13
source: "MDN Web Docs — HTTP caching"
sourceURL: https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Caching
---

# 어디까지 손이 닿는지 적는 표현

MDN의 *HTTP caching*은 응답이 어디에 저장되고, 언제 신선하고 언제 낡은 것이 되고, 무엇으로
그것을 되살리는지 정리한 긴 가이드다. 디렉티브 설명서인데도 읽다 보면 내용보다 **판단의
범위를 재는 문장**이 눈에 걸린다. 쿠키가 있다는 사실만으로는 응답이 개인용이 되지 않는다고
잘라 말하고, HTTPS가 보편화되어 낡은 프록시 걱정이 사라진 상황을 따로 떼어 적고, 재사용
기간은 구현에 맡기면서 사양의 권고값을 덧붙이고, 응답이 한번 저장된 뒤에는 서버가 할 수 있는
일이 없다고 선언한다. **장애 복구 요청에 대한 회신, 보안 감사 소견, 런북, 코드 리뷰 답변**처럼
내 손이 어디까지 닿고 어디서부터는 닿지 않는지를 상대에게 납득시켜야 하는 글에 그대로 옮겨
쓸 다섯 문장을 골랐다.

> **원문** — MDN Web Docs 기여자, *HTTP caching*,
> [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Caching)
> (상시 갱신), [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/) 라이선스.
> 라이선스는 원본 리포지터리의 [LICENSE.md](https://github.com/mdn/content/blob/main/LICENSE.md)에서
> 직접 확인했다 — "All prose content is available under (CC-BY-SA 2.5)".
> ([원본 마크다운](https://github.com/mdn/content/blob/main/files/en-us/web/http/guides/caching/index.md))
>
> 영어 문장은 원문 그대로 인용했고, 한글 설명과 응용 문장은 이 노트에서 새로 쓴 것이다.

{{< sentence
  en="Personalized contents are usually controlled by cookies, but the presence of a cookie does not always indicate that it is private, and thus a cookie alone does not make the response private."
  ko="개인화된 콘텐츠는 보통 쿠키로 제어되지만, 쿠키가 있다는 사실이 곧 그것이 개인용이라는 뜻은 아니며, 따라서 쿠키만으로 응답이 개인용이 되지는 않는다."
  source="MDN Web Docs · HTTP caching · Private caches"
  sourceURL="https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Caching"
  note="`the presence of X does not always indicate Y, and thus X alone does not make Z` — **신호 하나를 결론으로 쓰지 못하게 막는** 문형이다. 먼저 `usually`로 관행을 인정해 두는 게 중요하다. 관행을 부정하지 않고 그 관행의 **추론 방향만** 끊기 때문에 상대가 방어적으로 나오지 않는다. `the presence of`는 '있다는 사실'만 가리켜 그 신호를 최소 단위로 쪼개고, `does not always`는 전면 부정이 아니라 한정 부정이라 반례 하나만 있어도 성립한다. 마지막 `alone does not make`가 그 한정 부정을 **판정 금지**까지 끌고 간다. 감사 소견이나 리뷰에서 지표 하나로 합격 판정이 내려지는 관행을 막을 때 그대로 쓴다."
  app1="Privileged calls are usually controlled by an auth header, but the presence of a token does not always indicate that the caller was verified, and thus a token alone does not make the request authorized."
  app1ko="권한이 필요한 호출은 보통 인증 헤더로 제어되지만, 토큰이 있다는 사실이 곧 호출자가 검증됐다는 뜻은 아니며, 따라서 토큰만으로 그 요청이 인가되지는 않는다."
  app2="Release readiness is usually tracked by the pipeline status, but the presence of a green build does not always indicate that the migration ran, and thus a green build alone does not make the release safe."
  app2ko="릴리스 준비 상태는 보통 파이프라인 상태로 관리되지만, 빌드가 통과했다는 사실이 곧 마이그레이션이 실행됐다는 뜻은 아니며, 따라서 빌드 통과만으로 그 릴리스가 안전해지지는 않는다."
>}}

{{< sentence
  en="However, in recent years, as HTTPS has become more common and client/server communication has become encrypted, proxy caches in the path can only tunnel a response and can't behave as a cache, in many cases. So in that scenario, there is no need to worry about outdated proxy cache implementations that cannot even see the response."
  ko="그러나 최근 몇 년 사이 HTTPS가 더 보편화되고 클라이언트와 서버 사이의 통신이 암호화되면서, 많은 경우 경로 중간의 프록시 캐시는 응답을 터널링할 수 있을 뿐 캐시로 동작하지 못한다. 그러므로 그런 상황에서는 응답을 들여다보지도 못하는 낡은 프록시 캐시 구현을 걱정할 필요가 없다."
  source="MDN Web Docs · HTTP caching · Proxy caches"
  sourceURL="https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Caching"
  note="`as X has become more common, Y can only A and can't B, in many cases. So in that scenario, there is no need to worry about Z.` — 과거의 우려를 **틀렸다고 하지 않고 전제가 달라졌다고** 처리하는 2단 구성이다. 1단은 현재완료(`has become`)로 환경 변화를 쌓고, `can only A and can't B`로 남은 능력과 사라진 능력을 한 쌍으로 보여 준다. 2단의 `So in that scenario`가 면제 범위를 그 환경으로 **한정**하는 게 핵심 — 조건을 떼고 `there is no need to worry`만 쓰면 무조건 안심하라는 말이 된다. 꼬리의 `in many cases`와 `even`(`cannot even see`)은 각각 단정을 누그러뜨리고 면제의 근거를 한 덩어리로 붙인다. 오래된 방어 항목을 걷어내자고 설득할 때 쓴다."
  app1="However, in recent years, as mutual TLS has become the default and every hop has become authenticated, hosts outside the mesh can only reach the gateway and can't open a direct connection to a pod, in many cases. So in that scenario, there is no need to worry about the legacy IP allowlist that no longer matches any route."
  app1ko="그러나 최근 몇 년 사이 상호 TLS가 기본이 되고 모든 구간이 인증되면서, 많은 경우 메시 바깥의 호스트는 게이트웨이에 닿을 수 있을 뿐 파드로 직접 연결을 열지 못한다. 그러므로 그런 상황에서는 이제 어떤 경로와도 맞지 않는 낡은 IP 허용 목록을 걱정할 필요가 없다."
  app2="However, in recent years, as short-lived tokens have become the norm and long-lived keys have been removed from the runners, a leaked build log can only expose an expired credential and can't be replayed against the registry, in many cases. So in that scenario, there is no need to worry about rotation tickets for keys that no longer exist."
  app2ko="그러나 최근 몇 년 사이 단기 토큰이 일반화되고 장기 키가 러너에서 제거되면서, 많은 경우 유출된 빌드 로그는 이미 만료된 자격 증명을 드러낼 수 있을 뿐 레지스트리에 재전송될 수 없다. 그러므로 그런 상황에서는 이미 존재하지 않는 키에 대한 교체 티켓을 걱정할 필요가 없다."
>}}

{{< sentence
  en="How long to reuse is up to the implementation, but the specification recommends about 10% (in this case 0.1 year) of the time after storing."
  ko="얼마나 오래 재사용할지는 구현에 맡겨져 있지만, 사양은 저장 후 경과 시간의 약 10%(이 경우 0.1년)를 권고한다."
  source="MDN Web Docs · HTTP caching · Heuristic caching"
  sourceURL="https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Caching"
  note="`How long to X is up to A, but the specification recommends about Y` — **재량과 권고를 한 문장에서 갈라 적는** 문형이다. `is up to A`는 '알아서 하라'는 방임이 아니라 **결정 권한이 누구에게 있는지 지정하는** 표현이라, 나중에 값이 달라도 규칙 위반이 아니게 된다. 그 뒤의 `but ... recommends`가 재량을 거두지 않으면서 기본값을 건네므로 `must`의 강제와 침묵 사이의 자리를 얻는다. 숫자에 붙은 `about`과 괄호 속 환산값(`in this case 0.1 year`)은 그 값을 규격이 아니라 **출발점**으로 읽히게 한다. 런북이나 가이드에서 팀의 판단을 존중하면서도 빈손으로 돌려보내지 않을 때 쓴다."
  app1="How long to wait before paging the secondary is up to the on-call engineer, but the runbook recommends about 15 minutes (in this case one alert interval) after the first page goes unacknowledged."
  app1ko="2차 담당자를 호출하기까지 얼마나 기다릴지는 온콜 담당자에게 맡겨져 있지만, 런북은 첫 호출이 확인되지 않은 뒤 약 15분(이 경우 알림 간격 한 번)을 권고한다."
  app2="How many reviewers to request is up to the author, but the guideline recommends about two (in this case one owner and one domain reviewer) for any change that touches the billing path."
  app2ko="리뷰어를 몇 명 부를지는 작성자에게 맡겨져 있지만, 가이드는 결제 경로를 건드리는 변경에 약 두 명(이 경우 소유자 한 명과 도메인 리뷰어 한 명)을 권고한다."
>}}

{{< sentence
  en="You may want to overwrite that response once it expired on the server, but there is nothing the server can do once the response is stored — since no more requests reach the server due to caching."
  ko="서버에서 만료된 뒤 그 응답을 덮어쓰고 싶을 수 있지만, 응답이 한번 저장된 뒤에는 서버가 할 수 있는 일이 없다 — 캐싱 때문에 더 이상 요청이 서버에 도달하지 않으니까."
  source="MDN Web Docs · HTTP caching · Deleting stored responses"
  sourceURL="https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Caching"
  note="`You may want to X, but there is nothing A can do once Y — since Z.` — 상대의 바람을 먼저 받아 준 뒤 **불가능을 선언하는** 문형이다. `You may want to`는 요구를 반박하지 않고 자연스러운 것으로 인정해 주는 완충재다. 본론의 `there is nothing A can do`는 '어렵다'나 '권장하지 않는다'가 아니라 **쓸 수 있는 수단이 없다**는 말이라, 더 밀어붙여도 방법이 나오지 않는다는 뜻이 된다. `once Y`가 불가역이 시작되는 **시점**을 못 박아 범위를 제한하고(그 전에는 손을 쓸 수 있다), 대시 뒤의 `since Z`가 수단이 없는 이유를 메커니즘으로 설명한다. 사후 복구 요청을 거절하면서 변명처럼 들리지 않게 할 때 쓴다."
  app1="You may want to recall the page once you find the threshold was wrong, but there is nothing the alerting system can do once the notification is delivered — since the message has already left our queue."
  app1ko="임계값이 잘못됐다는 것을 알고 나서 호출을 취소하고 싶을 수 있지만, 알림이 한번 전달된 뒤에는 알림 시스템이 할 수 있는 일이 없다 — 그 메시지는 이미 우리 큐를 떠났으니까."
  app2="You may want to unpublish the token once you notice it in the build log, but there is nothing rotation can do once the value has been copied outside the org — since the copies never check back with our key service."
  app2ko="빌드 로그에서 토큰을 발견한 뒤 그것을 회수하고 싶을 수 있지만, 그 값이 한번 조직 밖으로 복사된 뒤에는 키 교체가 할 수 있는 일이 없다 — 그 복사본들은 우리 키 서비스에 다시 물어보지 않으니까."
>}}

{{< sentence
  en="Unlike subresources, main resources cannot be cache busted because their URLs can't be decorated in the same way that subresource URLs can be."
  ko="하위 자원과 달리 주 자원에는 캐시 버스팅을 적용할 수 없다. 그 URL은 하위 자원 URL처럼 꾸밀 수 없기 때문이다."
  source="MDN Web Docs · HTTP caching · Main resources"
  sourceURL="https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Caching"
  note="`Unlike A, B cannot X because ... in the same way that A can be.` — 잘 되는 쪽을 기준으로 세워 두고 **안 되는 쪽의 구조적 이유**를 붙이는 대조 문형이다. `Unlike A`를 문장 맨 앞에 놓아 독자가 이미 아는 사례에서 출발하게 하는 것이 이 문형의 값이다. 같은 방법을 왜 여기엔 못 쓰냐는 질문에 답할 때, 이유를 `because` 뒤의 **조건 차이**(`their URLs can't be decorated`)로 돌리기 때문에 누구의 실력이나 게으름 문제로 읽히지 않는다. 꼬리의 `in the same way that A can be`는 비교 대상을 한 번 더 불러와 '전혀 불가능'이 아니라 **그 방법만 불가능**하다는 범위를 남긴다. 리뷰 답변에서 제안된 기법을 거절하면서 대안 탐색의 여지를 열어 둘 때 쓴다."
  app1="Unlike batch jobs, streaming consumers cannot be re-run from the beginning because their offsets can't be rewound in the same way that batch inputs can be."
  app1ko="배치 작업과 달리 스트리밍 컨슈머는 처음부터 다시 돌릴 수 없다. 그 오프셋은 배치 입력처럼 되감을 수 없기 때문이다."
  app2="Unlike staging, production cannot be rebuilt from the manifests alone because its secrets can't be regenerated in the same way that staging secrets can be."
  app2ko="스테이징과 달리 프로덕션은 매니페스트만으로 다시 구축할 수 없다. 그 비밀값은 스테이징 비밀값처럼 재생성할 수 없기 때문이다."
>}}
