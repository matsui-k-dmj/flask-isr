import numpy as np
import cv2
from ISR.models import RDN, RRDN


def super_resolution(image_binary: bytearray):
    image_array = cv2.imdecode(np.array(image_binary, dtype=np.uint8), 1)

    cv2.imwrite('tmp.png', image_array)

    retval, buf = cv2.imencode('.png', image_array)

    return buf
