#!/usr/bin/env python3
"""(선택) 구글 Indexing API 통보 스텁.

구글은 IndexNow에 참여하지 않습니다. 구글의 가장 빠른 색인 경로는
1순위: Search Console 에 sitemap.xml 제출 + 'URL 검사 → 색인 요청'
2순위: Indexing API (아래) — 단, 구글 공식 지원 타입은 JobPosting/
       BroadcastEvent 뿐입니다. 일반 페이지에도 호출은 되지만 보장은 없습니다.

사전 준비:
  1) Google Cloud 프로젝트 생성 → Indexing API 사용 설정
  2) 서비스 계정 생성 → JSON 키 다운로드
  3) Search Console 속성에 서비스 계정 이메일을 '소유자'로 추가
  4) pip install google-auth requests
  5) 환경변수: export GOOGLE_APPLICATION_CREDENTIALS=/path/to/key.json

사용법:
  python tools/google_indexing.py https://siheung-si-massage.pages.dev/baegot-dong/
  python tools/google_indexing.py --all     # sitemap.xml 전체 (쿼터 200/일 주의)
"""
import os
import sys
import xml.etree.ElementTree as ET

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ENDPOINT = "https://indexing.googleapis.com/v3/urlNotifications:publish"
SCOPES = ["https://www.googleapis.com/auth/indexing"]


def sitemap_urls():
    tree = ET.parse(os.path.join(ROOT, "sitemap.xml"))
    ns = {"s": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    return [loc.text for loc in tree.iterfind(".//s:loc", ns)]


def main(urls):
    try:
        import google.auth.transport.requests
        from google.oauth2 import service_account
    except ImportError:
        print("google-auth 가 필요합니다: pip install google-auth requests")
        sys.exit(1)
    import requests

    cred_path = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS")
    if not cred_path or not os.path.exists(cred_path):
        print("GOOGLE_APPLICATION_CREDENTIALS 환경변수에 서비스 계정 JSON 경로를 지정하세요.")
        sys.exit(1)

    creds = service_account.Credentials.from_service_account_file(cred_path, scopes=SCOPES)
    creds.refresh(google.auth.transport.requests.Request())

    ok = 0
    for u in urls:
        r = requests.post(
            ENDPOINT,
            headers={"Authorization": f"Bearer {creds.token}"},
            json={"url": u, "type": "URL_UPDATED"},
            timeout=30,
        )
        print(r.status_code, u)
        ok += (r.status_code == 200)
    print(f"\n완료: {ok}/{len(urls)} (일일 쿼터 기본 200건)")


if __name__ == "__main__":
    args = sys.argv[1:]
    urls = sitemap_urls() if (args == ["--all"]) else args
    if not urls:
        print(__doc__)
        sys.exit(1)
    main(urls)
