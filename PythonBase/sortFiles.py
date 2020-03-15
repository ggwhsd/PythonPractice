# -*- coding: UTF-8 -*-
#python 3.7

import sys
import os

print os.path.split(__file__)[-1] 
print sys.argv[0] #输出当前路径包含文件名。
print os.getcwd() #获取当前工作目录路径
print os.path.abspath('.') #获取当前工作目录路径
print os.path.abspath('test.txt') #获取当前目录文件下的工作目录路径
print os.path.abspath('..') #获取当前工作的父目录 ！注意是父目录路径
print os.path.abspath(os.curdir) #获取当前工作目录路径


def show_file_name_method1(file_dir):
    print("current dir : %s"%(file_dir))
    dir_list = os.listdir(file_dir)
    for cur_file in dir_list:
        path = os.path.join(file_dir, cur_file)
        if os.path.isfile(path): 
            print("%s : is file!"%(cur_file))
        elif os.path.isdir(path):
            print("%s : is dir!"%(cur_file))
            #list_dir(path) # 递归子目录



def show_file_name_method2(file_dir):
    for root, dirs, files in os.walk(file_dir):
        #print("-----------")
        #print(root)  #os.walk()所在目录
        #print("dirs : %s" %(dirs))   #os.walk()所在目录的所有目录名
        #print(files)   #os.walk()所在目录的所有非目录文件名
        #print " "
        return files


self_file = os.path.split(__file__)[-1]
root =os.getcwd()
files = show_file_name_method2(root)
print("###")
#文件按照文件时间排序
files.sort(key=lambda filename: os.path.getmtime(root+'//'+filename))
print files

#files.sort(key=lambda filename: filename)
#print files

index = 0
for file in files:
	suffix=os.path.splitext(file)[-1]
	if suffix == ".py" and file != self_file:
		fullpath_filename = (os.path.abspath(file))
		new_filename = str(index)+"_"+file
		new_fullpath_filename = os.path.abspath(new_filename)
		print("modify")
		print(fullpath_filename)
		print(new_fullpath_filename)
		os.rename(fullpath_filename,new_fullpath_filename)
		index = index + 1
		print("%s -> %s"%(file,new_filename))


#show_file_name_method1(root)




