import os
import cv2
import numpy as np

def get_polygons_from_img(img):
    gray_mask = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    _, mask = cv2.threshold(gray_mask, 1, 255, cv2.THRESH_BINARY)
    height, width = mask.shape
    contours, hierarchy = cv2.findContours(gray_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    polygons = []
    for cnt in contours:
        polygon = []
        for point in cnt:
            x, y = point[0]
            polygon.append(x / width)
            polygon.append(y / height)
        polygons.append(polygon)

    return polygons

def write_polygons_to_file(polygons, class_id, file):
    for polygon in polygons:
        for p_, p in enumerate(polygon):
            if p_ == len(polygon) - 1:
                file.write(f'{p}\n')
            elif p_ == 0:
                file.write(f'{class_id} {p} ')
            else:
                file.write(f'{p} ')

def leave_color(color_to_leave, img, class_name):
    from PIL import Image

    img = img[:, :, ::-1] # images are in BGR format, need to be converted
    pil_image = Image.fromarray(img) 
    pixels = pil_image.load()
    width, height = pil_image.size
    new_image = Image.new(mode="RGB", size=(width, height))

    for y in range(height):
        for x in range(width):
            # tutaj wystarczy wstawic kolor czarny jak sie nie rowna
            if pixels[x, y] == color_to_leave:
                try:
                    new_image.putpixel((x, y), color_to_leave)
                except Exception as e:
                    print(f"Failed put new color to pixel for given mask: {str(e)}")
            else:
                new_image.putpixel((x, y), (0,0,0))
    
    return np.array(new_image)

def process_masks():
    masks_dir = 'training_images/all/new/masks'
    labels_dir = 'training_images/all/new/labels'

    car_color = (32,128,192)
    forest_color = (255,255,255)
    road_color = (255,255,0)
    building_color = (0, 255, 255)
    waters_color = (120, 100, 70)
    greass_color = (98,198,45)
    person_color = (255,160,0)

    car_class_id = 0
    forest_class_id = 1
    road_class_id = 2
    building_class_id = 3
    waters_class_id = 4
    grass_class_id = 5
    person_class_id = 6

    for mask_filename in os.listdir(masks_dir):

        mask_path = os.path.join(masks_dir, mask_filename)
        mask = cv2.imread(mask_path)

        with open('{}.txt'.format(os.path.join(labels_dir, mask_filename)[:-4]), 'w') as file:
        
            car_polygons = get_polygons_from_img(leave_color(car_color, mask, 'car'))
            print(f'Found {len(car_polygons)} car polygons')
            write_polygons_to_file(car_polygons, car_class_id, file)

            forest_polygons = get_polygons_from_img(leave_color(forest_color, mask, 'forest'))
            print(f'Found {len(forest_polygons)} forest polygons')
            write_polygons_to_file(forest_polygons, forest_class_id, file)

            road_polygons = get_polygons_from_img(leave_color(road_color, mask, 'road'))
            print(f'Found {len(road_polygons)} road polygons')
            write_polygons_to_file(road_polygons, road_class_id, file)

            building_polygons = get_polygons_from_img(leave_color(building_color, mask, 'building'))
            print(f'Found {len(building_polygons)} building polygons')
            write_polygons_to_file(building_polygons, building_class_id, file)

            waters_polygons = get_polygons_from_img(leave_color(waters_color, mask, 'waters'))
            print(f'Found {len(waters_polygons)} waters polygons')
            write_polygons_to_file(waters_polygons, waters_class_id, file)

            greass_polygons = get_polygons_from_img(leave_color(greass_color, mask, 'greass'))
            print(f'Found {len(greass_polygons)} greass polygons')
            write_polygons_to_file(greass_polygons, grass_class_id, file)

            person_polygons = get_polygons_from_img(leave_color(person_color, mask, 'person'))
            print(f'Found {len(person_polygons)} person polygons')
            write_polygons_to_file(person_polygons, person_class_id, file)
        
            file.close()

        print(f'Processed {mask_filename}')

process_masks()