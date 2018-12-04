#!/usr/bin/python
# -*- coding:utf-8 -*-
import os
import fnmatch

images=['*.sh','*.py','*.txt']
matches_sh=[]
matches_py=[]
matches_txt=[]
matches_all=[]

for root,dirnames,filenames in os.walk(os.path.expanduser('~/shell')):
    for extensions in images:
        for filename in fnmatch.filter(filenames,extensions):
            if filename[len(filename)-3:]==images[0][1:]:
                matches_sh.append(os.path.join(root,filename))
            elif filename[len(filename)-3:]==images[1][1:]:
                matches_py.append(os.path.join(root,filename))
            elif filename[len(filename)-4:]==images[2][1:]:
                matches_txt.append(os.path.join(root,filename))
            else:
                matches_all.append(os.path.join(root,filename))
print ('sh:',matches_sh)
print ('py:',matches_py)
print ('txt:',matches_txt)
print ('all:',matches_all)
