
## The following steps  are  evaluate  the  darknet  format model  on  the  test2017.
 (means that  the network file is ".cfg" and the  weight file is " .weights") 

- If you want evaluate the  Pytorch format model (means that  the network file is ".py" and the  weight file is " .pt or .pth")  on  the  test2017, try this https://github.com/open-mmlab/mmdetection


### I. Obtain the test images. 
   Go to  https://cocodataset.org/#download,  download the following files and then unzip these two  zip  files:  
   
   test2017.zip (about 6G ),  image_info_test2017.zip (1M).  
    
   test2017: This  file  contains  about 41K  images. 
   
     
   
### II. Introduce the image_info_test2017.
 -2.1 image_info_test2017/annotations/image_info_test2017: This  .json  file  contains about  41k images' information, such  as image's id_number, image's height and width, but NOT include object's  ground truth (like object's x,y, height, width) label.  
    
-2.2  image_info_test2017/annotations/image_info_test-dev2017:  This  .json  file  contains about  21k images' information,  we can regard test-dev2017 as the subset  of test2017, it  also NOT include object's  ground truth  label.

-2.3  There  is one  thing  we need  to  clear.  
- When we talk  about  evaluate on  the  test2017:  it means that  we test on 41k  images.
      
- When we talk  about  evaluate on  the  test-dev2017:  it  means that  we test on 21k  images.
      

             
 
### III. Next, we make the following hierarchy  of the folder. 

      1  COCO/images/train, put the training images  into this floder；
      2  COCO/images/val ,  put the val images  into this floder；
      3  COCO/labels/train, put the .txt(label of  training images ) into this floder；
      4  COCO/labels/val,   put the .txt(label of  val images ) into this floder；
      
1_get_image_id.py, then we  run this .py file,  this will generate  train_2017.txt , val_2017.txt , this  two .txt files  contain the  all  image_id  of the train/val  images.

### IV. At last, we use the  train_2017.txt , val_2017.txt to generate the  absolute path of images  for training and val.      
2-make-image_path.py: if we have the train_2017.txt,  val_2017.txt  and make the above  hierarchy folder correctly,  we generate the  train_coco2017.txt  and  vla_coco2017.txt.

Have a fun with the make dataset.
Good  luck  for  you.
