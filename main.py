import os
import cv2
from Tools import find_first_black_pixel, freeman_chain_code, ensure_Binary_Image
from Tools.Freeman_visual import count_histogram

# Construct absolute path to the image
script_dir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(script_dir, 'Processed', 'processedImage_300.jpg')

# Load the binary image
image = cv2.imread(image_path)

# Check if the image was loaded successfully
if image is None:
    print(f"Failed to load image from {image_path}")
else:
    image = ensure_Binary_Image(image)

    # Find the start pixel
    start_pixel = find_first_black_pixel(image)
    chain_code_result = None

    if start_pixel is not None:
        print("First black pixel:", start_pixel)

        # Compute the Freeman chain code
        chain_code_result = freeman_chain_code(image, start_pixel)
        print("Freeman Chain Code:", chain_code_result)
    else:
        print("No starting pixel found.")


hist_count = count_histogram(chain_code_result)
for (key, count) in hist_count:
   print(count, key)
