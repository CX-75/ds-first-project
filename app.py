import streamlit as st
from analysis import generate_plan

st.title("🧳 旅行攻略生成器 · MVP")

destination = st.text_input("你要去哪里？")
days = st.number_input("玩几天？", min_value=1, max_value=30, value=3)
people = st.number_input("几个人一起？", min_value=1, max_value=10, value=1)
style = st.selectbox(
    "旅行风格",
    ["悠闲", "特种兵", "美食为主", "亲子"]
)

if st.button("生成攻略"):
    plan = generate_plan(destination, days, people, style)

    st.subheader("🏨 住宿建议")
    st.write(plan["hotel"])

    st.subheader("🗺️ 行程路线")
    st.write(plan["route"])

    st.subheader("🍜 餐饮推荐")
    st.write(plan["food"])
