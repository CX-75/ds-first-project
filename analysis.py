def generate_plan(destination, days, people, style):
    plan = {}

    # 住宿建议
    if style == "悠闲":
        plan["hotel"] = "市中心高评分酒店，交通方便，适合慢慢玩"
    elif style == "特种兵":
        plan["hotel"] = "靠近地铁的性价比酒店，方便快速移动"
    elif style == "美食为主":
        plan["hotel"] = "美食街附近的精品酒店"
    else:
        plan["hotel"] = "家庭房或连通房酒店，空间更大"

    # 行程安排（非常 MVP）
    plan["route"] = f"{days} 天行程：每天安排 2–3 个主要景点，留出自由时间"

    # 餐饮推荐
    plan["food"] = f"重点体验 {destination} 的本地特色餐厅和小吃"

    return plan
