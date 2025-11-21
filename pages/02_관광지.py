import streamlit as st

st.set_page_config(page_title="서울 외국인 인기 관광지 Top10", layout="wide")
st.title("서울 외국인 인기 관광지 Top10 🌏")

# folium과 streamlit-folium 설치 여부 확인
try:
    import folium
    from streamlit_folium import st_folium
except ModuleNotFoundError:
    st.error("folium 또는 streamlit-folium 패키지가 설치되지 않았습니다.\n"
             "requirements.txt를 확인하고 앱을 다시 실행해주세요.")
    st.stop()

# 서울 관광지 Top10 데이터
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

# 마커 색상 지정: 1등 빨강, 2~10등 파랑
for i, spot in enumerate(tourist_spots):
    color = "red" if i == 0 else "blue"
    folium.Marker(
        location=[spot["lat"], spot["lon"]],
        popup=f"{i+1}위: {spot['name']}",
        icon=folium.Icon(color=color, icon="info-sign")
    ).add_to(m)

# 지도 표시
st.subheader("서울 인기 관광지 지도")
st_folium(m, width=700, height=500)
