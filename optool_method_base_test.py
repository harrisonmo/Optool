import numpy as py
import re

print("-------untitile---------")
print("Copyright (c) moqk")
#该构想由mqk提出，由mqk构建最初版本

a=open("C:/Users/moqk/Desktop/Optool/code/1.out","r+") #指针放在开头
print("文件名为：",a.name) #读取文件名
a.close()

#以下为字符串匹配与直接输出代码
aa=open("C:/Users/moqk/Desktop/Optool/code/1.out")
aa.seek(0)
i=0

#匹配基组、方法
while i!=-1:
    aa.seek(i)
    k=aa.readline(7)
    if k=='MaxDisk':
        k=aa.readline(1)
        while k!='#':
            i=i+1
            aa.seek(i)
            k=aa.readline(1)
        k=aa.readline()
        print("该计算使用的基组与方法为",k)
        i=-1
    else: 
        i=i+1

aa.close()