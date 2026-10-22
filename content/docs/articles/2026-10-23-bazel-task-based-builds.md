---
title: 권한을 준 대가를 짚고, 판단을 시스템에 넘기는 표현
description: 장점을 원인 삼아 단점을 꺼내고, 안전하냐는 질문에 조건 두 개로 답하고, 좋음의 기준을 먼저 못 박고, 사람들이 쓰는 우회로를 증거로 삼고, 일의 담당자를 사람에서 기계로 옮기는 문장 5개.
weight: -63
date: 2026-10-23
source: "Bazel Docs · Task-Based Build Systems"
sourceURL: https://bazel.build/basics/task-based-builds
---

# 권한을 준 대가를 짚고, 판단을 시스템에 넘기는 표현

Bazel 문서 중 빌드 시스템의 역사를 설명하는 장. Ant·Maven·Gradle 같은 태스크 기반
빌드 시스템이 왜 한계에 부딪히는지를 **기능 비교가 아니라 논증으로** 끌고 간다.
"엔지니어에게 너무 많은 권한을 주고 시스템에는 너무 적게 준다"는 한 줄을 세우고,
병렬화·증분 빌드·디버깅 순서로 그 주장을 떠받친다. 도구를 깎지 않으면서 도구를
바꾸자고 설득하는 문장들이라 그대로 가져다 쓸 만해서 발췌했다.

