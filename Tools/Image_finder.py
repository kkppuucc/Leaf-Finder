import os
import cv2

from Tools import ensure_binary_image


def convert_tiff_to_jpg(input_folder, output_format='jpg'):
    for filename in os.listdir(input_folder):
        if filename.endswith('.tiff') or filename.endswith('.tif'):
            image_path = os.path.join(input_folder, filename)
            image = cv2.imread(image_path)

            if image is not None:
                base_filename = os.path.splitext(filename)[0]
                new_filename = f"{base_filename}.{output_format}"
                new_image_path = os.path.join(input_folder, new_filename)

                if output_format == 'jpg' or output_format == 'jpeg':
                    cv2.imwrite(new_image_path, image, [int(cv2.IMWRITE_JPEG_QUALITY), 90])
                else:
                    cv2.imwrite(new_image_path, image)

                print(f"Saved {new_image_path}")
            else:
                print(f"Failed to read {image_path}")

def convert_jpg_to_binary_and_copy(input_folder, output_folder):
    for filename in os.listdir(input_folder):
        if filename.endswith('.jpg'):
            image_path = os.path.join(input_folder, filename)
            image = cv2.imread(image_path)

            if image is not None:
                binary_image = ensure_binary_image(image)

                # Create output path in the Processed folder
                output_path = os.path.join(output_folder, filename)

                # Save the binary image
                cv2.imwrite(output_path, binary_image)
                print("Converted and saved: {output_path}")
            else:
                print("Failed to read: {image_path}")

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_folder = os.path.join(script_dir, 'UnProcessed')

    # Convert TIFF images to JPEG format
    convert_tiff_to_jpg(input_folder, output_format='jpg')
