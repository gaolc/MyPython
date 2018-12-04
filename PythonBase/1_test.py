#!/usr/bin/python
# --*-- coding:utf-8 --*--
from __future__ import print_function 
import subprocess
import threading

#
def is_reacheable (ip):
    #subprocess.call() 调用系统命令
    #os.system()  
    if subprocess.call(["ping","-c","1",ip]):
        print ("{0} is alive ".format(ip))
    else:
        print  ("{0} is unreacheable ".format(ip))
        
        
def main ():
    #for i in {1..255} ;do echo 10.1.1.${i} >> ips.txt ;done
    #for i in $(seq 1  255) ;do echo 10.1.1.${i} >> ips.txt ;done
    with open("ips.txt") as f :
        lines =f.read()
        lines =lines.splitlines()    #去除换行
        threads=[]
        for line in lines:        #第一个参数是线程函数变量，第二个参数args是一个数组变量参数，如果只传递一个值，就只需要i, 如果需要传递多个参数，那么还可以继续传递下去其他的参数，其中的逗号不能少，少了就不是数组了，就会出错。
            thr=threading.Thread(target=is_reacheable, args=(line,))
            thr.start()
            threads.append(thr)
            
            
        for thr in threads:
            thr.join()

if __name__=="__main__":
    main()
            