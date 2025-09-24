# tabs/docs.py
import streamlit as st
from exporters import export_svg, export_dxf, export_json

def render(orientation: str, target_wwr: float, budget: str):
    st.subheader("도서작성 (CAD 내보내기)")
    cad = st.session_state.get("cad")
    if not cad:
        st.info("먼저 ‘입면계획’ 탭에서 제안안을 생성하세요.")
        return

    opt = cad["options"][cad["choice"]]
    svg = export_svg(opt, base_entities=cad["ents"])
    st.components.v1.html(svg, height=400, scrolling=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.download_button("SVG 다운로드", data=svg, file_name="facade_proposal.svg", mime="image/svg+xml")
    with col2:
        dxf_bytes = export_dxf(opt, base_entities=cad["ents"])
        st.download_button("DXF 다운로드", data=dxf_bytes, file_name="facade_proposal.dxf")
    with col3:
        meta_json = export_json(
            opt,
            brief=st.session_state.brief.dict(),
            orientation=orientation,
            target_wwr=target_wwr,
            budget=budget,
        )
        st.download_button("JSON 메타", data=meta_json, file_name="facade_meta.json", mime="application/json")
