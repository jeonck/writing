---
title: 근거를 대며 구조를 바꾸자고 말하는 표현
description: 용도를 한정해 이점만 주장하고, 아직 오지 않은 예외를 미리 꺼내고, 위험을 메커니즘으로 보여주고, 내가 안 건드려도 바뀐다는 전제를 깨고, 대안은 한 줄로 끊는 문장 5개.
weight: -51
date: 2026-10-11
source: "Argo CD Docs · Best Practices"
sourceURL: https://argo-cd.readthedocs.io/en/stable/user-guide/best_practices/
---

# 근거를 대며 구조를 바꾸자고 말하는 표현

GitOps 배포 도구 Argo CD의 공식 문서 중 Best Practices 페이지다. 애플리케이션 코드와
쿠버네티스 매니페스트를 왜 다른 저장소에 두는지, 어떤 것은 일부러 Git에 적지 않는지,
외부 베이스를 핀으로 고정하지 않으면 무엇이 조용히 깨지는지를 짧게 적어 둔 문서다.
권고 자체보다 **근거를 어디까지만 주장하는지**가 배울 점이라 골랐다 — 이점은 감사라는
용도에 한정하고, 반론이 될 예외는 먼저 꺼내 두고, 위험은 겁주는 대신 경로를 그려 보이고,
대안은 한 줄로 끊는다. 구조를 바꾸자고 설득할 때, 리뷰에서 핀 고정 없는 의존성을 문제
삼을 때, 자동화끼리 서로를 호출하는 사고를 지적할 때 그대로 틀을 가져다 쓸 수 있다.

