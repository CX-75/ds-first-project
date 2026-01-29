旅行攻略生成器 (MVP)

一个基于Python和Streamlit的简易旅行计划生成网站。

功能
- 根据用户输入生成旅行攻略
- 提供住宿、行程和餐饮建议
- 基于规则的逻辑（MVP 版本）

技术栈
- Python 3.13
- Streamlit
- VS Code + zsh

---

 How to Run Locally

1. Clone this repository:
   ```bash
   git clone https://github.com/CX-75/ds-first-project.git
2.Navigate to the project directory:
cd ds-first-project
3. Create a virtual environment (optional but recommended):
4.安装依赖：
python3 -m pip install streamlit
5.运行网站：
python3 -m streamlit run app.py
项目结构
ds-first-project/
├── app.py         Streamlit 前端
├── analysis.py    基于规则的攻略生成函数
├── README.md
└── venv/          虚拟环境（已被 git 忽略）
项目状态

这是 MVP 版本，后续计划：

支持多种旅行风格（悠闲、冒险等）

行程规划更详细

增加随机化和个性化推荐

Live demo: <https://ds-first-project-crb24pdpwg6bx3mxdnw2qw.streamlit.app/>
