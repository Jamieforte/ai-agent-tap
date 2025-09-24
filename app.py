# app.py — 탭 모듈들을 불러와 렌더링
import streamlit as st
from brief import BriefState
from tabs import site, massing, plan, facade, street, docs, images
from image_pipeline import get_provider_names

st.set_page_config(page_title="AI Facade Design Agent", layout="wide")
st.title("AI Façade Design Agent")

# Sidebar (공통 옵션)
with st.sidebar:
    st.header("Global")
    provider_name = st.selectbox("Image Provider", get_provider_names(), index=0)
    target_wwr = st.slider("목표 유리율(%)", 25, 70, 50)
    orientation = st.selectbox("향", ["남", "서", "동", "북", "복합"], index=0)
    budget = st.select_slider("예산", options=["저", "중", "고"], value="중")
    st.caption("이미지 제공자(API 키는 환경변수). DXF 사용 시 ezdxf 설치.")

# 세션 상태 준비
if "brief" not in st.session_state:
    st.session_state.brief = BriefState()

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
