# dataset-for-Ultray-yolov3v4

###   该脚本修改后，只产生训练和验证集两个部分。 
###   实现结果voc2007 + voc2012  两个数据集合并成一个，  最终16551张作为训练集， 2007_test,4952张图片作为测试集； 


###  1 去darkent 官网


     https://pjreddie.com/darknet/yolo/ following the above to parpare the voc2007+ 2012  
   
     wget https://pjreddie.com/media/files/VOCtrainval_11-May-2012.tar
   
     wget https://pjreddie.com/media/files/VOCtrainval_06-Nov-2007.tar
   
     wget https://pjreddie.com/media/files/VOCtest_06-Nov-2007.tar
   
      tar xf VOCtrainval_11-May-2012.tar
      tar xf VOCtrainval_06-Nov-2007.tar
      tar xf VOCtest_06-Nov-2007.tar
   
### 解压后产生一个 VOCdevkit文件夹， 其中包含VOC2007， VOC2012两部分；
 
1-voc_labels.py，
  该文件的作用：a: 在VOC2007，VOC2012中分别创建labels文件夹，并将每张图片的bbox格式由VOC转换成yolo格式，并将其写入到对应的image_id.txt文档中； 
            b: 读取了VOC2007， VOC2012 这两个文件夹中各自的ImageSets/Main/，中的train.txt, val.txt,test.txt,共五个.txt文件，这其每个txt中包含了对应的jpg图片的名称;
            c: 在labels文件夹中创建,年份+xxx.txt 总共五个.txt文件，并将b步骤中读取的图片名称 + 当前图片的路径内容写入 这五个.txt文件中，
             
             2007_test.txt 
             2007_train.txt  
             2007_val.txt    
             2012_train.txt  
             2012_val.txt
             
2-0: 将1中生成的文件合并： cat 2007_train.txt 2007_val.txt 2012_*.txt > train.txt ，  将这四个部分合并为一个训练集train.txt，  2007_test作为测试集；


2-make_floderAndCopy.py 该文件的作用：

      1 新建 VOC/images/train, 将 train.txt 中的 .jpg图片拷贝进去；
      2 新建 VOC/images/val ,  将  2007_test.txt 中的 .jpg 图片拷贝进去；
      3 新建 VOC/labels/train, 将  VOC2007/labels 中  txt 拷贝进去；
      4 新建 VOC/labels/val,   将  VOC2012/labels 中  txt 的拷贝进去；
      
      
3-final-imageTxt.py

      根据 VOC/images  路径，重新生成新的最终的0712_tain.txt, 0712_val.txt ， 这两个文件中所包含的图片路径，为后来新建的文件的图片路径；
