# tabs/massing.py
import streamlit as st

def render():
    st.subheader("볼륨검토 (Stub)")
    colA, colB, colC = st.columns(3)
    with colA:
        site_area = st.number_input("대지면적 (㎡)", min_value=0.0, value=2000.0, step=10.0)
        bcr_target = st.number_input("건폐율 목표 (%)", min_value=0.0, max_value=100.0, value=60.0, step=1.0)
    with colB:
        far_target = st.number_input("용적률 목표 (%)", min_value=0.0, max_value=2000.0, value=400.0, step=10.0)
        floors = st.number_input("층수 (지상)", min_value=1, value=12, step=1)
    with colC:
        h_floor = st.number_input("층고 (m)", min_value=2.7, value=3.6, step=0.1, format="%.1f")
        core_ratio = st.number_input("코어/수직동선 비율(%)", min_value=0.0, max_value=60.0, value=18.0, step=1.0)

    footprint = site_area * (bcr_target/100.0)
    gfa_target = site_area * (far_target/100.0)
    avg_floor_area = gfa_target / floors if floors else 0.0
    net_floor_area = avg_floor_area * (1 - core_ratio/100.0)

    m1, m2, m3, m4 = st.columns(4)
    m1.metric("최대 건축면적(㎡)", f"{footprint:,.0f}")
    m2.metric("목표 연면적(㎡)", f"{gfa_target:,.0f}")
    m3.metric("층당 목표 연면적(㎡)", f"{avg_floor_area:,.0f}")
    m4.metric("층당 순수 임대가능면적(㎡)", f"{net_floor_area:,.0f}")
    st.caption("※ 실제 법규·지표 검토는 지자체 기준/도면 기반 산정으로 정확화 필요")
