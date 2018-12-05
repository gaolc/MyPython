#!/usr/bin/python2
# -*- coding:utf-8 -*-
import os
import platform
import ctypes,sys 
import itertools    
import ConfigParser
from socket import *

 
STD_INPUT_HANDLE = -10
STD_OUTPUT_HANDLE = -11
STD_ERROR_HANDLE = -12

FOREGROUND_GREEN = 0x0a # green.
FOREGROUND_RED = 0x0c # red.
FOREGROUND_BLUE = 0x09 # blue.
# get handle
if len(sys.argv)!=2:
    print ('Using: python2 {0} <env>'.format(sys.argv[0]))
    print ('exp: python2 {0} prod'.format(sys.argv[0]))
    sys.exit(1)
elif len(sys.argv)==2:
    env=sys.argv[1].upper()
else:
    pass    
     
def linux_conn_scan(env,host,port):
    conn=socket(AF_INET,SOCK_STREAM)
    try:
        conn.settimeout(5)
        conn.connect((host,port)) 
        print ('\033[0;32m{0} ip:{1} port:{2} is avaliable !\33[0m'.format(env,host,port))
    except Exception as e:
        print ('\033[5;1;33mWarning: \33[0m\033[1;31m{0} ip:{1} port:{2} is not avaliable !\33[0m'.format(env,host,port))
    finally:
        conn.close()
        
def windows_conn_scan(env,host,port):
    conn=socket(AF_INET,SOCK_STREAM)
    try:
        conn.settimeout(5)
        conn.connect((host,port))
        printGreen ('IP:%s PORT:%s is avaliable !\n'%(host,port))
    except Exception as e:
        printRed ('IP:%s PORT:%s is not avaliable !\n'%(host,port))
    finally:
        conn.close()        

        
def main(env,host,port):
    
    if platform.system()=='Linux':
        linux_conn_scan(env,host,port)
    elif platform.system()=='Windows':
        std_out_handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
        def set_cmd_text_color(color, handle=std_out_handle):
            Bool = ctypes.windll.kernel32.SetConsoleTextAttribute(handle, color)
            return Bool 
        #reset white
        def resetColor():
            set_cmd_text_color(FOREGROUND_RED | FOREGROUND_GREEN | FOREGROUND_BLUE)
        def printGreen(mess):
            set_cmd_text_color(FOREGROUND_GREEN)
            sys.stdout.write(mess)
            resetColor()
        def printRed(mess):
            set_cmd_text_color(FOREGROUND_RED)
            sys.stdout.write(mess)
            resetColor()
        windows_conn_scan(env,host,port)
    else:
        pass        
if __name__=='__main__':
    portconf = ConfigParser.ConfigParser()   
    portconf.read('./conf/port_conf.ini')  
    p_conf=portconf.items(env)
    for ip in p_conf:
        if ip[0][len(ip[0])-2:len(ip[0])].lower()=='ip':
            print ('')
            ip_temp=ip[1].split(' ')
            n=ip[0].rfind('_')
            for port in p_conf:
                if port[0] == ip[0][0:n]+'_port':
                    port_temp=port[1].split(' ')
                    ip_port=itertools.product(ip_temp,port_temp)
                    for i in ip_port:
                        t_temp=(ip[0][0:n].upper(),i[0],int(i[1]))
                        main(*t_temp)  

        
#import urllib
#import os
#url = "http://www.baidu.com"
#try:
#    status = urllib.urlopen(url).code
#    print status
#except:
#    print {'result': 'false', 'msg': 'URL cannot access'}        