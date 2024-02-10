import os

glb_path = os.getcwd()

labels = input("請輸入標籤名稱(例如'dog','cat')：")

# 處理 xml_to_yolo.py
f1 = open('.\\data\\xml_to_yolo_.py', 'r', encoding='UTF-8')
f2 = open('.\\xml_to_yolo.py', 'w', encoding='UTF-8')
xml2yolo = '''import xml.etree.ElementTree as ET
import os

sets = ['train', 'val', 'test']
classes = [''' + labels + ']\n' + f1.read()

f2.write(xml2yolo)
f1.close()
f2.close()

# 處理 key.yaml
f = open('.\data\key.yaml', 'w', encoding='UTF-8')
key = '''train: '''+glb_path+'''\\path\\train.txt
val: '''+glb_path+'''\\path\\val.txt
test: '''+glb_path+'''\\path\\test.txt

nc: ''' + str(len(labels.split(','))) + '\nnames: [' + labels + ']\n'
f.write(key)
f.close()