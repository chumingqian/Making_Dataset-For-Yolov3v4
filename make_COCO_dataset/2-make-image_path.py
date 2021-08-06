import xml.etree.ElementTree as ET
import pickle
import os
from os import listdir, getcwd
from os.path import join


'''
sets=[('2017', 'train'), ('2017', 'val')]

wd = getcwd()
for year, image_set in sets:
    image_ids = open('VOCdevkit/VOC%s/ImageSets/Main/%s.txt'%(year, image_set)).read().strip().split()
    list_file = open('%s_%s.txt'%(year, image_set), 'w')
    for image_id in image_ids:
        list_file.write('%s/VOCdevkit/VOC%s/JPEGImages/%s.jpg\n'%(wd, year, image_id))
        convert_annotation(year, image_id)
    list_file.close()

'''

sets=[('2017', 'train'), ('2017', 'val')]
wd = getcwd()

for year, image_set in sets:
	image_ids = open('%s_%s.txt'%(image_set,year)).read().strip().split()
	list_file = open('%s_coco%s.txt'%(image_set, year), 'w')
	for image_id in image_ids:
		list_file.write('%s/images/%s/%s\n'%(wd,image_set, image_id))
	list_file.close()




