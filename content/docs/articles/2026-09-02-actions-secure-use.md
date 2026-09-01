---
title: 보장할 수 없는 것을 먼저 말하는 표현
description: 안전장치의 한계를 인정하고, 조건을 좁히고, 유일한 수단과 차선을 갈라 놓는 문장 5개.
weight: -13
date: 2026-09-02
source: "GitHub Docs — Secure use reference (GitHub Actions)"
sourceURL: https://docs.github.com/en/actions/reference/security/secure-use
---

# 보장할 수 없는 것을 먼저 말하는 표현

GitHub Actions의 'Secure use reference'는 워크플로를 쓸 때의 보안 권고를 모아 놓은 문서다.
권고 문서인데도 자기가 제공하는 안전장치를 자랑하지 않고 **어디까지만 동작하는지**부터 말하는
점이 특이해서 골랐다. 자동 마스킹이 왜 보장되지 않는지, 어떤 조건에서만 걸리는지, 왜 하필
그 조치를 권하는지, 무엇이 유일한 방법이고 무엇이 편의를 위한 차선인지를 각각 다른 문형으로
적어 놓는다. 런북, 보안 가이드, 감사 소견처럼 **내가 만든 장치의 한계를 스스로 적어야 하는
글**에 그대로 옮겨 쓸 틀만 다섯 개 뽑았다.

