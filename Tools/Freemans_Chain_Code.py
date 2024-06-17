from Tools import is_valid_pixel


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

    return chain_code