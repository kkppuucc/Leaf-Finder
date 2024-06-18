import cv2
import numpy as np


def ensure_binary_image(image):
    target_size = (500, 500)
    if image.size != target_size:
        # Resize the image to the target size
        resized_image = cv2.resize(image, target_size, interpolation=cv2.INTER_AREA)
    else:
        resized_image = image

    threshold = 200
    # Ensure the image is binary
    if resized_image.shape[2] == 3:  # If it has 3 channels
        gray_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)
        _, binary_image = cv2.threshold(gray_image, threshold, 255, cv2.THRESH_BINARY)
    else:
        _, binary_image = cv2.threshold(resized_image, threshold, 255, cv2.THRESH_BINARY)

    # Invert the binary image
    binary_image = cv2.bitwise_not(binary_image)

    # Convert the binary image to 1 and 0
    binary_image = (binary_image > 127).astype(np.uint8)
    return binary_image
