
# PartI: Prepare  for  install  OPENCV ;
1.1 First, check out if the version  between  nvidia-drive,  cuda and cudnn  are suitable  and make sure they are have  been installed  correctly.

My environment was  Ubuntu 16.04;  Geforce 1080Ti(12G),  the  drivers  for  Nvidia graph driver: 450.66,  Cuda:10.2,  cudnn:8;


1.2 Confirm the version between  gcc  and  g++  are  match;
             
         use " gcc --version   g++ --version " to check.
              
         if  we have not install them ,try this " sudo update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++-5 20 "
         
         if  we have  muti versions of  gcc  or  g++ ,  we  can  config the  priority:
                  sudo update-alternatives --config gcc
                  sudo update-alternatives --config g++

1.3 Download the opencv  version  you  want  install,  mine  is opencv3.4.15 ;
   




# PartII:  Install  the  OPENCV3.4
    
2.1  Unzip the  opecv.zip  file,  and  cd into  the opecv; cd  opencv/

2.2  "mkdir build",  "cd build/ "

2.3  Instructions  prepare for  CMAKE (important  step )
                      
             cmake -DCMAKE_BUILD_TYPE=RELEASE -DCMAKE_INSTALL_PREFIX=/usr/local -DINSTALL_PYTHON_EXAMPLES=ON -DINSTALL_C_EXAMPLES=OFF -DPYTHON_EXCUTABLE=/usr/bin/python3  -DWITH_CUDA=ON  -DWITH_CUBLAS=ON -DDCUDA_NVCC_FLAGS="-D_FORCE_INLINES" -DCUDA_ARCH_BIN="6.1" -DCUDA_ARCH_PTX="" -DCUDA_FAST_MATH=ON -DWITH_TBB=ON -DWITH_V4L=ON -DWITH_GTK=ON -DWITH_OPENGL=ON -DWITH_IPP=OFF -DOPENCV_EXTRA_MODULES_PATH= ../../opencv_contrib-3.4.0/modules -DBUILD_EXAMPLES=ON  -DCMAKE_BUILD_TYPE=Release -DCUDA_nppi_LIBRARY=true -DCUDA_HOST_COMPILER=/usr/bin/gcc-5 ..
             
             -DCUDA_ARCH_BIN="6.1" : Mine graph card is Geforce 1080Ti(12G), should be  changed  for  yours, check it out in Nvidia offical Website;
             -DWITH_IPP=OFF : turn off  download  the ipp file  since  i seldom use it;
             -DCUDA_HOST_COMPILER=/usr/bin/gcc-5 :  use the gcc-5  version;
   
   Tips:  if we  have errors for the cmake, we  can use  "ctrl + shift + F"  to  locate  whers  is "error "  on the  terminal;
             when we done, should  be sth like this:
                       
                       - General configuration for OpenCV 3.4.15 =====================================
                        --   Version control:               unknown
                        -- 
                        --   Platform:
                        --     Timestamp:                   2021-08-29T15:14:57Z
                        --     Host:                        Linux 5.6.19-050619-generic x86_64
                        --     CMake:                       3.20.5
                        --     CMake generator:             Unix Makefiles
                        --     CMake build tool:            /usr/bin/make
                        --     Configuration:               Release
                        ...
                        
                        -- Generating done
                        -- Build files have been written to: /home/deep-learning-chuyun/Documents/opencv-3.4.15/build

                                                                                       
                       
                      
2.4  sudo make ;  or use  make -j8  ;  make  -j12  to save our  times  if you machine support;
                     After  we  done,  should have the following informations：

                                [100%] Built target example_tutorial_pnp_detection
                                [100%] Linking CXX shared module ../../lib/cv2.so
                                [100%] Linking CXX shared module ../../lib/python3/cv2.cpython-35m-x86_64-linux-gnu.so
                                [100%] Built target opencv_python2
                                [100%] Built target opencv_python3


2.5  sudo  make  install ;

2.6  sudo gedit /etc/ld.so.conf ; 
     
     add the  following line into it:   include  /usr/local/lib; 
     update it:  sudo  ldconfig;   where the "/usr/local" is  associate with  " -DCMAKE_INSTALL_PREFIX=/usr/local" during the  cmake; 
 
2.7  Config  your  environment path:
                      
                      sudo gedit /etc/bash.bashrc
                      
                      add the this  content：
                        PKG_CONFIG_PATH=$PKG_CONFIG_PATH:/usr/local/lib/pkgconfig
                        export PKG_CONFIG_PATH

                      source /etc/bash.bashrc

2.8  Now, we  can  check it out if the opecv has  been installed correctly: use the command: " pkg-config opencv --modversion "
 



# PartIII:  Install  the  Darknet 

3.1  Clone  AlexAB's repository: " git clone https://github.com/AlexeyAB/darknet.git ",   and  "cd ./darknet".

3.2  Change  the  makefile  to  have  GPU  and OPENCV  enabled. 

                    sed -i 's/OPENCV=0/OPENCV=1/' Makefile
                    sed -i 's/GPU=0/GPU=1/' Makefile
                    sed -i 's/CUDNN=0/CUDNN=1/' Makefile
                    sed -i 's/CUDNN_HALF=0/CUDNN_HALF=1/' Makefil
                    
                    
                    
 3.3 Make darknet (builds darknet so that you can then use the darknet executable file to run or train object detectors)
     "make "                 

 3.4 Now, if we want check the darknet installation we may download pre-trained  YOLOV4  weights:
           
           wget https://github.com/AlexeyAB/darknet/releases/download/darknet_yolo_v3_optimal/yolov4.weights
  
            ```bash
            ./darknet detector test <path to .data file> <path to config> <path to weights> <path to image>
            ```
            
            ./darknet detector test cfg/coco.data cfg/yolov4.cfg yolov4.weights data/dog.jpg
            
            
That's  it,  enjoy  your  vision  time  and  have a  fun. :blush:
