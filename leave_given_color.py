from PIL import Image
import os

color_to_leave = (9, 143, 150)
destination_color = (32,128,192)
source_directory = '/Users/mac/Coding/inżynieria uczenia maszynowego/training_images/semantic drone dataset/RGB_color_image_masks/RGB_color_image_masks'
destination_directory = '/Users/mac/Coding/inżynieria uczenia maszynowego/training_images/car/masks'

def leave_color(filename, image_path, destination_directory, color_to_leave):
    img = Image.open(image_path)
    pixels = img.load()

    width, height = img.size
    new_image = Image.new(mode="RGB", size=(width, height))
    dest_path = os.path.join(destination_directory, filename)
    dest_png_path = os.path.splitext(dest_path)[0] + ".png"
    color_on_the_picture = False
    for y in range(height):
        for x in range(width):
            pixel = pixels[x, y]
            if pixel == color_to_leave or (pixel, pixel, pixel) == color_to_leave:
                try:
                    new_image.putpixel((x, y), destination_color)
                    color_on_the_picture = True
                except Exception as e:
                    print(f"Failed put new color to pixel for given mask: {image_path}: {str(e)}")
            else:
                new_image.putpixel((x, y), (0,0,0))

    if (color_on_the_picture == True):
        new_image.save(dest_png_path)

def iterate_files(source_directory, destination_directory):
    for filename in os.listdir(source_directory):
        source_path = os.path.join(source_directory, filename)
        if os.path.isfile(source_path) and source_path.endswith(".png"):
            leave_color(filename, source_path, destination_directory, color_to_leave)

# Usage
iterate_files(source_directory, destination_directory)