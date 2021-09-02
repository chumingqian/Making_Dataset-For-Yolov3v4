
#  make COCO_dataset-for-Ultralytics-yolov3v4

###     
###    


### I. First, go to the  https://cocodataset.org/#download.


     download the following   files:  
     train2017.zip, val2017.zip,  annotations_trainval2017.zip,   test2017;  Then  unzip the above zip  files.
   
     
   
### II.  Secondly, after we upzip above files, we will see the ./instance_val2017.json under the annotations_trainval2017 folder.
 
0_coco2voc.py: this  file will  convert the labels of all images ( train images:11827 test file :5000)  from  .json  format to  .txt  format  and save the .txt file under ./labels.

Notice that,  it  will generate 11828  + 50001 .txt files (add two class.txt, they are the class name of COCO dataset) under the train/val  folder, separately.
             
 
### III. Next, we make the following hierarchy  of the folder. 

      1  COCO/images/train, put the training images  into this floder；
      2  COCO/images/val ,  put the val images  into this floder；
      3  COCO/labels/train, put the .txt(label of  training images ) into this floder；
      4  COCO/labels/val,   put the .txt(label of  val images ) into this floder；
      
1_get_image_id.py, then we  run this .py file,  this will generate  train_2017.txt , val_2017.txt , this  two .txt files  contain the  all  image_id  of the train/val  images.

### IV. At last, we use the  train_2017.txt , val_2017.txt to generate the  absolute path of images  for training and val.      
2-make-image_path.py: if we have the train_2017.txt,  val_2017.txt  and make the above  hierarchy folder correctly,  we generate the  train_coco2017.txt  and  vla_coco2017.txt.


### Notice: If you want test you model ( ".cfg"  and " weights" file )  on the test-dev2017 which is a json file without ground truth and  submit  to  the  CodaLab.  

        ./readme_test-dev2017.md



Good  luck  for  you. 😊
