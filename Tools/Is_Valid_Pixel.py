def is_valid_pixel(image, x, y):
    rows, cols = image.shape[:2]
    return 0 <= x < cols and 0 <= y < rows and image[y, x] == 1  # Assuming white pixel for contour