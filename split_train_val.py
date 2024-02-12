# coding:utf-8

import os
import random
import argparse

def split_train_val():
    abs_path = os.getcwd()
    parser = argparse.ArgumentParser()
    # xml文件的地址，根据自己的数据进行修改 xml一般存放在Annotations下
    parser.add_argument('--xml_path', default=abs_path+'\dataSets\Annotations', type=str, help='input xml label path')
    # 数据集的划分，地址选择自己数据下的ImageSets/Main
    parser.add_argument('--txt_path', default=abs_path+'\dataSets\ImageSets/Main', type=str, help='output txt label path')
    opt = parser.parse_args()
    trainval_percent = 1.0  # 训练集和验证集所占比例。 这里没有划分测试集
    train_percent = 0.9  # 训练集所占比例，可自己进行调整
    val_percent = 0.1  # 验证集所占比例，可自己进行调整
    test_percent = 0.0  # 测试集所占比例，可自己进行调整
    xmlfilepath = opt.xml_path
    txtsavepath = opt.txt_path
    total_xml = os.listdir(xmlfilepath)
    if not os.path.exists(txtsavepath):
        os.makedirs(txtsavepath)

    num = len(total_xml)
    list_index = range(num)
    tr = int(num * train_percent)
    if test_percent == 0:
        tv = num-tr
    else:
        tv = int(num * val_percent)
    tt = int(num * test_percent)
    datasets = random.sample(list_index, num)
    train = datasets[:tr]
    val = datasets[tr:tr+tv]
    test = datasets[tr+tv:]

    file_test = open(txtsavepath + '/test.txt', 'w')
    file_train = open(txtsavepath + '/train.txt', 'w')
    file_val = open(txtsavepath + '/val.txt', 'w')

    for i in list_index:
        name = total_xml[i][:-4] + '\n'
        if i in train:
            file_train.write(name)
        elif i in val:
            file_val.write(name)
        else:
            file_test.write(name)

    file_train.close()
    file_val.close()
    file_test.close()

if __name__ == '__main__':
    split_train_val()