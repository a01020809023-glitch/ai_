import streamlit as st

# MBTI 기반 책/영화/진로 추천 앱
# This single-file Streamlit app recommends 2 books, 2 movies, and 2 career paths
# for the selected MBTI type. No extra libraries required (only streamlit).

st.set_page_config(page_title="MBTI 취향 추천 🎧📚🎬", page_icon="🧭", layout="centered")

st.title("MBTI로 골라주는 취향 추천 🌟")
st.write("안녕! MBTI 하나 골라주면 너한테 딱 맞는 책 2권, 영화 2편, 그리고 진로 2가지를 추천해줄게. 편하게 골라봐~ 😄")

MBTI_LIST = [
    "ISTJ","ISFJ","INFJ","INTJ",
    "ISTP","ISFP","INFP","INTP",
    "ESTP","ESFP","ENFP","ENTP",
    "ESTJ","ESFJ","ENFJ","ENTJ",
]

# 각 유형별 추천 데이터: 책 2권, 영화 2편, 진로 2가지, 간단한 코멘트
RECOMMENDATIONS = {
    "ISTJ": {
        "books": [("어떤 조직에서든 통하는 업무의 법칙", "체계적이고 현실적인 관점으로 업무·사회 구조를 이해하고 싶다면 추천해💼"), ("The Checklist Manifesto", "실무 중심의 문제 해결을 좋아하면 좋아해")],
        "movies": [("Spotlight", "사실과 절차 중심의 드라마—사건을 차분히 파헤치는 이야기"), ("Hidden Figures", "조직 안에서의 끈기와 성취를 좋아하면 딱!")],
        "careers": [("회계사", "정확성과 책임감을 살릴 수 있어"), ("품질관리 엔지니어", "절차를 세우고 지키는 일에 강해")]
    },
    "ISFJ": {
        "books": [("작은 것들의 행복", "따뜻하고 사람 중심의 이야기를 좋아한다면"), ("To Kill a Mockingbird", "공감과 도덕을 다루는 고전")],
        "movies": [("The Pursuit of Happyness", "가족·희생·돌봄의 가치가 담긴 영화"), ("About Time", "사소한 순간들을 소중히 여기는 감성물")],
        "careers": [("간호사", "남을 돌보는 걸 잘해"), ("사회복지사", "사람을 돕는 안정적인 역할")]
    },
    "INFJ": {
        "books": [("작은 것들의 신", "내면과 의미를 찾는 감수성이 풍부한 책"), ("Man's Search for Meaning", "삶의 의미를 탐구하는 깊이 있는 책")],
        "movies": [("Eternal Sunshine of the Spotless Mind", "내면의 감정과 기억을 섬세하게 다룸"), ("Her", "관계와 존재에 대한 사려깊은 SF")],
        "careers": [("상담심리사", "타인의 마음을 이해하고 도울 수 있어"), ("작가/콘텐츠 크리에이터", "의미를 전달하는 일에 적합")]
    },
    "INTJ": {
        "books": [("Thinking, Fast and Slow", "논리와 전략을 좋아하는 사람에게 추천"), ("The Innovator's Dilemma", "시스템과 전략을 분석하는 데 좋은 책")],
        "movies": [("Inception", "복잡한 구조와 지적 도전 좋아하면 굿"), ("The Social Network", "전략·야망·계획이 드러나는 이야기")],
        "careers": [("데이터 사이언티스트", "문제 해결과 전략에 강함"), ("연구개발(R&D)", "장기적 비전으로 시스템을 설계")]
    },
    "ISTP": {
        "books": [("The Art of Racing in the Rain", "행동 중심의 감동적인 스토리"), ("Zen and the Art of Motorcycle Maintenance", "기술과 철학의 결합을 즐기는 타입")],
        "movies": [("Mad Max: Fury Road", "액션 중심, 실감나는 몰입감"), ("Baby Driver", "리듬감 있는 액션과 스타일")],
        "careers": [("기술자/정비사", "손으로 만지는 작업에 재능이 있어"), ("파일럿/응급구조원", "즉각적인 판단과 행동이 요구되는 일")]
    },
    "ISFP": {
        "books": [("The Little Prince", "감성적이고 상징적인 이야기를 좋아한다면"), ("The Night Circus", "상상력과 분위기 있는 소설")],
        "movies": [("Amélie", "예쁜 감성, 따뜻한 일상 이야기"), ("La La Land", "감성적이고 음악적인 무드")],
        "careers": [("디자이너/아티스트", "미적 감각을 살릴 수 있어"), ("사진작가", "순간의 감정을 포착하는 일")]
    },
    "INFP": {
        "books": [("The Alchemist", "여정을 통해 자기답게 사는 이야기를 좋아한다면"), ("Norwegian Wood", "감수성 짙은 문학")],
        "movies": [("Into the Wild", "자아 탐색과 자유를 그린 영화"), ("The Secret Life of Walter Mitty", "상상과 모험의 감성")],
        "careers": [("작가/시인", "내면의 표현을 직업으로 삼을 수 있어"), ("상담사/교육자", "사람과 가치 중심의 역할")]
    },
    "INTP": {
        "books": [("Gödel, Escher, Bach", "지적 장난과 아이디어를 즐긴다면"), ("The Structure of Scientific Revolutions", "사고의 틀을 바꾸는 책")],
        "movies": [("The Matrix", "철학적이고 개념적인 SF"), ("Good Will Hunting", "지적 성장과 인간관계를 다룸")],
        "careers": [("연구원/이론가", "아이디어로 문제를 풀기 좋아함"), ("소프트웨어 개발자", "논리적 설계를 즐김")]
    },
    "ESTP": {
        "books": [("Shoe Dog", "도전과 실행을 좋아한다면 재밌게 읽을 수 있어"), ("Born to Run", "액티브한 라이프스타일에 영감")],
        "movies": [("The Fast and the Furious", "속도와 액션 좋아하는 타입"), ("Ocean's Eleven", "스릴과 재치 있는 팀플레이")],
        "careers": [("영업 및 마케팅", "즉흥적이고 사람을 잘 다룸"), ("기업가", "실행력으로 기회를 잡음")]
    },
    "ESFP": {
        "books": [("The Happiness Project", "현재의 즐거움을 중시하는 사람에게"), ("Eat Pray Love", "경험과 감각을 즐기는 이야기")],
        "movies": [("The Greatest Showman", "화려함과 즐거움을 즐기는 무드"), ("Mamma Mia!", "신나는 뮤지컬과 긍정 에너지")],
        "careers": [("연예/엔터테인먼트", "무대와 사람을 즐김"), ("이벤트 플래너", "일을 즐겁게 꾸밀 수 있어")]
    },
    "ENFP": {
        "books": [("Big Magic", "창의성과 모험을 응원하는 책"), ("The Perks of Being a Wallflower", "감성적이고 진솔한 성장담")],
        "movies": [("Amélie", "상상력과 따뜻함을 좋아한다면"), ("500 Days of Summer", "감정의 파도와 자유로운 관계")],
        "careers": [("창업가/콘텐츠 크리에이터", "아이디어로 사람을 움직임"), ("PR/광고", "사람과 스토리를 연결")]
    },
    "ENTP": {
        "books": [("The Lean Startup", "아이디어 실험과 빠른 피드백을 좋아하면"), ("Surely You're Joking, Mr. Feynman!", "호기심 많은 사람에게 추천")],
        "movies": [("The Social Network", "아이디어로 세상을 바꾸는 이야기"), ("Catch Me If You Can", "교묘하고 재치있는 플롯")],
        "careers": [("스타트업 창업자", "아이디어로 실험하길 좋아함"), ("컨설턴트", "빠르게 문제 해결하는 역할")]
    },
    "ESTJ": {
        "books": [("Good to Great", "리더십과 시스템을 좋아하는 사람에게"), ("The 7 Habits of Highly Effective People", "실용적 자기계발서")],
        "movies": [("Remember the Titans", "팀워크와 리더십을 다룬 실화"), ("A Few Good Men", "윤리·규율·책임을 생각하게 함")],
        "careers": [("관리자/운영 매니저", "구조와 규칙을 잘 세움"), ("법률/행정", "정확성과 권위를 발휘")]
    },
    "ESFJ": {
        "books": [("The Gifts of Imperfection", "관계와 돌봄을 중시한다면"), ("The Help", "공감과 연대의 이야기")],
        "movies": [("The Blind Side", "돌봄과 헌신의 감동 실화"), ("Julie & Julia", "사람과 음식을 잇는 따뜻한 이야기")],
        "careers": [("교사", "사람을 챙기고 돕는 걸 즐김"), ("간호·케어 분야", "돌봄에 강점이 있음")]
    },
    "ENFJ": {
        "books": [("Leaders Eat Last", "사람을 이끄는 가치에 공감한다면"), ("Daring Greatly", "진정성과 공감의 리더십")],
        "movies": [("Dead Poets Society", "영감을 주는 리더와 성장 이야기"), ("Freedom Writers", "변화를 이끄는 교육적 감동")],
        "careers": [("교수/교육 리더", "사람을 이끄는 소명감"), ("HR/조직개발", "사람을 성장시키는 역할")]
    },
    "ENTJ": {
        "books": [("The Hard Thing About Hard Things", "리더십의 현실적 조언을 원한다면"), ("Atlas Shrugged", "거대한 비전과 철학적 도전")],
        "movies": [("The Wolf of Wall Street", "야망과 전략이 돋보이는 이야기"), ("The Aviator", "거대한 비전과 추진력")],
        "careers": [("경영자/CEO", "비전과 추진력을 발휘"), ("전략 컨설턴트", "큰 그림을 설계하는 일")]
    },
}

