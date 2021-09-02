
## The following steps  are  evaluate  the  darknet  format model  on  the  test2017.
- darknet  format model means that  the network file is ".cfg" and the  weight file is " .weights" 

- If you want evaluate the  Pytorch format model (means that  the network file is ".py" and the  weight file is " .pt or .pth")  on  the  test2017, try this https://github.com/open-mmlab/mmdetection


### I. Obtain the test images. 
   Go to  https://cocodataset.org/#download,  download the following files and then unzip these two  zip  files:  
   
   test2017.zip (about 6G ),  image_info_test2017.zip (1M).  
    
   test2017: This  file  contains  about 41K  images. 
   
     
   
### II. Introduce the image_info_test2017.
-2.1 image_info_test2017/annotations/image_info_test2017: This .json  file  contains about  41k images' information, such  as image's id_number, image's height and width, but NOT include object's  ground truth (like object's x,y, height, width) label.  
    
-2.2  image_info_test2017/annotations/image_info_test-dev2017: This .json  file  contains about  21k images' information,  we can regard test-dev2017 as the subset  of test2017, it  also NOT include object's  ground truth  label.

-2.3  There  is one  thing  we need  to  clear. 

- When we talk  about  evaluate on  the  test2017:   it means that  we test on 41k  images.
      
- When we talk  about  evaluate on  the  test-dev2017:  it  means that  we test on 21k  images.
      

             
 
### III. Testing the model,  here is a reference [testing the yolo model in colab](https://colab.research.google.com/drive/1s7h9pMjw-K3vDWaeIczgGi8KTUrgvoi1?usp=sharing). 
3.1 Test one single image:
- ./darknet  detector   test   cfg/coco.data cfg/yolov4.cfg    yolov4.weights     data/dog.jpg
 
3.2 Test multi images and  save the result in VOC  format:
- ./darknet detector test cocotest.data  cfg/vars55M_yolov4.cfg    55Mmap45.weights  -ext_output -dont_show -out result_tmp.json < test_images.txt ; 
-  test_images.txt: include the test sample image's  path.

   
3.3 Validate the multi images and  save the result in COCO  format:
make sure there  is  result folder  nearby the exectuable  ./darknet. 

- ./darknet detector valid cocotest.data  cfg/vars55M_yolov4.cfg    55Mmap45.weights; 
- cocotest.data: --> valid -->  change the  test.txt, the test.txt will include all the image's path we may want test.   to  suit  your  test image's  path. 

-  result/coco_result.json:  默认的json 文件名 是 coco_results.json;: include the test sample image's  path.

 
 
 
### IV. At last, we use the  train_2017.txt , val_2017.txt to generate the  absolute path of images  for training and val.      
2-make-image_path.py: if we have the train_2017.txt,  val_2017.txt  and make the above  hierarchy folder correctly,  we generate the  train_coco2017.txt  and  vla_coco2017.txt.

Have a fun with the make dataset.
Good  luck  for  you.
