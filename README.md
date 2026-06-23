# 바로 GO — 시흥 출장마사지·홈타이 안내 사이트

경기도 시흥시 전지역 방문 관리(출장마사지·홈타이) 안내용 정적 사이트입니다.
상호: **바로 GO** · 전화예약: **0508-202-4719**

## 구조

- 정적 HTML 사이트 — 어느 호스팅(GitHub Pages, Netlify, 일반 웹서버)에서든 그대로 서빙 가능
- `build.py` + `content/` 패키지에서 페이지를 생성하는 빌드 방식
- 생성물(각 디렉터리의 `index.html`, `sitemap.xml`, `robots.txt`)도 저장소에 포함
- 메인(홈)은 도메인 루트 `/` 이며, 지역 페이지는 `/baegot-dong/`, 역세권은 `/station/...`, 생활권은 `/area/...` 구조입니다

```
build.py            # 빌드 스크립트 (레이아웃·스키마·글자수/디스크립션 검사·sitemap 생성)
content/
  site.py           # 상호(바로 GO)·전화·BASE_URL·텔레그램 문의·메뉴 구조
  main.py           # 시흥 메인 허브 (+ FAQPage JSON-LD)
  areas.py          # 지역별: 대표 동 15개
  stations.py       # 역세권별: 허브 + 역 12개
  living.py         # 생활권별: 허브 + 생활권 13개
  themes.py         # 테마별: 허브 + 14개 테마
  info.py           # 출장마사지 안내·코스·예약·가이드·후기·고객센터·약관
  magazine.py       # 매거진(도움되는 콘텐츠)
  about.py          # 운영자 소개 (E-E-A-T)
assets/             # CSS(프리미엄 토큰 + 컴포넌트 오버레이), 모바일 내비 JS
```

## 스키마(구조화 데이터)

- 모든 페이지에 `WebPage` + `Organization` + `ImageObject`(선호 이미지) JSON-LD 자동 주입
- 브레드크럼이 있는 페이지에 `BreadcrumbList` JSON-LD 자동 주입
- 메인 페이지에 `FAQPage` 추가
- 방문형(오프라인 사업장 주소 없음) 사이트이므로 `LocalBusiness` 스키마는 사용하지 않음

## 빌드

```bash
python3 build.py
```

빌드 시 페이지별 본문 글자수 리포트와 디스크립션 80자 초과 경고가 출력됩니다.

## SEO 운영 원칙 (빌드에 강제됨)

- 본문 **2,000자 미만 페이지는 자동 `noindex`** 처리되고 sitemap에서 제외
- 메타 디스크립션 **80자 이내** (초과 시 빌드 경고)
- 지역은 대표 동 15개 — 정왕본동~정왕4동·배곧1·2동 등 숫자 행정동은 대표 동으로 통합
- 역은 역 1개당 페이지 1개 — 환승역도 URL 하나, 출구별 페이지 없음
- 소래포구·광명·안산역은 인접 도시 성격 → 시흥(월곶·목감·정왕) 인접 생활권 기준으로만 안내
- **지역+역+테마 조합 페이지 없음** (도어웨이 방지) — 테마는 독립 페이지로만 운영
- 메뉴명·URL에 "출장마사지" 반복 없음 — 키워드는 Title·H1·첫 문단에만 자연스럽게
- 모든 페이지 본문은 페이지별 고유 작성 (지역명만 바꾼 복붙 없음)

## 배포 전 해야 할 일

1. `content/site.py`의 `BASE_URL`을 실제 도메인으로 변경
2. (선택) `TELEGRAM_BUILD` / `TELEGRAM_PARTNER` 텔레그램 링크 확인
3. `python3 build.py` 재실행 (canonical·sitemap·robots.txt에 반영됨)
4. Google Search Console에 `sitemap.xml` 제출
