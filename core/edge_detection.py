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
def apply_prewitt(image: np.ndarray, threshold: int = 0) -> np.ndarray:
    """Phát hiện cạnh bằng toán tử Prewitt."""
    gray = to_grayscale(image)

    kernel_x = np.array([
        [-1, 0, 1],
        [-1, 0, 1],
        [-1, 0, 1]
    ], dtype=np.float32)

    kernel_y = np.array([
        [-1, -1, -1],
        [0, 0, 0],
        [1, 1, 1]
    ], dtype=np.float32)

    prewitt_x = cv2.filter2D(gray, cv2.CV_64F, kernel_x)
    prewitt_y = cv2.filter2D(gray, cv2.CV_64F, kernel_y)

    magnitude = np.sqrt(prewitt_x**2 + prewitt_y**2)
    magnitude = np.clip(magnitude, 0, 255).astype(np.uint8)

    if threshold > 0:
        _, magnitude = cv2.threshold(
            magnitude, threshold, 255, cv2.THRESH_BINARY
        )

    return magnitude


def apply_roberts(image: np.ndarray, threshold: int = 0) -> np.ndarray:
    """Phát hiện cạnh bằng toán tử Roberts Cross."""
    gray = to_grayscale(image)

    kernel_x = np.array([
        [1, 0],
        [0, -1]
    ], dtype=np.float32)
    kernel_y = np.array([
        [0, 1],
        [-1, 0]
    ], dtype=np.float32)

    roberts_x = cv2.filter2D(gray, cv2.CV_64F, kernel_x)
    roberts_y = cv2.filter2D(gray, cv2.CV_64F, kernel_y)

    magnitude = np.sqrt(roberts_x**2 + roberts_y**2)
    magnitude = np.clip(magnitude, 0, 255).astype(np.uint8)

    if threshold > 0:
        _, magnitude = cv2.threshold(
            magnitude, threshold, 255, cv2.THRESH_BINARY
        )

    return magnitude


def apply_laplacian(
    image: np.ndarray,
    ksize: int = 3,
    threshold: int = 0
) -> np.ndarray:
    """Phát hiện cạnh bằng toán tử Laplacian."""
    gray = to_grayscale(image)

    lap = cv2.Laplacian(gray, cv2.CV_64F, ksize=ksize)

    magnitude = np.uint8(np.absolute(lap))

    if threshold > 0:
        _, magnitude = cv2.threshold(
            magnitude, threshold, 255, cv2.THRESH_BINARY
        )

    return magnitude