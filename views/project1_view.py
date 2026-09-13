import streamlit as st
import cv2
import numpy as np
import tempfile
import os

from core.edge_detection import (
    apply_sobel,
    # apply_prewitt,
    # apply_roberts,
    # apply_laplacian,
)

from views.components import (
    render_file_uploader,
    render_comparison_view,
    render_quad_view,
)


def render_project1_page():
    st.header(
        "Project 1: So sánh bộ phát hiện cạnh (Edge Detection)"
    )

    st.markdown(
        "Ứng dụng hỗ trợ phát hiện cạnh trên **Ảnh tĩnh** và **Video** "
        "bằng 4 thuật toán: **Sobel**, **Prewitt**, **Roberts**, "
        "và **Laplacian**. "
        "Thay đổi các tham số ở thanh điều khiển bên trái "
        "để quan sát kết quả thời gian thực."
    )

    # ============================================================
    # 1. KHUNG TẢI TỆP ĐẦU VÀO
    # ============================================================

    uploaded_file = render_file_uploader()

    if uploaded_file is None:
        st.info(
            "Vui lòng tải lên một tệp Ảnh (.png, .jpg, .jpeg) "
            "hoặc Video (.mp4, .avi) để bắt đầu."
        )
        return

    # Xác định loại tệp: image hoặc video
    file_type = uploaded_file.type.split("/")[0]

    # ============================================================
    # TRƯỜNG HỢP 1: XỬ LÝ ẢNH TĨNH
    # ============================================================

    if file_type == "image":

        # Đọc dữ liệu ảnh từ buffer vào NumPy Array
        file_bytes = np.asarray(
            bytearray(uploaded_file.read()),
            dtype=np.uint8,
        )

        image = cv2.imdecode(
            file_bytes,
            cv2.IMREAD_COLOR,
        )

        st.sidebar.markdown("---")
        st.sidebar.subheader("Cấu hình Project 1")

        # Chọn chế độ hiển thị
        mode = st.sidebar.radio(
            "Chọn chế độ hiển thị:",
            [
                "Tùy chỉnh đơn thuật toán",
                "So sánh đối chiếu 4 thuật toán (Lưới 2x2)",
            ],
        )

        # ========================================================
        # CHẾ ĐỘ 1: MỘT THUẬT TOÁN
        # ========================================================

        if mode == "Tùy chỉnh đơn thuật toán":

            algo = st.sidebar.selectbox(
                "Chọn bộ phát hiện cạnh:",
                [
                    "Sobel",
                    "Prewitt",
                    "Roberts",
                    "Laplacian",
                ],
            )

            threshold = st.sidebar.slider(
                "Ngưỡng phân đoạn (Threshold):",
                min_value=0,
                max_value=255,
                value=0,
                help=(
                    "Nếu đặt = 0 sẽ giữ dạng ảnh gradient xám. "
                    "Đặt > 0 để nhị phân hóa các cạnh."
                ),
            )

            processed_img = None

            # ----------------------------------------------------
            # SOBEL
            # ----------------------------------------------------

            if algo == "Sobel":

                ksize = st.sidebar.select_slider(
                    "Kích thước nhân (Kernel Size):",
                    options=[1, 3, 5, 7],
                    value=3,
                )

                processed_img = apply_sobel(
                    image,
                    ksize=ksize,
                    threshold=threshold,
                )

            # ----------------------------------------------------
            # PREWITT
            # ----------------------------------------------------

            elif algo == "Prewitt":

                processed_img = apply_prewitt(
                    image,
                    threshold=threshold,
                )

            # ----------------------------------------------------
            # ROBERTS
            # ----------------------------------------------------

            elif algo == "Roberts":

                processed_img = apply_roberts(
                    image,
                    threshold=threshold,
                )

            # ----------------------------------------------------
            # LAPLACIAN
            # ----------------------------------------------------

            elif algo == "Laplacian":

                ksize = st.sidebar.select_slider(
                    "Kích thước nhân (Kernel Size):",
                    options=[1, 3, 5, 7],
                    value=3,
                )

                processed_img = apply_laplacian(
                    image,
                    ksize=ksize,
                    threshold=threshold,
                )

            # Hiển thị ảnh gốc và ảnh kết quả
            render_comparison_view(
                image,
                processed_img,
                processed_title=f"Kết quả bộ lọc {algo}",
            )

        # ========================================================
        # CHẾ ĐỘ 2: SO SÁNH 4 THUẬT TOÁN
        # ========================================================

        else:

            threshold = st.sidebar.slider(
                "Ngưỡng phân đoạn chung (Threshold):",
                min_value=0,
                max_value=255,
                value=0,
            )

            ksize = st.sidebar.select_slider(
                "Kích thước nhân cho Sobel/Laplacian:",
                options=[1, 3, 5, 7],
                value=3,
            )

            # Tính toán kết quả cho cả 4 thuật toán
            results = {
                "Sobel Detector": apply_sobel(
                    image,
                    ksize=ksize,
                    threshold=threshold,
                ),

                "Prewitt Detector": apply_prewitt(
                    image,
                    threshold=threshold,
                ),

                "Roberts Cross": apply_roberts(
                    image,
                    threshold=threshold,
                ),

                "Laplacian Detector": apply_laplacian(
                    image,
                    ksize=ksize,
                    threshold=threshold,
                ),
            }

            # Hiển thị lưới 2x2
            render_quad_view(results)

    # ============================================================
    # TRƯỜNG HỢP 2: XỬ LÝ VIDEO
    # ============================================================

    elif file_type == "video":

        st.sidebar.markdown("---")
        st.sidebar.subheader("Cấu hình Xử lý Video")

        algo = st.sidebar.selectbox(
            "Chọn thuật toán áp dụng cho Video:",
            [
                "Sobel",
                "Prewitt",
                "Roberts",
                "Laplacian",
            ],
        )

        threshold = st.sidebar.slider(
            "Ngưỡng phân đoạn (Threshold):",
            min_value=0,
            max_value=255,
            value=0,
        )

        # Kernel mặc định
        ksize = 3

        # Chỉ Sobel và Laplacian cần kernel size
        if algo in ["Sobel", "Laplacian"]:

            ksize = st.sidebar.select_slider(
                "Kích thước nhân (Kernel Size):",
                options=[1, 3, 5, 7],
                value=3,
            )

        # ========================================================
        # LƯU VIDEO TẠM THỜI
        # ========================================================

        tfile = tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".mp4",
        )

        tfile.write(uploaded_file.read())
        tfile.close()

        # Mở video bằng OpenCV
        cap = cv2.VideoCapture(tfile.name)

        total_frames = int(
            cap.get(cv2.CAP_PROP_FRAME_COUNT)
        )

        st.subheader(
            f"🎬 Xem trước khung hình Video ({algo})"
        )

        # Chọn frame
        frame_idx = st.slider(
            "Chọn khung hình (Frame) để xử lý:",
            0,
            max(0, total_frames - 1),
            0,
        )

        # Di chuyển tới frame được chọn
        cap.set(
            cv2.CAP_PROP_POS_FRAMES,
            frame_idx,
        )

        ret, frame = cap.read()

        cap.release()

        # ========================================================
        # XỬ LÝ FRAME
        # ========================================================

        if ret:

            if algo == "Sobel":

                processed_frame = apply_sobel(
                    frame,
                    ksize=ksize,
                    threshold=threshold,
                )

            elif algo == "Prewitt":

                processed_frame = apply_prewitt(
                    frame,
                    threshold=threshold,
                )

            elif algo == "Roberts":

                processed_frame = apply_roberts(
                    frame,
                    threshold=threshold,
                )

            else:

                processed_frame = apply_laplacian(
                    frame,
                    ksize=ksize,
                    threshold=threshold,
                )

            # Hiển thị frame gốc và frame sau xử lý
            render_comparison_view(
                frame,
                processed_frame,
                processed_title=(
                    f"Khung hình {frame_idx} - {algo}"
                ),
            )

        # ========================================================
        # DỌN DẸP FILE TẠM
        # ========================================================

        try:
            os.remove(tfile.name)

        except Exception:
            pass