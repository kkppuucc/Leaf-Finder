import os

import cv2

from Tools import ensure_binary_image, find_first_black_pixel, freeman_chain_code, visualize_freeman_chain_code, \
    compute_differential_code, connect_to_database
from Tools.DB_Connection import insert_to_database
from Tools.Freeman_visual import count_histogram


def load_files_from_folder_convert_to_binary(folder_path):
    # List all files in the folder
    image_files = os.listdir(folder_path)

    for file_name in image_files:
        # Check if the file is a .jpg file
        if file_name.lower().endswith('.jpg'):
            # Construct absolute path to the image
            image_path = os.path.join(folder_path, file_name)
            image = cv2.imread(image_path)
            # Check if the image was loaded successfully
            if image is None:
                print("Failed to load image from {image_path}")
            else:
                # Ensure the image is binary
                image = ensure_binary_image(image, 1)

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

            # Count Freeman code from histogram
            hist_count = count_histogram(chain_code, 1)

            # Initialise the DB
            connection, cursor = connect_to_database()

            # Write into the DB
            insert_to_database(file_name, chain_code, hist_count, connection, cursor)