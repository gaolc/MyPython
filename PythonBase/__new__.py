#!/usr/bin/python
# -*- coding:utf-8 -*-
"""
__init__ 和 __new__ 有什么区别
__init__ 方法做的事情实在对象创建好后初始化变量
真正创建实例的是__new__ 
"""
class Persion(object):
    def __init__(self,name,age):
        print ("in __init__")
        self.name=name
        self.age=age
        
p=Persion('Wang',22)


class man(object):
    def __init__(self,name,age):
        print ("in __init__")
        self.name=name
        self.age=age
    def __new__(cls,*args,**kwargs):
        print ('in __new__')
        instance=object.__new__(cls,*args,**kwargs)
        return instance


p=man('Wang',22)        
