# tabs/facade.py
import streamlit as st
from cad_io import load_cad
from facade_extract import detect_floors, detect_vertical_grid, classify_openings, compute_wwr
from facade_rules import propose_options
from exporters import export_svg

def render(orientation: str, target_wwr: float, budget: str):
    st.subheader("입면계획 (CAD 분석 → 제안)")
    up = st.file_uploader("DXF(권장) 또는 DWG 업로드", type=["dxf", "dwg"], key="cad_for_facade")
    if not up:
        st.info("입면 계획을 위해 도면을 업로드하세요.")
        return

    ents, meta = load_cad(up)
    floors = detect_floors(ents)
    grid_x = detect_vertical_grid(ents)
    parts = classify_openings(ents, layer_hints=meta.get("layers", {}))
    wwr_val = compute_wwr(parts.get("windows", []), parts.get("walls", []))

    c = st.columns(3)
    c[0].metric("층 레벨 수", len(floors))
    c[1].metric("수직 모듈 수", len(grid_x))
    c[2].metric("기존 추정 WWR(%)", round(wwr_val, 1))

    options = propose_options(floors, grid_x, parts, target_wwr, orientation, budget)
    names = list(options.keys())
    choice = st.selectbox("제안안 선택", names)

    svg = export_svg(options[choice], base_entities=ents)
    st.components.v1.html(svg, height=600, scrolling=True)

    # Export 탭에서 재사용
    st.session_state["cad"] = dict(
        ents=ents, meta=meta, floors=floors, grid_x=grid_x, parts=parts, options=options, choice=choice
    )
