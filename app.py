# app.py — 탭 모듈들을 불러와 렌더링
import streamlit as st
from brief import BriefState
from tabs import site, massing, plan, facade, street, docs, images
from image_pipeline import get_provider_names

st.set_page_config(page_title="AI Facade Design Agent", layout="wide")
st.title("AI Design Agent")

provider_name = "OpenAI (stub)"
target_wwr = 50
orientation = "남"
budget = "중"


# 탭 구성
T_site, T_mass, T_plan, T_facade, T_street, T_docs, T_images = st.tabs(
    ["대지선정", "볼륨검토", "평면계획", "입면계획", "가로뷰합성", "도서작성(CAD)", "이미지"]
)

# 각 탭 렌더
with T_site:
    site.render(orientation, target_wwr, budget)

with T_mass:
    massing.render()

with T_plan:
    plan.render()

with T_facade:
    facade.render(orientation, target_wwr, budget)

with T_street:
    street.render()

with T_docs:
    docs.render(orientation, target_wwr, budget)

with T_images:
    images.render(orientation, target_wwr, budget, provider_name)
