---
title: 조건을 붙여 보장하고, 근거를 들어 거절하는 표현
description: 수치의 적용 범위를 되돌려 놓고, 의무와 권고를 갈라 쓰고, 기능 요청을 상대의 목적으로 되받아 거절하고, 장점을 인정한 뒤 다른 축의 문제를 얹고, 암묵적 기대를 꺼내 반례를 놓는 문장 5개.
weight: -61
date: 2026-10-21
source: "libsodium · AEAD constructions"
sourceURL: https://doc.libsodium.org/secret-key_cryptography/aead
---

# 조건을 붙여 보장하고, 근거를 들어 거절하는 표현

libsodium의 AEAD(인증된 암호화) 구성 설명 문서. 암호 라이브러리 문서인데도 표와 숫자만
늘어놓지 않고, 숫자를 하나 던질 때마다 **그 숫자가 언제까지 유효한지**를 같은 문단에서
되짚는다. 보장에 조건을 붙이는 방식, 그리고 지원하지 않겠다는 말을 상대의 목적으로
되받는 방식이 운영·보안 문서에 그대로 옮겨 쓸 만해서 발췌했다.

> **원문** — Frank Denis, *Authenticated Encryption with Additional Data*,
> [libsodium documentation](https://doc.libsodium.org/secret-key_cryptography/aead)
> ([원본 리포지터리](https://github.com/jedisct1/libsodium-doc/blob/master/secret-key_cryptography/aead.md)),
> [ISC 라이선스](https://opensource.org/license/isc-license-txt).
>
> 영어 문장은 원문 그대로 인용했고, 한글 설명과 응용 문장은 이 노트에서 새로 쓴 것이다.

{{< sentence
  en="These are single-key limits. Deployments using multiple keys, including deployments that rekey or maintain multiple connections, must also account for the aggregate multi-key limits."
  ko="이 수치는 단일 키 기준 한계다. 키를 교체하거나 여러 연결을 유지하는 배포를 포함해 여러 키를 쓰는 배포는, 다중 키 전체에 걸친 합산 한계도 함께 감안해야 한다."
  source="libsodium · AEAD constructions"
  sourceURL="https://doc.libsodium.org/secret-key_cryptography/aead"
  note="`These are X limits. Deployments doing Y must also account for Z.` — 바로 앞에 제시한 숫자를 다시 집어 **적용 범위를 좁히는** 문형이다. `These are`가 표를 가리키며 '방금 본 그 값'을 한 단어로 되돌려 놓고, `must also account for`가 '그 숫자를 지켰다고 끝이 아니다'를 추가 의무로 넘긴다. 가운데 `including ~` 삽입구가 핵심인데, **자기 얘기가 아니라고 생각할 독자를 미리 끌어오는** 장치다. 용량 산정·SLO·요금 한도처럼 숫자 하나가 혼자 떠돌면 오해를 낳는 문서에서 쓴다."
  app1="These are single-region numbers. Teams running active-active across regions, including teams that only fail over during a deploy, must also account for the cross-region replication lag."
  app1ko="이 수치는 단일 리전 기준이다. 배포 때만 전환하는 팀을 포함해 리전 간 액티브-액티브로 운영하는 팀은, 리전 사이의 복제 지연도 함께 감안해야 한다."
  app2="That is the per-pod rate limit. Services fanning out to several pods, including retries issued by the client SDK, must also account for the aggregate limit at the gateway."
  app2ko="그건 파드 하나 기준 요청 제한이다. 클라이언트 SDK가 보내는 재시도를 포함해 여러 파드로 퍼지는 서비스는, 게이트웨이에서의 합산 제한도 함께 감안해야 한다."
>}}

{{< sentence
  en="Applications are also encouraged to limit the number of attempts an adversary can make, for example by closing a session after a large number of decryption failures."
  ko="애플리케이션은 공격자가 시도할 수 있는 횟수를 제한하는 것도 권장된다. 예를 들어 복호화 실패가 많이 쌓이면 세션을 닫는 식이다."
  source="libsodium · AEAD constructions"
  sourceURL="https://doc.libsodium.org/secret-key_cryptography/aead"
  note="`X are also encouraged to Y, for example by Z.` — **강제할 수 없는 것을 강제하지 않으면서 방향만 주는** 권고 문형이다. 같은 문서가 몇 줄 위에서는 `applications must enforce a limit on the maximum size of a ciphertext to decrypt`라고 `must`를 쓴다. 어기면 안전성이 깨지는 것은 `must`, 지키면 더 나아지는 것은 `are encouraged to` — 이 둘을 갈라 쓰는 문서가 전부 `must`인 문서보다 신뢰를 얻는다. 뒤에 붙인 `for example by -ing`는 추상적인 권고를 **실행 가능한 행동 하나**로 착지시키는 자리다. 이게 없으면 권고는 읽히고 잊힌다."
  app1="Authors are also encouraged to keep the diff reviewable, for example by splitting unrelated refactors into a separate pull request."
  app1ko="작성자는 디프를 리뷰 가능한 크기로 유지하는 것도 권장된다. 예를 들어 관련 없는 리팩터링은 별도 PR로 떼어 내는 식이다."
  app2="On-call engineers are also encouraged to limit the blast radius of a rollback, for example by draining one zone before touching the rest."
  app2ko="온콜 엔지니어는 롤백의 영향 범위를 제한하는 것도 권장된다. 예를 들어 나머지를 건드리기 전에 한 존부터 빼내는 식이다."
>}}

{{< sentence
  en="There are no plans to support non hardware-accelerated implementations of AES-GCM, as correctly mitigating side-channels in a software implementation comes with major speed tradeoffs, that defeat the whole point of AES-GCM over ChaCha20-Poly1305."
  ko="하드웨어 가속을 쓰지 않는 AES-GCM 구현을 지원할 계획은 없다. 소프트웨어 구현에서 부채널을 제대로 막으려면 속도를 크게 내주어야 하는데, 그러면 ChaCha20-Poly1305 대신 AES-GCM을 고를 이유 자체가 사라지기 때문이다."
  source="libsodium · AEAD constructions"
  sourceURL="https://doc.libsodium.org/secret-key_cryptography/aead"
  note="`There are no plans to X, as Y comes with Z, that defeat the whole point of A over B.` — 요청을 **거절하면서 그 근거를 상대의 목적으로 되돌려 주는** 문형이다. `There are no plans to`는 `We will not`과 달리 주체를 지우고 로드맵의 현재 상태처럼 말해서 각이 덜 선다(나중에 다시 논의할 여지도 남는다). 진짜 일은 마지막 관계절 `that defeat the whole point of A over B`가 한다. '안 해 준다'가 아니라 **'해 줘도 당신이 원한 것이 남지 않는다'**로 끝내는 것. 이 논리는 비교 대상 `over B`를 명시해야 성립한다."
  app1="There are no plans to add a retry switch to this endpoint, as retrying a non-idempotent write comes with duplicate-charge risk, that defeats the whole point of this endpoint over the batch API."
  app1ko="이 엔드포인트에 재시도 옵션을 추가할 계획은 없다. 멱등하지 않은 쓰기를 재시도하면 중복 과금 위험이 따라오는데, 그러면 배치 API 대신 이 엔드포인트를 고를 이유가 사라지기 때문이다."
  app2="There are no plans to make the audit log editable, as allowing corrections comes with a gap in the chain of custody, that defeats the whole point of an audit log over an ordinary table."
  app2ko="감사 로그를 수정 가능하게 만들 계획은 없다. 정정을 허용하면 증적의 연속성에 구멍이 생기는데, 그러면 일반 테이블 대신 감사 로그를 둘 이유가 사라지기 때문이다."
>}}

{{< sentence
  en="While AES is very fast on dedicated hardware, its performance on platforms that lack such hardware is considerably lower. Another problem is that many software AES implementations are vulnerable to cache-collision timing attacks."
  ko="AES는 전용 하드웨어 위에서는 매우 빠르지만, 그런 하드웨어가 없는 플랫폼에서는 성능이 상당히 떨어진다. 또 다른 문제는 많은 소프트웨어 AES 구현이 캐시 충돌 타이밍 공격에 취약하다는 점이다."
  source="libsodium · AEAD constructions"
  sourceURL="https://doc.libsodium.org/secret-key_cryptography/aead"
  note="`While X, Y. Another problem is that Z.` — 장점을 그대로 인정한 뒤 **조건을 바꿔 단점을 드러내고, 성격이 다른 문제를 하나 더 얹는** 2단 구조다. `While`절은 상대 주장을 부정하지 않고 통과시키기 때문에 뒤 문장의 신뢰가 올라간다. 눈여겨볼 것은 단점을 **조건부로** 적었다는 점이다 — 'AES는 느리다'가 아니라 `on platforms that lack such hardware`에서 느리다. 그리고 `Another problem is that ~`은 앞 문제와 **같은 축이 아닌** 문제를 꺼낼 때 쓴다. 여기서는 성능 이야기 뒤에 보안 이야기가 온다. 대안을 깎지 않으면서 선택을 설명해야 하는 기술 선정 문서에 맞는다."
  app1="While the cache layer is very effective under steady traffic, its hit rate during a rolling deploy is considerably lower. Another problem is that a cold cache amplifies load on the primary database."
  app1ko="캐시 계층은 트래픽이 안정적일 때는 매우 효과적이지만, 롤링 배포 중에는 적중률이 상당히 떨어진다. 또 다른 문제는 차가운 캐시가 주 데이터베이스의 부하를 증폭시킨다는 점이다."
  app2="While the vendor scanner is very accurate on published CVEs, its coverage of our internal libraries is considerably lower. Another problem is that it reports findings without a reproducible path."
  app2ko="그 벤더 스캐너는 공개된 CVE에 대해서는 매우 정확하지만, 우리 내부 라이브러리에 대한 커버리지는 상당히 떨어진다. 또 다른 문제는 재현 경로 없이 결과만 보고한다는 점이다."
>}}

{{< sentence
  en="Ciphertexts are expected to be decrypted and verified using the same key as the key initially used for encryption. However, when using AES-GCM and ChaCha20-Poly1305, multiple keys that would cause a (ciphertext, tag) pair to verify can be efficiently computed."
  ko="암호문은 처음 암호화에 쓴 것과 같은 키로 복호화되고 검증되리라고 기대된다. 하지만 AES-GCM과 ChaCha20-Poly1305를 쓸 때는, 같은 (암호문, 태그) 쌍을 검증에 통과시키는 키를 여러 개 효율적으로 계산해 낼 수 있다."
  source="libsodium · AEAD constructions"
  sourceURL="https://doc.libsodium.org/secret-key_cryptography/aead"
  note="`X is expected to A. However, B.` — **아무도 적지 않던 암묵적 기대를 먼저 문장으로 꺼내 놓고, 그것이 보장이 아님을 보이는** 구조다. 열쇠는 `are expected to`에 있다. `must`나 `will`이 아니라 '기대'로 적었기 때문에, 뒤 문장이 그 기대를 깨도 문서가 자기모순에 빠지지 않는다. 처음부터 사실이 아니라 **통념**으로 올려놓은 것이다. 보안 리뷰나 설계 리뷰에서 누구를 탓하지 않고 가정을 수면 위로 올릴 때 이 순서를 쓴다. 기대를 한 문장으로 적고, `However`로 반례를 놓고, 거기서 멈춘다."
  app1="Webhook deliveries are expected to arrive in the order the events were produced. However, when a retry overlaps with a fresh delivery, the consumer can observe the newer event first."
  app1ko="웹훅 전달은 이벤트가 생성된 순서대로 도착하리라고 기대된다. 하지만 재시도가 새 전달과 겹치면, 소비자는 더 나중 이벤트를 먼저 볼 수 있다."
  app2="Tokens are expected to be presented only by the service they were issued to. However, when a token is written to a shared log, any job that can read that log can replay it."
  app2ko="토큰은 발급 대상 서비스만 제시하리라고 기대된다. 하지만 토큰이 공용 로그에 기록되면, 그 로그를 읽을 수 있는 어떤 작업이든 그대로 재사용할 수 있다."
>}}
