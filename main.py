import os
import cv2
from Tools import find_first_black_pixel, freeman_chain_code, ensure_binary_image, compute_differential_code, \
    connect_to_database, find_similar, convert_tiff_to_jpg, load_files_from_folder_convert_to_binary
from Tools.DB_Connection import insert_to_database
from Tools.Freeman_visual import count_histogram, visualize_freeman_chain_code
from Tools.Image_finder import convert_jpg_to_binary_and_copy

file_name = 'l2nr039.jpg'
un_processed = 'UnProcessed'
processed = 'Processed'
# Construct absolute path to the image
script_dir = os.path.dirname(os.path.abspath(__file__))
un_processed_path = os.path.join(script_dir, un_processed)
processed_path = os.path.join(script_dir, processed)



file_path = os.path.join(script_dir, un_processed)
image_path = os.path.join(script_dir, processed, file_name)

# convert_jpg_to_binary_and_copy(un_processed_path, processed_path, 1)
# load_files_from_folder_convert_to_binary(file_path)
# Load the binary image
image = cv2.imread(image_path)

# Check if the image was loaded successfully
if image is None:
    print("Failed to load image from {image_path}")
else:
    # Ensure the image is binary
    image = ensure_binary_image(image)

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

# Visualise Freeman Code
visualize_freeman_chain_code(chain_code)

# Compute the differential chain code
differential_code = compute_differential_code(chain_code)

# Count Freeman code from histogram
hist_count = count_histogram(chain_code, 1)

# Initialise the DB
connection, cursor = connect_to_database()

# Write into the DB
insert_to_database(file_name, chain_code, hist_count, connection, cursor)
