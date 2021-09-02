# Make_Dataset-for-Ultralytics-yolov3v4: 
  we make the dataset for  ultralytics-version yolo (https://github.com/ultralytics/yolov3 ) 
  
  and the origianl  darknet-version yolo    (https://github.com/AlexeyAB/darknet ), 
  
  both support for yolov3 and yolov4.
  
## This repository mainly include  three parts:

- Part I:  make  an environment  for the  Darknet

- Part II:  make_VOC_dataset

- Part III:  make_COCO_dataset and test on the  test2017. 
 



## Part I:  make  an environment  for the  Darknet   

- Pelease read about  the ./Env_For_Darknet.md



## Part II: make_VOC_dataset
2. Make_VOC_dataset : this  three  python  files  realized  the function of  convert the label  from the  ".xml"  format  to the  ".txt"  format, so that we can train the  YOLO with the .txt  format  label.

- If we make it out, the VOC dataset in the data folder should  be the following hierarchy.

```
├── data
│   ├── VOC         For  VOC dataset  folder
│   |     ├── images
|   |     |        ├── train
|   |     |        ├── val
|   |     ├── labels
|   |     |        ├── train
|   |     |        ├── val
|
```



## Part I:  make_COCO_dataset and evaluate on the  test2017 
3.1 make_COCO_dataset:  
The first three  python  files realized the function of convert the label from the " .json"  format  to the ".txt"  format, so that we can train the  YOLO network  with the .txt  format  label.

-If we make it out,  the COCO dataset in the data folder should  be the following hierarchy.

```            
├── data
│   ├── COCO      For  COCO dataset folder 
│   |     ├── images
|   |     |        ├── train
|   |     |        ├── val
|   |     ├── labels
|   |     |        ├── train
|   |     |        ├── val
|
```

3.2 If you want test your model  without the ground truth label, 

and  submit the reuslts.json  to the CodaLab   https://competitions.codalab.org/competitions/20794 ,  

here have a  simple tutorials: ./make_COCO_dataset/readme_test-dev2017.md 


- For the  COCO  dataset and yolovv3-v4 pretrained weights:
Download the following address, download and unzip the folder to copy to the data directory can be used.

- [COCO2017](https://pan.baidu.com/s/1KysFL6AmdbCBq4tHDebqlw)
  
  Extract code：hjln

- [COCO2014](https://pan.baidu.com/s/1EoXOR77yEVokqPCaxg8QGg)
  
  Extract code：k8ms
 Weights Download
- [yolov3_COCO pretraining weights](https://pan.baidu.com/s/1JZylwRQIgAd389oWUu0djg)

  Extract code：k8ms
 
- [yolov4_COCO pretraining weights](https://pan.baidu.com/s/1jAGNNC19oQhAIgBfUrkzmQ)

  Extract code：njdg
  
---



