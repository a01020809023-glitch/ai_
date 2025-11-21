import streamlit as st
import folium
from streamlit_folium import st_folium

# 앱 제목
st.title("서울 외국인 인기 관광지 Top10")

# 서울 관광지 데이터 (예시)
# 이름, 위도, 경도
tourist_spots = [
    {"name": "경복궁", "lat": 37.5796, "lon": 126.9770},
    {"name": "N서울타워", "lat": 37.5512, "lon": 126.9882},
    {"name": "명동거리", "lat": 37.5638, "lon": 126.9860},
    {"name": "인사동", "lat": 37.5740, "lon": 126.9857},
    {"name": "동대문디자인플라자(DDP)", "lat": 37.5663, "lon": 127.0090},
    {"name": "홍대거리", "lat": 37.5563, "lon": 126.9236},
    {"name": "청계천", "lat": 37.5700, "lon": 126.9769},
    {"name": "북촌한옥마을", "lat": 37.5826, "lon": 126.9830},
    {"name": "롯데월드타워", "lat": 37.5131, "lon": 127.1020},
    {"name": "코엑스몰", "lat": 37.5110, "lon": 127.0595},
]

# Folium 지도 생성
m = folium.Map(location=[37.5665, 126.9780], zoom_start=12)

# 마커 추가
for spot in tourist_spots:
    folium.Marker(
        location=[spot["lat"], spot["lon"]],
        popup=spot["name"],
        icon=folium.Icon(color="red", icon="info-sign")
    ).add_to(m)

# 지도 표시
st.subheader("지도 보기")
st_folium(m, width=700, height=500)
