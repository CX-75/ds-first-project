import pandas as pd

# 读取 CSV 数据
df = pd.read_csv("data/cities.csv")

def generate_plan(city, days, people, style):
    """
    生成旅行攻略
    city: 目的地
    days: 天数
    people: 人数
    style: 旅行风格（悠闲 / 冒险 / 家庭）
    """
    plan = {}
    
    # 过滤城市
    city_df = df[df["city"].str.lower() == city.lower()]
    if city_df.empty:
        return f"抱歉，我们暂时没有 {city} 的数据。"

    for day in range(1, days+1):
        day_df = city_df[city_df["day"] == day]
        if day_df.empty:
            continue
        plan[day] = []
        for _, row in day_df.iterrows():
            plan[day].append({
                "attraction": row["attraction"],
                "hotel": row["hotel"],
                "restaurant": row["restaurant"]
            })
    
    return plan
