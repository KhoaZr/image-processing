import cv2 
import numpy as np


def to_grayscale(image: np.ndarray) -> np.ndarray:
    """Chuyển đổi ảnh sang ảnh xám nếu ảnh đang ở dạng BGR/RGB"""
    if len(image.shape) == 3 and image.shape[2] == 3:
        return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return image

def apply_sobel(image: np.ndarray, ksize: int = 3, threshold: int = 0) -> np.ndarray:
    """Phát hiện cạnh bằng toán tử Sobel."""
    gray = to_grayscale(image)
    sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=ksize)
    sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=ksize)
    magnitude = np.sqrt(sobelx**2 + sobely**2)
    magnitude = np.clip(magnitude, 0, 255).astype(np.uint8)
    
    if threshold > 0:
        _, magnitude = cv2.threshold(magnitude, threshold, 255, cv2.THRESH_BINARY)
    return magnitude
