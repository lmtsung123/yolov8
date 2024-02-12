import PySimpleGUI as sg
import split_train_val as stv
import set_labels as sl
import xml_to_yolo as xty
import train as tr
import predect as pr
import train_continue as tc
import os

global_path = os.getcwd()

def split_train_val():
    layout = [  [sg.Text('請確認標籤及訓練照片已經放置在底下的資料夾中。',font=("宋体", 15))],
              [sg.Image('./assets/allinone/01.png')],
            [sg.Button('確定'),sg.Button('離開')] ]
    
    window = sg.Window('split_train_val', layout)
    
    while True:
        event, values = window.read()
        if event in (None, '離開'):   # 如果用户关闭窗口或点击`Cancel`
            break
        if event == '確定':
            stv.split_train_val()
            break
    window.close()

def set_labels():
    layout = [  [sg.Text('請輸入標籤名稱，依序一行一個標籤。',font=("宋体", 15))],
                [sg.Multiline('', enable_events=True, key='-INPUT-', expand_x=True, expand_y=True, justification='left')],
                [sg.Button('確定'),sg.Button('離開')] ]
    
    window = sg.Window('set_labels', layout)
    
    while True:
        event, values = window.read()
        if event in (None, '離開'):   # 如果用户关闭窗口或点击`Cancel`
            break
        if event == '確定':
            labels = values['-INPUT-'].split('\n')
            if len(labels) > 0:
                break
    window.close()
    sl.set_labels(labels)

def xml_to_yolo():
    layout = [  [sg.Text('請確認已經定義好標籤內容。',font=("宋体", 15))],
            [sg.Button('確定'),sg.Button('離開')] ]
    
    window = sg.Window('xml_to_yolo', layout)
    
    while True:
        event, values = window.read()
        if event in (None, '離開'):   # 如果用户关闭窗口或点击`Cancel`
            break
        if event == '確定':
            xty.xml_to_yolo()
            break
    window.close()
    
def train():

    layout = [  [sg.Text('epochs',font=("宋体", 15))],
                [sg.Listbox(values=[50,100,150,200,250,300], size=(20, 12), key='-LIST-', enable_events=True, default_values=[200])],
                [sg.Radio('GPU', "RADIO1", default=True, size=(10,1)), sg.Radio('CPU', "RADIO1")],
                [sg.Button('確定'),sg.Button('離開')] ]
    
    window = sg.Window('train', layout)
    
    while True:
        event, values = window.read()
        if event in (None, '離開', '確定'):   # 如果用户关闭窗口或点击`Cancel`
            break
    window.close()
    if event == '確定':
            tr.train(epochs=values['-LIST-'][0], device='CPU' if values[1] else 0)

def predect():
    # 定义要显示的文件类型及其描述
    file_types = [("trained file", "*.pt")]
    selected_file  = sg.popup_get_file('請選擇檔案', title="已訓練檔案選擇器", file_types=file_types)
    if selected_file :
        pr.predect(mod=selected_file )

def train_continue():

    tc.train_continue()



def main():
    sg.theme('DarkAmber')   # 设置当前主题
    # 界面布局，将会按照列表顺序从上往下依次排列，二级列表中，从左往右依此排列
    layout = [  [sg.Text('使用工具列表:',font=("宋体", 20))],
                [sg.Text('split_train_val.py ...',font=("宋体", 15)), sg.Button('執行',font=("宋体", 10),key='split_train_val')],
                [sg.Text('set_labels.py ...',font=("宋体", 15)), sg.Button('執行',font=("宋体", 10),key='set_labels')],
                [sg.Text('xml_to_yolo.py ...',font=("宋体", 15)), sg.Button('執行',font=("宋体", 10),key='xml_to_yolo')],
                [sg.Text('train.py ...',font=("宋体", 15)), sg.Button('執行',font=("宋体", 10),key='train')],
                [sg.Text('predect.py ...',font=("宋体", 15)), sg.Button('執行',font=("宋体", 10),key='predect')],
                [sg.Text('train_continue.py ...',font=("宋体", 15)), sg.Button('執行',font=("宋体", 10),key='train_continue')],
                [sg.Button('結束')] ]


    # 创造窗口
    window = sg.Window('YOLO v8 小白工具箱', layout)
    # 事件循环并获取输入值
    while True:
        event, values = window.read()
        if event in (None, '結束'):   # 如果用户关闭窗口或点击`Cancel`
            break
        if event == 'split_train_val':
            split_train_val()
        elif event == 'set_labels':
            set_labels()
        elif event == 'xml_to_yolo':
            xml_to_yolo()
        elif event == 'train':
            train()
        elif event == 'predect':
            predect()
        elif event == 'train_continue':
            train_continue()


    window.close()

if __name__ == '__main__':
    main()
