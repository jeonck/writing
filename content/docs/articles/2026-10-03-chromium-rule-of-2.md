---
title: 승인 기준과 그 예외를 규칙으로 적는 표현
description: 통과시키지 않는 조건의 조합을 먼저 못 박고, 예외를 허용하는 조건과 그 예외가 끝나는 지점까지 적어 두는 문장 5개.
weight: -43
date: 2026-10-03
source: "Chromium Docs · The Rule Of 2"
sourceURL: https://chromium.googlesource.com/chromium/src/+/main/docs/security/rule-of-2.md
---

# 승인 기준과 그 예외를 규칙으로 적는 표현

크로미엄 보안팀이 쓰는 "Rule of 2" 문서. 신뢰할 수 없는 입력, 메모리 안전하지 않은 언어,
높은 권한 — 이 셋 중 **둘까지만** 고르라는 규칙을 세우고, 그 규칙을 어길 수 있는 조건과
예외의 범위를 차례로 못 박는다. 기준을 글로 적어 두어야 하는 사람에게 그대로 쓸 문형이 많아 발췌했다.

> **원문** — The Chromium Authors, *The Rule Of 2*,
> [Chromium Docs](https://chromium.googlesource.com/chromium/src/+/main/docs/security/rule-of-2.md)
> ([GitHub 미러](https://github.com/chromium/chromium/blob/main/docs/security/rule-of-2.md)),
> [BSD 3-Clause](https://github.com/chromium/chromium/blob/main/LICENSE) 라이선스.
>
> 영어 문장은 원문 그대로 인용했고, 한글 설명과 응용 문장은 이 노트에서 새로 쓴 것이다.

{{< sentence
  en="Chrome Security Team will generally not approve landing a CL or new feature that involves all 3 of untrustworthy inputs, unsafe language, and high privilege."
  ko="크롬 보안팀은 신뢰할 수 없는 입력, 안전하지 않은 언어, 높은 권한 이 셋이 모두 걸린 CL이나 새 기능은 원칙적으로 승인하지 않는다."
  source="Chromium Docs · Solutions To This Puzzle"
  sourceURL="https://chromium.googlesource.com/chromium/src/+/main/docs/security/rule-of-2.md"
  note="`X will generally not approve Y that involves all 3 of A, B, and C.` — 거부 기준을 사람의 판단이 아니라 **조건의 조합**으로 적어 둔 문장이다. 핵심은 `all 3 of`다. 셋을 각각 금지하는 게 아니라 **동시에 겹칠 때만** 막는다고 말하므로, 읽는 사람은 곧바로 '무엇을 하나 떼어 내면 통과하는지'를 안다. `generally`는 재량의 여지를 남겨, 규칙을 절대 금지로 만들지 않으면서도 기본값은 거부로 세운다. 리뷰 기준이나 배포 게이트를 문서로 적을 때 쓴다."
  app1="We will generally not approve a deploy that involves all 3 of a schema migration, a config change, and a new dependency version."
  app1ko="스키마 마이그레이션, 설정 변경, 새 의존성 버전 이 셋이 한꺼번에 들어간 배포는 원칙적으로 승인하지 않는다."
  app2="Reviewers will generally not approve a PR that involves all 3 of a public API change, a missing test, and an unexplained timeout bump."
  app2ko="공개 API 변경, 테스트 누락, 설명 없는 타임아웃 상향이 모두 들어간 PR은 리뷰어가 원칙적으로 승인하지 않는다."
>}}

{{< sentence
  en="If you can be sure that the input comes from a trustworthy source, it can be OK to parse/evaluate it at high privilege in an unsafe language."
  ko="입력이 신뢰할 수 있는 출처에서 온다고 확신할 수 있다면, 안전하지 않은 언어로 높은 권한에서 그것을 파싱하거나 평가해도 괜찮을 수 있다."
  source="Chromium Docs · Verifying The Trustworthiness Of A Source"
  sourceURL="https://chromium.googlesource.com/chromium/src/+/main/docs/security/rule-of-2.md"
  note="`If you can be sure that X, it can be OK to Y` — 원칙을 어겨도 되는 **조건을 먼저 걸고** 허용을 뒤에 두는 문형. `it can be OK to`는 `it is fine to`보다 한참 약해서, 허가가 아니라 조건이 충족된 경우에만 성립하는 허용으로 읽힌다. `can be sure that`도 `know`가 아니라 '확신할 수 있다면'이어서 입증 책임을 상대에게 넘긴다. 예외를 승인하면서 그 예외가 무엇에 매달려 있는지 한 문장에 함께 넣는 방법."
  app1="If you can be sure that the job is idempotent, it can be OK to let the scheduler retry it without a dedup key."
  app1ko="그 작업이 멱등이라고 확신할 수 있다면, 중복 제거 키 없이 스케줄러가 재시도하도록 둬도 괜찮다."
  app2="If you can be sure that the dashboard reads from the replica, it can be OK to run the query without a time limit."
  app2ko="대시보드가 레플리카에서 읽는다고 확신할 수 있다면, 시간 제한 없이 그 쿼리를 돌려도 괜찮다."
>}}

{{< sentence
  en="Whenever the code branches on the byte values it's processing, the risk increases that an attacker can influence control flow and exploit bugs in the implementation."
  ko="코드가 처리 중인 바이트 값에 따라 분기할 때마다, 공격자가 제어 흐름에 영향을 주고 구현의 버그를 악용할 위험이 올라간다."
  source="Chromium Docs · Processing, Parsing, And Deserializing"
  sourceURL="https://chromium.googlesource.com/chromium/src/+/main/docs/security/rule-of-2.md"
  note="`Whenever X, the risk increases that Y` — 위험을 '있다/없다'가 아니라 **조건에 따라 올라가는 양**으로 말하는 문형. `increases`는 단정하지 않고 방향만 말하고, `the risk increases that ~`은 '무엇이 일어날 위험인지'를 that절로 뒤에 밀어 붙인 구조다(`the risk that`이 떨어져 있는 걸 어색해하지 말 것 — 영어에서는 이쪽이 더 자연스럽다). 장애 분석이나 설계 리뷰에서 '이건 위험하다' 대신 **무엇이 위험을 끌어올리는지** 지목할 때 쓴다."
  app1="Whenever a retry path writes to the same row, the risk increases that two workers overwrite each other silently."
  app1ko="재시도 경로가 같은 행에 쓰기를 할 때마다, 두 워커가 서로를 조용히 덮어쓸 위험이 올라간다."
  app2="Whenever an alert depends on a field the client fills in, the risk increases that we page someone for a formatting change."
  app2ko="알림이 클라이언트가 채우는 필드에 의존할 때마다, 포맷이 바뀐 것만으로 누군가를 호출할 위험이 올라간다."
>}}

{{< sentence
  en="Although we are all human and mistakes are always possible, a function that does not branch on input values has a better chance of being free of vulnerabilities."
  ko="우리는 모두 사람이고 실수는 언제든 가능하지만, 입력 값에 따라 분기하지 않는 함수는 취약점이 없을 가능성이 더 높다."
  source="Chromium Docs · Processing, Parsing, And Deserializing"
  sourceURL="https://chromium.googlesource.com/chromium/src/+/main/docs/security/rule-of-2.md"
  note="양보절로 **반론을 먼저 인정**하고, 정작 주장은 `has a better chance of being ~`으로 확률만 말한다. `is free of vulnerabilities`라고 쓰면 증명할 수 없는 약속이 되지만, `has a better chance of being free of`는 비교우위만 주장하므로 반박당하지 않는다. 보안·신뢰성처럼 '안전하다'를 단언할 수 없는 영역에서 그래도 이쪽이 낫다고 말해야 할 때의 기본형이다. 양보절에 `we are all human`처럼 **상대도 포함되는** 주어를 쓰면 훈계하는 톤이 빠진다."
  app1="Although no rollback is risk-free, a deploy that only adds a column has a better chance of being reversible than one that rewrites rows."
  app1ko="위험 없는 롤백은 없지만, 컬럼만 추가하는 배포는 행을 다시 쓰는 배포보다 되돌릴 수 있을 가능성이 더 높다."
  app2="Although reviewers miss things, a diff that touches one module has a better chance of being read carefully than one that touches twelve."
  app2ko="리뷰어도 놓치는 게 있지만, 한 모듈만 건드린 diff는 열두 모듈을 건드린 diff보다 꼼꼼히 읽힐 가능성이 더 높다."
>}}

{{< sentence
  en="Note that this exception only applies to Protobuf as a container format; complex data contained within a Protobuf must be handled according to this rule as well."
  ko="이 예외는 컨테이너 형식으로서의 Protobuf에만 적용된다는 점에 유의하라. Protobuf 안에 담긴 복잡한 데이터는 이 규칙에 따라 다루어야 한다."
  source="Chromium Docs · Exception: Protobuf"
  sourceURL="https://chromium.googlesource.com/chromium/src/+/main/docs/security/rule-of-2.md"
  note="예외를 허용한 **직후에 그 예외가 끝나는 지점**을 못 박는 문장. `only applies to A as B`가 예외의 자격을 좁히고(그 역할일 때만), 세미콜론 뒤의 `must be handled according to this rule as well`이 안쪽 내용물을 원래 규칙으로 돌려보낸다. `as well`은 '예외를 하나 받았어도 이건 그대로'라는 뜻을 가볍게 얹는 자리다. 면제나 예외를 승인하는 문서에는 이 한 줄이 있어야 '예외를 받았으니 전부 면제'라는 해석이 생기지 않는다."
  app1="Note that this waiver only applies to the legacy endpoint as a transport; the payloads it carries must be validated according to the same schema rules."
  app1ko="이 면제는 전송 수단으로서의 레거시 엔드포인트에만 적용된다. 그 엔드포인트가 실어 보내는 데이터는 동일한 스키마 규칙에 따라 검증해야 한다."
  app2="Note that the exemption only applies to read-only queries; any statement that writes must go through review as well."
  app2ko="이 예외는 읽기 전용 쿼리에만 적용된다. 쓰기를 하는 구문은 그대로 리뷰를 거쳐야 한다."
>}}
