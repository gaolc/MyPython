#!/usr/bin/python
# -*- coding:utf-8 -*-
import openpyxl
import datetime
import re
import time
current_vcomp='component4.xlsx'
#读取excel
wb=openpyxl.load_workbook(current_vcomp)
#active : 获取活跃的Worksheet
#read_only : 是否只读模式打开Excel文档
#encoding : 文档的字符编码
#properties : 文档的元数据，如标题，创建者，创建日期等
#worksheets : 以列表的形式返回所有的sheet
#sheet_master2 = wb.worksheets[9]
#sheet_master2['B1']
#获取sheet_master B1 的值
#B1=sheet_master2['B1'].value
#sheet_master2['C1']=datetime.datetime.now()
#wb.save('example.xlsx')
sheet_master2 = wb.worksheets[9]
max_line=sheet_master2.max_row 
for i in range(2,max_line+1):
    i=str(i)
    filename=sheet_master2['B'+i].value
    with open('init/'+filename,'w') as f:
        data='{"'+sheet_master2['B'+i].value+'":"'+sheet_master2['C'+i].value+'"}'
        data=json.loads(data)
        json.dump(data,f)
        
        
        