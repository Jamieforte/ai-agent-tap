# tabs/plan.py
import streamlit as st

def render():
    st.subheader("평면계획 (Stub)")
    c1, c2, c3 = st.columns(3)
    with c1:
        bay = st.number_input("수평 모듈 (bay, m)", min_value=1.0, value=8.4, step=0.1)
    with c2:
        grid = st.number_input("기둥 간격 (m)", min_value=3.0, value=8.4, step=0.1)
    with c3:
        cores = st.number_input("코어 수(개)", min_value=1, value=1, step=1)

    st.write(
        f"- 제안 모듈: **{bay:.1f}m bay / {grid:.1f}m grid**, 코어 **{cores}개** (가이드)\n"
        "  - 실제 평면 최적화: 코어 배치, 피난/설비 샤프트, 서비스 존 고려하여 업데이트 예정"
    )
