#!/usr/bin/python
# -*- coding:utf-8 -*-
import openpyxl
import datetime
import re
import time
#定义变量
current_vcomp='component4.xlsx'
release_filename='191版本发布.txt'
current_line=""
models_dir={}
now=time.strftime("%Y%m%d %X",time.localtime())[0:8]

#读取excel
wb=openpyxl.load_workbook(current_vcomp)
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
sheet_master2.max_row 




def get_update_models(linecontent):
    for i in linecontent:
         pass




def get_current_num(filename):
    f=open(filename,'r', encoding='UTF-8')
    for num,value in enumerate(f):
        if value.strip() != "" and value.strip()[0:8] == now :
            return num  
    f.close()            
            
current_line=get_current_num(release_filename)
ff=open(release_filename,'r', encoding='UTF-8')
conent=ff.readlines()[current_line+1:]
for i in conent:
    if i.strip() != "" :
        t=re.split(r" +",i)
        models_dir[t[0]]={}
        models_dir[t[0]]['Author']=t[1]
        models_dir[t[0]]['oldtonew']= t[2][t[2].find('[')+1:t[2].find(']')]

 
for (k,v) in models_dir.items():
    print ('{0} \t {1} \t{2}'.format(k,v['Author'],v['oldtonew']))
 	
