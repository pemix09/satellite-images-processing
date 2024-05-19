from PIL import Image
import os

car_mask_source_color = (32, 128, 192)
car_mask_dest_color = (32,128,192)

person_mask_source_color = (255, 22, 96)
person_mask_dest_color = (255,160,0)

building_mask_source_color = (70, 70, 70)
building_mask_dest_color = (0, 255, 255)

road_mask_source_color = (32,224,224)
road_mask_dest_color = (255,255,0)

forest_mask_source_color = (51, 51, 0)
forest_mask_dest_color = (255,255,255)

water_mask_source_color = (28, 42, 168)
water_mask_dest_color = (120, 100, 70)

grass_mask_source_color = (0, 102, 0)
grass_mask_dest_color = (98,198,45)

masks_directory = 'training_images/car-road/masks'
images_directory = 'training_images/car-road/images'
destination_directory = 'training_images/car-road/masks-processed'

def leave_color(mask_filename, img_source_filename, mask_source_path, img_source_path):
    img = Image.open(mask_source_path)
    pixels = img.load()

    width, height = img.size
    new_mask_image = Image.new(mode="RGB", size=(width, height))
    color_on_the_picture = False
    for y in range(height):
        for x in range(width):
            pixel = pixels[x, y]
            if pixel == car_mask_source_color or (pixel, pixel, pixel) == car_mask_source_color:
                try:
                    new_mask_image.putpixel((x, y), car_mask_dest_color)
                    color_on_the_picture = True
                except Exception as e:
                    print(f"Failed put new color to pixel for given mask: {mask_filename}: {str(e)}")
            elif pixel == person_mask_source_color or (pixel, pixel, pixel) == person_mask_source_color:
                try:
                    new_mask_image.putpixel((x, y), person_mask_dest_color)
                    color_on_the_picture = True
                except Exception as e:
                    print(f"Failed put new color to pixel for given mask: {mask_filename}: {str(e)}")
            elif pixel == building_mask_source_color or (pixel, pixel, pixel) == building_mask_source_color:
                try:
                    new_mask_image.putpixel((x, y), building_mask_dest_color)
                    color_on_the_picture = True
                except Exception as e:
                    print(f"Failed put new color to pixel for given mask: {mask_filename}: {str(e)}")
            elif pixel == road_mask_source_color or (pixel, pixel, pixel) == road_mask_source_color:
                try:
                    new_mask_image.putpixel((x, y), road_mask_dest_color)
                    color_on_the_picture = True
                except Exception as e:
                    print(f"Failed put new color to pixel for given mask: {mask_filename}: {str(e)}")
            elif pixel == forest_mask_source_color or (pixel, pixel, pixel) == forest_mask_source_color:
                try:
                    new_mask_image.putpixel((x, y), forest_mask_dest_color)
                    color_on_the_picture = True
                except Exception as e:
                    print(f"Failed put new color to pixel for given mask: {mask_filename}: {str(e)}")
            elif pixel == water_mask_source_color or (pixel, pixel, pixel) == water_mask_source_color:
                try:
                    new_mask_image.putpixel((x, y), water_mask_dest_color)
                    color_on_the_picture = True
                except Exception as e:
                    print(f"Failed put new color to pixel for given mask: {mask_filename}: {str(e)}")
            elif pixel == grass_mask_source_color or (pixel, pixel, pixel) == grass_mask_source_color:
                try:
                    new_mask_image.putpixel((x, y), grass_mask_dest_color)
                    color_on_the_picture = True
                except Exception as e:
                    print(f"Failed put new color to pixel for given mask: {mask_filename}: {str(e)}")
            else:
                new_mask_image.putpixel((x, y), (0,0,0))

    if (color_on_the_picture == True):
        new_mask_image.save(destination_directory + os.path.splitext(mask_filename)[0] + ".png")

        new_img = Image.open(img_source_path)
        new_img.save(os.path.join(destination_directory, os.path.splitext(img_source_filename)[0] + ".jpg"))

for mask_filename in os.listdir(masks_directory):
    mask_source_path = os.path.join(masks_directory, mask_filename)
    img_source_filename = os.path.splitext(mask_filename)[0] + '.jpg'
    img_source_path = os.path.join(images_directory, img_source_filename)
    if os.path.isfile(mask_source_path) and mask_source_path.endswith(".png"):
        leave_color(mask_filename, img_source_filename, mask_source_path, img_source_path)
