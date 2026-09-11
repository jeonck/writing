---
title: 규칙이 맡는 몫과 맡지 않는 몫을 나누는 표현
description: 금지 조합을 규칙으로 정의하고, 무엇을 넣어야 무엇이 나오는지 묶고, 아직 못 하는 자리에 할 수 있는 것을 내밀고, 요구 사항을 가정법으로 못 박고, 특별 취급이 없다고 선언하는 문장 5개.
weight: -23
date: 2026-09-12
source: "OPA Documentation — Access Control Systems"
sourceURL: https://openpolicyagent.org/docs/comparisons/access-control-systems
---

# 규칙이 맡는 몫과 맡지 않는 몫을 나누는 표현

Open Policy Agent(OPA) 문서의 *Access Control Systems*는 RBAC, ABAC, AWS IAM, XACML 같은
**기존 접근 제어 방식을 하나씩 불러다 놓고 같은 정책을 Rego로 다시 써 보이는** 비교 페이지다.
정책 언어 설명서인데도 코드보다 그 사이에 낀 산문이 흥미롭다. 금지 규칙을 "누구도 동시에
가져서는 안 된다"로 정의하고, 도구에 무엇을 넣어야 무엇이 나오는지 한 문장으로 묶고, 아직
안 되는 기능을 밝히면서 같은 문장 안에서 되는 기능으로 넘어가고, 요구 사항과 논의 범위를
문법으로 갈라 놓는다. **권한 설계 문서, 예외 승인 회신, 감사 보고서, 사내 도구 안내**처럼
내 규칙이 어디까지를 맡는지 남에게 납득시켜야 하는 글에 그대로 옮겨 쓸 다섯 문장을 골랐다.

