import numpy as np
import pandas as pd
 
#sheetname：默认是sheetname为0，返回多表使用sheetname=[0,1]，若sheetname=None是返回全表 。
#注意：int/string返回的是dataframe，而none和list返回的是dict of dataframe。
sheet = pd.read_excel('test.xlsx',sheetname= [0,1])
sheet = pd.read_excel('test.xlsx',sheetname= [0,3])


#通过表名
sheet = pd.read_excel('test.xlsx',sheetname= 'Sheet3')

#通过表的位置
sheet = pd.read_excel('test.xlsx',sheetname= 1)

#默认第一行数据作为列名,
#header ：指定作为列名的行，默认0，即取第一行，数据为列名行以下的数据；若数据不含列名，则设定 header = None；
sheet = pd.read_excel('test.xlsx',sheetname= 2,header=0)

sheet = pd.read_excel('test.xlsx',sheetname= 'Sheet3')


import openpyxl
import datatime
import re
wb=openpyxl.load_workbook('example.xlsx')
#active : 获取活跃的Worksheet
#read_only : 是否只读模式打开Excel文档
#encoding : 文档的字符编码
#properties : 文档的元数据，如标题，创建者，创建日期等
#worksheets : 以列表的形式返回所有的sheet
sheet_master2 = wb.worksheets[1]
sheet_master2['B1']
#获取sheet_master B1 的值
B1=sheet_master2['B1'].value
sheet_master2['C1']=datetime.datetime.now()
wb.save('example.xlsx')

import linecache
count=len(open('191-版本发布.txt','r', encoding='UTF-8').readlines())

for i in range(count-1):
    fst_line=linecache.getline('myout',i)
    sec_line=linecache.getline('myout',i+1)
    print (fst_line.split(" ")[0])
    print (sec_line.split(" ")[0])


a = datetime.datetime.now()
print a                                  
## a变量不指向一个字符串对象，而是指向一个datetime.datetime类型的对象    
import datetime
import time
release_filename='191-版本发布.txt'
current_line=""
models_dir={}
now=time.strftime("%Y-%m-%d %X",time.localtime())[0:10]

def get_update_models(linecontent):
    for i in linecontent:
         pass




def get_current_num(filename):
    f=open(filename,'r', encoding='UTF-8')
    for num,value in enumerate(f):
        if value.strip() != "" and value.strip()[0:10] == now :
            return num  
    f.close()            
            
current_line=get_current_num(release_filename)
ff=open(release_filename,'r', encoding='UTF-8')
conent=ff.readlines()[current_line+1:]

for i in conent:

i="2224         33"
t=re.split(r" +\t+\n+",i)