import os

masks_dir = '/Users/mac/Coding/inżynieria uczenia maszynowego/training_images/car/masks'
img_dir = '/Users/mac/Coding/inżynieria uczenia maszynowego/training_images/car/images'

for img_filename in os.listdir(img_dir):
    img_filename_without_extensions = os.path.splitext(img_filename)[0]

    if os.path.isfile(f'{masks_dir}/{img_filename_without_extensions}' + '.png') == False:
        os.remove(f'{img_dir}/{img_filename}')
        print(f"Deleted {img_filename}")