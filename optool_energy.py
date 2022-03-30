import numpy as py
import re

print("-------optool---------")
print("Copyright (c) moqk")
#该构想由mqk提出，由mqk构建最初版本

op_reagfilename=open("C:/Users/moqk/Desktop/Optool/code/example/int1b.log","r") #指针放在开头
print("读取到的文件名为：",op_reagfilename.name) #读取文件名
op_reagfilename.close()

#以下为字符串匹配与直接输出代码
op_read=open("C:/Users/moqk/Desktop/Optool/code/example/int1b.log","r")
op_read.readlines
#print("读取的数据为：",op_read.readlines())

for line in op_read.readlines():
    line=line.strip()
    readsit0=(re.match('Zero-point correction',line))
    readsit1=(re.match('Thermal correction to Energy',line))
    readsit2=(re.match('Thermal correction to Enthalpy',line))
    readsit3=(re.match('Thermal correction to Gibbs Free Energy',line))
    
    if (readsit0!=None):
        print("%s"%(line))
    else: 0

    if (readsit1!=None):
        print("%s"%(line))
    else: 0

    if (readsit2!=None):
        print("%s"%(line))
    else: 0

    if (readsit3!=None):
        print("%s"%(line))
    else: 0

print('任务完成')
op_read.close()
