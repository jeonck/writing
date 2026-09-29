---
title: 수치 정확도 문서의 표현
description: 반론을 미리 두 개 막고, 추론의 비약을 끊고, 한계를 의존성에서 물려받았다고 밝히는 문장 5개.
weight: -40
date: 2026-09-30
source: "PyTorch 문서"
sourceURL: https://github.com/pytorch/pytorch/blob/main/docs/source/notes/numerical_accuracy.md
---

# 수치 정확도 문서의 표현

같은 계산인데 CPU와 GPU에서, 버전과 하드웨어에 따라 결과가 왜 달라지는지를 설명하는 PyTorch
문서. **무엇을 보장하지 않는지**를 먼저 선언하고, 완화책을 권하면서 그 한계를 같은 문장에
적어 두는 문형이 줄줄이 나와 발췌했다. 재현되지 않는 장애를 보고하거나 만능이 아닌 대책을
공지할 때 그대로 쓸 수 있는 틀이다.

> **원문** — PyTorch Contributors, *Numerical accuracy* (PyTorch Documentation),
> [pytorch/pytorch · docs/source/notes/numerical_accuracy.md](https://github.com/pytorch/pytorch/blob/main/docs/source/notes/numerical_accuracy.md)
> (2026-09-30 확인), [BSD 3-Clause](https://github.com/pytorch/pytorch/blob/main/LICENSE) 라이선스.
> 같은 문서가 렌더링된 페이지는 `docs.pytorch.org/docs/stable/notes/numerical_accuracy.html`
> 이지만, 아래 발췌는 위 리포지터리의 `main` 브랜치 원문에서 축자로 확인한 것이다.
>
> 영어 문장은 원문 그대로 인용했고, 한글 설명과 응용 문장은 이 노트에서 새로 쓴 것이다.

{{< sentence
  en="In particular, CPU and GPU results can be different even for bitwise-identical inputs and even after controlling for the sources of randomness."
  ko="특히 CPU와 GPU의 결과는 입력이 비트 단위로 동일해도, 그리고 무작위성의 출처를 통제한 뒤에도 서로 다를 수 있다."
  source="PyTorch 문서 · Numerical accuracy"
  sourceURL="https://github.com/pytorch/pytorch/blob/main/docs/source/notes/numerical_accuracy.md"
  note="`A can be different even for X and even after Y` — 뻔한 반론을 **문장 안에서 미리 두 개 막아 두는** 구조다. `even`이 두 번 나오는 것이 핵심인데, 첫 번째는 '입력이 같다'는 조건을, 두 번째는 '상대가 이미 해 봤을 조치'를 가리킨다. 그래서 &quot;입력도 같고 시드도 고정했는데 왜 다르냐&quot;는 되물음이 아예 생기지 않는다. `controlling for`는 통계에서 온 표현으로 '없앴다'가 아니라 **변수로 묶어 고정했다**는 뜻이라, 완전 제거를 주장하지 않으면서도 통제했다고 말할 수 있다. 재현되지 않는 장애, 환경에 따라 갈리는 테스트 결과를 보고할 때 그대로 쓴다."
  app1="Staging and production can behave differently even for identical request payloads and even after pinning the same image digest."
  app1ko="요청 본문이 완전히 같아도, 그리고 같은 이미지 다이제스트로 고정한 뒤에도 스테이징과 프로덕션의 동작은 다를 수 있다."
  app2="Two reviewers can reach different conclusions even for the same evidence set and even after agreeing on the checklist in advance."
  app2ko="증적 묶음이 같아도, 그리고 체크리스트를 미리 합의한 뒤에도 리뷰어 두 사람의 결론은 다를 수 있다."
>}}

{{< sentence
  en="A value being representable in a dtype does not guarantee that all intermediate or output values of an operation will remain finite."
  ko="어떤 값이 그 자료형으로 표현 가능하다는 것이, 연산의 모든 중간값과 출력값이 유한하게 남는다는 보장은 아니다."
  source="PyTorch 문서 · Extremal values"
  sourceURL="https://github.com/pytorch/pytorch/blob/main/docs/source/notes/numerical_accuracy.md"
  note="`A being X does not guarantee that Y` — 동명사구를 주어로 올려 **한 사실에서 다른 사실로 건너가는 추론을 끊는** 문형이다. `The fact that a value is representable does not guarantee ~`보다 짧고, `If a value is representable, it does not mean ~`보다 단호하다. 요령은 보장하지 않는 내용을 `that`절에 통째로 넣는 것이고, `all`과 `remain`이 결과뿐 아니라 **중간 과정 전체**까지 범위를 넓힌다. '입력 검증을 통과했으니 괜찮다', '빌드가 됐으니 동작한다' 같은 비약을 리뷰나 회고에서 끊어야 할 때 꺼내 쓴다."
  app1="A request passing schema validation does not guarantee that every downstream service will accept it."
  app1ko="요청이 스키마 검증을 통과했다는 것이, 하위 서비스 전부가 그 요청을 받아들인다는 보장은 아니다."
  app2="A dependency being listed in the SBOM does not guarantee that the version we ship is the version we reviewed."
  app2ko="의존성이 SBOM에 적혀 있다는 것이, 우리가 배포하는 버전이 우리가 검토한 버전이라는 보장은 아니다."
>}}

{{< sentence
  en="The external libraries (backends) that `torch.linalg` uses provide no guarantees on their behaviour when the inputs have non-finite values like `inf` or `NaN`. As such, neither does PyTorch."
  ko="torch.linalg가 쓰는 외부 라이브러리(백엔드)는 입력에 inf나 NaN처럼 유한하지 않은 값이 있을 때의 동작을 전혀 보장하지 않는다. 그러므로 PyTorch도 보장하지 않는다."
  source="PyTorch 문서 · Linear algebra — Non-finite values"
  sourceURL="https://github.com/pytorch/pytorch/blob/main/docs/source/notes/numerical_accuracy.md"
  note="`X provides no guarantees on ... As such, neither does Y.` — 우리 쪽 한계를 **의존성에서 물려받았다고 밝히는** 두 문장 구조다. 힘은 뒷문장에 있다: `neither does Y`가 앞 문장의 동사구를 `does` 하나로 받아 되풀이 없이 같은 부정을 우리에게 옮긴다. 그래서 한계가 우리 태만이 아니라 **아래에 깔린 것의 결과**로 읽힌다. `provide no guarantees on B`는 `do not guarantee B`보다 형식적이어서 책임 범위를 다루는 문서에 어울린다. 우리 SLA가 클라우드 사업자의 SLA를 넘을 수 없다는 말, 스캐너가 못 잡는 것은 우리도 못 잡는다는 말에 그대로 쓴다."
  app1="Our upstream registry provides no guarantees on availability during its maintenance windows. As such, neither do we."
  app1ko="상위 레지스트리는 점검 시간대의 가용성을 전혀 보장하지 않는다. 그러므로 우리도 보장하지 않는다."
  app2="The vendor provides no guarantees on ordering when messages are replayed. As such, neither does our consumer."
  app2ko="벤더는 메시지가 재전송될 때의 순서를 전혀 보장하지 않는다. 그러므로 우리 컨슈머도 보장하지 않는다."
>}}

{{< sentence
  en="Running the computation in `float64` (as NumPy does by default) often helps, but it does not solve these issues in all cases."
  ko="계산을 float64로 돌리면(NumPy가 기본으로 그러는 것처럼) 도움이 되는 경우가 많지만, 모든 경우에 이 문제를 해결해 주지는 않는다."
  source="PyTorch 문서 · Extremal values in linalg"
  sourceURL="https://github.com/pytorch/pytorch/blob/main/docs/source/notes/numerical_accuracy.md"
  note="`X often helps, but it does not solve these issues in all cases.` — 대책을 권하면서 **효과의 한계를 같은 문장에 적어 두는** 틀이다. 동사가 `solves`가 아니라 `helps`라 약속의 크기가 이미 작고, `often`이 빈도까지 한 번 더 깎는다. 뒤의 `not ~ in all cases`는 `sometimes fails`와 사실상 같은 말이지만, 실패를 앞세우지 않아 **권고를 취소하지 않은 채** 예외를 인정하는 쪽으로 읽힌다. 괄호 안 `(as NumPy does by default)`처럼 남이 이미 그렇게 한다는 사실을 끼워 넣어 권고에 무게를 더하는 것도 훔칠 만하다. 런북이나 장애 공지에 완화책을 적고 그것이 만능은 아니라는 단서를 붙일 자리에 쓴다."
  app1="Raising the timeout often helps, but it does not solve these issues in all cases; a slow query still needs an index."
  app1ko="타임아웃을 늘리면 도움이 되는 경우가 많지만, 모든 경우에 문제를 해결해 주지는 않는다. 느린 쿼리에는 결국 인덱스가 필요하다."
  app2="Rotating the credential often helps, but it does not solve these issues in all cases: if the token was printed to a log, the log is still there."
  app2ko="자격 증명을 교체하면 도움이 되는 경우가 많지만, 모든 경우에 문제를 해결해 주지는 않는다. 토큰이 로그에 찍혔다면 그 로그는 그대로 남아 있다."
>}}

{{< sentence
  en="For performance, certain GPU architectures, especially more recent ones, allow a few truncations of the intermediate accumulation results to the reduced precision (e.g., half-precision). This change is often benign from the perspective of model convergence, though it may lead to unexpected results (e.g., `inf` values when the final result should be representable in half-precision)."
  ko="성능을 위해 일부 GPU 아키텍처, 특히 더 최근의 것들은 중간 누산 결과를 낮은 정밀도(예: 반정밀도)로 몇 번 잘라 내는 것을 허용한다. 이 변경은 모델 수렴의 관점에서는 대체로 무해하지만, 예상하지 못한 결과(예: 최종 결과가 반정밀도로 표현 가능한데도 inf가 나오는 것)를 낳을 수 있다."
  source="PyTorch 문서 · Reduced Precision Reduction for FP16 and BF16 GEMMs"
  sourceURL="https://github.com/pytorch/pytorch/blob/main/docs/source/notes/numerical_accuracy.md"
  note="`X is often benign from the perspective of A, though it may lead to B` — 같은 변경을 **자를 지정해 두 번 재는** 문형이다. `benign`만 쓰면 '문제없다'로 읽히지만 `from the perspective of model convergence`가 붙으면 어느 자로 재서 무해한지가 드러나고, 다른 자로 재는 사람의 반론에 `though it may lead to ~`로 미리 자리를 내준다. 앞 문장의 `For performance, ... allow ...`는 트레이드오프를 밝히는 도입이다. **무엇을 위해 무엇을 허용했는지**를 먼저 적고 영향을 뒤에 적는 순서라, 읽는 사람이 결론을 먼저 의심하지 않는다. 성능 최적화, 표집률 인하, 캐시 도입처럼 대체로 괜찮지만 드물게 이상해지는 변경을 공지할 때 쓴다."
  app1="For cost, we keep only one in ten traces on this service. This change is often benign from the perspective of latency dashboards, though it may lead to incidents where the one request we needed was never recorded."
  app1ko="비용 때문에 이 서비스에서는 트레이스를 열 건에 한 건만 남긴다. 이 변경은 지연 시간 대시보드의 관점에서는 대체로 무해하지만, 정작 필요했던 그 요청이 기록되지 않은 장애를 낳을 수 있다."
  app2="Batching the audit writes is often benign from the perspective of daily reporting, though it may lead to gaps if the process dies before the batch is flushed."
  app2ko="감사 로그 기록을 묶어서 쓰는 것은 일일 보고의 관점에서는 대체로 무해하지만, 배치가 비워지기 전에 프로세스가 죽으면 기록에 구멍을 낳을 수 있다."
>}}
