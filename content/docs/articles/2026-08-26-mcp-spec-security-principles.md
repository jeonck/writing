---
title: 권한을 주면서 조건을 다는 표현
description: 독자를 넓게 포괄하고, 능력에 책임을 붙이고, 위험한 것의 정체를 다시 말하고, 신뢰의 기본값을 불신으로 두고, 제약을 의도로 선언하는 문장 5개.
weight: -6
date: 2026-08-26
source: "Model Context Protocol Spec (2025-06-18)"
sourceURL: https://modelcontextprotocol.io/specification/2025-06-18
---

# 권한을 주면서 조건을 다는 표현

LLM 애플리케이션이 외부 데이터와 도구에 붙는 방식을 정의하는 MCP 명세의 최상위 문서. 강력한
기능을 제공하면서 동시에 그 기능을 어떻게 다뤄야 하는지 규정해야 하는 글이라, **권한과 조건을
한 문단 안에서 함께 못 박는 문형**이 몰려 있다 — 독자를 고르지 않고 여는 도입, 능력 뒤에 책임을
도치로 붙이기, 순한 이름 뒤의 정체를 다시 말하기, 신뢰의 기본값을 불신으로 두기, 없는 기능을
설계로 선언하기. 릴리스 노트, 권한 확대 RFC, 보안 규정에 그대로 옮겨 쓸 수 있어 발췌했다.

