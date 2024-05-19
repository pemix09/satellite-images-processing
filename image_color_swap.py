from PIL import Image
import os

directory = '/Users/mac/Coding/inżynieria uczenia maszynowego/training_images/road/labels'
black_color = (0, 0, 0)  # black
source_color = (255, 255, 255)  # white
new_color = (255, 255, 0)  # yellow

def swap_color(image_path, source_color, new_color):
    img = Image.open(image_path)
    pixels = img.load()

    width, height = img.size
    new_image = Image.new(mode="RGB", size=(width, height))
    for y in range(height):
        for x in range(width):
            pixel = pixels[x, y]
            if pixel == source_color or (pixel, pixel, pixel) == source_color:
                try:
                    new_image.putpixel((x, y), new_color)
                except Exception as e:
                    print(f"Failed to convert {image_path}: {str(e)}")

    new_image.save(image_path)

def iterate_files(directory):
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path) and file_path.endswith(".png"):
            swap_color(file_path, source_color, new_color)

# Usage
iterate_files(directory)