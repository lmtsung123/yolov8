from tkinter import filedialog, messagebox
from ultralytics import YOLO
from multiprocessing import freeze_support
import PySimpleGUI as sg


def train_continue():
    freeze_support()
    
    # 設定顯示的檔案類型為 .pt 檔
    file_types = [("PT files", "*.pt")]

    # 打開文件對話框，僅顯示 .pt 檔
    selected_file = sg.popup_get_file('請選擇最後一次的訓練檔:',  title="接續訓練檔選擇器",font=("宋体", 15), file_types=file_types)

    # 如果有選擇檔案，則輸出所選檔案的路徑
    if selected_file:
        try:
            # Load a model
            model = YOLO(selected_file)  # load a partially trained model
            # Train the model using the 'key.yaml' dataset for 300 epochs
            results = model.train(data='data\\key.yaml', resume=True)

            # Evaluate the model's performance on the validation set
            results = model.val()
        except Exception as e:
            messagebox.showerror("錯誤", "檔案讀取有問題")
            model = None


if __name__ == '__main__':
    train_continue()