> **원문** — Model Context Protocol contributors, *Specification (2025-06-18)*,
> [Model Context Protocol](https://modelcontextprotocol.io/specification/2025-06-18)
> ([원본 마크다운](https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/docs/specification/2025-06-18/index.mdx)),
> [Apache-2.0](https://www.apache.org/licenses/LICENSE-2.0) 라이선스
> (명세 기여분은 Apache-2.0, 재라이선스 동의를 받지 못한 일부 초기 기여분은 MIT).
>
> 영어 문장은 원문 그대로 인용했고, 한글 설명과 응용 문장은 이 노트에서 새로 쓴 것이다.

{{< sentence
  en="Whether you're building an AI-powered IDE, enhancing a chat interface, or creating custom AI workflows, MCP provides a standardized way to connect LLMs with the context they need."
  ko="AI 기반 IDE를 만드는 중이든, 채팅 인터페이스를 개선하는 중이든, 맞춤형 AI 워크플로를 만드는 중이든, MCP는 LLM을 그것이 필요로 하는 맥락에 연결하는 표준화된 방법을 제공한다."
  source="Model Context Protocol Spec · 2025-06-18"
  sourceURL="https://modelcontextprotocol.io/specification/2025-06-18"
  note="`Whether you're A-ing, B-ing, or C-ing, X provides a standardized way to D.` — 문서의 첫 문단에서 **읽는 사람을 고르지 않겠다**고 선언하는 문형이다. `If you are a platform engineer,`처럼 대상을 특정해 열면 나머지 독자는 첫 줄에서 자기 얘기가 아니라고 판단하고 덮는다. `Whether ... , ... , or ...`는 갈래를 늘어놓되 어느 쪽이든 **결론은 같다**고 미리 못 박아 그 이탈을 막는다. 셋을 고르는 요령은 서로 멀리 떨어진 예를 잡는 것이다 — 여기서는 개발 도구, 제품 화면, 자동화로 층위가 셋 다 다르다. 비슷한 예 셋을 늘어놓으면 오히려 적용 범위가 좁아 보인다. 그리고 주절은 반드시 **하나의 약속**으로 끝나야 한다. 갈래는 여럿이어도 제공하는 것이 하나일 때만 이 문형이 성립한다. 도구 소개 문서의 첫 문단, 온보딩 자료의 표지 문장에 쓴다."
  app1="Whether you're joining the on-call rotation, debugging a paging storm, or writing a postmortem, the runbook index provides a standardized way to reach the procedure you need."
  app1ko="온콜 로테이션에 새로 들어왔든, 알림 폭주를 디버깅하는 중이든, 포스트모템을 쓰는 중이든, 런북 색인은 필요한 절차에 닿는 표준화된 방법을 제공한다."
  app2="Whether you're preparing for an external audit, investigating an incident, or reviewing an access request, the identity log provides a standardized way to answer who did what and when."
  app2ko="외부 감사를 준비하는 중이든, 장애를 조사하는 중이든, 접근 요청을 검토하는 중이든, 아이덴티티 로그는 누가 무엇을 언제 했는지에 답하는 표준화된 방법을 제공한다."
>}}

{{< sentence
  en="The Model Context Protocol enables powerful capabilities through arbitrary data access and code execution paths. With this power comes important security and trust considerations that all implementors must carefully address."
  ko="모델 컨텍스트 프로토콜은 임의의 데이터 접근과 코드 실행 경로를 통해 강력한 기능을 가능하게 한다. 그 힘과 함께, 모든 구현자가 신중하게 다뤄야 할 중요한 보안과 신뢰의 고려사항이 따라온다."
  source="Model Context Protocol Spec · 2025-06-18"
  sourceURL="https://modelcontextprotocol.io/specification/2025-06-18"
  note="`X enables powerful capabilities through <위험한 수단>. With this power comes <책임> that all <행위자> must carefully address.` — 자기 기능을 자랑한 **바로 다음 문장에서** 그 대가를 청구하는 두 문장 한 쌍이다. 기술은 뒷문장의 **도치**에 있다. `Important security considerations come with this power.`라고 바로 쓰면 무거운 명사구가 문장 머리를 막아 읽는 속도가 떨어진다. `With this power comes ...`는 앞 문장을 대명사로 받아 곧장 이어 붙이면서, 정작 중요한 명사구를 문장 끝 강조 자리로 밀어낸다. 이 쌍을 지탱하는 것은 첫 문장의 `through` 구다 — 능력을 추상적으로 자랑하지 않고 **무엇을 열어 주는지**(임의 접근, 코드 실행)를 적었기 때문에, 뒤따르는 경고가 겁주기가 아니라 산수처럼 읽힌다. 마지막의 `all implementors`는 책임의 주체를 명시해 누군가 알아서 하겠지를 막는다. 위험을 동반하는 기능의 릴리스 노트, 권한을 넓히는 제안서 첫 문단에 그대로 쓴다."
  app1="The new deploy bot enables one-command releases through direct write access to production. With this power comes a review requirement that every team enabling it must carefully address."
  app1ko="새 배포 봇은 프로덕션에 대한 직접 쓰기 권한을 통해 명령 한 줄짜리 릴리스를 가능하게 한다. 그 힘과 함께, 이 봇을 켜는 모든 팀이 신중하게 다뤄야 할 리뷰 요건이 따라온다."
  app2="Shared service accounts enable fast incident response through credentials that bypass per-user approval. With this power comes an attribution gap that every audit of this system must carefully address."
  app2ko="공용 서비스 계정은 사용자별 승인을 우회하는 자격 증명을 통해 빠른 장애 대응을 가능하게 한다. 그 힘과 함께, 이 시스템에 대한 모든 감사가 신중하게 다뤄야 할 귀속 공백이 따라온다."
>}}

{{< sentence
  en="Tools represent arbitrary code execution and must be treated with appropriate caution."
  ko="도구는 임의의 코드 실행에 해당하므로, 그에 걸맞은 주의로 다뤄야 한다."
  source="Model Context Protocol Spec · 2025-06-18"
  sourceURL="https://modelcontextprotocol.io/specification/2025-06-18"
  note="`X represents <실제로 무엇인지> and must be treated with appropriate caution.` — 이름이 순해서 위험이 가려지는 대상의 **정체를 다시 말해 주는** 문형이다. `Tools are dangerous.`는 감정이고, `Tools can be risky.`는 아무 지시도 하지 않는다. `represent`가 하는 일은 **범주 이동**이다 — tool이라는 무해한 낱말을, 이미 사내에 취급 규정이 있는 범주(임의 코드 실행)로 옮겨 놓는다. 옮김이 끝나면 뒤의 처우는 새로 설득해야 할 규칙이 아니라 **기존 규칙의 당연한 적용**이 되어, 반박할 자리가 사라진다. `appropriate`는 얼버무림처럼 보이지만 의도적이다. 구체적 조치는 구현마다 다르므로 수준만 지정하고 판단은 읽는 쪽에 넘긴다 — 대신 수준을 낮출 자유는 주지 않는다. 위험을 축소해 부르는 사내 용어(임시 스크립트, 수동 패치, 잠깐 열어 둔 포트)를 제자리에 돌려놓을 때 쓴다."
  app1="A migration script represents an unreviewed write to every row in the table and must be treated with appropriate caution."
  app1ko="마이그레이션 스크립트는 그 테이블의 모든 행에 대한 리뷰되지 않은 쓰기에 해당하므로, 그에 걸맞은 주의로 다뤄야 한다."
  app2="A long-lived personal access token represents a standing key to production and must be treated with appropriate caution."
  app2ko="만료가 없는 개인 액세스 토큰은 프로덕션으로 들어가는 상시 열쇠에 해당하므로, 그에 걸맞은 주의로 다뤄야 한다."
>}}

{{< sentence
  en="In particular, descriptions of tool behavior such as annotations should be considered untrusted, unless obtained from a trusted server."
  ko="특히 애노테이션처럼 도구의 동작을 설명하는 서술은, 신뢰된 서버에서 얻은 것이 아닌 한 신뢰할 수 없는 것으로 취급해야 한다."
  source="Model Context Protocol Spec · 2025-06-18"
  sourceURL="https://modelcontextprotocol.io/specification/2025-06-18"
  note="`X should be considered untrusted, unless obtained from Y.` — 신뢰의 **기본값을 뒤집어 놓는** 문형이다. `You should verify X.`는 검증하지 않아도 규정을 어긴 것이 아니지만, `should be considered untrusted`는 **아무것도 하지 않았을 때의 상태**를 불신으로 못 박는다. 그래서 신뢰하려면 근거를 대야 하고, 인정되는 근거는 뒤의 `unless` 절 하나뿐이다. 이 문장의 실제 규칙은 그 예외를 **출처 하나로만** 좁힌 데 있다 — 내용이 그럴듯한지는 판단 기준이 아니고 어디서 왔는지만 본다. 판단 기준이 하나면 다투는 사람이 없다. 문두의 `In particular`는 방금 말한 일반 규칙에서 **사람들이 예외로 착각하기 쉬운 항목**을 끄집어내 다시 못 박는 표시다. 하필 그 항목이 설명문인 이유는, 설명은 데이터가 아니라 안내처럼 읽혀서 검사망을 그냥 통과하기 때문이다. 외부 입력 처리 규정, 서드파티 리포트, 자동 생성 요약을 다루는 문서에 그대로 쓴다."
  app1="In particular, remediation advice pasted from a vendor report should be considered untrusted, unless confirmed against our own configuration."
  app1ko="특히 벤더 리포트에서 그대로 옮겨 온 조치 권고는, 우리 설정에 비추어 확인된 것이 아닌 한 신뢰할 수 없는 것으로 취급해야 한다."
  app2="In particular, a comment explaining why a check was removed should be considered untrusted, unless backed by a linked ticket."
  app2ko="특히 어떤 검사를 왜 없앴는지 설명하는 주석은, 링크된 티켓으로 뒷받침된 것이 아닌 한 신뢰할 수 없는 것으로 취급해야 한다."
>}}

{{< sentence
  en="The protocol intentionally limits server visibility into prompts"
  ko="이 프로토콜은 프롬프트에 대한 서버의 가시성을 의도적으로 제한한다."
  source="Model Context Protocol Spec · 2025-06-18"
  sourceURL="https://modelcontextprotocol.io/specification/2025-06-18"
  note="`X intentionally limits Y.` — 없는 기능을 **결함이 아니라 설계**로 선언하는 한 문장이다. 같은 사실을 `The protocol does not expose prompts to servers.`라고 쓰면 언젠가 채워질 빈칸처럼 읽혀서, 왜 안 되느냐는 이슈가 반년마다 다시 열린다. `intentionally` 하나가 그 질문의 성격을 바꾼다 — 덜 만든 것이 아니라 그렇게 하기로 정한 것이므로, 이의를 제기하려면 버그 리포트가 아니라 **설계 변경 제안**을 들고 와야 한다. 동사 `limits`도 `hides`나 `blocks`보다 낫다. 상대를 적으로 규정하지 않고 **범위를 정했다**고만 말하기 때문에, 제약을 지키는 쪽도 방어할 것이 없다. 로드맵에 넣지 않기로 한 기능, 일부러 켜지 않은 알림, 일부러 좁혀 둔 권한을 문서에 적을 때 이 한 줄이면 끝난다. (원문에서는 목록 항목이라 마침표가 없다. 인용은 원문 그대로 옮겼다.)"
  app1="The runbook intentionally limits what the on-call engineer can change without a second approver."
  app1ko="이 런북은 온콜 담당자가 두 번째 승인자 없이 바꿀 수 있는 범위를 의도적으로 제한한다."
  app2="The staging environment intentionally limits access to real customer records."
  app2ko="스테이징 환경은 실제 고객 레코드에 대한 접근을 의도적으로 제한한다."
>}}