> **원문** — The Argo Authors, *Best Practices*,
> [argoproj/argo-cd](https://github.com/argoproj/argo-cd/blob/master/docs/user-guide/best_practices.md)
> (문서 사이트: [Argo CD Docs — Best Practices](https://argo-cd.readthedocs.io/en/stable/user-guide/best_practices/)),
> [Apache-2.0](https://github.com/argoproj/argo-cd/blob/master/LICENSE) 라이선스.
>
> 영어 문장은 원문 그대로 인용했고, 한글 설명과 응용 문장은 이 노트에서 새로 쓴 것이다.

{{< sentence
  en="For auditing purposes, a repo which only holds configuration will have a much cleaner Git history of what changes were made, without the noise coming from check-ins due to normal development activity."
  ko="감사 목적에서 보면, 설정만 담는 저장소는 어떤 변경이 이루어졌는지에 대해 훨씬 깔끔한 Git 이력을 갖게 된다. 평소 개발 활동에서 생기는 체크인이 만드는 소음이 없기 때문이다."
  source="Argo CD Docs · Separating Config Vs. Source Code Repositories"
  sourceURL="https://argo-cd.readthedocs.io/en/stable/user-guide/best_practices/"
  note="`For auditing purposes, X will have a much cleaner Y, without the noise coming from Z.` — 이점을 주장하기 전에 **그 이점이 성립하는 용도를 먼저 못 박는** 틀이다. `For auditing purposes`가 문장의 사정거리를 좁힌다. 저장소를 쪼개는 쪽이 언제나 낫다고는 말하지 않고 감사라는 한 관점에서만 낫다고 말하므로, 다른 관점을 든 반박이 이 문장을 무너뜨리지 못한다. `much cleaner`는 비교급인데 비교 대상을 적지 않은 것도 의도적이다 — 상대의 현재 저장소를 지목해 깎지 않는다. 마지막 `without the noise coming from ~`은 **빼기로 이득을 설명하는** 방식이다. 무엇이 좋아지는지 말하는 대신 무엇이 사라지는지 말하면, 읽는 사람이 자기 이력을 떠올리며 스스로 납득한다. 로그·지표·이력을 갈라 두자고 제안할 때 쓴다."
  app1="For auditing purposes, a log stream which only holds privileged actions will have a much clearer trail of who did what, without the noise coming from health checks firing every second."
  app1ko="감사 목적에서 보면, 권한 있는 동작만 담는 로그 스트림은 누가 무엇을 했는지에 대해 훨씬 또렷한 기록을 남긴다. 매초 도는 헬스 체크가 만드는 소음이 없기 때문이다."
  app2="For incident review purposes, a timeline which only holds operator actions will have a much clearer sequence of what was tried, without the noise coming from alerts re-firing every five minutes."
  app2ko="장애 리뷰 목적에서 보면, 운영자의 조치만 담는 타임라인은 무엇을 시도했는지에 대해 훨씬 또렷한 순서를 보여 준다. 5분마다 다시 울리는 알림이 만드는 소음이 없기 때문이다."
>}}

{{< sentence
  en="There will be times when you wish to modify just the manifests without triggering an entire CI build."
  ko="매니페스트만 고치고 CI 빌드 전체는 돌리지 않고 싶은 때가 있을 것이다."
  source="Argo CD Docs · Separating Config Vs. Source Code Repositories"
  sourceURL="https://argo-cd.readthedocs.io/en/stable/user-guide/best_practices/"
  note="`There will be times when you wish to A without B.` — 지금은 문제가 아닌 **예외를 미리 꺼내 근거로 쓰는** 틀이다. 빈도를 숫자로 대지 않고도 드물지만 분명히 있다는 말을 확보한다. `sometimes you may want to`보다 센 이유는 가능성이 아니라 **예정된 사실**로 적기 때문이다 — `will`은 그 상황이 올지를 논점에서 빼 버린다. 주어가 `you`인 것도 중요하다. 내 불편이 아니라 읽는 사람의 불편으로 돌려놓으면, 구조를 바꾸자는 요구가 개인 취향으로 보이지 않는다. 뒤에 붙는 `without B`가 실제 쟁점이다. 하고 싶은 일(A)과 거기에 딸려 오는 비용(B)을 한 문장에 나란히 놓아, 지금 구조에서는 둘을 떼어낼 수 없다는 사실을 설명 없이 드러낸다."
  app1="There will be times when you wish to roll back the config without redeploying the binary."
  app1ko="바이너리는 다시 배포하지 않고 설정만 되돌리고 싶은 때가 있을 것이다."
  app2="There will be times when you wish to silence one alert without putting the whole service into maintenance mode."
  app2ko="서비스 전체를 점검 모드로 넣지 않고 알림 하나만 끄고 싶은 때가 있을 것이다."
>}}

{{< sentence
  en="If you are automating your CI pipeline, pushing manifest changes to the same Git repository can trigger an infinite loop of build jobs and Git commit triggers."
  ko="CI 파이프라인을 자동화하고 있다면, 같은 Git 저장소에 매니페스트 변경을 푸시하는 일이 빌드 잡과 Git 커밋 트리거의 무한 루프를 일으킬 수 있다."
  source="Argo CD Docs · Separating Config Vs. Source Code Repositories"
  sourceURL="https://argo-cd.readthedocs.io/en/stable/user-guide/best_practices/"
  note="`If you are doing A, doing B can trigger an infinite loop of X and Y.` — 조건절로 **해당되는 사람만 골라낸 뒤** 그 사람에게만 실패 경로를 보여주는 틀이다. `If you are automating ~`은 진행형이라 상대가 자기 상황인지 바로 판단한다. `If you automate`로 쓰면 일반론이 되지만 진행형은 지금 네 파이프라인 이야기가 된다. 핵심은 `can trigger` 뒤에 위험의 **이름이 아니라 메커니즘**을 적은 것이다. `an infinite loop of build jobs and Git commit triggers`처럼 루프를 이루는 두 축을 나란히 세우면 읽는 사람이 머릿속에서 순환을 한 바퀴 돌려 볼 수 있고, 그러면 겁주려 과장한다는 의심이 생기지 않는다. 자동화가 서로를 호출해 사고가 나는 구조를 리뷰에서 지적할 때 쓴다."
  app1="If you are auto-formatting on commit, letting the bot push to the same branch can trigger an infinite loop of format commits and lint jobs."
  app1ko="커밋할 때 자동 포매팅을 돌리고 있다면, 봇이 같은 브랜치로 푸시하게 두는 일이 포맷 커밋과 린트 잡의 무한 루프를 일으킬 수 있다."
  app2="If you are mirroring alerts into the ticket system, opening a ticket on every status change can trigger an infinite loop of ticket updates and webhook deliveries."
  app2ko="알림을 티켓 시스템으로 미러링하고 있다면, 상태가 바뀔 때마다 티켓을 여는 일이 티켓 업데이트와 웹훅 전달의 무한 루프를 일으킬 수 있다."
>}}

{{< sentence
  en="The above kustomization has a remote base to the HEAD revision of the argo-cd repo. Since this is not a stable target, the manifests for this kustomize application can suddenly change meaning, even without any changes to your own Git repository."
  ko="위 kustomization은 argo-cd 저장소의 HEAD 리비전을 원격 베이스로 가리킨다. 이것은 고정된 대상이 아니므로, 이 kustomize 애플리케이션의 매니페스트는 내 Git 저장소에 아무 변경이 없어도 갑자기 의미가 달라질 수 있다."
  source="Argo CD Docs · Ensuring Manifests At Git Revisions Are Truly Immutable"
  sourceURL="https://argo-cd.readthedocs.io/en/stable/user-guide/best_practices/"
  note="`Since this is not a stable target, X can suddenly change meaning, even without any changes to your own Y.` — 가만히 있었는데도 결과가 달라지는 일을 설명하는 틀이다. `Since`는 `because`와 달리 상대가 이미 아는 사실을 근거로 끌어오는 접속사라, 지적이 아니라 확인처럼 들린다. 진짜 일을 하는 건 끝의 `even without any changes to your own ~`이다. 사람은 내가 안 건드렸으니 그대로일 것이라는 전제로 디버깅을 시작하므로, 그 전제를 문장 안에서 먼저 깨 주지 않으면 원인 추적이 아예 시작되지 않는다. `change meaning`이라는 말도 가져다 쓸 만하다 — 파일이 바뀐다고 하지 않고 **뜻이 바뀐다**고 적어, 같은 커밋을 보고 있는데 결과가 다른 현상을 그대로 가리킨다. 핀을 고정하지 않은 의존성, 떠 있는 태그, 외부 설정에 기대는 동작을 문제 삼을 때 쓴다."
  app1="The job pulls its base image by the latest tag. Since this is not a stable target, the build can suddenly change meaning, even without any changes to your own Dockerfile."
  app1ko="그 잡은 base 이미지를 latest 태그로 가져온다. 이것은 고정된 대상이 아니므로, 빌드는 우리 Dockerfile에 아무 변경이 없어도 갑자기 의미가 달라질 수 있다."
  app2="The check reads its threshold from a shared config map. Since this is not a stable target, a green test run can suddenly change meaning, even without any changes to your own test code."
  app2ko="그 검사는 임계값을 공용 컨피그맵에서 읽는다. 이것은 고정된 대상이 아니므로, 테스트가 통과했다는 사실은 우리 테스트 코드에 아무 변경이 없어도 갑자기 의미가 달라질 수 있다."
>}}

{{< sentence
  en="A better version would be to use a Git tag or commit SHA."
  ko="더 나은 쪽은 Git 태그나 커밋 SHA를 쓰는 것이다."
  source="Argo CD Docs · Ensuring Manifests At Git Revisions Are Truly Immutable"
  sourceURL="https://argo-cd.readthedocs.io/en/stable/user-guide/best_practices/"
  note="`A better version would be to X.` — 고칠 것을 말하면서 지금 것을 틀렸다고는 하지 않는 제안 틀이다. 주어가 사람이 아니라 `version`, 즉 **코드의 판본**인 게 전부다. `You should use ~`는 상대의 선택을 교정하는 문장이고, 이 문장은 두 판본을 나란히 놓고 하나가 더 낫다고만 말한다 — 내용은 같아도 받는 쪽의 방어가 줄어든다. `would`도 일부러 가정법이다. 아직 존재하지 않는 판본을 가리키므로 쓸지 말지는 상대에게 남는다. 그리고 짧다. 코드 리뷰에서 대안을 낼 때는 근거를 앞 문장에 다 쏟고 제안 자체는 이렇게 한 줄로 끊는 편이 통과된다."
  app1="A better version would be to fail the request early instead of letting it time out at the gateway."
  app1ko="더 나은 쪽은 게이트웨이에서 타임아웃이 나게 두는 대신 요청을 일찍 실패시키는 것이다."
  app2="A better version would be to page on the error budget burn rate rather than on a single failed probe."
  app2ko="더 나은 쪽은 실패한 프로브 하나가 아니라 에러 예산 소진율에 호출을 거는 것이다."
>}}
