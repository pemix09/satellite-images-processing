from ultralytics import YOLO
import cv2

model_path = '/Users/mac/Coding/inżynieria uczenia maszynowego/runs/segment/train-all-classes-extended/weights/best.pt'
image_path = '/Users/mac/Desktop/Screenshot 2024-05-19 at 10.55.52.png'

img = cv2.imread(image_path)
height, width, _ = img.shape

model = YOLO(model_path)

results = model(image_path, save_conf=True)

for result in results:
    boxes = result.boxes  # Boxes object for bounding box outputs
    masks = result.masks  # Masks object for segmentation masks outputs
    keypoints = result.keypoints  # Keypoints object for pose outputs
    probs = result.probs  # Probs object for classification outputs
    obb = result.obb  # Oriented boxes object for OBB outputs
    result.show()  # display to screen
    result.save(filename='result.jpg')  # save to disk