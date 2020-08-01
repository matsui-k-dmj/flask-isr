import numpy as np
import cv2
from ISR.models import RDN, RRDN


def super_resolution(img: np.ndarray, algo: str) -> np.ndarray:
    """[summary]

    Args:
        img (np.ndarray): 画像の行列, BGR

    Returns:
        np.ndarray: 画像の行列, BGR
    """

    if algo in ["psnr-large", "psnr-small", "noise-cancel"]:
        model = RDN
    elif algo == 'gans':
        model = RRDN

    model = model(weights=algo)

    return model.predict(img)
