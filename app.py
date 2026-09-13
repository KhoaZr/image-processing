import streamlit as st

from views.project1_view import render_project1_page


# ============================================================
# 1. CẤU HÌNH GIAO DIỆN TRANG STREAMLIT
# ============================================================

st.set_page_config(
    page_title="Xử lý ảnh số - Chủ đề 7",
    page_icon="",
    layout="wide",
    # Hiển thị dạng khung rộng để so sánh ảnh song song
    initial_sidebar_state="expanded",
)


def main():

    # ========================================================
    # 2. THANH ĐIỀU HƯỚNG SIDEBAR
    # ========================================================

    st.sidebar.title("Xử lý ảnh số")
    st.sidebar.subheader("Bài tiểu luận - Chủ đề 7")

    st.sidebar.markdown("---")

    # ========================================================
    # 3. CHUYỂN ĐỔI GIỮA 2 PROJECT
    # ========================================================

    project_choice = st.sidebar.radio(
        " Chọn bài toán xử lý:",
        [
            " Project 1: Phát hiện cạnh (Edge Detection)",
            " Project 2: Nâng cao chất lượng ảnh",
        ],
    )

    st.sidebar.markdown("---")

    st.sidebar.info(
        "**Thông tin công nghệ:**\n"
        "• Framework: Streamlit Web\n"
        "• Thư viện lõi: OpenCV & NumPy\n"
        "• Xử lý: Ảnh tĩnh & Video"
    )

    # ========================================================
    # 4. ĐIỀU HƯỚNG HIỂN THỊ MÀN HÌNH
    # ========================================================

    if "Project 1" in project_choice:

        render_project1_page()

    elif "Project 2" in project_choice:

        # Giữ chỗ cho Project 2
        # cho đến khi hoàn thiện views/project2_view.py

        st.header(
            " Project 2: Nâng cao chất lượng ảnh số"
        )

        st.warning(
            " Module Project 2 chưa được khởi tạo. "
            "Bạn vui lòng chọn **Project 1** ở thanh Menu bên trái "
            "để thử nghiệm tính năng phát hiện cạnh!"
        )


# ============================================================
# 5. CHẠY ỨNG DỤNG
# ============================================================

if __name__ == "__main__":
    main()