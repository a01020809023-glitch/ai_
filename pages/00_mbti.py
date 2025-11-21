import streamlit as st

st.set_page_config(page_title="MBTI 취향 추천 🎧📚🎬", page_icon="🧭", layout="centered")

st.title("MBTI로 골라주는 취향 추천 🌟")
st.write("안녕! MBTI 하나 골라주면 너한테 딱 맞는 책 2권, 영화 2편, 그리고 진로 2가지를 추천해줄게. 편하게 골라봐~ 😄")

MBTI_LIST = [
    "ISTJ","ISFJ","INFJ","INTJ",
    "ISTP","ISFP","INFP","INTP",
    "ESTP","ESFP","ENFP","ENTP",
    "ESTJ","ESFJ","ENFJ","ENTJ",
]

# 추천 데이터 (간단히 예시)
RECOMMENDATIONS = {
    "ISTJ": {
        "books": [("책1","설명1"),("책2","설명2")],
        "movies": [("영화1","설명1"),("영화2","설명2")],
        "careers": [("진로1","설명1"),("진로2","설명2")]
    },
    "ISFJ": {
        "books": [("책1","설명1"),("책2","설명2")],
        "movies": [("영화1","설명1"),("영화2","설명2")],
        "careers": [("진로1","설명1"),("진로2","설명2")]
    },
    # 나머지 MBTI도 동일 구조
}

mbti = st.selectbox("너의 MBTI를 골라줘! 😊", MBTI_LIST)

if st.button("추천 받기 ✨"):
    data = RECOMMENDATIONS.get(mbti)
    if not data:
        st.warning("아직 그 유형에 대한 추천이 준비되지 않았어...😅")
    else:
        st.markdown(f"### {mbti} — 추천 리스트 🎯")
        st.write("**책 추천 (2권)** 📚")
        for title, note in data["books"]:
            st.markdown(f"- **{title}** — {note}")

        st.write("**영화 추천 (2편)** 🎬")
        for title, note in data["movies"]:
            st.markdown(f"- **{title}** — {note}")

        st.write("**진로 추천 (2가지)** 💼")
        for title, note in data["careers"]:
            st.markdown(f"- **{title}** — {note}")

        st.success("마음에 드는 추천 찾았어? 더 보고 싶다면 MBTI를 바꿔서 다시 눌러봐~ 😄")
