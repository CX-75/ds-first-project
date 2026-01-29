# analysis.py
import random

# 风格对应景点池
STYLE_POOLS = {
    "悠闲": ["博物馆", "咖啡馆漫步", "公园", "广场", "艺术中心", "购物街"],
    "冒险": ["徒步路线", "攀岩场所", "探险活动", "山地骑行", "漂流"],
    "特种兵": ["极限运动场", "探险活动", "跳伞体验", "高空索道"]
}

HOTELS_POOL = ["豪华酒店", "精品酒店", "经济型酒店", "民宿", "青年旅舍"]
RESTAURANTS_POOL = ["米其林餐厅", "当地特色餐厅", "咖啡厅", "小酒馆", "快餐店"]

def generate_itinerary_ai(city, days, people, style):
    """
    随机生成每日行程
    """
    itinerary = {}
    attractions_pool = STYLE_POOLS.get(style, STYLE_POOLS["悠闲"])
    
    used_attractions = set()
    
    for day in range(1, days + 1):
        day_plan = []
        num_attractions = min(3, len(attractions_pool))
        daily_attractions = random.sample(attractions_pool, num_attractions)
        
        for attraction_name in daily_attractions:
            if attraction_name in used_attractions:
                continue
            used_attractions.add(attraction_name)
            
            hotel = random.choice(HOTELS_POOL)
            restaurant = random.choice(RESTAURANTS_POOL)
            
            day_plan.append({
                "attraction": f"{city} {attraction_name}",
                "hotel": f"{city} {hotel}",
                "restaurant": f"{city} {restaurant}"
            })
        
        itinerary[day] = day_plan
    
    return itinerary

# 测试用
if __name__ == "__main__":
    plan = generate_itinerary_ai("巴黎", 2, 2, "悠闲")
    for day, items in plan.items():
        print(f"第 {day} 天:")
        for i, item in enumerate(items, 1):
            print(f"  {i}. 景点: {item['attraction']}")
            print(f"     酒店: {item['hotel']}")
            print(f"     餐厅: {item['restaurant']}")
        print("\n")
