# P01 批量读取文件名，并将读取的文件名保存到指定路径下的txt中（带.*** 后缀）

import os
sets = [('train', 2017), ('val', 2017)]

def ListFilesToTxt(dir, file, wildcard, recursion):
    exts = wildcard.split(" ")
    files = os.listdir(dir)
    for name in files:
        fullname = os.path.join(dir, name)
        if (os.path.isdir(fullname) & recursion):
            ListFilesToTxt(fullname, file, wildcard, recursion)
        else:
            for ext in exts:
                if (name.endswith(ext)):
                    file.write(name + "\n")
                    break


dir_path = [('./images/train', 'train_2017.txt'), ('./images/val', 'val_2017.txt')]

def ReadName1():
     for tmp_dir, outfile in dir_path:
        print(" current dir : %s" % tmp_dir )  # 读取文件路径
        print(" current output_path : %s" % outfile ) # 将文件名写入train_coco2017.txt
        wildcard = ".jpg" # 读取jpg图片
        #   wildcard = ".jpg .txt .exe .dll .lib"      #要读取的文件类型；
        file = open(outfile, "w")
        if not file:
          print("cannot open the file %s for writing" % outfile)
        ListFilesToTxt(tmp_dir, file, wildcard, 1)
        file.close()




def ReadName():
        dir = "./images/train"  # 读取文件路径
        outfile = "train_coco2017.txt"  # 将文件名写入train_coco2017.txt
        wildcard = ".jpg" # 读取jpg图片
        #   wildcard = ".jpg .txt .exe .dll .lib"      #要读取的文件类型；
        file = open(outfile, "w")
        if not file:
          print("cannot open the file %s for writing" % outfile)
        ListFilesToTxt(dir, file, wildcard, 1)
        file.close()




#if __name__ == "__main__":
# ReadName()
ReadName1()