> **원문** — Open Policy Agent contributors, *Access Control Systems*,
> [openpolicyagent.org](https://openpolicyagent.org/docs/comparisons/access-control-systems)
> (OPA 공식 문서, 상시 갱신), [Apache License 2.0](https://github.com/open-policy-agent/opa/blob/main/LICENSE)
> — 문서 하단 저작권 표기: © Open Policy Agent contributors. Licensed under the Apache License,
> Version 2.0.
> ([원본 마크다운](https://github.com/open-policy-agent/opa/blob/main/docs/docs/comparisons/access-control-systems.md))
>
> 영어 문장은 원문 그대로 인용했고, 한글 설명과 응용 문장은 이 노트에서 새로 쓴 것이다.

{{< sentence
  en="Separation of duty (SOD) refers to the idea that there are certain combinations of permissions that no one should have at the same time. For example, no one should be able to both create payments and approve payments."
  ko="직무 분리(SOD)란 어떤 권한 조합은 누구도 동시에 가져서는 안 된다는 생각을 가리킨다. 예를 들어 누구도 결제를 생성하면서 동시에 결제를 승인할 수 있어서는 안 된다."
  source="OPA Docs · RBAC Separation of duty (SOD)"
  sourceURL="https://openpolicyagent.org/docs/comparisons/access-control-systems#rbac-separation-of-duty-sod"
  note="`X refers to the idea that ...` — 용어를 `X is ...`로 잘라 정의하는 대신 **그 용어가 가리키는 생각**을 풀어 주는 문형이다. 표준 정의를 인용하지 않고도 뜻이 서기 때문에 정의 문구를 놓고 다투지 않아도 된다. 금지 규칙 자체는 `there are certain X that no one should Y at the same time` 골격으로 적는데, 주어 `no one`이 예외 없는 금지를 만들고 `at the same time`이 **금지 대상은 개별 권한이 아니라 조합**이라는 점을 못 박는다. 뒤 문장은 주어를 `no one`으로 유지한 채 `both A and B`로 조합 하나를 보여 준다 — 추상 규칙 한 줄과 같은 문형의 예시 한 줄을 붙여 두는 방식이라, 규칙을 받아 읽는 사람이 자기 상황을 대입하기 쉽다."
  app1="Toxic access refers to the idea that there are certain combinations of permissions that no one on the on-call rotation should have at the same time. For example, no one should be able to both deploy to production and approve the deployment."
  app1ko="위험 권한 조합이란 온콜 로테이션에 있는 누구도 동시에 가져서는 안 되는 권한 조합이 있다는 생각을 가리킨다. 예를 들어 누구도 프로덕션에 배포하면서 동시에 그 배포를 승인할 수 있어서는 안 된다."
  app2="Reviewer independence refers to the idea that there are certain roles that no one should hold on the same change at the same time. For example, no one should be able to both write a migration and sign off on its rollback plan."
  app2ko="리뷰어 독립성이란 같은 변경에 대해 누구도 동시에 맡아서는 안 되는 역할이 있다는 생각을 가리킨다. 예를 들어 누구도 마이그레이션을 작성하면서 동시에 그 롤백 계획을 승인할 수 있어서는 안 된다."
>}}

{{< sentence
  en="Once you provide RBAC with both those assignments, RBAC tells you how to make an authorization decision. A user is authorized for all those permissions assigned to any of the roles she is assigned to."
  ko="그 두 가지 할당표를 RBAC에 넣어 주고 나면, RBAC는 권한 결정을 어떻게 내리면 되는지 알려 준다. 사용자는 자신에게 배정된 역할 중 어느 하나에라도 부여된 권한을 모두 갖는다."
  source="OPA Docs · Role-based access control (RBAC)"
  sourceURL="https://openpolicyagent.org/docs/comparisons/access-control-systems#role-based-access-control-rbac"
  note="`Once you provide X with Y, X tells you how to Z.` — 도구가 **무엇을 받아야 무엇을 돌려주는지**를 한 문장에 묶는 계약문이다. `Once`는 시점이 아니라 **선행 조건**을 걸기 때문에, Y를 채우지 않으면 Z도 없다는 말이 따로 적지 않아도 따라붙는다. 동사 선택이 이 문장의 핵심인데 `decides for you`가 아니라 `tells you how to`다 — 결정을 대신 내려 주는 게 아니라 **결정하는 방법을 알려 준다**로 한 칸 낮춰 잡아, 도구의 몫과 사람의 몫을 조용히 갈라 놓는다. 그리고 바로 다음 문장에서 그 방법을 한 줄 규칙으로 적어 약속을 확인해 준다. 사내 도구·자동화·대시보드가 무엇을 해 주는 물건인지 첫 문단에서 설명할 때 쓴다."
  app1="Once you provide the runbook generator with both the alert name and the service tier, it tells you which escalation path to follow."
  app1ko="알림 이름과 서비스 등급을 둘 다 넣어 주고 나면, 런북 생성기가 어느 에스컬레이션 경로를 따르면 되는지 알려 준다."
  app2="Once you provide the access review with both the entitlement export and the joiner-mover-leaver log, it tells you which accounts to revoke first."
  app2ko="권한 목록 산출물과 입사·이동·퇴사 기록을 둘 다 넣어 주고 나면, 접근 권한 검토가 어느 계정부터 회수해야 하는지 알려 준다."
>}}

{{< sentence
  en="OPA's API does not yet let you enforce SOD by rejecting improper role-assignments, but it does let you express SOD constraints and ask for all SOD violations, as shown below."
  ko="OPA의 API는 잘못된 역할 배정을 거절하는 방식으로 직무 분리를 강제하게 해 주지는 아직 못 하지만, 직무 분리 제약을 표현하고 모든 위반 사례를 물어볼 수 있게는 해 준다. 아래에 보인 대로다."
  source="OPA Docs · RBAC Separation of duty (SOD)"
  sourceURL="https://openpolicyagent.org/docs/comparisons/access-control-systems#rbac-separation-of-duty-sod"
  note="`X does not yet let you A, but it does let you B.` — 못 하는 것을 먼저 말하고 **같은 문장 안에서** 할 수 있는 것으로 넘어가는 문형이다. 세 군데가 톤을 결정한다. `yet`은 한계를 영구 결함이 아니라 **아직 오지 않은 상태**로 표시하고, 강조의 `does`(`it does let you`)는 뒤 절이 앞 절을 덮는 변명이 아니라 **지금 실제로 쓸 수 있는 것**임을 소리 내어 밀어 준다. 진짜 배울 점은 A와 B를 고른 방식이다 — 막는 일(`enforce`, `rejecting`) 대신 **드러내는 일**(`express`, `ask for all violations`)을 내놓아, 예방은 못 해도 탐지는 된다는 실무의 흔한 절충을 그대로 문장에 담았다. 기능 요청을 반려하거나 도구의 현재 사정거리를 알릴 때 그대로 쓴다."
  app1="The current pipeline does not yet let you block a deploy on a failing budget check, but it does let you record the breach and page the service owner."
  app1ko="지금 파이프라인은 예산 점검 실패를 근거로 배포를 막아 주지는 아직 못 하지만, 위반을 기록하고 서비스 담당자를 호출할 수 있게는 해 준다."
  app2="Our audit tooling does not yet let you revoke stale credentials automatically, but it does let you list every credential unused for ninety days."
  app2ko="우리 감사 도구는 방치된 자격 증명을 자동으로 회수해 주지는 아직 못 하지만, 90일 동안 쓰이지 않은 자격 증명을 전부 뽑아 볼 수 있게는 해 준다."
>}}

{{< sentence
  en="The dynamic version of SOD allows a single user to be assigned two conflicting roles but requires that the same user not utilize those roles on the same transaction, which is out of scope for this document."
  ko="동적 직무 분리는 한 사용자가 충돌하는 두 역할을 배정받는 것 자체는 허용하되, 같은 사용자가 같은 거래에서 그 두 역할을 사용하지는 않을 것을 요구한다. 이는 이 문서의 범위 밖이다."
  source="OPA Docs · RBAC Separation of duty (SOD)"
  sourceURL="https://openpolicyagent.org/docs/comparisons/access-control-systems#rbac-separation-of-duty-sod"
  note="`X allows A but requires that B not C, which is out of scope for this document.` — 한 문장에 세 가지를 싣는다: 무엇을 허용하는지, 그 허용에 무슨 단서가 붙는지, 그리고 **여기서는 더 다루지 않는다**는 선언. 문법에서 눈여겨볼 곳은 `requires that the same user not utilize`다 — `does not utilize`도 `should not utilize`도 아닌 **not + 동사원형**(mandative subjunctive, 요구의 가정법)이다. `require`, `recommend`, `insist`, `demand` 뒤의 that절에서 쓰며, 시제와 인칭 표시를 지워 버리기 때문에 **일어난 일의 서술이 아니라 지켜야 할 요구 사항**으로 읽힌다. 규정·정책 문서의 표준 문체이니 그런 글을 쓸 때 `that ... not do`를 꺼내 쓰면 된다. 끝의 `which is out of scope for this document`는 비제한적 관계절로 붙여 **존재는 인정하되 여기서 다루지는 않겠다**고 말한다 — 모른다가 아니라 범위 밖이라고 말하는 자리다."
  app1="The looser policy allows an engineer to hold both the deploy and the approve role but requires that the same engineer not use both on one release, which is out of scope for this runbook."
  app1ko="느슨한 쪽 정책은 한 엔지니어가 배포 역할과 승인 역할을 둘 다 갖는 것은 허용하되, 같은 엔지니어가 한 릴리스에서 그 둘을 다 쓰지는 않을 것을 요구한다. 이는 이 런북의 범위 밖이다."
  app2="The exception process allows a team to keep the legacy endpoint but requires that the team not expose it outside the VPC, which is out of scope for this review."
  app2ko="예외 절차는 팀이 레거시 엔드포인트를 유지하는 것은 허용하되, 그 팀이 그것을 VPC 밖으로 노출하지는 않을 것을 요구한다. 이는 이번 검토의 범위 밖이다."
>}}

{{< sentence
  en="In OPA, there's nothing special about users and objects. You can attach attributes to anything."
  ko="OPA에서는 사용자와 객체가 특별할 것이 없다. 무엇에든 속성을 붙일 수 있다."
  source="OPA Docs · Attribute-based access control (ABAC)"
  sourceURL="https://openpolicyagent.org/docs/comparisons/access-control-systems#attribute-based-access-control-abac"
  note="`In X, there's nothing special about A and B. You can attach C to anything.` — 읽는 사람이 당연히 특별하다고 여기는 것을 **특별하지 않다고 선언해서** 전제를 깨는 문형이다. 앞 문장이 부정형으로 기존 구분을 지우고, 뒤 문장이 `anything`으로 지운 자리를 더 넓은 규칙으로 채운다 — 지우기와 채우기가 한 쌍으로 움직이기 때문에 &quot;그럼 뭐가 되는 건데?&quot;라는 질문이 남지 않는다. `there is nothing special about ~`은 깎아내리는 말이 아니라 **일반화**의 신호라서, 우리 시스템에는 특례가 없다는 사실을 자랑도 변명도 아닌 톤으로 전할 수 있다. 신입에게 구조를 설명하거나 설계 리뷰에서 불필요한 예외 처리를 걷어낼 때 꺼내 쓴다."
  app1="In this pipeline, there is nothing special about the production environment. You can attach approval rules to any stage."
  app1ko="이 파이프라인에서 프로덕션 환경이 특별할 것은 없다. 어느 단계에든 승인 규칙을 붙일 수 있다."
  app2="In the new schema, there is nothing special about incidents and deploys. You can attach a timeline entry to anything."
  app2ko="새 스키마에서는 장애와 배포가 특별할 것이 없다. 무엇에든 타임라인 항목을 붙일 수 있다."
>}}
