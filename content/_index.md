---
title: Writing Notes
type: docs
bookToc: false
---

# 문장 발췌 노트

아티클을 읽다가 **살려 쓰고 싶은 문장**을 만나면 여기에 남긴다.
문장 하나마다 세 가지를 붙인다.

<div class="home-grid">
  <div class="home-grid__item">
    <h3>발췌 문장</h3>
    <p>원문에서 그대로 가져온 영어 문장과 한국어 직역. 어디서 왔는지 출처도 함께 적는다.</p>
  </div>
  <div class="home-grid__item">
    <h3>한글 설명</h3>
    <p>왜 이렇게 썼는지 — 구조, 표현의 뉘앙스, 대체 가능한 표현을 한국어로 풀어 쓴다.</p>
  </div>
  <div class="home-grid__item">
    <h3>응용 문장 2개</h3>
    <p>같은 구조를 내 맥락으로 옮긴 문장 두 개. 읽고 끝내지 않고 쓸 수 있게 만드는 단계.</p>
  </div>
</div>

## 시작하기

- [발췌 노트 전체 보기]({{< relref "/docs/articles" >}}) — 아티클별로 정리된 문장 카드
- [노트 작성 가이드]({{< relref "/docs/guide/how-to-write" >}}) — 새 노트를 추가하는 방법

## 이렇게 보인다

{{< sentence
  en="The system degrades gracefully when a single node fails."
  ko="노드 하나가 죽어도 시스템은 완만하게 성능이 떨어진다."
  note="`degrade gracefully`는 장애가 나면 전부 멈추는 게 아니라 **기능을 일부만 잃고 계속 동작한다**는 뜻의 관용 표현이다. `fail`처럼 이분법으로 말하지 않고 저하의 정도를 표현할 때 쓴다."
  app1="Our search falls back to keyword matching, so quality degrades gracefully when the embedding service is down."
  app1ko="임베딩 서비스가 내려가면 검색이 키워드 매칭으로 폴백해서 품질이 완만하게 떨어진다."
  app2="The dashboard degrades gracefully on slow connections: charts load last, numbers load first."
  app2ko="느린 회선에서 대시보드는 완만하게 저하된다 — 숫자가 먼저 뜨고 차트가 마지막에 뜬다."
>}}
