# app.py
import streamlit as st
from analysis import generate_itinerary_ai

# 页面配置
st.set_page_config(
    page_title="智能旅行攻略生成器",
    page_icon="🗺️",
    layout="wide"
)

st.image("https://images.unsplash.com/photo-1507525428034-b723cf961d3e?fit=crop&w=1200&q=80", width=700)
st.title("🗺️ 智能旅行攻略生成器")
st.write("输入城市、天数、人数和旅行风格，生成每日行程攻略！")

# 左右栏布局
col1, col2 = st.columns([1, 2])

with col1:
    city = st.text_input("城市", "巴黎")
    days = st.number_input("天数", min_value=1, max_value=14, value=2)
    people = st.number_input("人数", min_value=1, max_value=20, value=2)
    style = st.selectbox("旅行风格", ["悠闲", "冒险", "特种兵"])
    generate = st.button("生成攻略")

with col2:
    if generate:
        with st.spinner("生成中，请稍候..."):
            itinerary = generate_itinerary_ai(city, days, people, style)
        
        st.success("攻略生成完成！")
        for day, items in itinerary.items():
            with st.expander(f"📅 第 {day} 天"):
                for i, item in enumerate(items, 1):
                    st.markdown(f"🏛️ **景点:** {item['attraction']}")
                    st.markdown(f"🏨 **酒店:** {item['hotel']}")
                    st.markdown(f"🍽️ **餐厅:** {item['restaurant']}")
                    st.markdown("---")  # 每个景点分隔
