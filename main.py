import os
import cv2
from Tools import find_first_black_pixel, freeman_chain_code, ensure_Binary_Image, compute_differential_code, \
    connect_to_database
from Tools.Freeman_visual import count_histogram, visualize_freeman_chain_code

# Construct absolute path to the image
script_dir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(script_dir, 'Processed', 'processedImage_300.jpg')

# Load the binary image
image = cv2.imread(image_path)

# Check if the image was loaded successfully
if image is None:
    print("Failed to load image from {image_path}")
else:
    image = ensure_Binary_Image(image)

    # Find the start pixel
    start_pixel = find_first_black_pixel(image)
    chain_code = None

    if start_pixel is not None:
        print("First black pixel:", start_pixel)

        # Compute the Freeman chain code
        chain_code = freeman_chain_code(image, start_pixel)
        print("Freeman Chain Code:", chain_code)
    else:
        print("No starting pixel found.")
visualize_freeman_chain_code(chain_code)
differential_code = compute_differential_code(chain_code)
hist_count = count_histogram(chain_code)
connection, cursor = connect_to_database()
print(hist_count[0], hist_count[1])

