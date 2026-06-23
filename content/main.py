# 시흥 메인(홈) — 허브 역할. 키워드를 밀어 넣지 않고 상세 페이지로 연결한다.
# WebPage·Organization·BreadcrumbList·ImageObject 스키마는 build.py가 공통 주입한다.
# 메인 추가 스키마는 FAQPage 만 둔다. (방문형 사이트 → LocalBusiness 미사용)
from .site import BASE_URL, BRAND, NAVER_VERIFY, PHONE, PHONE_DISPLAY
from .pricing import PRICING

_NAVER = f'<meta name="naver-site-verification" content="{NAVER_VERIFY}">\n'

_JSONLD = f"""<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {{
      "@type": "Question",
      "name": "시흥시 전지역 방문이 가능한가요?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "예약 시간, 정확한 위치, 배정 상황에 따라 가능 여부가 달라집니다. 배곧동, 정왕동, 목감동, 은행동, 능곡동 등 대표 지역과 생활권 페이지에서 확인할 수 있습니다."
      }}
    }},
    {{
      "@type": "Question",
      "name": "오이도역이나 정왕역 근처도 가능한가요?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "오이도역, 정왕역, 시흥시청역, 신천역 등 주요 역세권은 역 상세 페이지에서 인근 생활권과 함께 안내합니다. 정확한 가능 여부는 예약 시 위치 기준으로 확인합니다."
      }}
    }},
    {{
      "@type": "Question",
      "name": "정왕1동·배곧2동처럼 숫자 동은 왜 따로 없나요?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "정왕본동~정왕4동은 정왕동 대표 페이지로, 배곧1·2동은 배곧동 대표 페이지로 통합해 중복 페이지 위험을 줄입니다."
      }}
    }},
    {{
      "@type": "Question",
      "name": "당일 예약도 가능한가요?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "가능할 수 있지만 저녁 시간대와 주말은 문의가 많을 수 있어 사전 예약을 권장합니다."
      }}
    }},
    {{
      "@type": "Question",
      "name": "출장마사지와 홈타이는 어떻게 다른가요?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "출장마사지는 관리사가 직접 방문하는 서비스 전체를 가리키고, 홈타이는 그중 집에서 받는 타이마사지를 뜻합니다. 홈타이 이용 가이드에서 차이를 확인할 수 있습니다."
      }}
    }}
  ]
}}
</script>
"""

_HERO = f"""<section class="hero">
  <div class="hero-inner">
    <p class="hero-badge">Premium Visiting Spa · 시흥시 전지역</p>
    <h1>시흥시 출장마사지 · 시흥시 홈타이<br>지역별 예약 안내</h1>
    <p class="hero-lead">샵까지 갈 필요 없이, 계신 곳에서 받는 프리미엄 방문 관리.<br>배곧·정왕·목감·은계·능곡 어디든 전화 한 통이면 예약이 끝납니다.</p>
    <div class="hero-actions">
      <a class="hero-btn primary" href="tel:{PHONE}">📞 {PHONE_DISPLAY}</a>
      <a class="hero-btn" href="/courses/">코스 안내 보기</a>
    </div>
    <ul class="hero-stats">
      <li><strong>15개</strong><span>대표 지역</span></li>
      <li><strong>12개</strong><span>역세권 안내</span></li>
      <li><strong>13개</strong><span>생활권 안내</span></li>
      <li><strong>24시간</strong><span>예약 상담</span></li>
    </ul>
  </div>
</section>
"""

