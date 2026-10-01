---
title: 선택지를 권하면서 조건을 먼저 붙이는 표현
description: 단점을 먼저 인정하고 교환하는 문장, 금지의 근거를 반사실로 세우는 문장, 전제가 깨지면 권하지 않는다고 말하는 문장 5개.
weight: -42
date: 2026-10-02
source: "Let's Encrypt Docs · Challenge Types"
sourceURL: https://letsencrypt.org/docs/challenge-types/
---

# 선택지를 권하면서 조건을 먼저 붙이는 표현

도메인 소유를 증명하는 ACME 챌린지 세 가지를 비교한 Let's Encrypt 공식 문서. 여러 방식을 나란히 놓고
**어느 것을 누구에게 권하는지**를 가려 적어야 하는 글이라, 조건·근거·대상을 문장 안에서 먼저 처리하는
문형이 모여 있다. 도구를 고르게 하거나 예외 요청을 반려하거나 위험한 옵션을 문서화할 때 그대로 옮겨
쓸 수 있는 틀이어서 발췌했다.

> **원문** — Let's Encrypt 문서 기여자, *Challenge Types*,
> [Let's Encrypt Documentation](https://letsencrypt.org/docs/challenge-types/) (2026-02-12 최종 수정),
> [MPL-2.0](https://www.mozilla.org/en-US/MPL/2.0/) 라이선스.
> 라이선스(리포지터리 `LICENSE.txt` = Mozilla Public License Version 2.0)와 발췌는 이 문서의 원본인
> [letsencrypt/website 리포지터리](https://github.com/letsencrypt/website/blob/main/content/en/docs/challenge-types.md)에서
> 직접 확인했다 (2026-10-02 확인).
>
> 영어 문장은 원문 그대로 인용했고, 한글 설명과 응용 문장은 이 노트에서 새로 쓴 것이다.

{{< sentence
  en="This challenge asks you to prove that you control the DNS for your domain name by putting a specific value in a TXT record under that domain name. It is harder to configure than HTTP-01, but can work in scenarios that HTTP-01 can’t."
  ko="이 챌린지는 해당 도메인 이름 아래 TXT 레코드에 특정 값을 넣어, 그 도메인의 DNS를 당신이 통제한다는 것을 증명하라고 요구한다. HTTP-01보다 설정하기 어렵지만, HTTP-01으로는 안 되는 상황에서도 동작한다."
  source="Let's Encrypt Docs · Challenge Types"
  sourceURL="https://letsencrypt.org/docs/challenge-types/"
  note="`It is harder to X than A, but can work in scenarios that A can’t.` — 비용과 적용 범위를 한 문장에서 맞교환하는 트레이드오프 문형이다. **단점을 먼저 인정하고** `but` 뒤에 그 비용을 지불할 이유를 두는 순서가 핵심 — 장점부터 말하면 영업처럼 들리고, 단점부터 말하면 판단을 도와주는 말이 된다. `can work in scenarios that A can’t`는 '더 좋다'가 아니라 **A가 닿지 않는 구간을 덮는다**는 뜻이라, 우열을 매기지 않고도 선택 근거가 선다. 둘 중 하나를 고르게 하는 자리(도구 선정, 방식 제안)에서 첫 문장으로 쓴다."
  app1="Canary rollout is harder to set up than a straight deploy, but it can catch regressions that staging can’t."
  app1ko="카나리 배포는 그냥 배포하는 것보다 설정이 어렵지만, 스테이징에서는 잡히지 않는 회귀를 잡아낸다."
  app2="Reading the migration by hand is slower than running the linter, but it can catch ordering problems that the linter can’t."
  app2ko="마이그레이션을 직접 읽는 것은 린터를 돌리는 것보다 느리지만, 린터로는 잡히지 않는 순서 문제를 잡아낸다."
>}}

{{< sentence
  en="The HTTP-01 challenge can only be done on port 80. Allowing clients to specify arbitrary ports would make the challenge less secure, and so it is not allowed by the ACME standard."
  ko="HTTP-01 챌린지는 80번 포트에서만 수행할 수 있다. 클라이언트가 임의의 포트를 지정하도록 허용하면 챌린지의 보안이 약해지므로, ACME 표준은 그것을 허용하지 않는다."
  source="Let's Encrypt Docs · Challenge Types"
  sourceURL="https://letsencrypt.org/docs/challenge-types/"
  note="제한을 먼저 못 박고, 그 뒤에 `Allowing X would make Y less Z, and so it is not allowed by W.`로 **금지의 근거를 반사실 가정으로** 세우는 문형이다. `would`가 아직 일어나지 않은 일을 가정하게 만들어서, 요청을 거절하면서도 요청한 사람을 탓하지 않는다. 마지막 절이 제일 중요하다 — `it is not allowed by the ACME standard`처럼 **금지의 주체를 표준·정책으로 돌려** 두면 내 취향이 아니라 규칙이라는 뜻이 된다. `and so`는 `therefore`보다 가벼워서 규칙 설명에 어울린다. 예외를 요청받고 반려할 때 쓴다."
  app1="Deploy tokens can only be read from the secret store. Letting jobs pass them as build arguments would leave them in the image history, and so it is not allowed by our pipeline policy."
  app1ko="배포 토큰은 시크릿 저장소에서만 읽을 수 있다. 잡이 그것을 빌드 인자로 넘기게 허용하면 이미지 히스토리에 남게 되므로, 우리 파이프라인 정책은 그것을 허용하지 않는다."
  app2="Allowing reviewers to approve their own pull requests would make the audit trail meaningless, and so it is not allowed by the branch protection rules."
  app2ko="리뷰어가 자기 PR을 스스로 승인하도록 허용하면 감사 기록이 무의미해지므로, 브랜치 보호 규칙은 그것을 허용하지 않는다."
>}}

{{< sentence
  en="Since automation of issuance and renewals is really important, it only makes sense to use DNS-01 challenges if your DNS provider has an API you can use to automate updates."
  ko="발급과 갱신의 자동화가 정말 중요하기 때문에, DNS-01 챌린지는 DNS 제공자가 업데이트를 자동화할 수 있는 API를 제공할 때에만 쓸 만하다."
  source="Let's Encrypt Docs · Challenge Types"
  sourceURL="https://letsencrypt.org/docs/challenge-types/"
  note="`Since X is really important, it only makes sense to use Y if Z.` — 권고를 **전제에 묶어 두는** 문형이다. `it only makes sense to`는 `do not use`보다 부드럽지만 `only ... if` 때문에 조건 밖에서는 아예 선택지가 아니라고 못 박는다. 순서가 핵심 — `Since ~`로 **그 조건이 왜 조건인지**를 먼저 깔아 둔다. 이유 없이 조건만 말하면 규정으로 들리고, 이유를 먼저 대면 판단으로 읽힌다. 도입 가능 여부를 묻는 질문에 '된다/안 된다'로 답하지 않고 조건을 돌려줄 때 쓴다."
  app1="Since every page has to be actionable, it only makes sense to alert on this metric if there is a runbook step that changes the outcome."
  app1ko="모든 호출은 조치가 가능해야 하므로, 이 지표로 알림을 걸 일은 결과를 바꾸는 런북 절차가 있을 때에만 쓸 만하다."
  app2="Since rollbacks have to finish inside the maintenance window, it only makes sense to ship this migration if it can be reversed without a full restore."
  app2ko="롤백은 점검 시간 안에 끝나야 하므로, 이 마이그레이션은 전체 복원 없이 되돌릴 수 있을 때에만 내보낼 만하다."
>}}

{{< sentence
  en="Note that putting your full DNS API credentials on your web server significantly increases the impact if that web server is hacked."
  ko="전체 권한을 가진 DNS API 자격 증명을 웹 서버에 두면, 그 웹 서버가 침해당했을 때의 영향이 크게 커진다는 점에 유의하라."
  source="Let's Encrypt Docs · Challenge Types"
  sourceURL="https://letsencrypt.org/docs/challenge-types/"
  note="사고가 날 **확률**이 아니라 사고가 났을 때의 **피해 크기**를 말하는 문형이다. `increases the impact if X`가 핵심 — `is risky`처럼 뭉개지 않고, 어떤 사건을 전제로 무엇이 커지는지를 갈라 놓는다. 그래서 상대가 반박하려면 '그 사건은 안 일어난다'를 증명해야 하고, 그건 보통 못 한다. `significantly`는 숫자를 댈 수 없을 때 쓰는 정도 표현이고, `Note that ~`은 금지가 아니라 **결정의 대가를 알려 주는** 톤이라 설계 리뷰에서 반대표를 던지지 않고 우려만 남길 때 맞다."
  app1="Note that giving the CI runner a long-lived admin token significantly increases the impact if a workflow file is compromised."
  app1ko="CI 러너에 만료가 긴 관리자 토큰을 주면, 워크플로 파일이 침해됐을 때의 영향이 크게 커진다는 점에 유의하라."
  app2="Note that keeping the only copy of the audit log on the same host significantly increases the impact if that host is lost."
  app2ko="감사 로그의 사본을 같은 호스트에만 두면, 그 호스트를 잃었을 때의 영향이 크게 커진다는 점에 유의하라."
>}}

{{< sentence
  en="This challenge is not suitable for most people. It is best suited to authors of TLS-terminating reverse proxies that want to perform host-based validation like HTTP-01, but want to do it entirely at the TLS layer in order to separate concerns."
  ko="이 챌린지는 대부분의 사람에게 적합하지 않다. HTTP-01처럼 호스트 기반 검증을 하고 싶지만 관심사를 분리하려고 그것을 전부 TLS 계층에서 처리하려는, TLS 종단 리버스 프록시의 작성자에게 가장 알맞다."
  source="Let's Encrypt Docs · Challenge Types"
  sourceURL="https://letsencrypt.org/docs/challenge-types/"
  note="`X is not suitable for most people. It is best suited to A that want to B, but want to C in order to D.` — 기능을 소개하면서 **독자 대부분을 먼저 제외하는** 문형이다. 순서를 바꾸면 안 된다: `not suitable for most people`로 기대를 끊고 나서야 `best suited to`로 남는 대상을 묶는데, 그 대상을 직군 + 하려는 일 + 제약 세 겹으로 아주 좁게 적는다. `but want to ~ in order to ~`가 **목적은 같은데 방식이 달라서 이게 필요한 사람**을 집어내는 장치다. 쓸 수는 있지만 아무나 써서는 안 되는 옵션을 문서화할 때 그대로 쓴다."
  app1="This escape hatch is not suitable for most teams. It is best suited to services that already own their failover path, but want to trigger it from our console in order to keep one audit trail."
  app1ko="이 비상 통로는 대부분의 팀에게 적합하지 않다. 자기 페일오버 경로를 이미 직접 관리하고 있지만 감사 기록을 한곳에 모으려고 우리 콘솔에서 그것을 띄우려는 서비스에 가장 알맞다."
  app2="Direct database access is not suitable for most responders. It is best suited to engineers who already know the failing query, but need the row count first in order to justify a rollback."
  app2ko="데이터베이스 직접 접근은 대부분의 대응자에게 적합하지 않다. 실패하는 쿼리를 이미 알고 있지만 롤백을 정당화하려고 먼저 행 수를 확인해야 하는 엔지니어에게 가장 알맞다."
>}}
