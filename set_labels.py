import os

def get_labels():
    labels = input("請輸入標籤名稱(例如 dog,cat )：")
    return labels.split(',')

def set_labels(labels):
    glb_path = os.getcwd()
    # 處理 xml_to_yolo.py
    f1 = open('.\\data\\xml_to_yolo_.py', 'r', encoding='UTF-8')
    f2 = open('.\\xml_to_yolo.py', 'w', encoding='UTF-8')
    xml2yolo = '''import xml.etree.ElementTree as ET
import os

sets = ['train', 'val', 'test']
classes = ''' + str(labels) + '\n' + f1.read()

    f2.write(xml2yolo)
    f1.close()
    f2.close()

    # 處理 key.yaml
    f = open('.\data\key.yaml', 'w', encoding='UTF-8')
    key = '''train: '''+glb_path+'''\\dataSets\\path\\train.txt
val: '''+glb_path+'''\\dataSets\\path\\val.txt
test: '''+glb_path+'''\\dataSets\\path\\test.txt

nc: ''' + str(len(labels)) + '\nnames: ' + str(labels) + '\n'
    f.write(key)
    f.close()

if __name__ == '__main__':
    labels = get_labels()
    set_labels(labels)