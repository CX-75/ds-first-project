# 旅行攻略生成器 (MVP)

一个基于 **Python** 和 **Streamlit** 的简易旅行计划生成网站。

## 功能
- 根据用户输入生成旅行攻略
- 提供住宿、行程和餐饮建议
- 基于规则的逻辑（MVP 版本）

## 技术栈
- Python 3.13
- Streamlit
- VS Code + zsh

## 使用方法
1. 克隆项目到本地：
```bash
git clone <你的仓库地址>
cd ds-first-project
2. 创建虚拟环境并激活
3.安装依赖：
python3 -m pip install streamlit
4.运行网站：
python3 -m streamlit run app.py
##项目结构
ds-first-project/
├── app.py         # Streamlit 前端
├── analysis.py    # 基于规则的攻略生成函数
├── README.md
└── venv/          # 虚拟环境（已被 git 忽略）
###项目状态

这是 MVP 版本，后续计划：

支持多种旅行风格（悠闲、冒险等）

行程规划更详细

增加随机化和个性化推荐
# Travel Planner MVP 🌍

This is a minimum viable product (MVP) travel planning web app built with Streamlit.

Users can input:
- Destination
- Number of travelers
- Trip duration
- Travel style

The app then generates a basic travel plan including:
- Accommodation suggestions
- Travel routes
- Food recommendations

🔗 Live demo: <https://ds-first-project-crb24pdpwg6bx3mxdnw2qw.streamlit.app/>
