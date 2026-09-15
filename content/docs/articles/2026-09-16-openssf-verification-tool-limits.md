---
title: 무엇을 못 하는지 먼저 적는 표현
description: 감도를 낮춘 대가를 말하고, 감당할 수 있는 만큼으로 범위를 줄이고, 눈길이 가는 경계 너머를 끌어들이고, 이름 논쟁을 실질로 돌리고, 조용한 것을 안전의 근거로 삼지 말라고 말하는 문장 5개.
weight: -27
date: 2026-09-16
source: "OpenSSF — Developing Secure Software (LFD121)"
sourceURL: https://github.com/ossf/secure-sw-dev-fundamentals/blob/main/docs/lfd121.md
---

# 무엇을 못 하는지 먼저 적는 표현

OpenSSF Best Practices 워킹그룹의 강좌 *Developing Secure Software (LFD121)*는 취약점을
찾는 도구, 위협 모델링, 암호 라이브러리 선택을 차례로 다루는데, 각 장이 **그 방법이 무엇을
못 하는지**를 먼저 적고 나서 요구를 꺼낸다. 오탐을 줄이면 미탐이 늘고, 위협 모델링이 필요
없는 경우가 있고, 최근에 깨진 소식이 없다는 것이 안전하다는 뜻은 아니라는 식이다. 그래서
**자기 방법의 약점을 인정하면서도 결론은 약해지지 않는 문형**이 촘촘하다. 도구 도입 제안,
보안 감사 회신, 설계 리뷰, 기술 선택 회의에 그대로 옮겨 쓸 다섯 문장을 골랐다.