> **원문** — The Bazel Authors, *Task-Based Build Systems*,
> [Bazel Documentation](https://bazel.build/basics/task-based-builds)
> ([원본 리포지터리](https://github.com/bazelbuild/bazel/blob/master/docs/basics/task-based-builds.mdx)),
> [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0).
>
> 영어 문장은 원문 그대로 인용했고, 한글 설명과 응용 문장은 이 노트에서 새로 쓴 것이다.

{{< sentence
  en="Because these tools essentially let engineers define any script as a task, they are extremely powerful, allowing you to do pretty much anything you can imagine with them. But that power comes with drawbacks, and task-based build systems can become difficult to work with as their build scripts grow more complex."
  ko="이 도구들은 사실상 엔지니어가 어떤 스크립트든 태스크로 정의할 수 있게 해 주기 때문에 대단히 강력하고, 상상할 수 있는 거의 모든 일을 할 수 있게 해 준다. 하지만 그 힘에는 대가가 따르고, 태스크 기반 빌드 시스템은 빌드 스크립트가 복잡해질수록 다루기 어려워질 수 있다."
  source="Bazel Docs · Task-Based Build Systems"
  sourceURL="https://bazel.build/basics/task-based-builds"
  note="`Because X lets you do anything, it is extremely powerful. But that power comes with drawbacks, and ...` — 장점을 끝까지 인정한 다음 **그 장점 자체를 원인으로 삼아** 단점을 꺼내는 문형이다. 핵심은 `that power`에 있다. 새 주어를 세우지 않고 방금 칭찬한 것을 지시대명사로 그대로 받기 때문에, 뒤 문장이 반대 의견이 아니라 **같은 성질의 뒷면**으로 읽힌다. 끝에 붙은 `as their build scripts grow more complex`도 계산된 자리다. 단점을 지금이 아니라 규모가 커진 뒤로 미뤄 놓아서, 그 도구를 잘 쓰고 있는 사람을 공격하지 않는다. 유연한 도구나 넓은 권한을 회수하자고 제안할 때 이 순서를 쓴다."
  app1="Because the on-call role can run any kubectl command in production, it is extremely flexible, letting us recover from incidents we never planned for. But that flexibility comes with drawbacks, and the audit trail gets harder to read as more of the recovery happens by hand."
  app1ko="온콜 역할은 운영 환경에서 어떤 kubectl 명령이든 실행할 수 있기 때문에 대단히 유연하고, 계획에 없던 장애에서도 복구할 수 있게 해 준다. 하지만 그 유연함에는 대가가 따르고, 복구가 수작업으로 이뤄질수록 감사 추적을 읽기가 어려워진다."
  app2="Because the config loader accepts arbitrary Python, it is extremely powerful, allowing each team to express whatever rollout logic they want. But that power comes with drawbacks, and reviewing a config change turns into a full code review as these files grow."
  app2ko="설정 로더가 임의의 파이썬 코드를 받아들이기 때문에 대단히 강력하고, 각 팀이 원하는 어떤 롤아웃 로직이든 표현할 수 있게 해 준다. 하지만 그 힘에는 대가가 따르고, 파일이 커질수록 설정 변경 하나를 보는 일이 사실상 코드 리뷰가 된다."
>}}

{{< sentence
  en="Because tasks B and C have no dependency on each other, is it safe to run them at the same time so that the system can more quickly get to task A? Maybe, if they don’t touch any of the same resources. But maybe not—perhaps both use the same file to track their statuses and running them at the same time causes a conflict."
  ko="태스크 B와 C는 서로 의존하지 않으니, 시스템이 태스크 A에 더 빨리 도달하도록 둘을 동시에 실행해도 안전할까? 아마도 — 둘이 같은 자원을 하나도 건드리지 않는다면. 하지만 아닐 수도 있다. 어쩌면 둘 다 같은 파일에 자기 상태를 기록하고 있어서, 동시에 돌리면 충돌이 날지도 모른다."
  source="Bazel Docs · Task-Based Build Systems"
  sourceURL="https://bazel.build/basics/task-based-builds"
  note="`Is it safe to X? Maybe, if A. But maybe not—perhaps B.` — 스스로 질문을 던지고 **예/아니오 대신 조건 두 개로 답하는** 문형이다. `Maybe, if ~`가 긍정을 조건에 묶어 두고, `But maybe not—perhaps ~`가 그 조건이 깨지는 **구체적인 장면 하나**를 든다. 그냥 '경우에 따라 다르다'와 갈리는 지점이 여기다. 반례를 하나 들어 줘야 상대가 자기 상황을 대입해 본다. 대시 뒤의 `perhaps`는 그 반례가 확인된 사실이 아니라 **아직 배제하지 못한 가능성**임을 표시하는 장치라서, 틀려도 말이 남지 않는다. 안전하냐고 묻는 사람에게 된다/안 된다로 답할 수 없을 때, 발을 빼지 않으면서 판단 조건을 돌려주는 방법."
  app1="Because the two jobs read from different shards, is it safe to replay them in parallel so that we can clear the backlog before the morning peak? Maybe, if they don’t write to the same summary table. But maybe not—perhaps both update the same daily counter and running them together double-counts it."
  app1ko="두 작업은 서로 다른 샤드에서 읽으니, 아침 피크 전에 밀린 처리를 비우도록 둘을 병렬로 재처리해도 안전할까? 아마도 — 둘이 같은 요약 테이블에 쓰지 않는다면. 하지만 아닐 수도 있다. 어쩌면 둘 다 같은 일일 카운터를 갱신하고 있어서, 함께 돌리면 두 번 세어질지도 모른다."
  app2="Because the reporting account only has read permissions, is it safe to hand it to the vendor so that they can pull the numbers themselves? Maybe, if the tables it can read hold no personal data. But maybe not—perhaps one of the views joins in the customer email column and nobody has looked at it since it was created."
  app2ko="그 리포팅 계정은 읽기 권한만 있으니, 벤더가 직접 수치를 뽑아 가도록 계정을 넘겨도 안전할까? 아마도 — 그 계정이 읽을 수 있는 테이블에 개인정보가 없다면. 하지만 아닐 수도 있다. 어쩌면 뷰 하나가 고객 이메일 컬럼을 조인해 두었고, 만들어진 뒤로 아무도 들여다보지 않았을지도 모른다."
>}}

{{< sentence
  en="A good build system allows engineers to perform reliable incremental builds such that a small change doesn’t require the entire codebase to be rebuilt from scratch."
  ko="좋은 빌드 시스템은 엔지니어가 믿을 수 있는 증분 빌드를 할 수 있게 해 준다 — 작은 변경 하나 때문에 코드베이스 전체를 처음부터 다시 빌드하지 않아도 되도록."
  source="Bazel Docs · Task-Based Build Systems"
  sourceURL="https://bazel.build/basics/task-based-builds"
  note="`A good X allows Y to Z such that W.` — 무언가를 비판하기 전에 **좋음의 기준을 먼저 한 문장으로 못 박는** 문형이다. 잣대를 미리 공개하는 셈이라, 뒤에 오는 지적이 '마음에 안 든다'가 아니라 '이 기준에 못 미친다'가 된다. 실제 일은 `such that` 절이 한다. `allows ... incremental builds`까지는 기능 이름일 뿐이고, `such that a small change doesn’t require ...`가 그 기능이 충족해야 할 **관찰 가능한 조건**을 붙인다. 기준을 기능 이름에서 끊으면 아무도 반박할 수 없고 아무것도 판정할 수 없다. 도구 선정서, 설계 리뷰, SLO 합의처럼 평가가 뒤따르는 문서의 첫 문단에 놓는다."
  app1="A good alerting setup allows the on-call engineer to act on a page such that no alert requires opening three dashboards before deciding whether it matters."
  app1ko="좋은 알림 체계는 온콜 엔지니어가 호출 하나만 보고 바로 움직일 수 있게 해 준다 — 어떤 알림도 중요한지 아닌지 판단하려고 대시보드를 세 개씩 열어 봐야 하는 일이 없도록."
  app2="A good review checklist allows a reviewer to finish in one sitting such that a disagreement doesn’t require the author to guess which comment is blocking the merge."
  app2ko="좋은 리뷰 체크리스트는 리뷰어가 한자리에서 리뷰를 끝낼 수 있게 해 준다 — 의견이 갈릴 때 작성자가 어느 코멘트가 머지를 막고 있는지 추측하지 않아도 되도록."
>}}

{{< sentence
  en="When this happens frequently, engineers get into the habit of running clean before every build to get a fresh state, completely defeating the purpose of having an incremental build in the first place."
  ko="이런 일이 잦아지면 엔지니어들은 깨끗한 상태를 얻으려고 빌드할 때마다 먼저 clean을 돌리는 습관을 들이게 되고, 그러면 애초에 증분 빌드를 둔 목적이 완전히 무너진다."
  source="Bazel Docs · Task-Based Build Systems"
  sourceURL="https://bazel.build/basics/task-based-builds"
  note="`When this happens frequently, people get into the habit of X, completely defeating the purpose of Y in the first place.` — 사람을 탓하지 않고 **제도가 길러 낸 우회 행동**을 적는 문형이다. 주어는 `engineers`지만 원인은 앞 문장의 `this`에 걸려 있고, `get into the habit of`가 그 행동을 개인의 판단이 아니라 **쌓여서 굳은 습관**으로 그린다. 결정타는 분사구문 `completely defeating the purpose of ~ in the first place`인데, 비용을 '느려졌다'가 아니라 **'이 기능을 왜 만들었는지가 사라졌다'**로 환산한다. `in the first place`가 있어야 시선이 지금의 불편에서 애초의 목적으로 돌아간다. 포스트모템이나 프로세스 개선 제안에서, 사람들이 우회로를 쓰고 있다는 사실 자체를 증거로 들 때."
  app1="When this happens frequently, developers get into the habit of rerunning the pipeline until it goes green, completely defeating the purpose of gating merges on tests in the first place."
  app1ko="이런 일이 잦아지면 개발자들은 초록불이 뜰 때까지 파이프라인을 다시 돌리는 습관을 들이게 되고, 그러면 애초에 테스트로 머지를 막아 둔 목적이 완전히 무너진다."
  app2="When this happens frequently, teams get into the habit of requesting the broad admin role up front, completely defeating the purpose of handing out scoped permissions in the first place."
  app2ko="이런 일이 잦아지면 팀들은 처음부터 넓은 관리자 역할을 신청하는 습관을 들이게 되고, 그러면 애초에 권한을 잘게 쪼개 내준 목적이 완전히 무너진다."
>}}

{{< sentence
  en="Figuring out when a task needs to be rerun is surprisingly subtle, and is a job better handled by machines than humans."
  ko="태스크를 언제 다시 돌려야 하는지 알아내는 일은 생각보다 까다롭고, 사람보다 기계가 맡는 편이 나은 일이다."
  source="Bazel Docs · Task-Based Build Systems"
  sourceURL="https://bazel.build/basics/task-based-builds"
  note="`Doing X is surprisingly subtle, and is a job better handled by A than B.` — 어떤 일을 사람 손에서 떼어 낼 때 쓰는 2단 문형이다. 먼저 `surprisingly subtle`이 **쉬워 보인다는 통념을 인정하면서 뒤집는다**. '어렵다'가 아니라 '보기보다 까다롭다'여서, 지금 그 일을 하고 있는 사람의 체면이 상하지 않는다. 그다음 `a job better handled by A than B`가 담당자를 바꾸자고 제안하는데, 비교급으로 적었기 때문에 사람이 **못한다**가 아니라 **적임이 아니다**가 된다. 같은 결론을 `humans are bad at this`로 적으면 논증이 인신공격으로 바뀐다. 자동화 도입, 수기 체크리스트 폐지, 리뷰 항목을 린터로 옮기자는 제안에 쓴다."
  app1="Deciding which import ordering a file should use is surprisingly subtle, and is a job better handled by the formatter than by reviewers."
  app1ko="어떤 파일이 어떤 임포트 순서를 써야 하는지 정하는 일은 생각보다 까다롭고, 리뷰어보다 포매터가 맡는 편이 나은 일이다."
  app2="Working out which of last night’s alerts belonged to the same incident is surprisingly subtle, and is a job better handled by correlation rules than by whoever writes the morning summary."
  app2ko="어젯밤 알림들 가운데 어느 것이 같은 장애에 속하는지 가려내는 일은 생각보다 까다롭고, 아침 요약을 쓰는 사람보다 상관 규칙이 맡는 편이 나은 일이다."
>}}
