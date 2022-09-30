import os
import numpy as np

#.txt文件的路径
path = 'txt/hxd.txt'

with open(path) as f1:
    cNames = f1.readlines()  #.readlines()读取.txt文件的每行


#open(path,'w')以可写方式打开.txt文件，将处理过的cNames写入新的文件中
with open(path,'w') as f2:
    f2.writelines(cNames)
