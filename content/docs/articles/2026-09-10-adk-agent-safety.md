---
title: 무엇을 못 하게 막아 두었는지 말하는 표현
description: 일의 순서를 강제하고, 노출 범위를 좁혀 위험군을 통째로 지우고, 판단과 무관하게 차단된다고 못 박는 문장 5개.
weight: -21
date: 2026-09-10
source: "Agent Development Kit — Safety and Security for AI Agents"
sourceURL: https://adk.dev/safety/
---

# 무엇을 못 하게 막아 두었는지 말하는 표현

Google의 Agent Development Kit 문서 중 *Safety and Security for AI Agents* 페이지는 LLM
에이전트에 도구를 쥐여 줄 때 무엇이 위험해지는지, 그 위험을 신원·가드레일·샌드박스·네트워크
경계 중 어디에서 끊을지를 정리한다. 통제를 설명하는 문서라 **무엇을 허용했고 무엇이 구조적으로
불가능한지 말로 확정하는 문장**이 계속 나온다 — 일의 순서를 강제하고, 노출 범위를 좁혀 위험
동작을 부류째 지우고, 실행 주체를 신뢰하지 않고도 결론이 유지된다고 못 박는다. 권한 설계 문서,
보안 감사 답변, 설계 리뷰 코멘트처럼 **내가 무엇을 막아 두었는지 남에게 납득시켜야 하는 글**에
그대로 옮겨 쓸 다섯 문장을 골랐다.

