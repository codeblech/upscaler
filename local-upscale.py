import argparse
import os
from PIL import Image
from PIL import UnidentifiedImageError


def upscale_image(image_path, upscale_percentage, resampling_option, output_path):
    # Load the image
    try:
        image = Image.open(image_path)
    except UnidentifiedImageError:
        print(f"Skipping file \"{image_path}\" as it's not a recognized image format.")
        return

    # Get the current dimensions of the image
    width, height = image.size

    # Calculate the new dimensions based on the percentage
    new_width = int(width * (upscale_percentage / 100))
    new_height = int(height * (upscale_percentage / 100))

    # Select the resampling filter based on the user's choice
    # 1. Nearest Neighbor (for pixel art or sharp edges)
    # 2. Bilinear (for smooth gradients)
    # 3. Bicubic (for high-quality resizing)
    # 4. Lanczos (for high-quality resizing with sharper results)
    if resampling_option == 1:
        resampling_filter = Image.NEAREST
    elif resampling_option == 2:
        resampling_filter = Image.BILINEAR
    elif resampling_option == 3:
        resampling_filter = Image.BICUBIC
    elif resampling_option == 4:
        resampling_filter = Image.LANCZOS
    else:
        print("Invalid resampling option selected. Using default (LANCZOS).")
        resampling_filter = Image.LANCZOS

    # Upscale the image
    upscaled_image = image.resize((new_width, new_height), resampling_filter)

    # Save the upscaled image
    upscaled_image.save(output_path)

    print("Image upscaled and saved successfully!")

def upscale_directory(directory_path, upscale_percentage, resampling_option, output_directory):
    # Get the list of image files in the directory
    image_files = [f for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, f))]

    # Upscale each image in the directory
    for image_file in image_files:
        image_path = os.path.join(directory_path, image_file)
        output_path = os.path.join(output_directory, image_file)
        upscale_image(image_path, upscale_percentage, resampling_option, output_path)

    print("All images upscaled and saved successfully!")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Upscale an image or a directory of images.")
    parser.add_argument("input_path", help="Path to the image file or directory")
    parser.add_argument("upscale_percentage", type=int, help="Upscale percentage (e.g., 200 for doubling the size)")
    parser.add_argument("resampling_option", type=int, choices=[1, 2, 3, 4],
                        help="""Resampling option - 1. Nearest Neighbor (for pixel art or sharp edges)
                                                    2. Bilinear (for smooth gradients)
                                                    3. Bicubic (for high-quality resizing)
                                                    4. Lanczos (for high-quality resizing with sharper results)""")
    parser.add_argument("output_path", help="Path to save the upscaled image or directory")
    args = parser.parse_args()

    if os.path.isfile(args.input_path):
        # Upscale a single image
        upscale_image(args.input_path, args.upscale_percentage, args.resampling_option, args.output_path)
    elif os.path.isdir(args.input_path):
        # Upscale a directory of images
        upscale_directory(args.input_path, args.upscale_percentage, args.resampling_option, args.output_path)
    else:
        print("Invalid input path. Please provide a valid image file or directory.")
