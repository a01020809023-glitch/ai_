import streamlit as st

st.set_page_config(page_title="MBTI 진로 추천 💫", page_icon="🎯")

st.title("🎯 MBTI로 알아보는 나의 진로 탐색 💬")
st.write("안녕! 👋 아래에서 너의 MBTI 유형을 골라봐.  
그럼 너한테 잘 맞는 진로 2가지랑,  
그 진로에 어울리는 학과와 성격 특징도 알려줄게! 😎")

# MBTI 리스트
mbti_list = [
    "INTJ", "INTP", "ENTJ", "ENTP",
    "INFJ", "INFP", "ENFJ", "ENFP",
    "ISTJ", "ISFJ", "ESTJ", "ESFJ",
    "ISTP", "ISFP", "ESTP", "ESFP"
]

selected_mbti = st.selectbox("👉 너의 MBTI를 골라봐!", mbti_list)

# MBTI별 진로 데이터
career_data = {
    "INTJ": {
        "careers": ["데이터 분석가", "전략 기획자"],
        "major": "통계학, 경영학, 산업공학",
        "traits": "논리적이고 미래를 예측하는 걸 좋아하는 사람에게 찰떡!"
    },
    "INTP": {
        "careers": ["연구원", "개발자"],
        "major": "컴퓨터공학, 물리학, 수학",
        "traits": "아이디어 뱅크! 독창적인 해결책 찾는 걸 즐기는 타입 💡"
    },
    "ENTJ": {
        "careers": ["경영 컨설턴트", "프로젝트 매니저"],
        "major": "경영학, 경제학, 리더십 관련 학과",
        "traits": "리더십 넘치는 추진력의 소유자! 💪 목표지향적인 사람에게 딱"
    },
    "ENTP": {
        "careers": ["창업가", "마케팅 기획자"],
        "major": "경영학, 광고홍보학, 미디어학",
        "traits": "도전정신 MAX🔥 새로운 아이디어로 세상을 바꾸고 싶어하는 사람"
    },
    "INFJ": {
        "careers": ["심리상담사", "교사"],
        "major": "심리학, 교육학, 사회복지학",
        "traits": "타인의 마음을 잘 이해하고, 세상을 따뜻하게 만들고 싶은 사람 💕"
    },
    "INFP": {
        "careers": ["작가", "예술가"],
        "major": "문예창작, 디자인, 철학",
        "traits": "감성이 풍부하고 자기만의 색깔을 중요하게 생각하는 타입 🎨"
    },
    "ENFJ": {
        "careers": ["교육자", "인사담당자"],
        "major": "교육학, 심리학, 사회학",
        "traits": "사람을 이끄는 따뜻한 리더 🌈 팀워크를 중요하게 생각하는 사람"
    },
    "ENFP": {
        "careers": ["광고기획자", "콘텐츠 크리에이터"],
        "major": "미디어학, 디자인, 커뮤니케이션학",
        "traits": "창의력 폭발💥 사람들과 어울리며 에너지 주는 타입"
    },
    "ISTJ": {
        "careers": ["회계사", "공무원"],
        "major": "경영학, 법학, 행정학",
        "traits": "성실하고 책임감 있는 완벽주의자 👍 현실적이고 계획적인 사람"
    },
    "ISFJ": {
        "careers": ["간호사", "사회복지사"],
        "major": "간호학, 사회복지학, 심리학",
        "traits": "배려심 깊고 따뜻한 마음의 소유자 💗 사람을 도와주는 일에 행복함을 느낌"
    },
    "ESTJ": {
        "careers": ["관리자", "경영자"],
        "major": "경영학, 경제학, 행정학",
        "traits": "조직적이고 효율적인 현실주의자 🧠 규칙과 시스템을 잘 다루는 타입"
    },
    "ESFJ": {
        "careers": ["교사", "간호사"],
        "major": "교육학, 간호학, 사회복지학",
        "traits": "친절하고 협동적인 분위기 메이커 🎀 사람 사이의 조화를 중요하게 생각해"
    },
    "ISTP": {
        "careers": ["엔지니어", "파일럿"],
        "major": "기계공학, 항공학, 컴퓨터공학",
        "traits": "문제 해결 능력 갑 💪 손으로 직접 무언가 만드는 걸 좋아하는 타입"
    },
    "ISFP": {
        "careers": ["디자이너", "사진작가"],
        "major": "디자인학, 미술학, 예술 관련 학과",
        "traits": "감각적이고 따뜻한 예술가 타입 🎨 자유로운 분위기를 선호해"
    },
    "ESTP": {
        "careers": ["영업사원", "스포츠 매니저"],
        "major": "체육학, 마케팅, 경영학",
        "traits": "활동적이고 에너지 넘치는 현실파 💥 즉흥적이지만 문제 해결력도 뛰어나!"
    },
    "ESFP": {
        "careers": ["연예인", "이벤트 플래너"],
        "major": "공연예술학, 방송연예학, 커뮤니케이션학",
        "traits": "사람들과 어울리는 걸 즐기고, 즐거운 분위기를 만드는 타입 🌟"
    },
}

if selected_mbti:
    st.subheader(f"✨ {selected_mbti} 유형에게 어울리는 진로 ✨")
    st.write(f"**추천 진로:** {career_data[selected_mbti]['careers'][0]} 🧭, {career_data[selected_mbti]['careers'][1]} 🚀")
    st.write(f"**적합 학과:** {career_data[selected_mbti]['major']}")
    st.write(f"**이런 성격이 잘 맞아요:** {career_data[selected_mbti]['traits']}")
    st.success("너랑 잘 어울리는 길을 찾아봐! 💫")
