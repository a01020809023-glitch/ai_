import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(page_title="서울 지하철 승하차 TOP10", layout="wide")

# -------------------------------
# 데이터 불러오기
# -------------------------------
@st.cache_data
def load_data():
    df = pd.read_csv("CARD_SUBWAY_MONTH_202510.csv", encoding="cp949", sep="\t")
    df["총승객수"] = df["승차총승객수"] + df["하차총승객수"]
    return df

df = load_data()

st.title("🚇 2025년 10월 지하철 역별 승하차 TOP10 분석")
st.markdown("날짜와 호선을 선택하면 **승차+하차 승객수가 가장 많은 10개 역**을 보여줘요!")

# -------------------------------
# 사이드바 선택
# -------------------------------
dates = sorted(df["사용일자"].unique())
lines = sorted(df["노선명"].unique())

selected_date = st.sidebar.selectbox("📅 날짜 선택", dates)
selected_line = st.sidebar.selectbox("🚈 호선 선택", lines)

# -------------------------------
# 데이터 필터링
# -------------------------------
filtered = df[(df["사용일자"] == selected_date) & (df["노선명"] == selected_line)]

if filtered.empty:
    st.warning("해당 조건에 맞는 데이터가 없습니다.")
    st.stop()

# TOP10 역 추출
top10 = filtered.sort_values("총승객수", ascending=False).head(10)

# -------------------------------
# 색상 (1등 빨간색, 나머지 파란 → 연파랑 그라데이션)
# -------------------------------
colors = ["red"] + [
    f"rgba(0, 0, 255, {opacity})" for opacity in 
    list(reversed([0.1 + 0.08 * i for i in range(1, 10)]))
]

# -------------------------------
# Plotly 그래프
# -------------------------------
fig = go.Figure()

fig.add_trace(
    go.Bar(
        x=top10["역명"],
        y=top10["총승객수"],
        marker=dict(color=colors),
        text=top10["총승객수"],
        textposition="outside"
    )
)

fig.update_layout(
    title=f"📊 {selected_date} / {selected_line} 승하차 TOP10 역",
    xaxis_title="역명",
    yaxis_title="총 승객수(명)",
    template="plotly_white",
    height=600
)

st.plotly_chart(fig, use_container_width=True)
