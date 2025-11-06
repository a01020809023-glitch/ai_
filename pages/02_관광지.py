아래 두 파일을 함께 만들었습니다: `app.py` (Streamlit 앱 코드)와 `requirements.txt`.

---

# 파일: app.py

```python
# app.py
# Streamlit + Folium: 서울 외국인 인기 관광지 Top10 표시 앱

import streamlit as st
from streamlit_folium import st_folium
import folium
from folium.plugins import MarkerCluster

st.set_page_config(page_title="Seoul Top10 for Foreigners 🌏", layout="wide")

st.title("서울 외국인 인기 관광지 Top10 지도 🗺️🇰🇷")
st.markdown("간단하게 서울의 외국인 인기 스팟 10곳을 지도에 표시해줘요. 사이드바에서 설정을 바꿀 수 있어요!")

# 관광지 데이터 (이름, 위도, 경도, 한줄설명, 이모지)
spots = [
    {"name": "경복궁 (Gyeongbokgung)", "lat": 37.579617, "lon": 126.977041, "desc": "조선의 대표 궁궐, 한복 체험 인기", "emoji": "🏯"},
    {"name": "창덕궁 (Changdeokgung)", "lat": 37.579417, "lon": 126.991072, "desc": "비원(후원)로 유명한 궁궐", "emoji": "🌿"},
    {"name": "N서울타워 (Namsan Seoul Tower)", "lat": 37.551169, "lon": 126.988226, "desc": "서울 전경을 한눈에!", "emoji": "🗼"},
    {"name": "명동 (Myeongdong)", "lat": 37.563730, "lon": 126.985240, "desc": "쇼핑·길거리음식의 메카", "emoji": "🛍️"},
    {"name": "인사동 (Insadong)", "lat": 37.574389, "lon": 126.985000, "desc": "전통 공예·찻집 골목", "emoji": "🖼️"},
    {"name": "북촌한옥마을 (Bukchon Hanok Village)", "lat": 37.582604, "lon": 126.983163, "desc": "한옥 골목 산책 코스", "emoji": "🏘️"},
    {"name": "동대문디자인플라자 (DDP)", "lat": 37.566295, "lon": 127.009379, "desc": "현대 건축 + 야시장 근처", "emoji": "🏙️"},
    {"name": "홍대 (Hongdae / Hongik Univ)", "lat": 37.556264, "lon": 126.923893, "desc": "젊음의 거리·클럽·카페", "emoji": "🎸"},
    {"name": "강남역 (Gangnam)", "lat": 37.498095, "lon": 127.027610, "desc": "쇼핑·먹거리·K-pop 문화의 중심", "emoji": "💃"},
    {"name": "롯데월드타워 (Lotte World Tower)", "lat": 37.512573, "lon": 127.102645, "desc": "초고층 전망대 + 쇼핑몰", "emoji": "🏢"},
]

# 사이드바 컨트롤
st.sidebar.header("설정")
map_type = st.sidebar.selectbox("지도 스타일", ["OpenStreetMap", "Stamen Terrain", "Stamen Toner"], index=0)
use_cluster = st.sidebar.checkbox("마커 클러스터 사용 (권장)", value=True)
show_popups = st.sidebar.checkbox("팝업 내용 표시", value=True)
zoom = st.sidebar.slider("초기 확대 수준", min_value=10, max_value=15, value=12)

# 필터 (검색어로 스팟 필터링)
query = st.sidebar.text_input("스팟 필터 (이름으로 검색)", value="")

filtered = [s for s in spots if query.strip().lower() in s["name"].lower()]
if not filtered:
    filtered = spots  # 빈 검색이면 전체 표시

# Folium 지도 생성
center_lat = sum(s["lat"] for s in filtered) / len(filtered)
center_lon = sum(s["lon"] for s in filtered) / len(filtered)

tiles = {
    "OpenStreetMap": "OpenStreetMap",
    "Stamen Terrain": "Stamen Terrain",
    "Stamen Toner": "Stamen Toner",
}[map_type]

m = folium.Map(location=[center_lat, center_lon], zoom_start=zoom, tiles=tiles)

# 마커 그룹 or 클러스터 생성
if use_cluster:
    cluster = MarkerCluster(name="Tourist Spots").add_to(m)
    marker_container = cluster
else:
    marker_container = folium.FeatureGroup(name="Tourist Spots").add_to(m)

for s in filtered:
    popup_html = f"<b>{s['emoji']} {s['name']}</b><br>{s['desc']}"
    if show_popups:
        popup = folium.Popup(popup_html, max_width=300)
    else:
        popup = None

    folium.Marker(
        location=[s["lat"], s["lon"]],
        popup=popup,
        tooltip=s["name"],
        icon=folium.Icon(icon="info-sign"),
    ).add_to(marker_container)

# 클릭 좌표 표시
m.add_child(folium.LatLngPopup())

folium.LayerControl().add_to(m)

# 지도 출력
st.subheader("지도 보기")
map_data = st_folium(m, width=900, height=650)

# 클릭한 좌표 정보를 하단에 표시
if map_data and map_data.get("last_clicked"):
    latlon = map_data["last_clicked"]
    st.info(f"마커가 없는 지점을 클릭했어요 — 위도: {latlon['lat']:.6f}, 경도: {latlon['lng']:.6f}")

st.markdown("---")
st.caption("Tip: '스팟 필터'에 영어/한글 일부 단어를 넣으면 해당 장소만 볼 수 있어요. 예: 'Gyeong' 또는 '경복'")
```

---

# 파일: requirements.txt

```
streamlit>=1.20.0
folium>=0.14.0
streamlit-folium>=0.11.0

# (Optional but safe)
branca>=0.6.0
```

---

# 배포 / 실행 방법

1. 위의 `app.py`와 `requirements.txt` 파일을 같은 깃허브 리포지토리에 올리세요.
2. Streamlit Cloud([https://streamlit.io/cloud)에서](https://streamlit.io/cloud%29에서) "New app" → GitHub 리포 연결 → 레포와 `app.py` 경로 선택 → 배포.
3. 로컬에서 테스트하려면:

```bash
python -m venv .venv
source .venv/bin/activate  # 윈도우: .venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

필요하면 `지도 스타일`, `마커 클러스터` 등 UI 조정 더 해줄게요. 캔버스에 코드와 requirements.txt 모두 올려뒀어요.
