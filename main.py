import streamlit as st
st.title('나의 첫 웹 서비스 만들기!')
st.write('안녕하세요, 감사해용 잘있어용!')
name=st.text_input('너의 이름은!')
if st.button('인사말 생성'):
  st.write(name+'님!! 반갑습니다!!!)
