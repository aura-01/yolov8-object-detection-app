# utils/image_utils.py
import numpy as np
import io
from PIL import Image

def image_bytes_to_numpy(image_bytes):
    return np.asarray(bytearray(image_bytes), dtype=np.uint8)

def numpy_to_pil(np_image):
    return Image.fromarray(np_image)
