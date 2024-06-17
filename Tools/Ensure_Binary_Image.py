import cv2
import numpy as np


def ensure_Binary_Image(image):
    # Ensure the image is binary
    if image.shape[2] == 3:  # If it has 3 channels
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        _, binary_image = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY)
    else:
        _, binary_image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

    # Invert the binary image
    binary_image = cv2.bitwise_not(binary_image)

    # Convert the binary image to 1 and 0
    binary_image = (binary_image > 127).astype(np.uint8)
    return binary_image
