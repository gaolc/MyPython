#!/usr/bin/python 
#测试多线程并行
import threading
import time


def fn(n):
    print n
    print str(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()))
    time.sleep(1)
def main():
    tpool = []
    for i in range(10):
        t = threading.Thread(target=fn,args=(i,))
        tpool.append(t)

    for t in tpool:
        t.start()

    for t in tpool:
        threading.Thread.join(t)

if __name__ == '__main__':
    main()
    
    