import cv2
import numpy as np


def is_valid_pixel(image, x, y):
    rows, cols = image.shape[:2]
    return 0 <= x < cols and 0 <= y < rows and image[y, x] == 1  # Assuming white pixel for contour


def find_first_black_pixel(image):
    rows, cols = image.shape
    for y in range(rows):
        for x in range(cols):
            if image[y, x] == 1:
                return (x, y)
    return None  # Return None if no black pixel with value 1 is found


def freeman_chain_code(image, start_pixel):
    chain_code = []
    directions = [(1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1)]
    current_pixel = start_pixel
    pos = 0  # Start checking from direction 0 (east)

    while True:
        found = False
        for i in range(8):
            direction_calculation = (pos + i + 6) % 8
            dx, dy = directions[direction_calculation]
            next_x, next_y = current_pixel[0] + dx, current_pixel[1] + dy
            if is_valid_pixel(image, next_x, next_y):
                chain_code.append(direction_calculation)
                current_pixel = (next_x, next_y)
                next_pixel_calculation = (pos + i + 6) % 8
                pos = (pos + i + 6) % 8  # Move to direction opposite to the current direction
                found = True
                break

        if not found:
            break
        if current_pixel == start_pixel and len(chain_code) > 1:
            break

    return [start_pixel, chain_code]


image = cv2.imread('../UnProcessed/processedImage_300.jpg')


# Ensure the image is binary
_, image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

# Find the start pixel
if image.shape[2] == 3:  # If it has 3 channels
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, image = cv2.threshold(gray_image, 127, 1, cv2.THRESH_BINARY)

start_pixel = find_first_black_pixel(image)
print("First black pixel:", start_pixel)

# Compute the Freeman chain code
if start_pixel:
    chain_code_result = freeman_chain_code(image, start_pixel)
    print("Freeman Chain Code:", chain_code_result)
else:
    print("No starting pixel found.")