> **원문** — David A. Wheeler, *Developing Secure Software (LFD121)*,
> [`ossf/secure-sw-dev-fundamentals` · `docs/lfd121.md`](https://github.com/ossf/secure-sw-dev-fundamentals/blob/main/docs/lfd121.md)
> (책 형태 게시본: `lfd121.openssf.org/lfd121`),
> [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
>
> 영어 문장은 원문 그대로 인용했고, 한글 설명과 응용 문장은 이 노트에서 새로 쓴 것이다.

{{< sentence
  en="Tools can be designed or configured to have fewer false positives (incorrect reports), but that lack of sensitivity typically means that it will often have more false negatives (it will fail to report things that you might expect it to report)."
  ko="도구는 오탐(잘못된 보고)이 더 적도록 설계하거나 설정할 수 있지만, 그렇게 감도가 낮아지면 대개 미탐이 더 많아진다는 뜻이 된다(찾아 주리라 기대한 것을 보고하지 못하게 된다)."
  source="Developing Secure Software (LFD121) · True and False Reports"
  sourceURL="https://github.com/ossf/secure-sw-dev-fundamentals/blob/main/docs/lfd121.md"
  note="`X can be configured to have fewer A, but that lack of ~ typically means it will often have more B.` — 두 지표가 **한쪽을 누르면 다른 쪽이 올라오는 관계**임을 한 문장에 담는 문형이다. 핵심은 중간의 `that lack of sensitivity`다. 앞 절의 결과를 그대로 받아 **이름을 붙여 되돌려 주기** 때문에 '조용해졌다'가 '둔해졌다'로 번역되고, 그래서 뒤 절이 새로운 주장이 아니라 같은 사실의 뒷면으로 읽힌다. `typically`와 `often`은 단정을 피하면서도 경향은 못 박는 장치라 반례 하나로 문장이 무너지지 않는다. 알림 임계값을 올리자는 요구, 린트 규칙을 끄자는 제안, 필터를 강화하자는 요청에 **반대가 아니라 대가를 말하는 방식**으로 답할 때 쓴다."
  app1="Alert rules can be tuned to page less often, but that lack of sensitivity typically means that we will often learn about a degradation from a customer instead of from the pager."
  app1ko="알림 규칙은 호출이 덜 울리도록 조정할 수 있지만, 그렇게 감도가 낮아지면 대개 성능 저하를 호출기가 아니라 고객에게서 먼저 듣게 된다는 뜻이 된다."
  app2="The review checklist can be shortened to keep pull requests moving, but that lack of coverage typically means that we will often merge changes whose failure modes nobody has looked at."
  app2ko="리뷰 체크리스트는 PR이 막히지 않도록 줄일 수 있지만, 그렇게 보는 범위가 줄면 대개 아무도 실패 시나리오를 살피지 않은 변경을 병합하게 된다는 뜻이 된다."
>}}

{{< sentence
  en="There is no point in trying to detect more issues than you can deal with."
  ko="감당할 수 있는 것보다 더 많은 문제를 찾아내려 해 봐야 소용이 없다."
  source="Developing Secure Software (LFD121) · Applying Tools"
  sourceURL="https://github.com/ossf/secure-sw-dev-fundamentals/blob/main/docs/lfd121.md"
  note="`There is no point in trying to X more than you can deal with.` — 범위를 줄이자는 말을 **게으름이 아니라 산수**로 들리게 하는 문형이다. `There is no point in ~ing`는 '하지 마라'가 아니라 '해 봐야 효과가 없다'는 뜻이라 금지가 아닌 판단으로 들리고, 무게는 비교급 `more ~ than you can deal with`에 실린다. 목표치를 낮추자는 게 아니라 **처리 능력을 기준선으로 삼자**는 제안이 되기 때문에, 더 많이 켜자는 쪽도 반박하려면 처리 능력을 함께 늘리자고 말해야 한다. 스캐너를 전면 적용하자는 요구, 쌓여 가는 감사 지적 사항, 알림 종류를 늘리자는 제안 앞에서 **먼저 감당할 양을 정하자**고 말할 때 쓴다."
  app1="There is no point in collecting more debug logs than you can search during an incident."
  app1ko="장애 중에 검색할 수 있는 것보다 더 많은 디버그 로그를 모아 봐야 소용이 없다."
  app2="There is no point in opening more audit findings than the team can triage this quarter."
  app2ko="이번 분기에 팀이 분류할 수 있는 것보다 더 많은 감사 지적 사항을 열어 봐야 소용이 없다."
>}}

{{< sentence
  en="While it is tempting to focus only on the specific system you are developing, in reality, you may need to include components or services outside your own system."
  ko="당신이 개발하는 바로 그 시스템만 보고 싶은 마음이 들지만, 실제로는 당신의 시스템 바깥에 있는 구성요소나 서비스까지 포함해야 할 수도 있다."
  source="Developing Secure Software (LFD121) · Threat Modeling"
  sourceURL="https://github.com/ossf/secure-sw-dev-fundamentals/blob/main/docs/lfd121.md"
  note="`While it is tempting to focus only on X, in reality, you may need to include Y.` — 남이 그어 둔 경계를 넓히자고 말하면서 **상대를 게으르다고 하지 않는** 문형이다. `it is tempting to`가 좁게 보는 선택을 실수가 아니라 **누구나 끌리는 자연스러운 선택**으로 처리해 주기 때문에, 뒤에 오는 확장이 비판이 아니라 보완으로 들린다. `in reality`는 '원칙적으로는'이 아니라 실제 사고가 나는 자리를 가리키고, `may need to`는 무조건 넓히라는 게 아니라 **판단해 보라**는 여지를 남긴다. 장애 범위 산정, 위협 모델 범위 합의, 리뷰 대상 결정처럼 **우리 코드만 보면 되느냐**는 물음이 나올 때 쓴다."
  app1="While it is tempting to focus only on the service that emitted the error, in reality, you may need to include the queue and the cron job that feed it."
  app1ko="오류를 낸 그 서비스만 보고 싶은 마음이 들지만, 실제로는 거기에 데이터를 넣는 큐와 크론 작업까지 포함해야 할 수도 있다."
  app2="While it is tempting to focus only on the code we wrote this quarter, in reality, you may need to include the deploy scripts and the base images we inherited."
  app2ko="이번 분기에 우리가 쓴 코드만 보고 싶은 마음이 들지만, 실제로는 물려받은 배포 스크립트와 베이스 이미지까지 포함해야 할 수도 있다."
>}}

{{< sentence
  en="Industry terminology differs a lot here, and we want to focus on what is useful to do, not what to call it."
  ko="이 분야의 업계 용어는 서로 많이 다르며, 우리는 그것을 뭐라고 부를지가 아니라 무엇을 하는 것이 쓸모 있는지에 집중하려 한다."
  source="Developing Secure Software (LFD121) · Introduction to Threat Modeling"
  sourceURL="https://github.com/ossf/secure-sw-dev-fundamentals/blob/main/docs/lfd121.md"
  note="`X terminology differs a lot here, and we want to focus on what is useful to do, not what to call it.` — 용어 논쟁을 **끝내는 것이 아니라 옆으로 치우는** 문형이다. 먼저 `differs a lot`으로 누구의 정의도 틀렸다고 하지 않은 채 불일치를 사실로 인정하고, 그다음 `not what to call it`으로 **논쟁의 대상 자체를 논외로** 밀어 둔다. `what is useful to do`가 대신 놓이는 기준인데, 여기서 to do가 붙어 있어 '무엇이 옳은가'가 아니라 **무엇을 할 것인가**로 논의를 옮긴다. 주어가 `we`인 것도 계산된 선택이다 — 상대에게 그만하라고 요구하는 대신 우리 쪽 입장을 밝히는 형태라 반박할 표면이 없다. 회고·설계 회의에서 인시던트 등급이나 용어 정의로 시간이 흐를 때, 같은 것을 팀마다 다르게 부를 때 쓴다."
  app1="Team terminology differs a lot here, and we want to focus on what is useful to do when the pager fires, not what to call the severity level."
  app1ko="이 부분의 용어는 팀마다 많이 다르며, 우리는 심각도를 뭐라고 부를지가 아니라 호출이 울렸을 때 무엇을 하는 것이 쓸모 있는지에 집중하려 한다."
  app2="Vendor terminology differs a lot here, and we want to focus on what is useful to check before we sign, not what to call the certification."
  app2ko="이 분야의 벤더 용어는 서로 많이 다르며, 우리는 그 인증을 뭐라고 부를지가 아니라 계약 전에 무엇을 확인하는 것이 쓸모 있는지에 집중하려 한다."
>}}

{{< sentence
  en="So before choosing anything in cryptography, do some searches to make sure that what you are choosing is not weak or broken. Perhaps nothing has been broken recently… but it would be unwise to assume that."
  ko="그러니 암호 분야에서 무엇을 고르든, 고르려는 것이 약하거나 깨진 것은 아닌지 검색해 확인하라. 최근에 깨진 것이 아무것도 없을 수도 있다… 하지만 그렇다고 가정하는 것은 현명하지 못하다."
  source="Developing Secure Software (LFD121) · Introduction to Cryptography"
  sourceURL="https://github.com/ossf/secure-sw-dev-fundamentals/blob/main/docs/lfd121.md"
  note="`Perhaps nothing has been X recently… but it would be unwise to assume that.` — **소식이 없다는 것을 안전의 근거로 삼지 말라**고 말하는 문형이다. 앞에서 상대의 낙관을 `Perhaps`로 먼저 인정해 주기 때문에 대립이 생기지 않고, 부정되는 것은 사실이 아니라 `assume`, 즉 **확인 없이 그렇게 치는 태도**다. 그래서 '당신 생각이 틀렸다'가 아니라 '확인은 해 보자'로 착지한다. `it would be unwise`는 가정법이라 상대를 unwise하다고 부르지 않으면서 그 선택만 평가하는 완충 장치이고, 앞 문장의 `do some searches`가 **대안 행동을 이미 손에 쥐여 준다** — 걱정만 늘리는 지적이 되지 않는 이유다. 오래된 의존성을 그대로 두자고 할 때, 사고가 없었으니 괜찮다는 회신에 답할 때 쓴다."
  app1="So before reusing this library in the payment path, do some searches to make sure that the version we pin is not weak or broken. Perhaps nothing has been reported recently… but it would be unwise to assume that."
  app1ko="그러니 이 라이브러리를 결제 경로에 다시 쓰기 전에, 우리가 고정한 버전이 약하거나 깨진 것은 아닌지 검색해 확인하라. 최근에 보고된 것이 아무것도 없을 수도 있다… 하지만 그렇다고 가정하는 것은 현명하지 못하다."
  app2="So before signing off on the quarterly access review, do some searches to make sure that the service accounts we are approving are not stale or over-privileged. Perhaps nothing has been flagged recently… but it would be unwise to assume that."
  app2ko="그러니 분기 접근 권한 검토를 승인하기 전에, 승인하려는 서비스 계정이 방치되었거나 권한이 과도한 것은 아닌지 검색해 확인하라. 최근에 지적된 것이 아무것도 없을 수도 있다… 하지만 그렇다고 가정하는 것은 현명하지 못하다."
>}}
