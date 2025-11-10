# streamlit_population_app.py
# Single-file Streamlit app that reads a wide-format population CSV (like /mnt/data/population.csv)
# and draws an interactive Plotly line chart showing age (x) vs population (y) for a selected region.

import re
from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title="Population by Age — Interactive", layout="wide")

st.title("지역별 연령별 인구수 시각화 📊")
st.markdown(
    "업로드한 CSV(또는 동일한 폴더의 `population.csv`)에서 `행정구역`을 선택하면 나이-인구수 꺾은선 그래프를 그려줍니다."
)

# Sidebar: file uploader or use default
st.sidebar.header("데이터 입력")
uploaded = st.sidebar.file_uploader("CSV 파일 업로드 (인코딩 CP949 또는 UTF-8 권장)", type=["csv"]) 
use_sample = False

if uploaded is None:
    default_path = Path("./population.csv")
    if default_path.exists():
        try:
            df = pd.read_csv(default_path)
            use_sample = True
        except Exception:
            # try cp949 fallback
            df = pd.read_csv(default_path, encoding='cp949')
            use_sample = True
    else:
        st.sidebar.error("업로드할 파일이 없습니다. 왼쪽에서 CSV 파일을 업로드하세요.")
        st.stop()
else:
    # try multiple encodings gracefully
    try:
        df = pd.read_csv(uploaded)
    except Exception:
        try:
            uploaded.seek(0)
            df = pd.read_csv(uploaded, encoding='cp949')
        except Exception:
            uploaded.seek(0)
            df = pd.read_csv(uploaded, encoding='latin1')

st.sidebar.markdown(f"파일 로드: {'/mnt/data/population.csv (디폴트)' if use_sample else '업로드된 파일'}")

# Quick data checks
st.sidebar.header("데이터 확인")
st.sidebar.write(f"행 수: {df.shape[0]}  |  열 수: {df.shape[1]}")

# Ensure expected column for region
if '행정구역' not in df.columns:
    st.error("데이터에 '행정구역' 열이 필요합니다. 파일을 확인해주세요.")
    st.stop()

# Identify age columns (columns that contain '세' or '100세 이상')
age_col_pattern = re.compile(r"(\d{1,3})세$")
age_cols = []
extra_100 = None
for col in df.columns:
    m = age_col_pattern.search(col)
    if m:
        age_cols.append((int(m.group(1)), col))
    elif '100세' in col:  # for '100세 이상' style
        extra_100 = col

# sort by age
age_cols.sort(key=lambda x: x[0])
ages = [a for a, c in age_cols]
age_column_names = [c for a, c in age_cols]
if extra_100:
    ages.append(100)
    age_column_names.append(extra_100)

if len(age_column_names) == 0:
    st.error("연령 칼럼(예: '0세', '1세', ... 또는 '100세 이상')을 찾지 못했습니다.")
    st.stop()

# Region selector
regions = df['행정구역'].astype(str).tolist()
selected_region = st.selectbox("지역구 선택", regions)

# Filter row
row = df[df['행정구역'].astype(str) == str(selected_region)]
if row.empty:
    st.error("선택한 지역의 데이터가 없습니다.")
    st.stop()

# extract age & population values and build tidy DataFrame
pop_values = []
for col, age in zip(age_column_names, ages):
    try:
        val = row.iloc[0][col]
        # if value is string with commas, remove
        if isinstance(val, str):
            val = val.replace(',', '').strip()
        val = pd.to_numeric(val, errors='coerce')
    except Exception:
        val = None
    pop_values.append(val)

plot_df = pd.DataFrame({
    'age': ages,
    'population': pop_values
}).dropna()

# Plotly line chart
fig = px.line(plot_df, x='age', y='population', markers=True,
              title=f"{selected_region} — 나이별 인구수",
              labels={'age': '나이 (세)', 'population': '인구수'})
fig.update_traces(hovertemplate='나이: %{x}세<br>인구수: %{y:,.0f}<extra></extra>')
fig.update_layout(xaxis=dict(tickmode='linear'))

st.plotly_chart(fig, use_container_width=True)

# Show raw table and download option
with st.expander('원본 탭/원자료 보기'):
    st.write(row.reset_index(drop=True))

# Allow download of the tidy data for the selected region
csv = plot_df.to_csv(index=False)
st.download_button('선택지역 데이터 CSV로 저장', csv, file_name=f"{selected_region}_age_population.csv", mime='text/csv')

st.markdown("---")
st.caption("CSV의 연령 컬럼명이 '0세','1세',... 또는 '100세 이상' 같은 형식이면 자동으로 인식합니다.")


# requirements.txt content (for Streamlit Cloud)
# ----------------------
# streamlit
# pandas
# plotly
# ----------------------
# Save this file as 'streamlit_app.py' (Streamlit Cloud의 기본 엔트리 파일 이름은 'streamlit_app.py' 또는 'app.py' 둘 중 하나입니다.)
