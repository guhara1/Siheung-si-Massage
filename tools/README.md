# 색인(인덱싱) 가속 가이드

시흥 사이트를 네이버·구글·빙에 가장 빠르게 색인시키는 절차입니다.

## 0. 생성되는 색인 파일 (build.py 자동)

| 파일 | 용도 |
|---|---|
| `/sitemap.xml` | 색인 허용 전 페이지 + `lastmod` (구글·네이버·빙 공통) |
| `/feed.xml` | RSS 2.0 피드 (새 글 발견용, head 에 `alternate` 링크 연결) |
| `/robots.txt` | 전체 허용 + `Sitemap:` 라인 |
| `/<INDEXNOW_KEY>.txt` | IndexNow 키 검증 파일 |

```bash
python build.py     # 위 파일 전부 재생성
```

## 1. 네이버 (Naver Search Advisor)

1. https://searchadvisor.naver.com → 사이트 등록 `https://siheung-si-massage.pages.dev/`
2. 소유확인: 메인페이지 `<head>` 의 `naver-site-verification` 메타 사용 (이미 삽입됨)
3. 요청 → **사이트맵 제출**: `sitemap.xml`
4. 요청 → **RSS 제출**: `feed.xml`
5. (선택) '웹페이지 수집' 에서 주요 URL 개별 수집 요청

## 2. 구글 (Search Console)

1. https://search.google.com/search-console → 속성 추가 (URL 접두어)
2. 색인 → **Sitemaps** 에 `sitemap.xml` 제출
3. 새 글은 상단 'URL 검사' → **색인 생성 요청**
4. (선택, 고급) Indexing API: `tools/google_indexing.py` 참고 — 서비스 계정 필요,
   공식 지원 타입은 JobPosting/BroadcastEvent 라 일반 페이지는 보장되지 않음.
   ※ 과거의 `google.com/ping?sitemap=` 핑 엔드포인트는 2023년 폐지됨.

## 3. 빙·네이버·얀덱스 — IndexNow (즉시 통보)

IndexNow 한 번 호출로 **Bing·Naver·Yandex·Seznam** 에 동시 통보됩니다.
(네이버는 IndexNow 참여사 — Search Advisor 제출과 병행하면 가장 빠름)

```bash
# 첫 일괄 통보 — sitemap.xml 의 모든 URL
python tools/indexnow.py

# 글을 새로 올리거나 고칠 때마다 — 바뀐 URL만
python tools/indexnow.py https://siheung-si-massage.pages.dev/baegot-dong/
```

전제: `build.py` 로 빌드 후 **배포가 끝나** 루트의 `<INDEXNOW_KEY>.txt` 가
실제 도메인에서 열려야 합니다(검색엔진이 키 파일로 소유권을 검증).

## 권장 운영 루틴 (글 1건 올릴 때)

```bash
# 1) 콘텐츠 추가/수정 후 빌드
python build.py
# 2) 커밋·푸시 → Cloudflare Pages 배포 완료 대기
git add -A && git commit -m "..." && git push
# 3) 배포 끝나면 바뀐 URL 즉시 통보 (빙·네이버)
python tools/indexnow.py https://siheung-si-massage.pages.dev/<새-경로>/
# 4) 구글은 Search Console 'URL 검사 → 색인 요청' (또는 Indexing API)
```
