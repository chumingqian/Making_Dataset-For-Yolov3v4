# Make_Dataset-for-Ultralytics-yolov3v4

### This  repository has two part make_COCO_dataset &  make_VOC_dataset

###   1. make_COCO_dataset : this  three  python  files  realized the function of  convert the label from the .json  format  to the  .txt  format, so that we can train the  YOLO with the .txt  format  label.

- if we make it  out, the VOC dataset in the data folder should  be the following hierarchy

```
├── data
│   ├── VOC         for  VOC dataset
│   |     ├── images
|   |     |        ├── train
|   |     |        ├── val
|   |     ├── labels
|   |     |        ├── train
|   |     |        ├── val
|
```





- For the  COCO  dataset and pretrained weights,
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



### 2. make_VOC_dataset : this  three  python  files  realized  the function of  convert the label  from the .xml  format  to the .txt  format, so that we can train the  YOLO with the .txt  format  label.

- if we make it out, the COCO dataset in the data folder should  be the following hierarchy

```            
├── data
│   ├── COCO         for  COCO dataset
│   |     ├── images
|   |     |        ├── train
|   |     |        ├── val
|   |     ├── labels
|   |     |        ├── train
|   |     |        ├── val
|
```


