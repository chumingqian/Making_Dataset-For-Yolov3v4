# dataset-for-Ultray-yolov3v4

###  该脚本修改后， 只产生训练和 验证集 两个部分， 
###   实现结果voc2007 + voc2012  两个数据集，合并成一个， 最终16551 张作为训练集， 2007_test作为测试集； 


###  1 去darkent 官网，  https://pjreddie.com/darknet/yolo/ following the above to parpare the voc2007+ 2012  
   wget https://pjreddie.com/media/files/VOCtrainval_11-May-2012.tar
   wget https://pjreddie.com/media/files/VOCtrainval_06-Nov-2007.tar
   wget https://pjreddie.com/media/files/VOCtest_06-Nov-2007.tar
   tar xf VOCtrainval_11-May-2012.tar
   tar xf VOCtrainval_06-Nov-2007.tar
   tar xf VOCtest_06-Nov-2007.tar
   
 解压后产生一个 VOCdevkit文件夹， 其中包含VOC2007， VOC2012两部分；
  之后运行 1-voc_label.py文件，该文件的作用：
            a: 创建labels文件夹，
            b: 读取了VOC2007， VOC2012 这两个文件夹中各自的ImageSets/Main/... , train.txt, val.txt,test.txt;
            c: 在labels文件夹中创建;年份+xxx.txt , 2007_test.txt   
             2007_train.txt  
             2007_val.txt    
             2012_train.txt  
             2012_val.txt
