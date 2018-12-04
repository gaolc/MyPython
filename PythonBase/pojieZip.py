#!/usr/bin/python
import zipfile
f=zipfile.ZipFile('V1.3.zip')

with open('password.txt') as pf:
    for line in pf:
        l=line.split()
        for i in l:
            try:
                f.extractall(pwd=i)
                print("password is {0}".format(i))
            except:
                pass