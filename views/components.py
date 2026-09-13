import streamlit as st
import cv2
import numpy as np
from PIL import Image

from core.utils import (
    fix_color_for_streamlit,
    convert_image_to_bytes,
)


def render_file_uploader(
    allowed_types=["png", "jpg", "jpeg", "mp4", "avi", "mov"]
):
    """
    Thành phần tải tệp đầu vào (Ảnh tĩnh hoặc Video).
    """
    uploaded_file = st.file_uploader(
        "Tải lên Ảnh hoặc Video để xử lý",
        type=allowed_types,
        help=(
            "Hỗ trợ các định dạng ảnh "
            "(.png, .jpg, .jpeg) và video (.mp4, .avi, .mov)"
        ),
    )

    return uploaded_file


def render_comparison_view(
    original_img: np.ndarray,
    processed_img: np.ndarray,
    processed_title: str = "Ảnh sau xử lý",
):
    """
    Hiển thị so sánh song song 2 cột:
    Ảnh gốc (Trái) vs Ảnh kết quả (Phải).

    Tích hợp sẵn nút tải ảnh kết quả xuống máy tính.
    """

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Ảnh gốc")
        st.image(
            fix_color_for_streamlit(original_img),
            use_container_width=True,
        )

    with col2:
        st.subheader(f"{processed_title}")
        st.image(
            fix_color_for_streamlit(processed_img),
            use_container_width=True,
        )

    # Nút tải ảnh kết quả
    img_bytes = convert_image_to_bytes(processed_img)

    st.download_button(
        label="Tải ảnh kết quả",
        data=img_bytes,
        file_name="processed_result.png",
        mime="image/png",
        use_container_width=True,
    )


def render_quad_view(results_dict: dict):
    """
    Hiển thị lưới 2x2 so sánh đối chiếu
    cùng lúc 4 thuật toán phát hiện cạnh.

    :param results_dict:
        Dictionary dạng:
        {"Tên thuật toán": numpy_array}
    """

    st.subheader(
        "So sánh đối chiếu 4 bộ phát hiện cạnh (Lưới 2x2)"
    )

    cols = st.columns(2)
    items = list(results_dict.items())

    for idx, (title, img) in enumerate(items):
        col = cols[idx % 2]

        with col:
            st.markdown(f"**{title}**")

            st.image(
                fix_color_for_streamlit(img),
                use_container_width=True,
            )

            img_bytes = convert_image_to_bytes(img)

            st.download_button(
                label=f"Tải {title}",
                data=img_bytes,
                file_name=(
                    f"{title.lower().replace(' ', '_')}_result.png"
                ),
                mime="image/png",
                key=f"dl_btn_{idx}",
            )