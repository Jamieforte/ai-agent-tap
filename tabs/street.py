# tabs/street.py
import streamlit as st

def render():
    st.subheader("가로뷰 합성 (Stub)")
    street = st.file_uploader("가로뷰(현장 사진) 업로드", type=["jpg", "jpeg", "png"], key="street_photo")
    _ = st.text_input("합성 메모 / 카메라 높이·초점거리 등", value="도로 레벨 1.5m, 35mm 환산")

    if street:
        st.image(street, caption="현장 가로뷰", use_column_width=True)
        st.success("합성 파이프라인(마스크/정합)은 추후 연결 예정입니다.")
    else:
        st.info("가로뷰 사진을 업로드하면 합성 가이드를 표시합니다. (Stub)")