st.selectbox("너의 MBTI를 골라줘! 😊", MBTI_LIST, key="mbti_select")
mbti = st.session_state.mbti_select

if st.button("추천 받기 ✨"):
    data = RECOMMENDATIONS.get(mbti)
    if not data:
        st.warning("아직 그 유형에 대한 추천이 준비되지 않았어...😅")
    else:
        st.markdown(f"### {mbti} — 추천 리스트 🎯")
        st.write("**책 추천 (2권)** 📚")
        for title, note in data["books"]:
            st.markdown(f"- **{title}** — {note}")

        st.write("\n**영화 추천 (2편)** 🎬")
        for title, note in data["movies"]:
            st.markdown(f"- **{title}** — {note}")

        st.write("\n**진로 추천 (2가지)** 💼")
        for title, note in data["careers"]:
            st.markdown(f"- **{title}** — {note}")

        st.success("마음에 드는 추천 찾았어? 더 보고 싶다면 MBTI를 바꿔서 다시 눌러봐~ 😄")

st.markdown("---")
st.info("이 앱은 예시 추천을 담고 있어. 진로 선택은 너의 경험과 상담을 통해 결정하는 걸 권장해! 💡")

# 간단한 저작권/출처 안내
st.caption("추천은 일반적 성향에 기반한 제안입니다 — 취향은 사람마다 다름! 🙌")
