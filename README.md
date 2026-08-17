# Writing Notes

아티클에서 발췌한 문장에 **한글 설명**과 **응용 문장 2개**를 붙여 정리하는 사이트.

- 사이트: <https://writing.metacog.co.kr>
- 테마: [hugo-book](https://github.com/alex-shpak/hugo-book) (git submodule)
- 배포: GitHub Actions → GitHub Pages

## 로컬 실행

```bash
git clone --recurse-submodules https://github.com/jeonck/writing.git
cd writing
hugo server -D
```

이미 클론한 저장소라면 테마를 먼저 받는다.

```bash
git submodule update --init --recursive
```

## 노트 추가하기

```bash
hugo new docs/articles/my-article.md
```

파일 안에서 문장 하나당 `sentence` 숏코드 하나를 쓴다.

```
{{< sentence
  en="The system degrades gracefully when a single node fails."
  ko="노드 하나가 죽어도 시스템은 완만하게 성능이 떨어진다."
  source="매체 이름"
  sourceURL="https://example.com/article"
  note="한글 설명. 마크다운을 쓸 수 있다."
  app1="응용 문장 1"
  app1ko="응용 문장 1의 한국어"
  app2="응용 문장 2"
  app2ko="응용 문장 2의 한국어"
>}}
```

전체 파라미터와 작성 원칙은 사이트의 [작성 가이드](https://writing.metacog.co.kr/docs/guide/how-to-write/) 참고.

## 구조

```
content/
  _index.md                 홈
  docs/
    articles/               아티클별 발췌 노트 (사이드바에 노출)
    guide/how-to-write.md   작성 가이드
layouts/shortcodes/
  sentence.html             발췌·설명·응용 문장 카드
assets/styles/custom.css    카드 스타일 (hugo-book 오버라이드)
static/CNAME                커스텀 도메인
.github/workflows/deploy.yml
```

## 배포

`main`에 push하면 Actions가 Hugo로 빌드해서 Pages에 올린다.
커스텀 도메인은 `static/CNAME`으로 관리한다 — 저장소 설정에서 바꾸지 말고 이 파일을 고친다.
