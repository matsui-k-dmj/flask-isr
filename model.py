import numpy as np
import cv2
from ISR.models import RDN, RRDN


def super_resolution(img: np.ndarray) -> np.ndarray:
    """[summary]

    Args:
        img (np.ndarray): 画像の行列, BGR

    Returns:
        np.ndarray: 画像の行列, BGR
    """
    cv2.imwrite('tmp.png', img)

    return img
