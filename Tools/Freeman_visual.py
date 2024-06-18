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


def count_histogram(chain_code, visualize=0):
    # Create a histogram and get the bin counts
    counts, bin_edges = np.histogram(chain_code, bins=8, range=(0, 8))

    if (visualize):
        # Plot the histogram
        plt.hist(chain_code, bins=8, range=(0, 8))
        plt.xlabel('Chain Code')
        plt.ylabel('Frequency')
        plt.title('Histogram of Freeman Chain Code')
        plt.show()

    return counts
