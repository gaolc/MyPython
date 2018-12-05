#!/usr/bin/python
# -*- coding:utf-8 -*-

import time
def climbStairs(n):
    """
    计算n级台阶的算法，每次可走1步或2步
    :param n :台阶总数
    :return : n 级台阶的走法
    构建模型:
    F(1)=1
    F(2)=2
    F(n)=F(n-1)+F(n-2) (3<=n<=10)
    """
    if n<1:
        return 0
    elif n==1:
        return 1
    elif n==2:
        return 2
    else:
        return climbStairs(n-1)+climbStairs(n-2)       
def climb(n,value):
    """
    计算n级台阶的算法，每次可走1步或2步
    :param n :台阶总数
    :return : n 级台阶的走法
    ::param value :存储不同台阶走法的dict
    构建模型:
    F(1)=1
    F(2)=2
    F(n)=F(n-1)+F(n-2) (3<=n<=10)
    """
    if value.get(n) is not None:
        return value.get(n)
    else:
        if n<1:
            value[n]=0
        elif n==1:
            value[n]=1
        elif n==2:
            value[n]=2
        else:
            value[n]=climb(n-1,value)+climb(n-2,value)
    return value[n]
if __name__=="__main__":
    t1=int(time.time())
    a=climbStairs(100)
    t2=int(time.time())
    value={}
    b=climb(100,value)
    t3=int(time.time())
    print "Metho:{0}  time:{1}".format(a,t2-t1)
    print "Metho:{0}  time:{1}".format(b,t3-t2)
    