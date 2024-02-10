from ultralytics import YOLO
import cv2
from multiprocessing import freeze_support
from time import sleep
import tkinter as tk
from tkinter import filedialog, messagebox
import os

model = None
def open_pt_file():
    file_path = filedialog.askopenfilename(title="選擇訓練檔", filetypes=[("trained file", "*.pt")])
    
    try:
        # Load a model
        model = YOLO(file_path)  # load a pretrained YOLOv8n model

        root.destroy()
        
    # Run batched inference on a list of images
        results = model.predict(source='./assets',save=True, stream=True)  # predict on an image
        #results = model('.\\predect')  # return a list of Results objects

        # Process results list
        #i=1
        for result in results:
            boxes = result.boxes  # Boxes object for bbox outputs
            masks = result.masks  # Masks object for segmentation masks outputs
            keypoints = result.keypoints  # Keypoints object for pose outputs
            probs = result.probs  # Probs object for classification outputs
        #    cv2.namedWindow("YOLOv8"+str(i), cv2.WINDOW_NORMAL)
        #    cv2.imshow("YOLOv8"+str(i), result.plot())
        #    i+=1

        #cv2.waitKey(0)
        #cv2.destroyAllWindows()
            
    except Exception as e:
        messagebox.showerror("錯誤", "檔案讀取有問題")
        model = None


if __name__ == '__main__':
    freeze_support()
    
    # 建立視窗
    root = tk.Tk()
    root.title("訓練檔選擇器")

    # 選擇訓練檔按鈕
    open_button = tk.Button(root, text="選擇訓練檔", command=open_pt_file)
    open_button.pack()
    # 顯示的標籤
    label = tk.Label(root)
    label.pack()

    root.mainloop()