> **원문** — Google ADK Authors, *Safety and Security for AI Agents*,
> [adk.dev](https://adk.dev/safety/) (Agent Development Kit Documentation), 문서 라이선스
> [Apache-2.0](https://github.com/google/adk-docs/blob/main/LICENSE)
> ([원본 마크다운](https://github.com/google/adk-docs/blob/main/docs/safety/index.md)).
>
> 영어 문장은 원문 그대로 인용했고, 한글 설명과 응용 문장은 이 노트에서 새로 쓴 것이다.

{{< sentence
  en="Before implementing safety measures, perform a thorough risk assessment specific to your agent's capabilities, domain, and deployment context."
  ko="안전 장치를 구현하기 전에, 그 에이전트의 능력·도메인·배포 맥락에 맞춘 철저한 위험 평가를 수행하라."
  source="ADK Documentation · Safety and Security Risks"
  sourceURL="https://adk.dev/safety/"
  note="`Before X-ing, do Y specific to A, B, and C.` — 순서를 강제하는 명령문이다. 힘은 뒤쪽 `specific to A, B, and C`에 있다. '철저히 하라'로 끝내면 훈계가 되지만, **무엇에 맞춰야 하는지 축을 세어 주면 그 자리에서 체크리스트가 된다.** `thorough` 같은 큰 형용사는 이 목록이 뒤를 받쳐 줄 때만 공허해지지 않는다. 순서를 틀리면 뒤 작업이 통째로 헛일이 되는 요구(설계 전 조사, 마이그레이션 전 인벤토리, 권한 부여 전 검토)에 그대로 쓴다."
  app1="Before adding new alerts, perform a review of the existing pages specific to their owning team, their false-positive rate, and the action they ask for."
  app1ko="새 알림을 추가하기 전에, 기존 알림들을 담당 팀·오탐률·요구하는 조치라는 축으로 먼저 점검하라."
  app2="Before granting the new role, perform an access review specific to the data it can read, the environments it covers, and how long it is needed."
  app2ko="새 역할을 부여하기 전에, 그 역할이 읽을 수 있는 데이터·적용 환경·필요 기간에 맞춘 접근 권한 검토를 먼저 수행하라."
>}}

{{< sentence
  en="Tools can be designed with security in mind: we can create tools that expose the actions we want the model to take and nothing else. By limiting the range of actions we provide to the agents, we can deterministically eliminate classes of rogue actions that we never want the agent to take."
  ko="도구는 보안을 염두에 두고 설계할 수 있다. 모델이 하기를 바라는 동작만 노출하고 그 밖의 것은 전혀 노출하지 않는 도구를 만들 수 있다. 에이전트에게 주는 동작의 범위를 좁히면, 에이전트가 절대 하지 않기를 바라는 위험 동작들을 부류째 확정적으로 없앨 수 있다."
  source="ADK Documentation · In-tool guardrails"
  sourceURL="https://adk.dev/safety/"
  note="`... X and nothing else` + `By limiting A, we can deterministically eliminate classes of B` — 사고를 하나씩 막는 대신 **가능한 동작의 목록 자체를 줄여 문제를 부류째 지운다**는 논리를 두 문장에 담는다. `and nothing else`는 짧지만 허용 목록(allowlist)을 선언하는 말이고, 톤을 정하는 단어는 `deterministically`다 — 잘 타이르면 될 일이 아니라 아예 불가능해졌다는 뜻이라 확률 이야기가 끼어들 자리를 없앤다. `classes of ~` 덕분에 사고 사례를 나열하지 않고도 범위를 말할 수 있다. 노출 범위를 좁힌 설계를 정당화할 때 쓴다."
  app1="The deploy script exposes the two commands the on-call actually needs and nothing else. By limiting what the script can do, we deterministically eliminate the class of accidents where a rollback also drops production data."
  app1ko="배포 스크립트는 온콜이 실제로 필요한 명령 두 개만 노출하고 그 밖의 것은 노출하지 않는다. 스크립트가 할 수 있는 일을 좁히면, 롤백이 운영 데이터까지 지워 버리는 부류의 사고를 확정적으로 없앨 수 있다."
  app2="The review checklist asks for the three things we would block a merge over and nothing else."
  app2ko="리뷰 체크리스트는 우리가 머지를 막을 사유 세 가지만 묻고, 그 밖의 것은 묻지 않는다."
>}}

{{< sentence
  en="The agent identity must be explicitly authorized in the external system access policies, like adding an agent's service account to a database's IAM policy for read access. Such policies constrain the agent in only performing actions that the developer intended as possible: by giving read-only permissions to a resource, no matter what the model decides, the tool will be prohibited from performing write actions."
  ko="에이전트의 신원은 외부 시스템의 접근 정책에 명시적으로 허가되어 있어야 한다. 데이터베이스 IAM 정책에 에이전트의 서비스 계정을 읽기 권한으로 추가하는 식이다. 그런 정책은 개발자가 가능하다고 의도한 동작만 하도록 에이전트를 묶어 둔다. 리소스에 읽기 전용 권한만 주면, 모델이 무엇을 하기로 결정하든 그 도구는 쓰기 동작을 하지 못하도록 금지된다."
  source="ADK Documentation · Agent-Auth"
  sourceURL="https://adk.dev/safety/"
  note="규칙 → 예시 → 결과의 3단인데, 문장을 떠받치는 것은 마지막 절 `no matter what X decides, Y will be prohibited from Z`다. **판단 주체를 전혀 신뢰하지 않아도 결론이 그대로 유지된다**를 한 절에 담는다. `no matter what ~ decides`는 상대의 선의나 판단력을 논쟁거리에서 아예 빼 버리는 장치라, 누구를 의심한다는 인상 없이 통제를 요구할 수 있다. 수동형 `will be prohibited from`도 계산된 선택이다 — 막는 주체가 사람이 아니라 정책이라는 뜻이라 감정이 실리지 않는다. 최소 권한을 설득하는 문서, 감사 답변, 재발 방지책에 그대로 쓴다."
  app1="The CI token is scoped to this repository alone, so no matter what a workflow file asks for, the job will be prohibited from pushing anywhere else."
  app1ko="CI 토큰은 이 리포지터리 하나로만 범위가 묶여 있어서, 워크플로 파일이 무엇을 요구하든 그 잡은 다른 어디에도 푸시하지 못하도록 금지된다."
  app2="The support console is granted read-only access to the orders table, so no matter what the operator clicks, the tool will be prohibited from changing a customer record."
  app2ko="지원 콘솔에는 주문 테이블에 대한 읽기 전용 권한만 부여되어 있어서, 상담원이 무엇을 클릭하든 그 도구는 고객 레코드를 바꾸지 못하도록 금지된다."
>}}

{{< sentence
  en="Callbacks provide a simple, agent-specific method for adding pre-validation to tool and model I/O, whereas plugins offer a reusable solution for implementing general security policies across multiple agents."
  ko="콜백은 도구와 모델의 입출력에 사전 검증을 붙이는, 해당 에이전트에만 적용되는 간단한 방법이다. 반면 플러그인은 여러 에이전트에 걸친 일반적인 보안 정책을 구현하는 재사용 가능한 수단이다."
  source="ADK Documentation · Callbacks and Plugins for Security Guardrails"
  sourceURL="https://adk.dev/safety/"
  note="`A provides a <형용사> method for X, whereas B offers a <형용사> solution for Y` — 선택지 둘을 우열이 아니라 **적용 범위**로 갈라 놓는 대조문이다. `whereas`는 `but`과 달리 앞 절을 부정하지 않는다 — 둘 다 맞고 쓰는 자리가 다르다는 뜻이라, 지금 앞쪽을 쓰고 있는 사람이 방어적으로 읽지 않는다. 요령은 형용사 자리에 선택 기준을 박아 두는 것이다(`simple, agent-specific` ↔ `reusable ... across multiple agents`) — 읽는 사람이 자기 상황을 그 형용사에 대 보고 스스로 고른다. 방식 두 개를 비교하는 기술 검토서에 쓴다."
  app1="A dashboard panel provides a quick, team-specific view of one service's error rate, whereas an SLO offers a shared threshold the whole org can act on."
  app1ko="대시보드 패널은 서비스 하나의 에러율을 그 팀만 빠르게 보는 수단인 반면, SLO는 조직 전체가 함께 대응 기준으로 삼을 공통 임계값이다."
  app2="A hotfix branch provides a fast, incident-specific path for shipping one change, whereas the release train provides a predictable process for everything else."
  app2ko="핫픽스 브랜치는 변경 하나를 빠르게 내보내는, 그 사고에만 쓰는 경로인 반면, 릴리스 트레인은 나머지 전부를 위한 예측 가능한 절차다."
>}}

{{< sentence
  en="Care must be taken when agent output is visualized in a browser: if HTML or JS content isn't properly escaped in the UI, the text returned by the model could be executed, leading to data exfiltration."
  ko="에이전트의 출력을 브라우저에 표시할 때는 주의해야 한다. UI에서 HTML이나 JS 내용이 제대로 이스케이프되지 않으면, 모델이 돌려준 텍스트가 실행될 수 있고, 그 결과 데이터가 빠져나갈 수 있다."
  source="ADK Documentation · Always Escape Model-Generated Content in UIs"
  sourceURL="https://adk.dev/safety/"
  note="`Care must be taken when X: if Y, Z could happen, leading to W.` — 경고를 사람 탓으로 만들지 않는 문형이다. 앞은 행위자가 없는 수동형(`Care must be taken`)이라 누구를 나무라는 말이 아니고, 콜론 뒤는 **조건 → 결과 → 최종 피해**의 사슬이라 '왜 주의해야 하는지'가 문장 안에 남는다. `could be executed`의 `could`는 확률이 아니라 가능성을 여는 조동사고, `leading to ~`는 그 가능성이 실제로 어디까지 굴러가는지에 이름을 붙인다. **아직 사고는 안 났지만 경로가 열려 있다**를 말해야 하는 코드 리뷰·설계 리뷰 코멘트에 그대로 쓴다."
  app1="Care must be taken when the log line includes the request body: if the payload isn't redacted, a customer's token could be written to disk, leading to a credential leak."
  app1ko="로그 한 줄에 요청 본문을 담을 때는 주의해야 한다. 페이로드가 마스킹되지 않으면 고객 토큰이 디스크에 기록될 수 있고, 그 결과 자격 증명이 유출될 수 있다."
  app2="Care must be taken when a retry is added to this call: if the request isn't idempotent, a timeout could charge the customer twice, leading to a refund the team has to handle by hand."
  app2ko="이 호출에 재시도를 붙일 때는 주의해야 한다. 요청이 멱등하지 않으면 타임아웃 한 번에 고객에게 두 번 청구될 수 있고, 그 결과 팀이 손으로 처리해야 하는 환불이 생긴다."
>}}
