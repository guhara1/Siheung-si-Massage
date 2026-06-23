# 사이트 공통 설정
# 배포 도메인: Cloudflare Pages
BASE_URL = "https://siheung-si-massage.pages.dev"

BRAND = "바로 GO"
BRAND_MARK = "GO"  # 헤더 로고 원형 마크
PHONE = "0508-202-4719"
PHONE_DISPLAY = "0508-202-4719"

# 제작·제휴 문의 텔레그램 링크 (푸터 오렌지 버튼)
TELEGRAM_BUILD = "https://t.me/googleseolab"   # 웹사이트 제작문의
TELEGRAM_PARTNER = "https://t.me/googleseolab"  # 제휴문의

# 시흥 메인 경로 — 홈/지역 허브
HOME = "/"

# 네이버 웹마스터도구 사이트 소유확인 메타 (메인페이지 head 에 출력)
NAVER_VERIFY = "50e6866c684d881806f1a927afb5395635ead7f4"

# IndexNow 키 (Bing·Naver·Yandex 즉시 색인 통보). 루트에 <키>.txt 파일로도 발행된다.
INDEXNOW_KEY = "5581df66857b21ed0560063531eb3063"

# 상단 메뉴 — 메뉴명·URL에는 "출장마사지"를 반복하지 않는다(지역명·역명만 표시).
NAV = [
    ("홈", "/", []),
    ("지역별 안내", "/", [
        ("시흥시 전체", "/"),
        ("배곧동", "/baegot-dong/"),
        ("정왕동", "/jeongwang-dong/"),
        ("거북섬동", "/geobukseom-dong/"),
        ("월곶동", "/wolgot-dong/"),
        ("군자동", "/gunja-dong/"),
        ("목감동", "/mokgam-dong/"),
        ("능곡동", "/neunggok-dong/"),
        ("장곡동", "/janggok-dong/"),
        ("연성동", "/yeonseong-dong/"),
        ("은행동", "/eunhaeng-dong/"),
        ("대야동", "/daeya-dong/"),
        ("신천동", "/sincheon-dong/"),
        ("신현동", "/sinhyeon-dong/"),
        ("매화동", "/maehwa-dong/"),
        ("과림동", "/gwarim-dong/"),
    ]),
    ("역세권 안내", "/station/", [
        ("역 전체", "/station/"),
        ("오이도역", "/station/oido-station/"),
        ("정왕역", "/station/jeongwang-station/"),
        ("월곶역", "/station/wolgot-station/"),
        ("달월역", "/station/darwol-station/"),
        ("시흥시청역", "/station/siheung-cityhall-station/"),
        ("시흥능곡역", "/station/siheung-neunggok-station/"),
        ("신현역", "/station/sinhyeon-station/"),
        ("신천역", "/station/sincheon-station/"),
        ("시흥대야역", "/station/siheung-daeya-station/"),
        ("소래포구역 인접", "/station/soraepogu-nearby-area/"),
        ("광명역 인접", "/station/gwangmyeong-nearby-area/"),
        ("안산역 인접", "/station/ansan-nearby-area/"),
    ]),
    ("생활권 안내", "/area/", [
        ("생활권 전체", "/area/"),
        ("배곧신도시", "/area/baegot-newtown/"),
        ("정왕·시화공단", "/area/jeongwang-sihwa-industrial/"),
        ("오이도·거북섬", "/area/oido-geobukseom/"),
        ("월곶포구", "/area/wolgot-port/"),
        ("목감·광명 인접", "/area/mokgam-gwangmyeong-nearby/"),
        ("은계·대야", "/area/eungye-daeya/"),
        ("신천·은행", "/area/sincheon-eunhaeng/"),
        ("능곡·장현", "/area/neunggok-janghyeon/"),
        ("시흥시청·연성", "/area/cityhall-yeonseong/"),
        ("장곡·하중", "/area/janggok-hajung/"),
        ("매화·신현", "/area/maehwa-sinhyeon/"),
        ("군자·장현 인접", "/area/gunja-janghyeon/"),
        ("과림·광명부천 인접", "/area/gwarim-gwangmyeong-bucheon/"),
    ]),
    ("테마별 안내", "/themes/", [
        ("전체 테마", "/themes/"),
        ("스웨디시", "/themes/swedish/"),
        ("로미로미", "/themes/lomilomi/"),
        ("타이마사지", "/themes/thai/"),
        ("중국마사지", "/themes/chinese/"),
        ("아로마테라피", "/themes/aroma/"),
        ("홈케어", "/themes/homecare/"),
        ("호텔식마사지", "/themes/hotel-style/"),
        ("발마사지", "/themes/foot/"),
        ("스포츠·경락", "/themes/sports/"),
        ("스킨케어", "/themes/skincare/"),
        ("왁싱", "/themes/waxing/"),
        ("커플 관리", "/themes/couple/"),
        ("24시간", "/themes/24hours/"),
        ("수면 가능", "/themes/overnight/"),
    ]),
    ("코스안내", "/courses/", [
        ("전체 코스", "/courses/"),
        ("피로 회복 관리", "/courses/#recovery"),
        ("아로마 관리", "/courses/#aroma"),
        ("스포츠 관리", "/courses/#sports"),
        ("홈타이 코스", "/courses/#hometai"),
        ("커플·가족 방문 관리", "/courses/#couple"),
        ("기업·단체 방문 관리", "/courses/#group"),
        ("가격 안내", "/courses/#price"),
        ("코스 선택 가이드", "/courses/#guide"),
    ]),
    ("예약안내", "/reservation/", [
        ("예약 방법", "/reservation/#how"),
        ("예약 가능 시간", "/reservation/#hours"),
        ("방문 가능 장소", "/reservation/#place"),
        ("결제 안내", "/reservation/#payment"),
        ("변경·취소 안내", "/reservation/#change"),
        ("예약 전 체크사항", "/reservation/#check"),
    ]),
    ("이용가이드", "/guide/", [
        ("처음 이용하시는 분", "/guide/#first"),
        ("방문 전 준비사항", "/guide/#prepare"),
        ("위생 및 안전 기준", "/guide/#hygiene"),
        ("관리 후 주의사항", "/guide/#after"),
        ("금지행위 안내", "/guide/#prohibited"),
        ("이용 FAQ", "/guide/#faq"),
    ]),
    ("매거진", "/magazine/", [
        ("전체 글", "/magazine/"),
        ("마사지 비교 가이드", "/magazine/swedish-vs-thai/"),
        ("처음 이용 가이드", "/magazine/first-time-guide/"),
        ("수면과 마사지", "/magazine/sleep-and-massage/"),
        ("운동 후 회복", "/magazine/post-workout-timing/"),
        ("어깨·목 결림 관리", "/magazine/neck-shoulder-care/"),
        ("부모님 선물 가이드", "/magazine/parents-gift/"),
    ]),
    ("후기", "/reviews/", [
        ("전체 후기", "/reviews/"),
        ("지역별 후기", "/reviews/#area"),
        ("역세권 후기", "/reviews/#station"),
        ("후기 작성 안내", "/reviews/#write"),
    ]),
    ("고객센터", "/support/", [
        ("공지사항", "/support/#notice"),
        ("자주 묻는 질문", "/support/#faq"),
        ("1:1 문의", "/support/#contact"),
        ("제휴·기업 문의", "/support/#biz"),
        ("개인정보처리방침", "/support/privacy/"),
        ("이용약관", "/support/terms/"),
    ]),
]
