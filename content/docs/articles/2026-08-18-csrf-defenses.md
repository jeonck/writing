---
title: 웹 보안 가이드의 표현
description: 속은 경로를 서술하고, 반론을 선제 처리하고, 숨은 신뢰 범위를 드러내는 문장 5개.
weight: 4
date: 2026-08-18
source: "MDN Web Docs · CSRF"
sourceURL: https://developer.mozilla.org/en-US/docs/Web/Security/Attacks/CSRF
---

# 웹 보안 가이드의 표현

CSRF 공격이 어떻게 성립하고 무엇으로 막는지 정리한 MDN 보안 가이드.
방어책을 설명하면서 **그 방어가 어디까지 유효한지**를 같은 문단에서 못 박는 문형이 많아 발췌했다.

> **원문** — MDN Web Docs 기여자, *Cross-site request forgery (CSRF)*,
> [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/Security/Attacks/CSRF),
> [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/) 라이선스.
> 라이선스와 발췌는 이 문서의 원본인 [mdn/content 리포지터리](https://github.com/mdn/content/blob/main/files/en-us/web/security/attacks/csrf/index.md)에서 직접 확인했다.
>
> 영어 문장은 원문 그대로 인용했고, 한글 설명과 응용 문장은 이 노트에서 새로 쓴 것이다.

{{< sentence
  en="In a cross-site request forgery (CSRF) attack, an attacker tricks the user or the browser into making an HTTP request to the target site from a malicious site. The request includes the user's credentials and causes the server to carry out some harmful action, thinking that the user intended it."
  ko="크로스 사이트 요청 위조(CSRF) 공격에서 공격자는 사용자나 브라우저를 속여, 악성 사이트에서 대상 사이트로 HTTP 요청을 보내게 만든다. 그 요청은 사용자의 자격 증명을 담고 있고, 서버가 사용자의 의도라고 여긴 채 해로운 동작을 수행하게 만든다."
  source="MDN Web Docs · CSRF"
  sourceURL="https://developer.mozilla.org/en-US/docs/Web/Security/Attacks/CSRF"
  note="`trick A into -ing`은 '속여서 ~하게 만들다'를 한 덩어리로 처리하는 동사 틀이다. 진짜 훔칠 것은 문장 끝의 `, thinking that ...` 분사구 — **행위자의 틀린 믿음**을 뒤에 슬쩍 붙인다. 서버는 고장 난 게 아니라 잘못된 전제 위에서 정상 동작했다는 뜻이라, 시스템을 탓하지 않으면서 사고 경로를 서술할 수 있다. 장애 리포트에서 '왜 아무도 못 막았나'를 설명할 때 그대로 쓴다."
  app1="A stale cache tricked the health checker into marking the node as ready, and the scheduler kept routing traffic to it, thinking that the pod was still serving."
  app1ko="낡은 캐시가 헬스 체커를 속여 노드를 준비됨으로 표시하게 만들었고, 스케줄러는 파드가 여전히 응답 중이라고 여긴 채 계속 트래픽을 보냈다."
  app2="In a replay attack, an attacker tricks the gateway into accepting a captured token, and the service grants access, thinking that the user had just signed in."
  app2ko="재전송 공격에서 공격자는 게이트웨이를 속여 캡처한 토큰을 받아들이게 만들고, 서비스는 사용자가 방금 로그인했다고 여긴 채 접근을 허용한다."
>}}

{{< sentence
  en="Because an attacker can't guess the token value, they can't issue a successful forgery. Even if the attacker does discover a token after it has been used, the request can't be replayed if the token changes every time."
  ko="공격자는 토큰 값을 추측할 수 없으므로 위조 요청을 성공시킬 수 없다. 설령 공격자가 이미 쓰인 토큰을 알아내더라도, 토큰이 매번 바뀐다면 그 요청은 재전송될 수 없다."
  source="MDN Web Docs · CSRF tokens"
  sourceURL="https://developer.mozilla.org/en-US/docs/Web/Security/Attacks/CSRF"
  note="방어를 설명하는 표준 2단 구성이다. `Because X, Y`로 **왜 막히는지**를 먼저 말하고, `Even if ..., ... if ...`로 **그래도 뚫리면?** 이라는 반론을 상대가 꺼내기 전에 처리한다. 강조 조동사 `does`(`does discover`)가 '설령 정말로 알아낸다 해도'라는 양보의 세기를 만든다. 마지막 `if the token changes every time`은 방어가 성립하는 **조건**을 되붙여, 무조건적 보장으로 읽히는 것을 막는 안전장치다."
  app1="Because the worker checks the idempotency key before writing, a duplicate delivery can't create a second charge. Even if the queue does redeliver a message after the timeout, the write can't be applied twice if the key is stored in the same transaction."
  app1ko="워커가 쓰기 전에 멱등 키를 확인하므로, 중복 전달이 두 번째 청구를 만들 수 없다. 설령 큐가 타임아웃 뒤에 메시지를 정말로 재전달하더라도, 키가 같은 트랜잭션에 저장된다면 그 쓰기는 두 번 적용될 수 없다."
  app2="Because the deploy key is read-only, a leaked runner token can't push to the repository. Even if an attacker does obtain the token, the change can't reach production if every release still requires a signed tag."
  app2ko="배포 키가 읽기 전용이므로, 유출된 러너 토큰으로는 리포지터리에 푸시할 수 없다. 설령 공격자가 그 토큰을 정말로 손에 넣더라도, 모든 릴리스가 서명된 태그를 요구한다면 그 변경은 프로덕션까지 갈 수 없다."
>}}

{{< sentence
  en="Since forms have been able to make cross-origin requests since the early days of the web, it's important for compatibility that they should still be able to make cross-origin requests. This is why we need to implement other strategies to defend forms against CSRF, such as using a CSRF token."
  ko="폼은 웹 초창기부터 교차 출처 요청을 보낼 수 있었기 때문에, 호환성을 위해 지금도 교차 출처 요청을 보낼 수 있어야 한다. 그래서 CSRF 토큰 사용처럼, 폼을 CSRF로부터 지키는 다른 전략을 따로 구현해야 한다."
  source="MDN Web Docs · Avoiding simple requests"
  sourceURL="https://developer.mozilla.org/en-US/docs/Web/Security/Attacks/CSRF"
  note="**위험한 걸 알면서도 막지 않는 이유**를 대고, 그래서 무엇을 대신 하는지로 넘어가는 2단 구조다. 핵심은 `it's important for compatibility that ~` — '호환성 때문에'를 이유 자리에 놓아, 그대로 두는 것이 게으름이 아니라 **제약**임을 못 박는다. `Since`는 상대도 이미 아는 사실을 근거로 꺼낼 때 쓰는 연결어라 `Because`보다 톤이 부드럽고, `This is why`가 앞 문장을 그대로 결론의 근거로 삼는다. 레거시를 못 걷어내는 설계 판단을 적을 때 쓴다."
  app1="Since the batch job has been reading the legacy table since before the migration, it's important for compatibility that it should still read the legacy table. This is why we need to keep the two tables in sync, such as writing through on every update."
  app1ko="배치 작업은 마이그레이션 전부터 레거시 테이블을 읽어 왔기 때문에, 호환성을 위해 지금도 레거시 테이블을 읽을 수 있어야 한다. 그래서 매 갱신마다 함께 쓰는 식으로, 두 테이블을 계속 동기화해 두어야 한다."
  app2="Since the public API has accepted unauthenticated reads since launch, it's important for compatibility that it should still accept them. This is why we need to defend the endpoint another way, such as rate limiting by client."
  app2ko="공개 API는 출시 때부터 인증 없는 읽기를 받아 왔기 때문에, 호환성을 위해 지금도 그것을 받아 주어야 한다. 그래서 클라이언트별 요청 제한처럼, 그 엔드포인트를 다른 방식으로 지켜야 한다."
>}}

{{< sentence
  en="To take advantage of this protection you must understand all the places in your website where you are using state-changing HTTP requests, and ensure you're using the defense provided by your chosen framework."
  ko="이 보호를 실제로 누리려면, 상태를 바꾸는 HTTP 요청을 쓰는 웹사이트 안의 모든 지점을 파악하고, 선택한 프레임워크가 제공하는 방어를 실제로 쓰고 있는지 확인해야 한다."
  source="MDN Web Docs · CSRF tokens"
  sourceURL="https://developer.mozilla.org/en-US/docs/Web/Security/Attacks/CSRF"
  note="'프레임워크가 지원한다'는 설명 바로 뒤에 붙는 **책임 되돌리기** 문장이다. `To take advantage of X you must ...`는 '기능이 있다'와 '보호받는다'가 다르다는 말을 비난 없이 하는 방법. 무게는 `all the places ... where`에 실린다 — 한 군데만 빠져도 무의미하다는 **전수 점검** 요구다. 이어지는 `ensure you're using ~`은 '켜 뒀다고 생각하지 말고 실제로 쓰이는지 확인하라'는 뜻이라, 설정과 실제 사용을 갈라 놓는다."
  app1="To take advantage of the new rate limiter you must know all the places in the service where you are reaching the database directly, and ensure each of them goes through the shared client."
  app1ko="새 요청 제한기를 실제로 누리려면, 서비스 안에서 데이터베이스에 직접 접근하는 모든 지점을 알고 있어야 하고, 그 각각이 공용 클라이언트를 거치는지 확인해야 한다."
  app2="To take advantage of the audit log you must understand all the places where the service writes customer data, and ensure every write goes through the logged code path."
  app2ko="감사 로그를 실제로 누리려면, 서비스가 고객 데이터를 쓰는 모든 지점을 파악하고, 그 쓰기가 전부 로그가 남는 코드 경로를 지나는지 확인해야 한다."
>}}

{{< sentence
  en="Effectively, if you rely on same-site protection, you have to trust all your site's subdomains."
  ko="결국 같은 사이트 기준의 보호에 기대는 순간, 내 사이트의 모든 서브도메인을 신뢰하는 셈이 된다."
  source="MDN Web Docs · Defense in depth: SameSite cookies"
  sourceURL="https://developer.mozilla.org/en-US/docs/Web/Security/Attacks/CSRF"
  note="어떤 방어를 고르면 **덤으로 떠안게 되는 신뢰 범위**를 드러내는 문장이다. `Effectively`가 톤을 결정한다 — 명세에 그렇게 적혀 있지는 않지만 실질적인 결과가 그렇다는 뜻이라, 문서에 없는 함의를 지적할 때 딱 맞는다. `you have to trust ~`는 신뢰를 미덕이 아니라 **치러야 할 비용**으로 취급하는 표현이다. 위협 모델을 이야기하거나 설계 리뷰에서 '이 선택의 진짜 경계가 어디냐'를 물을 때 꺼낸다."
  app1="Effectively, if you rely on the VPN for authorization, you have to trust every device that can join the network."
  app1ko="결국 인가를 VPN에 기대는 순간, 그 네트워크에 들어올 수 있는 모든 장비를 신뢰하는 셈이 된다."
  app2="Effectively, if you rely on the base image for patching, you have to trust whoever can push a tag to it."
  app2ko="결국 패치를 베이스 이미지에 기대는 순간, 그 이미지에 태그를 밀어 넣을 수 있는 사람 전부를 신뢰하는 셈이 된다."
>}}
