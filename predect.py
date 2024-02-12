from ultralytics import YOLO
import cv2


def predect(mod='best.pt'):
    # Load a model
    model = YOLO(mod)  # pretrained YOLOv8n model

    # Run batched inference on a list of images
    results = model.predict(source='.\\predect',save=True)  # predict on an image
    #results = model('.\\predect')  # return a list of Results objects

    # Process results list
    for result in results:
        boxes = result.boxes  # Boxes object for bbox outputs
        masks = result.masks  # Masks object for segmentation masks outputs
        keypoints = result.keypoints  # Keypoints object for pose outputs
        probs = result.probs  # Probs object for classification outputs
    
if __name__ == '__main__':
    predect()