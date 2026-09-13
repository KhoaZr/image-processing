# Image Processing Project
*Dự án xử lý ảnh số phục vụ bài tiểu luận môn học Xử lý ảnh. Chương trình bao gồm hai bài toán lớn được tích hợp chung trên một nền tảng giao diện đồ họa (GUI) modular và có tính tái sử dụng cao.*
## 📌 Thành viên thực hiện
**Dương Công Khoa** - MSSV: 24651191  
**Nguyễn Văn Đức** - MSSV: 24719721

---

## 📂 Cấu trúc thư mục dự án (Modular Architecture)

```text
image-processing-chude7/
├── .gitignore                   # Cấu hình loại bỏ file rác/file lớn khi push GitHub
├── README.md                    # File hướng dẫn chạy dự án & thông tin nhóm (File này)
├── requirements.txt             # Thư viện phụ thuộc (streamlit, opencv-python, numpy, matplotlib,...)
├── app.py                       # Tệp khởi chạy Web chính (Streamlit Web App)
│
├── core/                        # TẦNG XỬ LÝ THUẬT TOÁN (Tái sử dụng lõi)
│   ├── __init__.py
│   ├── utils.py                 # Hàm phụ trợ: Đọc/ghi video, chuyển đổi màu, tính FPS
│   ├── edge_detection.py        # Thuật toán Project 1: Sobel, Prewitt, Roberts, Laplacian
│   └── image_enhancement.py     # Thuật toán Project 2: Histogram Eq, CLAHE, Gamma, Gaussian, Median, Sharpen
│
├── views/                       # TẦNG GIAO DIỆN WEB (Streamlit Modules)
│   ├── __init__.py
│   ├── components.py            # Giao diện dùng chung: Khung tải ảnh/video, bảng so sánh Trước/Sau
│   ├── project1_view.py         # Màn hình điều khiển Project 1 (Thanh trượt tham số phát hiện cạnh)
│   └── project2_view.py         # Màn hình điều khiển Project 2 (Thanh trượt tham số nâng cao chất lượng)
│
├── data/                        # DỮ LIỆU KIỂM THỬ (≥10 ảnh mỗi project)
│   ├── input_p1/                # Bộ dữ liệu ảnh/video đầu vào cho Project 1
│   ├── input_p2/                # Bộ dữ liệu ảnh/video đầu vào cho Project 2
│   └── sample_outputs/          # Ảnh kết quả mẫu dùng để chèn vào báo cáo
│
└── docs/                        # TÀI LIỆU VÀ BÁO CÁO NỘP BÀI
    ├── Project1_Report.pdf      # Báo cáo Project 1
    └── Project2_Report.pdf      # Báo cáo Project 2
```

---

## 🛠️ Công nghệ sử dụng (Tech Stack)
* **Ngôn ngữ:** Python 3.10+
* **Web Framework:** Streamlit
* **Xử lý ảnh & Video:** OpenCV (`opencv-python`), NumPy
* **Trực quan hóa dữ liệu:** Matplotlib, Pillow
* **Triển khai (Deployment):** Streamlit Community Cloud (Miễn phí)

## 🎯 Chi tiết tính năng theo từng Project

### 🟢 Project 1: So sánh bộ phát hiện cạnh
* **Thuật toán triển khai:**
  * **Sobel Detector:** Cho phép tùy chỉnh `kernel_size` (1, 3, 5, 7) và ngưỡng `threshold`.
  * **Prewitt Detector:** Phát hiện cạnh theo hướng ngang (X) và dọc (Y).
  * **Roberts Cross Detector:** Bộ phát hiện cạnh ma trận 2x2 nhanh và nhạy với nhiễu.
  * **Laplacian Detector:** Đạo hàm cấp 2, phát hiện cạnh đa hướng.
* **Tính năng:**
  * So sánh song song kết quả của 4 thuật toán trên cùng 1 ảnh/video.
  * Tùy chỉnh tham số trực tiếp bằng thanh kéo Slider với phản hồi thời gian thực.

### 🔵 Project 2: Nâng cao chất lượng ảnh số
* **Thuật toán triển khai:**
  * **Cải thiện độ tương phản/độ sáng:** Histogram Equalization, CLAHE (Contrast Limited Adaptive Histogram Equalization), Gamma Correction.
  * **Khử nhiễu & Làm mịn:** Gaussian Filter, Median Filter (tự chọn kích thước nhân lọc $k \times k$).
  * **Tăng cường độ nét:** Sharpening Filter (Kernel Unsharp Masking).
* **Tính năng:**
  * Hiển thị Biểu đồ tần số (Histogram) trước và sau khi cân bằng.
  * Tự do kết hợp chuỗi xử lý (ví dụ: Khử nhiễu -> Tăng tương phản -> Làm nét).

---

## 🚀 Hướng dẫn Cài đặt & Chạy ứng dụng Local

### 1. Khởi tạo môi trường
```bash
# Clone dự án từ GitHub
git clone https://github.com/username/image-processing-chude7.git
cd image-processing-chude7

# Tạo môi trường ảo
python -m venv venv

# Kích hoạt môi trường ảo (Windows)
venv\Scripts\activate

# Kích hoạt môi trường ảo (macOS/Linux)
source venv/bin/activate

# Cài đặt các thư viện cần thiết
pip install -r requirements.txt
```

### 2. Chạy ứng dụng Web
Chạy lệnh duy nhất để khởi động Web App:
```bash
streamlit run app.py
```
Trình duyệt sẽ tự động mở địa chỉ: `http://localhost:8501`. Tại thanh Sidebar bên trái, bạn có thể chuyển đổi linh hoạt giữa **Project 1** và **Project 2**.

---