> **원문** — GitHub Docs, *Secure use reference*,
> [docs.github.com](https://docs.github.com/en/actions/reference/security/secure-use)
> ([github.com/github/docs](https://github.com/github/docs/blob/main/content/actions/reference/security/secure-use.md)),
> [CC BY 4.0](https://github.com/github/docs/blob/main/LICENSE).
>
> 영어 문장은 원문 그대로 인용했고, 한글 설명과 응용 문장은 이 노트에서 새로 쓴 것이다.

{{< sentence
  en="Because there are multiple ways a secret value can be transformed, automatic redaction is not guaranteed."
  ko="시크릿 값이 변형될 수 있는 경로가 여럿이기 때문에, 자동 마스킹은 보장되지 않는다."
  source="GitHub Docs · Secure use reference"
  sourceURL="https://docs.github.com/en/actions/reference/security/secure-use"
  note="`Because there are multiple ways A can happen, B is not guaranteed.` — 자기가 제공하는 안전장치의 **보장을 스스로 거둬들이는** 문형이다. 순서가 핵심인데, 이유를 앞에 두고 결론을 뒤에 둔다. 결론부터 말하면(`Automatic redaction is not guaranteed because...`) 못 한다는 고백으로 들리지만, 이유를 먼저 깔면 **원리상 불가능하다**는 설명이 된다. 같은 사실인데 책임의 위치가 달라진다. `multiple ways`도 계산된 표현이다. 구체적으로 몇 가지인지 세지 않으므로 목록을 방어할 필요가 없고, 그 목록이 앞으로 늘어나도 문장이 틀리지 않는다. 그리고 `not guaranteed`는 동작하지 않는다가 아니라 **보장의 범위만** 부인하므로, 그 기능을 계속 쓰라고 권하면서도 거기 기대지는 말라고 말할 수 있다. 탐지 규칙, 자동 스캔, 마스킹처럼 내가 만든 장치를 남에게 넘길 때 그 한계를 적는 첫 문장으로 쓴다."
  app1="Because there are multiple paths a request can take into the cluster, the audit log is not guaranteed to show every caller."
  app1ko="요청이 클러스터로 들어오는 경로가 여럿이기 때문에, 감사 로그가 모든 호출자를 보여 준다고 보장되지 않는다."
  app2="Because there are multiple ways a job can exit early, the cleanup step is not guaranteed to run."
  app2ko="잡이 일찍 종료될 수 있는 경로가 여럿이기 때문에, 정리 단계가 실행된다고 보장되지 않는다."
>}}

{{< sentence
  en="Redacting of secrets is performed by your workflow runners. This means a secret will only be redacted if it was used within a job and is accessible by the runner."
  ko="시크릿 마스킹은 워크플로 러너가 수행한다. 즉 시크릿은 잡 안에서 사용되었고 러너가 접근할 수 있을 때만 마스킹된다."
  source="GitHub Docs · Secure use reference"
  sourceURL="https://docs.github.com/en/actions/reference/security/secure-use"
  note="`X is performed by Y. This means X only happens if A and B.` — **어디서 실행되는지를 먼저 말하고, 거기서 조건을 끌어내는** 2단 구성이다. 규칙을 외우게 하지 않고 위치를 알려 주는 방식이라, 읽는 사람이 문서에 없는 상황도 스스로 판단할 수 있게 된다. 조건을 먼저 나열하고 이유를 붙이는 순서였다면 그냥 예외 목록이 됐을 것이다. `only ... if`의 자리도 눈여겨볼 만하다. `only`가 조동사 뒤에 붙어(`will only be redacted`) 부정하는 대상이 **마스킹되는 경우의 범위**로 좁혀진다. 문두로 옮기면(`Only if...`) 강조가 조건 쪽으로 쏠려 경고문처럼 읽힌다. 그리고 두 조건을 `and`로 묶어 둘 다 필요하다는 것을 명시한다. 로그 수집기, 알림 라우팅, 권한 검사처럼 **동작하는 위치가 곧 사각지대를 결정하는** 것을 설명할 때 쓴다."
  app1="Rate limiting is enforced by the edge proxy. This means a request will only be counted if it entered through the public endpoint and carried a resolvable client identity."
  app1ko="레이트 리밋은 엣지 프록시가 적용한다. 즉 요청은 공개 엔드포인트로 들어왔고 식별 가능한 클라이언트 신원을 달고 있을 때만 집계된다."
  app2="Deduplication is performed by the alert manager. This means two pages will only be merged if they arrived within the grouping window and carry the same alert name."
  app2ko="중복 제거는 얼럿 매니저가 수행한다. 즉 두 호출은 그룹핑 구간 안에 도착했고 같은 얼럿 이름을 달고 있을 때만 하나로 합쳐진다."
>}}

{{< sentence
  en="Rotate secrets periodically to reduce the window of time during which a compromised secret is valid."
  ko="시크릿을 주기적으로 교체해 탈취된 시크릿이 유효한 시간 구간을 줄여라."
  source="GitHub Docs · Secure use reference"
  sourceURL="https://docs.github.com/en/actions/reference/security/secure-use"
  note="`Do X periodically to reduce the window of time during which Y.` — 조치를 시키면서 **그 조치가 무엇을 줄이는지**를 같은 문장에 박아 넣는 문형이다. 목적을 `to`절로 붙였을 뿐인데 효과가 크다. 권고가 규칙이 아니라 **거래**가 되기 때문이다. 주기를 얼마로 할지 다투는 사람도 이제 줄이려는 것이 무엇인지를 두고 다투게 된다. 핵심 표현은 `the window of time during which`다. 위험을 없앤다고 하지 않고 **유효한 구간의 길이**로 바꿔 말하므로, 지킬 수 없는 약속을 하지 않으면서도 무엇이 나아지는지는 분명해진다(`to prevent leaks`였다면 한 번만 새도 거짓말이 된다). 교체 주기, 토큰 수명, 캐시 TTL처럼 **완전한 차단이 불가능한 대상**에 값을 정할 때 그 근거로 쓴다."
  app1="Expire staging credentials nightly to reduce the window of time during which a leaked token still reaches production data."
  app1ko="스테이징 자격 증명을 매일 밤 만료시켜 유출된 토큰이 운영 데이터에 아직 닿을 수 있는 시간 구간을 줄여라."
  app2="Review the on-call handover notes at the start of each shift to reduce the window of time during which a known issue goes unattributed."
  app2ko="교대를 시작할 때마다 온콜 인수인계 노트를 확인해 이미 알려진 문제가 주인 없이 떠도는 시간 구간을 줄여라."
>}}

{{< sentence
  en="Pinning an action to a full-length commit SHA is currently the only way to use an action as an immutable release."
  ko="액션을 전체 길이 커밋 SHA에 고정하는 것이 현재로서는 액션을 불변 릴리스로 쓰는 유일한 방법이다."
  source="GitHub Docs · Secure use reference"
  sourceURL="https://docs.github.com/en/actions/reference/security/secure-use"
  note="`X is currently the only way to Y.` — 여러 방법이 있어 보이는 자리에서 **하나만 남기는** 문형이다. 유일하다는 주장은 반박당하기 쉬운데, 이 문장은 두 장치로 그것을 버틴다. 하나는 `currently`다. 시점을 붙여 두면 나중에 다른 방법이 생겨도 문장이 틀린 것이 아니라 **낡은 것**이 되므로, 지금 강하게 말하고도 나중에 물러설 자리가 남는다. 다른 하나는 목적을 `to use an action as an immutable release`로 좁게 못 박은 것이다. 안전하게 쓰는 유일한 방법이라고 했다면 태그도 안전하다는 반례가 바로 나오지만, **불변 릴리스로 쓰는 것**이 목적이면 태그는 정의상 자격이 없다. 유일성을 주장할 때는 이렇게 목적어를 좁히는 편이 근거를 늘리는 것보다 낫다. 표준을 정하거나 예외 요청을 거절할 때 쓴다."
  app1="Recording the image digest in the deploy manifest is currently the only way to know afterwards which build actually ran."
  app1ko="배포 매니페스트에 이미지 다이제스트를 적어 두는 것이 현재로서는 어떤 빌드가 실제로 돌았는지 나중에 알 수 있는 유일한 방법이다."
  app2="Reproducing the failure on a clean environment is currently the only way to rule out local state as the cause."
  app2ko="깨끗한 환경에서 실패를 재현하는 것이 현재로서는 로컬 상태를 원인에서 배제할 수 있는 유일한 방법이다."
>}}

{{< sentence
  en="Although pinning to a commit SHA is the most secure option, specifying a tag is more convenient and is widely used."
  ko="커밋 SHA에 고정하는 것이 가장 안전한 선택이긴 하지만, 태그를 지정하는 쪽이 더 편리하고 널리 쓰인다."
  source="GitHub Docs · Secure use reference"
  sourceURL="https://docs.github.com/en/actions/reference/security/secure-use"
  note="`Although X is the most secure option, Y is more convenient and is widely used.` — 자기가 권한 것을 **모두가 따르지는 않는다는 사실을 문서에 적어 넣는** 양보 문형이다. 앞 문장에서 유일한 방법이라고 못 박은 직후에 이 문장이 오는 배치가 중요하다. 권고를 취소하지 않으면서 현실을 인정하는 자리를 만들고, 그래서 뒤에 이어지는 태그 사용 시 주의사항이 **타협이 아니라 준비된 안내**가 된다. 종속절과 주절의 무게가 뒤집혀 있는 것도 보라. 양보절에 최상급(`the most secure`)을 넣고 주절에는 편리하다는 약한 근거를 두었으니 논리적으로는 앞이 세지만, 주절이 결론 자리를 차지하므로 **읽는 사람의 실제 선택**이 문장의 결론이 된다. `is widely used`가 마지막에 오는 것도 계산이다. 필자의 판단이 아니라 관찰된 사실이라 반박할 대상이 없다. 원칙과 관행이 어긋나는 것을 알면서 가이드를 써야 할 때 쓴다."
  app1="Although reviewing every dependency bump by hand is the most secure option, batching them into a weekly pull request is faster and is what most teams do."
  app1ko="의존성 갱신을 하나하나 손으로 검토하는 것이 가장 안전한 선택이긴 하지만, 주 단위 풀 리퀘스트로 묶는 쪽이 더 빠르고 대부분의 팀이 그렇게 한다."
  app2="Although paging the service owner directly is the most reliable option, posting in the team channel is less disruptive and is what happens most nights."
  app2ko="서비스 담당자를 직접 호출하는 것이 가장 확실한 선택이긴 하지만, 팀 채널에 올리는 쪽이 덜 방해가 되고 실제로 대부분의 밤에는 그렇게 한다."
>}}