_BODY = f"""
<section id="intro">
<h2>시흥시에서 출장마사지를 찾을 때 먼저 확인할 기준</h2>
<p>시흥시 출장마사지를 찾는 분들은 보통 현재 위치가 배곧, 정왕, 오이도, 월곶, 목감, 은계, 능곡, 장현 중 어디에 가까운지 먼저 확인합니다. 시흥시는 동서로 생활권 차이가 큰 도시라, 같은 시흥이라도 어느 동에 계신지에 따라 방문 조건과 이동 기준이 달라집니다. 이 페이지는 시흥시 전체 구조를 설명하는 허브 역할을 하며, 더 자세한 내용은 대표 지역·역세권·생활권 안내 페이지에서 확인하실 수 있습니다. {BRAND}는 예약 확인부터 방문 관리까지 정해진 절차에 따라 진행하며, 처음 이용하시는 분도 어렵지 않게 예약할 수 있도록 각 단계를 명확하게 안내해 드립니다. 시흥시 행정 구역과 생활권 정보는 <a href="https://www.siheung.go.kr/" target="_blank" rel="noopener">시흥시청 공식 누리집</a>에서도 확인할 수 있습니다.</p>
</section>

<section id="living">
<h2>배곧·정왕·목감·은계·능곡 생활권 차이</h2>
<p>배곧과 거북섬은 신도시·해안 생활권이고, 정왕동은 정왕역과 시화공단, 시흥스마트허브 생활권이 함께 있습니다. 목감동은 광명·안산 인접권과 연결되고, 은행동·대야동·신천동은 은계·대야 생활권으로 묶입니다. 능곡동, 장곡동, 연성동은 장현지구와 시흥시청 생활권을 중심으로 설명하는 것이 좋습니다. 같은 시흥시라도 신도시, 산업단지, 원도심, 외곽 주거지가 모두 다른 리듬으로 돌아가기 때문에, 위치를 먼저 확인하면 예약이 한결 빨라집니다. 생활권 단위로 정리한 안내는 <a href="/area/">생활권 안내</a>에서 한눈에 비교하실 수 있습니다.</p>
<ul class="card-grid">
<li><a href="/area/baegot-newtown/">배곧신도시 생활권</a></li>
<li><a href="/area/jeongwang-sihwa-industrial/">정왕·시화공단 생활권</a></li>
<li><a href="/area/oido-geobukseom/">오이도·거북섬 생활권</a></li>
<li><a href="/area/eungye-daeya/">은계·대야 생활권</a></li>
<li><a href="/area/neunggok-janghyeon/">능곡·장현 생활권</a></li>
<li><a href="/area/mokgam-gwangmyeong-nearby/">목감·광명 인접 생활권</a></li>
</ul>
</section>

<section id="areas">
<h2>대표동별 방문 가능 지역 안내</h2>
<p>대표 지역은 배곧동, 정왕동, 거북섬동, 월곶동, 군자동, 목감동, 능곡동, 장곡동, 연성동, 은행동, 대야동, 신천동, 신현동, 매화동, 과림동으로 구성합니다. 배곧동은 배곧신도시와 서울대 시흥캠퍼스 인접 생활권을 중심으로, 정왕동은 정왕역·오이도역·시화공단 생활권을 중심으로 안내합니다. 정왕본동부터 정왕4동, 배곧1·2동처럼 숫자로 나뉜 동은 각각 페이지를 만들지 않고 대표동 페이지에서 통합합니다. 거주하시거나 머무시는 동을 선택해 주세요.</p>
<ul class="card-grid">
<li><a href="/baegot-dong/">배곧동</a></li>
<li><a href="/jeongwang-dong/">정왕동</a></li>
<li><a href="/geobukseom-dong/">거북섬동</a></li>
<li><a href="/wolgot-dong/">월곶동</a></li>
<li><a href="/gunja-dong/">군자동</a></li>
<li><a href="/mokgam-dong/">목감동</a></li>
<li><a href="/neunggok-dong/">능곡동</a></li>
<li><a href="/janggok-dong/">장곡동</a></li>
<li><a href="/yeonseong-dong/">연성동</a></li>
<li><a href="/eunhaeng-dong/">은행동</a></li>
<li><a href="/daeya-dong/">대야동</a></li>
<li><a href="/sincheon-dong/">신천동</a></li>
<li><a href="/sinhyeon-dong/">신현동</a></li>
<li><a href="/maehwa-dong/">매화동</a></li>
<li><a href="/gwarim-dong/">과림동</a></li>
</ul>
</section>

<section id="stations">
<h2>오이도역·정왕역·시흥시청역·신천역 역세권 안내</h2>
<p>역을 기준으로 위치를 설명하는 것이 편하시다면 역세권 안내를 참고하세요. 오이도역, 정왕역, 월곶역, 달월역, 시흥시청역, 시흥능곡역, 신현역, 신천역, 시흥대야역을 역마다 한 페이지씩 안내하며, 환승역이라도 노선별로 나누거나 출구별 페이지를 만들지 않습니다. 소래포구역·광명역·안산역은 시흥 성격이 아니므로 각각 월곶·목감·정왕 인접 생활권 기준으로만 설명합니다.</p>
<ul class="card-grid">
<li><a href="/station/oido-station/">오이도역</a></li>
<li><a href="/station/jeongwang-station/">정왕역</a></li>
<li><a href="/station/wolgot-station/">월곶역</a></li>
<li><a href="/station/darwol-station/">달월역</a></li>
<li><a href="/station/siheung-cityhall-station/">시흥시청역</a></li>
<li><a href="/station/siheung-neunggok-station/">시흥능곡역</a></li>
<li><a href="/station/sinhyeon-station/">신현역</a></li>
<li><a href="/station/sincheon-station/">신천역</a></li>
<li><a href="/station/siheung-daeya-station/">시흥대야역</a></li>
</ul>
<p>역 전체 구조와 노선별 정리는 <a href="/station/">역세권 안내 허브</a>에서 확인하실 수 있습니다.</p>
</section>

<section id="themes">
<h2>테마별 관리 안내</h2>
<p>관리 유형이 먼저 궁금하시면 테마별 안내를 확인하세요. 부드러운 압의 <a href="/themes/swedish/">스웨디시</a>, 오일 없이 받는 <a href="/themes/thai/">타이마사지</a>(홈타이), 좁은 공간에서도 편한 <a href="/themes/homecare/">홈케어</a>, 운동 후 회복을 위한 <a href="/themes/sports/">스포츠·경락</a>, 늦은 시간 이용을 위한 <a href="/themes/24hours/">24시간</a> 안내까지 유형별 특징과 추천 대상을 정리했습니다. 테마는 독립 페이지로만 운영하며, 지역·역과 테마를 조합한 페이지는 만들지 않습니다.</p>
</section>

<section id="check">
<h2>시흥시 홈타이 예약 전 확인사항</h2>
<p>시흥시 출장마사지 예약 전에는 방문 가능 지역, 예약 가능 시간, 추가 이동비, 결제 방식, 취소 기준, 개인정보 처리 기준을 먼저 확인해야 합니다. 배곧, 정왕, 은계, 능곡처럼 접근성이 좋은 지역도 있지만 매화동, 과림동, 신현동, 군자동 일부는 시간대와 주소에 따라 이동 기준이 달라질 수 있습니다. 자세한 절차는 <a href="/reservation/">예약안내</a>와 <a href="/guide/">이용가이드</a>에서, 추가 이동비 여부는 예약 통화에서 미리 확인해 드립니다. 시흥시 홈타이는 자택·숙소·오피스텔·사무실 인근에서 예약 가능 여부를 확인한 뒤 이용하는 방문형 관리 서비스입니다.</p>
</section>

<section id="policy">
<h2>시흥시 페이지 중복 방지 운영 기준</h2>
<p>시흥시 홈타이 사이트에서 가장 중요한 부분은 번호 동을 무리하게 쪼개지 않는 것입니다. 정왕본동·정왕1~4동, 배곧1·2동을 각각 개별 페이지로 만들면 본문이 비슷해질 위험이 큽니다. 그래서 정왕동·배곧동 대표 페이지로 통합하고 각 페이지 안에서 세부 생활권을 설명합니다. 배곧동 페이지와 배곧신도시 생활권 페이지는 같은 본문을 쓰지 않고, 정왕동 페이지와 정왕역 페이지는 지역 기준과 역세권 기준으로 역할을 나눕니다. 지역명만 바꾼 복제 문장 없이, 페이지마다 고유한 정보를 담는 것이 운영 원칙입니다. 운영 주체와 콘텐츠 작성·검수 방식은 <a href="/about/">운영자 소개</a>에 공개되어 있습니다.</p>
</section>

<section id="how">
<h2>시흥시 출장마사지 사이트 이용 방법</h2>
<p>이용 방법은 간단합니다. 먼저 거주하시거나 머무시는 위치를 대표 지역·역세권·생활권 안내에서 찾고, 해당 페이지에서 방문 조건과 어울리는 테마를 확인한 뒤, 전화로 위치와 희망 시간을 알려주시면 됩니다. 메인 페이지는 시흥 전체 안내를, 대표 지역 페이지는 배곧동·정왕동·목감동·은행동 같은 세부 검색을, 역세권 페이지는 오이도역·정왕역·시흥시청역 같은 실제 검색 수요를, 생활권 페이지는 위치를 더 쉽게 찾도록 보조합니다. 어느 경로로 들어오셔도 예약 절차와 비용 기준은 동일합니다.</p>
</section>

<section id="faq">
<h2>자주 묻는 질문</h2>
<div class="faq-item">
<h3>시흥시 전지역 방문이 가능한가요?</h3>
<p>예약 시간, 정확한 위치, 배정 상황에 따라 가능 여부가 달라집니다. 배곧동, 정왕동, 목감동, 은행동, 능곡동 등 대표 지역과 생활권 페이지에서 확인할 수 있습니다.</p>
</div>
<div class="faq-item">
<h3>오이도역이나 정왕역 근처도 가능한가요?</h3>
<p>오이도역, 정왕역, 시흥시청역, 신천역 등 주요 역세권은 역 상세 페이지에서 인근 생활권과 함께 안내합니다. 정확한 가능 여부는 예약 시 위치 기준으로 확인합니다.</p>
</div>
<div class="faq-item">
<h3>정왕1동·배곧2동처럼 숫자 동은 왜 따로 없나요?</h3>
<p>정왕본동부터 정왕4동은 정왕동 대표 페이지로, 배곧1·2동은 배곧동 대표 페이지로 통합해 중복 페이지 위험을 줄입니다.</p>
</div>
<div class="faq-item">
<h3>당일 예약도 가능한가요?</h3>
<p>가능할 수 있지만 저녁 시간대와 주말은 문의가 많을 수 있어 사전 예약을 권장합니다.</p>
</div>
<div class="faq-item">
<h3>출장마사지와 홈타이는 어떻게 다른가요?</h3>
<p>출장마사지는 관리사가 직접 방문하는 서비스 전체를 가리키고, 홈타이는 그중 집에서 받는 타이마사지를 뜻합니다. <a href="/guide/">홈타이 이용 가이드</a>에서 차이를 확인할 수 있습니다.</p>
</div>
</section>

{PRICING}
<section id="contact" class="cta">
<h2>예약문의</h2>
<p>시흥시 방문 관리 예약과 상담은 전화로 가장 빠르게 진행됩니다. 위치와 희망 시간을 알려주시면 가능 여부를 바로 확인해 드립니다.</p>
<a class="cta-phone" href="tel:{PHONE}">{PHONE_DISPLAY}</a>
</section>
"""

PAGE = {
    "path": "",
    "title": "시흥시 출장마사지｜배곧·정왕·목감·은계 홈타이 지역 안내",
    "desc": "시흥시 출장마사지·홈타이 예약 전 배곧, 정왕, 목감, 은계, 능곡, 월곶 생활권을 확인하세요.",
    "h1": "시흥시 출장마사지 · 시흥시 홈타이 지역별 예약 안내",
    "body": _BODY,
    "extra_head": _NAVER + _JSONLD,
    "breadcrumb": [],
    "hero": _HERO,
}
