---
title: 누가 무엇을 맡는지 정하는 표현
description: 처리량의 상한을 진단하고, 도구 선택의 근거를 대고, 자격과 여력을 갈라 말하는 문장 5개.
weight: -36
date: 2026-09-26
source: "Kubernetes Contributor Guide — OWNERS Files"
sourceURL: https://github.com/kubernetes/community/blob/master/contributors/guide/owners.md
---

# 누가 무엇을 맡는지 정하는 표현

쿠버네티스가 `OWNERS` 파일로 코드베이스의 **책임 범위를 지정하고** reviewer와 approver 두 단계로
리뷰를 굴리는 방식을 설명하는 문서. 규칙을 나열하는 문서인데도 "왜 이 사람에게 더 높은 기준을
적용하는지", "왜 저 도구를 쓰지 않는지"를 매번 한 문장으로 붙여 놓아서, **권한과 책임을 나눠 맡기는
글에 그대로 쓸 문형**이 많다. 사람을 역할에서 내리는 문장을 어떻게 쓰는지도 볼 만해서 발췌했다.

> **원문** — Kubernetes community contributors, *OWNERS Files*,
> [kubernetes/community · contributors/guide/owners.md](https://github.com/kubernetes/community/blob/master/contributors/guide/owners.md)
> (master 브랜치, 2026-09-26 확인), [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0).
>
> 영어 문장은 원문 그대로 인용했고, 한글 설명과 응용 문장은 이 노트에서 새로 쓴 것이다.

{{< sentence
  en="The velocity of a project that uses code review is limited by the number of people capable of reviewing code. The quality of a person's code review is limited by their familiarity with the code under review. Our goal is to address both of these concerns through the prudent use and maintenance of OWNERS files."
  ko="코드 리뷰를 하는 프로젝트의 속도는 코드를 리뷰할 수 있는 사람의 수에 의해 제한된다. 한 사람의 코드 리뷰 품질은 리뷰 대상 코드에 대한 익숙함에 의해 제한된다. 우리의 목표는 OWNERS 파일을 분별 있게 쓰고 관리함으로써 이 두 가지 문제를 함께 다루는 것이다."
  source="Kubernetes Contributor Guide · OWNERS Files, Overview"
  sourceURL="https://github.com/kubernetes/community/blob/master/contributors/guide/owners.md"
  note="`The X of A is limited by B. The Y of A is limited by C.` — 같은 골격을 두 번 반복해 **서로 다투는 두 개의 상한**을 나란히 세우는 구조다. `limited by`는 '부족하다'는 불만이 아니라 '여기가 천장이다'라는 진단이어서, 원인을 사람 탓이 아니라 구조의 한계로 옮겨 놓는다. 두 상한이 반대 방향으로 당기는 것을 보여 준 다음 `Our goal is to address both of these concerns through ~`로 **둘을 한꺼번에 받는 수단**을 내놓는 게 이 단락의 설계다. 상충하는 요구를 정리하고 대책을 제안하는 문서의 도입부에 그대로 쓴다. `prudent`는 '신중한'보다 '분별 있게, 낭비 없이'에 가까워서, 규칙을 늘리자는 게 아니라 있는 것을 잘 쓰자는 뜻이 된다."
  app1="Our release cadence is limited by the number of engineers who can run a release. The safety of a release is limited by how recently that engineer has done one. Our goal is to address both of these concerns through a rotation that pairs a new releaser with a veteran."
  app1ko="우리 릴리스 주기는 릴리스를 진행할 수 있는 엔지니어의 수에 의해 제한된다. 릴리스의 안전성은 그 엔지니어가 얼마나 최근에 릴리스를 해 봤는지에 의해 제한된다. 우리의 목표는 신규 담당자와 숙련자를 짝지우는 로테이션으로 이 두 문제를 함께 다루는 것이다."
  app2="The number of audits we can close per quarter is limited by the number of reviewers with system access. The depth of each audit is limited by how well that reviewer knows the system."
  app2ko="분기에 마감할 수 있는 감사 건수는 시스템 접근 권한이 있는 검토자의 수에 의해 제한된다. 각 감사의 깊이는 그 검토자가 그 시스템을 얼마나 잘 아는지에 의해 제한된다."
>}}

{{< sentence
  en="We use aliases for groups instead of GitHub Teams, because changes to GitHub Teams are not publicly auditable."
  ko="우리는 그룹을 나타낼 때 GitHub Teams 대신 별칭을 쓴다. GitHub Teams의 변경은 공개적으로 감사할 수 없기 때문이다."
  source="Kubernetes Contributor Guide · OWNERS Files, OWNERS_ALIASES"
  sourceURL="https://github.com/kubernetes/community/blob/master/contributors/guide/owners.md"
  note="`We use A instead of B, because <B의 성질>.` — 선택을 설명하면서 **탈락한 쪽의 결격 사유 하나만** 대는 문형이다. A의 장점을 늘어놓지 않는 것이 핵심이다. 기준을 하나로 좁혀 놓으면 반박도 그 하나에만 걸리므로 논의가 짧게 끝난다. `not publicly auditable`처럼 `-able` 형용사에 `publicly`를 붙이면 '그 기능이 되냐 안 되냐'가 아니라 **바깥에서 누가 확인할 수 있느냐**로 기준이 옮겨 간다. 도구·저장 위치·기록 형식을 고른 이유를 적을 때 그대로 쓴다."
  app1="We keep approvals in pull requests instead of chat threads, because messages in chat are not publicly auditable."
  app1ko="우리는 승인 기록을 채팅 스레드가 아니라 풀 리퀘스트에 남긴다. 채팅 메시지는 공개적으로 감사할 수 없기 때문이다."
  app2="We grant access through a checked-in policy file instead of the console, because console changes are not reviewable before they take effect."
  app2ko="우리는 콘솔이 아니라 저장소에 커밋된 정책 파일로 권한을 부여한다. 콘솔에서 준 변경은 적용되기 전에 검토할 수 없기 때문이다."
>}}

{{< sentence
  en="These people may be domain experts over certain areas of the codebase, but can no longer dedicate the time needed to handle the responsibilities of reviewing and approving changes."
  ko="이 사람들은 코드베이스의 특정 영역에서 도메인 전문가일 수 있지만, 변경을 리뷰하고 승인하는 책임을 감당하는 데 필요한 시간을 더는 낼 수 없다."
  source="Kubernetes Contributor Guide · OWNERS Files, Emeritus"
  sourceURL="https://github.com/kubernetes/community/blob/master/contributors/guide/owners.md"
  note="`X may be <자격>, but can no longer dedicate the time needed to <책임>.` — 사람을 역할에서 내릴 때 **실력과 여력을 갈라 놓는** 문형이다. `may be`가 전문성을 먼저 인정해 주고, `no longer`가 변한 것은 능력이 아니라 상황임을 못 박는다. `dedicate the time needed to ~`는 '바쁘다'를 **책임에 필요한 시간**이라는 셀 수 있는 말로 바꿔 주기 때문에, 평가처럼 들리지 않으면서 결정을 설명할 수 있다. 온콜 로테이션이나 리뷰어 목록에서 누군가를 빼는 글에 쓴다."
  app1="The original author may still be the only person who knows this pipeline end to end, but can no longer dedicate the time needed to handle the responsibilities of primary on-call."
  app1ko="최초 작성자는 여전히 이 파이프라인을 처음부터 끝까지 아는 유일한 사람일 수 있지만, 1차 온콜의 책임을 감당하는 데 필요한 시간을 더는 낼 수 없다."
  app2="Our security lead may be the right reviewer for this design, but can no longer dedicate the time needed to handle every change that touches authentication."
  app2ko="보안 리드는 이 설계를 볼 적임자일 수 있지만, 인증을 건드리는 모든 변경을 감당하는 데 필요한 시간을 더는 낼 수 없다."
>}}

{{< sentence
  en="Those listed in OWNERS files have a higher activity requirement, as they directly impact the ability of others to contribute."
  ko="OWNERS 파일에 이름이 올라 있는 사람에게는 더 높은 활동 요건이 적용된다. 그들이 다른 사람의 기여 능력에 직접 영향을 주기 때문이다."
  source="Kubernetes Contributor Guide · OWNERS Files, Cleanup"
  sourceURL="https://github.com/kubernetes/community/blob/master/contributors/guide/owners.md"
  note="`Those who X have a higher Y requirement, as they directly impact Z.` — 같은 조직 안에서 **누구에게만 기준을 더 높이 적용하는지**를 정당화하는 문형이다. 근거가 '직책이 높으니까'가 아니라 `they directly impact the ability of others to ~`, 즉 **남의 일을 막을 수 있는 자리인가**로 잡혀 있다. 그래서 요건이 사람에 대한 평가가 아니라 자리에 붙은 조건이 된다. `as`는 `because`보다 목소리가 낮아 규정문에 어울린다. 승인자, 릴리스 담당, 관리자 권한 보유자처럼 권한을 가진 쪽에 추가 의무를 얹을 때 그대로 쓴다."
  app1="Those holding production credentials have a higher review requirement, as they directly impact the ability of others to trust the audit trail."
  app1ko="운영 환경 자격 증명을 가진 사람에게는 더 높은 검토 요건이 적용된다. 그들이 다른 사람이 감사 기록을 신뢰할 수 있는지에 직접 영향을 주기 때문이다."
  app2="Those who own a shared library have a higher response-time requirement, as they directly impact the ability of other teams to ship."
  app2ko="공용 라이브러리를 소유한 팀에는 더 높은 응답 시간 요건이 적용된다. 그들이 다른 팀의 배포 능력에 직접 영향을 주기 때문이다."
>}}

{{< sentence
  en="Drive-by reviews from non-members are encouraged as a way of demonstrating experience and intent to become a member or reviewer."
  ko="비구성원이 지나가며 남기는 리뷰는 구성원이나 리뷰어가 되려는 경험과 의지를 보여 주는 방법으로 권장된다."
  source="Kubernetes Contributor Guide · OWNERS Files, Quirks of the Process"
  sourceURL="https://github.com/kubernetes/community/blob/master/contributors/guide/owners.md"
  note="`X is encouraged as a way of demonstrating Y.` — 규정에 없는 자발적 행동을 막거나 방치하지 않고 **자격을 증명하는 경로로 다시 이름 붙이는** 문형이다. `encouraged`가 의무는 아니라는 여지를 남기고, `as a way of demonstrating ~`이 그 행동의 용도를 지정해 준다. 목적어에 `intent`까지 넣는 것이 포인트다 — 실력만이 아니라 **하겠다는 의사 표시**로도 읽어 준다는 뜻이어서, 아직 잘 못하는 사람도 그 문을 쓸 수 있게 된다. 권한이 없는 사람이 기여하려 할 때 길을 열어 주는 문장으로 쓴다."
  app1="Shadowing an on-call shift is encouraged as a way of demonstrating readiness and intent to join the rotation."
  app1ko="온콜 근무를 따라붙어 지켜보는 것은 로테이션에 합류할 준비와 의지를 보여 주는 방법으로 권장된다."
  app2="Writing up a postmortem for an incident you did not handle is encouraged as a way of demonstrating judgment and intent to take on incident command."
  app2ko="자신이 대응하지 않은 장애의 포스트모템을 정리해 보는 것은 판단력과 인시던트 커맨더를 맡겠다는 의지를 보여 주는 방법으로 권장된다."
>}}
