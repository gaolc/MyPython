# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
list=[1,2,3,4,5,6,7,8,9]

list2=[i for i in list if i%3==0 ]
print (list2)

import time 

#带有不定参的装饰器
def deco(func):
    def wrapper(*args,**kwargs):
        startTime=time.time()
        func(*args,**kwargs)
        endTime=time.time()
        msecs=(endTime-startTime)*1000
        print ("time is {0} ms ".format(msecs))
    return wrapper

@deco
def func(a,b):
    print ("hello, here is a func for add :")
    time.sleep(1)
    print ("result is %d"%(a+b))
    
@deco
def func2(a,b,c):
    print ("hello,here is a func for add:")
    time.sleep(1)
    print ("result is %d"%(a+b+c))


def deco01(func):
    def wrapper(*args, **kwargs):
        print("this is deco01")
        startTime = time.time()
        func(*args, **kwargs)
        endTime = time.time()
        msecs = (endTime - startTime)*1000
        print("time is %d ms" %msecs)
        print("deco01 end here")
    return wrapper

def deco02(func):
    def wrapper(*args, **kwargs):
        print("this is deco02")
        func(*args, **kwargs)

        print("deco02 end here")
    return wrapper

#多个装饰器
@deco01
@deco02
def func3(a,b):
    print("hello，here is a func for add :")
    time.sleep(1)
    print("result is %d" %(a+b))
    
if __name__=='__main__':
    #f=func
    #func2(3,4,5)
    # f(3,4)
    func3(4,5)
    
    