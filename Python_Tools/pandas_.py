import numpy as np
import pandas as pd
 
#sheetname��Ĭ����sheetnameΪ0�����ض��ʹ��sheetname=[0,1]����sheetname=None�Ƿ���ȫ�� ��
#ע�⣺int/string���ص���dataframe����none��list���ص���dict of dataframe��
sheet = pd.read_excel('test.xlsx',sheetname= [0,1])
sheet = pd.read_excel('test.xlsx',sheetname= [0,3])


#ͨ������
sheet = pd.read_excel('test.xlsx',sheetname= 'Sheet3')

#ͨ�����λ��
sheet = pd.read_excel('test.xlsx',sheetname= 1)

#Ĭ�ϵ�һ��������Ϊ����,
#header ��ָ����Ϊ�������У�Ĭ��0����ȡ��һ�У�����Ϊ���������µ����ݣ������ݲ������������趨 header = None��
sheet = pd.read_excel('test.xlsx',sheetname= 2,header=0)

sheet = pd.read_excel('test.xlsx',sheetname= 'Sheet3')


import openpyxl
import datetime
import re
wb=openpyxl.load_workbook('component4.xlsx')
wb=openpyxl.load_workbook('example.xlsx')
#active : ��ȡ��Ծ��Worksheet
#read_only : �Ƿ�ֻ��ģʽ��Excel�ĵ�
#encoding : �ĵ����ַ�����
#properties : �ĵ���Ԫ���ݣ�����⣬�����ߣ��������ڵ�
#worksheets : ���б����ʽ�������е�sheet
sheet_master2 = wb.worksheets[1]
sheet_master2['B1']
#��ȡsheet_master B1 ��ֵ
B1=sheet_master2['B1'].value
sheet_master2['C1']=datetime.datetime.now()
wb.save('example.xlsx')

import linecache
count=len(open('191-�汾����.txt','r', encoding='UTF-8').readlines())

for i in range(count-1):
    fst_line=linecache.getline('myout',i)
    sec_line=linecache.getline('myout',i+1)
    print (fst_line.split(" ")[0])
    print (sec_line.split(" ")[0])


a = datetime.datetime.now()
print a                                  
## a������ָ��һ���ַ������󣬶���ָ��һ��datetime.datetime���͵Ķ���    
import datetime
import time
release_filename='191-�汾����.txt'
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