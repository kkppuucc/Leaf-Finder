import matplotlib.pyplot as plt
import cv2
import numpy as np

def visualize_freeman_chain_code(chain_code):
    # Starting point (arbitrary, can be adjusted)
    start_point = (0, 0)

    # Directions dictionary for movement based on Freeman Chain Code
    directions = {
        0: (1, 0),  # East
        1: (1, -1),  # Southeast
        2: (0, -1),  # South
        3: (-1, -1),  # Southwest
        4: (-1, 0),  # West
        5: (-1, 1),  # Northwest
        6: (0, 1),  # North
        7: (1, 1)  # Northeast
    }

    # Initialize current position
    current_pos = start_point
    x_values = [current_pos[0]]
    y_values = [current_pos[1]]

    # Iterate through the chain code to generate path
    for direction in chain_code:
        dx, dy = directions[direction]
        new_x = current_pos[0] + dx
        new_y = current_pos[1] + dy
        x_values.append(new_x)
        y_values.append(new_y)
        current_pos = (new_x, new_y)

    # Plotting the path
    plt.figure(figsize=(8, 8))
    plt.plot(x_values, y_values, marker='o', linestyle='-', color='b')
    plt.title('Visualization of Freeman Chain Code')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid(True)
    plt.gca().invert_yaxis()  # Invert y-axis to match image coordinates
    plt.show()
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


# Load the binary image
image = cv2.imread('../UnProcessed/processedImage_300.jpg')

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

# Find the start pixel
start_pixel = find_first_black_pixel(binary_image)
print("First black pixel:", start_pixel)

# Compute the Freeman chain code
if start_pixel:
    chain_code_result = freeman_chain_code(binary_image, start_pixel)
    print("Freeman Chain Code:", chain_code_result)
else:
    print("No starting pixel found.")


start_pixel, chain_code = chain_code_result

visualize_freeman_chain_code(chain_code)

# Create a histogram and get the bin counts
counts, bin_edges = np.histogram(chain_code, bins=8, range=(0, 8))

# Print the counts for each bin
for i in range(len(counts)):
    print(f"Direction {i}: {counts[i]} times")

# Plot the histogram
plt.figure(figsize=(8, 6))  # Optional: Set the figure size
plt.hist(chain_code, bins=8, edgecolor='black')  # bins specifies the number of intervals

# Add titles and labels
plt.title('Histogram of Freeman Chain Code Directions')
plt.xlabel('Direction')
plt.ylabel('Frequency')

# Display the histogram
plt.show()

