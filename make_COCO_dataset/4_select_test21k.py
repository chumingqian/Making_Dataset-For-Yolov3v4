import xml.etree.ElementTree as ET
import pickle
import os
from os import listdir, getcwd
from os.path import join
import shutil

'''
# 创建VOC文件夹及子文件夹
wd = os.getcwd()
data_base_dir = os.path.join(wd, "VOC/")
if not os.path.isdir(data_base_dir):
    os.mkdir(data_base_dir)

img_dir = os.path.join(data_base_dir, "images/")
if not os.path.isdir(img_dir):
    os.mkdir(img_dir)    
img_train_dir = os.path.join(img_dir, "train/")
if not os.path.isdir(img_train_dir):
    os.mkdir(img_train_dir)
img_val_dir = os.path.join(img_dir, "val/")
if not os.path.isdir(img_val_dir):
    os.mkdir(img_val_dir)

label_dir = os.path.join(data_base_dir, "labels/")
if not os.path.isdir(label_dir):
    os.mkdir(label_dir)    
label_train_dir = os.path.join(label_dir, "train/")
if not os.path.isdir(label_train_dir):
    os.mkdir(label_train_dir)
label_val_dir = os.path.join(label_dir, "val/")
if not os.path.isdir(label_val_dir):
    os.mkdir(label_val_dir)
'''

wd = os.getcwd()
data_base_dir = os.path.join(wd, "COCO/")
if not os.path.isdir(data_base_dir):
    os.mkdir(data_base_dir)

img_dir = os.path.join(data_base_dir, "images/")
if not os.path.isdir(img_dir):
    os.mkdir(img_dir)
img_test_dir = os.path.join(img_dir, "test/")
if not os.path.isdir(img_test_dir):
    os.mkdir(img_test_dir)

label_dir = os.path.join(data_base_dir, "labels/")
if not os.path.isdir(label_dir):
    os.mkdir(label_dir)
label_test_dir = os.path.join(label_dir, "test/")
if not os.path.isdir(label_test_dir):
    os.mkdir(label_test_dir)



dst_test =  'COCO/images/test'
print(os.path.exists('test_dev_21k.txt'))
f = open('test_dev_21k.txt', 'r')
lines = f.readlines()

for line in lines:
    line = line.replace('\n', '')
    if (os.path.exists(line)):
        print("123 %s \n" % line )
        # shutil.copy(line, dst_test)  # 复制图片
        shutil.copy(line, dst_test)
        print('copying test img file  %s' % line + '\n')

    line = line.replace('JPEGImages', 'labels')
    line = line.replace('jpg', 'txt')
    if (os.path.exists(line)):
        shutil.copy(line, "VOC/labels/val")  # 复制label
        print('copying val img label %s' % line + '\n')

assert  "that's  we have  copy the images "

print(os.path.exists('train.txt'))
f = open('train.txt', 'r')
lines = f.readlines()

# 使用train.txt中的图片作为yolov5的训练集
for line in lines:
    line = line.replace('\n', '')
    if (os.path.exists(line)):
        shutil.copy(line, "VOC/images/train") # 复制图片
        print('copying train img file  %s' % line + '\n')
        
    line = line.replace('JPEGImages', 'labels') # 复制label
    line = line.replace('jpg', 'txt')
    if (os.path.exists(line)):
        shutil.copy(line, "VOC/labels/train")
        print('copying train label file  %s' % line + '\n')

