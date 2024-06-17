def find_first_black_pixel(image):
    rows, cols = image.shape
    for y in range(rows):
        for x in range(cols):
            if image[y, x] == 1:
                return x, y
    return None  # Return None if no black pixel with value 1 is found
