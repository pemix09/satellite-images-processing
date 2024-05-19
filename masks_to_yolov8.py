import os
import cv2
import numpy as np

def convert_masks_to_yolov8(masks_dir, output_dir, class_names):
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Get list of mask files
    mask_files = os.listdir(masks_dir)

    for mask_file in mask_files:
        # Load mask image
        mask_path = os.path.join(masks_dir, mask_file)
        mask = cv2.imread(mask_path)

        # Convert mask to YOLO v8 txt format
        height, width, _ = mask.shape
        mask = mask.reshape(-1, 3)
        mask_classes = np.unique(mask, axis=0)

        # Create YOLO v8 txt file
        txt_file = os.path.splitext(mask_file)[0] + ".txt"
        txt_path = os.path.join(output_dir, txt_file)

        with open(txt_path, "w") as f:
            for mask_class in mask_classes:
                class_index = np.where((class_names == mask_class).all(axis=1))[0]
                if len(class_index) > 0:
                    class_index = class_index[0]
                    class_id = class_index + 1  # YOLO class IDs start from 1
                    class_mask = np.all(mask == mask_class, axis=1)
                    class_mask_indices = np.where(class_mask)[0]
                    class_mask_boxes = class_mask_indices.reshape(-1, 2)

                    for box in class_mask_boxes:
                        x_center = (box[1] + 0.5) / width
                        y_center = (box[0] + 0.5) / height
                        box_width = 1 / width
                        box_height = 1 / height

                        f.write(f"{class_id} {x_center} {y_center} {box_width} {box_height}\n")

    print("Conversion completed successfully!")

# Example usage
masks_dir = "training_images/all/masks-temp"
output_dir = "training_images/all/masks-temp-yolov8"
class_names = np.array([[32,128,192], [255,255,255], [255,255,0], [0, 255, 255], [120, 100, 70], [98,198,45], [255,160,0]])  # Example class names

convert_masks_to_yolov8(masks_dir, output_dir, class_names)
