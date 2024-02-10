from multiprocessing import freeze_support
from ultralytics import YOLO
from time import sleep
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import ImageTk, Image
import os

def open_pt_file():
    file_path = filedialog.askopenfilename(title="選擇訓練檔", filetypes=[("trained file", "*.pt")])
    
    try:
        # Load a model
        model = YOLO(file_path)  # load a partially trained model

        root.destroy()

        # Train the model using the 'key.yaml' dataset for 300 epochs
        results = model.train(data='data\\key.yaml', epochs=300, imgsz=640, device=0, workers=1)

        # Evaluate the model's performance on the validation set
        results = model.val()
        
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


