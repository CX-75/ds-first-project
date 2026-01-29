import streamlit as st
from analysis import generate_plan

st.title("智能旅行攻略生成器 🌍✈️")

city = st.text_input("目的地")
days = st.number_input("旅行天数", min_value=1, max_value=14, value=2)
people = st.number_input("人数", min_value=1, max_value=10, value=1)
style = st.selectbox("旅行风格", ["悠闲", "冒险", "家庭"])

if st.button("生成攻略"):
    plan = generate_plan(city, days, people, style)
    if isinstance(plan, str):
        st.warning(plan)
    else:
        for day, items in plan.items():
            st.subheader(f"第 {day} 天")
            for i, item in enumerate(items, 1):
                st.markdown(
                    f"**{i}. 景点:** {item['attraction']}  \n"
                    f"**酒店:** {item['hotel']}  \n"
                    f"**餐厅:** {item['restaurant']}"
                )
