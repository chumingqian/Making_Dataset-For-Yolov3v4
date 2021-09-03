
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

- When we talk  about  evaluate on  the  test2017:    it means that  we test on 41k  images.
      
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

-  result/coco_result.json:  the name of  generated  .json  file  will be "coco_results.json".

 
### IV. Obtain  the  21k  images'  id  number . 
 
4.1 Obtain  the  21k  images'  id  number:
The exactly  name of  20288 image's  are  saved  in  the  ./test_dev21k.txt. If you  ask where is code through  test-dev2017.json  file to obtain images' id number and   generate  this test_dev21k.txt file.   I may tell you  [here](https://raw.githubusercontent.com/AlexeyAB/darknet/master/scripts/testdev2017.txt)

-Tips:  on the ubuntu 18.04  or above system,  we can open  this  test.txt  file,   use the  "find  and replace " to change the  testing images' actual  path to your  suitation. 

4.2 Copy  21k  images  to  a  new  folder:
use the  ./4_select_test21k.py   to select  21k images  from  the  test2017(41k images)   and  copy them  to  a new  folder.

 
 

Good  luck  for  you.
