import numpy as py
import re
import os
import glob

#获取文件夹下的文件,得到文件列表
def getallfile():
    filepath="example"
    filelist=os.listdir(filepath)
    return filelist

#读取log文件个数,得到log文件列表
def getlog(filelist):
    numoflog=0
    filename=[0]
    for line in filelist:       
       if (re.search("log",line)!=None):           
            numoflog=numoflog+1
            filename.append("%s"%(line))

    filename[0]=numoflog
    return filename

#由文件名拼接路径
def getpath(logs):    
    path=[0]   
    pathnum=0
    while pathnum<logs[0]:
        path.append("example/"+logs[pathnum+1])
        pathnum=pathnum+1

    path[0]=logs[0]
    return path

#读文件名
def readfilename(num,path):
    op_readfilename=open(path,"r") #指针放在开头，相对路径
    print("读取到的第",num,"个文件名为：",op_readfilename.name) #读取文件名
    op_readfilename.close()

#读log文件中的字符串
def readstring(path,string):
    op_read=open(path,"r")
    op_read.readlines
    for line in op_read.readlines():      
       if (re.search(string,line)!=None):           
            print("%s"%(line))
    
    op_read.close()

#读SCF Done
def scfdone(path):
    op_read=open(path,"a")
    op_read.readlines
    for line in op_read.readlines():      
       if (re.search(string,line)!=None):           
            print("%s"%(line))
    
    op_read.close()

#判断是否正常结束
def ifnormalend(path):
    ifnormalendnum=0
    op_read=open(path,"r")
    op_read.readlines
    for line in op_read.readlines():      
       if (re.search("Normal termination",line)!=None):           
            ifnormalendnum=ifnormalendnum+1
            print("该Gaussian计算中的第",ifnormalendnum,"个任务正常结束")
    op_read.close()        
    if ifnormalendnum==0:
      print("该计算任务未正常结束")
    return ifnormalendnum

#以下为主程序
print("--------optool---------")
print("Copyright (c) moqk")
#该构想由mqk提出，由mqk构建最初版本
    

filelist=getallfile()
logs=getlog(filelist)

path=getpath(logs)

#输出所有log文件的数据
num=0
while num<path[0]:
    readfilename(num+1,path[num+1])
    ifnen=ifnormalend(path[num+1])
    if (ifnen!=0):
        readstring(path[num+1],'Zero-point correction')
        readstring(path[num+1],'Thermal correction to Energy')
        readstring(path[num+1],'Thermal correction to Enthalpy')
        readstring(path[num+1],'Thermal correction to Gibbs Free Energy')
     #   scfdone(path[num+1])

    num=num+1

print("normal end")
