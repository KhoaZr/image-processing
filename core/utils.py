import cv2
import numpy as np
import io
from PIL import Image


def fix_color_for_streamlit(image: np.ndarray) -> np.ndarray:
    """
    OpenCV mặc định đọc ảnh dạng BGR,
    nhưng Streamlit hiển thị dạng RGB.
    Hàm này chuyển BGR sang RGB.
    """
    if len(image.shape) == 2:
        return image

    return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)


def convert_image_to_bytes(
    image: np.ndarray,
    file_format: str = "PNG"
) -> bytes:
    """
    Chuyển đổi numpy array thành bytes
    để dùng cho st.download_button().
    """
    if len(image.shape) == 2:
        pil_img = Image.fromarray(image)
    else:
        rgb_img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        pil_img = Image.fromarray(rgb_img)

    buffer = io.BytesIO()

    pil_img.save(
        buffer,
        format=file_format
    )

    return buffer.getvalue()