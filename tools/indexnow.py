#!/usr/bin/env python3
"""IndexNow 즉시 색인 통보 — Bing·Naver·Yandex·Seznam.

글을 새로 올리거나 수정할 때마다 실행하면 IndexNow 참여 검색엔진에
변경 URL을 즉시 통보합니다. (구글은 IndexNow 미참여 → tools/README.md 참고)

사용법:
  python tools/indexnow.py                  # sitemap.xml 의 모든 URL 일괄 통보
  python tools/indexnow.py https://...A/ ...B/   # 지정 URL만 통보 (새 글 1~수개)

전제: 루트에 키 검증 파일 <INDEXNOW_KEY>.txt 가 실제 도메인에 배포되어 있어야 함
      (build.py 가 자동 생성하므로 빌드·배포 후 실행하세요).
"""
import json
import os
import sys
import urllib.request
import xml.etree.ElementTree as ET

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
from content.site import BASE_URL, INDEXNOW_KEY  # noqa: E402

HOST = BASE_URL.split("://", 1)[-1].strip("/")
KEY_LOCATION = f"{BASE_URL.rstrip('/')}/{INDEXNOW_KEY}.txt"
ENDPOINT = "https://api.indexnow.org/indexnow"


def sitemap_urls():
    tree = ET.parse(os.path.join(ROOT, "sitemap.xml"))
    ns = {"s": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    return [loc.text for loc in tree.iterfind(".//s:loc", ns)]


def submit(urls):
    # IndexNow 권장: 1회 최대 10,000 URL
    payload = {
        "host": HOST,
        "key": INDEXNOW_KEY,
        "keyLocation": KEY_LOCATION,
        "urlList": urls,
    }
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        ENDPOINT, data=data,
        headers={"Content-Type": "application/json; charset=utf-8"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            print(f"IndexNow OK: {r.status} {r.reason}  ({len(urls)} URLs)")
            print(f"  host={HOST}\n  keyLocation={KEY_LOCATION}")
    except urllib.error.HTTPError as e:
        print(f"IndexNow HTTP {e.code}: {e.reason}")
        print("  202=수락(검증 대기), 200=성공, 400=형식오류, 403=키불일치, 422=URL/호스트불일치")
        sys.exit(1)


if __name__ == "__main__":
    urls = sys.argv[1:] or sitemap_urls()
    if not urls:
        print("통보할 URL이 없습니다. 먼저 python build.py 로 sitemap.xml 을 생성하세요.")
        sys.exit(1)
    print(f"통보 대상 {len(urls)}개 URL → IndexNow(Bing·Naver·Yandex)")
    submit(urls)
