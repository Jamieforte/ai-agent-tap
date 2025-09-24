# tabs/site.py
import streamlit as st
from brief import build_prompt_from_brief

def render(orientation: str, target_wwr: float, budget: str):
    st.subheader("대지선정 / 프로젝트 브리프")
    b = st.session_state.brief

    c1, c2 = st.columns(2)
    with c1:
        b.location = st.text_input("위치", b.location or "서울 강남")
        b.usage = st.text_input("용도", b.usage or "상업시설")
        b.style = st.text_input("스타일 키워드", b.style or "현대적, 유리 중심")
        b.materials = st.text_input("재료 키워드", b.materials or "Low-E 유리, 알루미늄, 세라믹 패널")
    with c2:
        b.site_notes = st.text_area("부지/맥락 메모", b.site_notes or "", height=120)
        b.constraints = st.text_area("제약사항(법규/예산/공법 등)", b.constraints or "", height=120)

    st.success("브리프 저장 완료")
    st.markdown("#### 이미지 프롬프트 (미리보기)")
    st.code(build_prompt_from_brief(b, orientation, target_wwr, budget), language="text")
