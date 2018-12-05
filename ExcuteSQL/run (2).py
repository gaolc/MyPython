#!/usr/bin/python 
# - *- coding: utf-8 -*-
import os
import sys
import time
import datetime
import platform
import ConfigParser
from subprocess import Popen, PIPE

# python test.py arg1 arg2 arg3
# sys.argv[0] 表示脚本名。
# sys.argv[1:] 过滤掉脚本名
DIR_DATE=[]
ENV_LIST=[]
dir_date=sys.argv[1]
file_no_list=sys.argv[2:]

def ini_env():
    global ENV_LIST
    dbconf = ConfigParser.ConfigParser()
    dbconf.read('./conf/dbconf.ini') 
    env_d=dict(dbconf.items('env_list'))
    for i in env_d.values():
        sql_env=dbconf.get(i,'username')+'/'+dbconf.get(i,'password')+'@'+dbconf.get(i,'IP')+':'+dbconf.get(i,'port')+'/'+dbconf.get(i,'service_name')
        proc=Popen(["sqlplus", "-S",sql_env ], stdout=PIPE, stdin=PIPE, stderr=PIPE)
        sql='select 1 from dual ;'
        proc.stdin.write(sql)
        (out, err) = proc.communicate()
        if out.split()[0]=='1' and out.split()[2]=='1':
            print ('Database initialize sucess :{0}!'.format(sql_env))
        else:
            print ('ERROR : Database initialize fail {0} !'.format(sql_env))
            sys.exit(1)       
        if len(err) != 0:
            print (err)
            print ('ERROR : Database initialize fail {0} !'.format(sql_env))
            sys.exit(1)
        ENV_LIST.append(sql_env)

        
def get_dirlist(today):
    global DIR_DATE
    dir1=os.listdir('.')
    for d in dir1:
        if d.find('-'):
            k=d.find('-')
            d1=d[0:k]
            d2=d[k+1:]
        if d1 <= today and today <= d2 :
            DIR_DATE.append(d) 


def excute_sql(dir,sql_list,env):
    if len(sql_list)==0:
        print ('Nothing to do ,it will to exit!')
        sys.exit(0)
    for env_n in env:        
        proc =Popen(["sqlplus", "-S", env_n], stdout=PIPE, stdin=PIPE, stderr=PIPE)
        for file in sql_list:
            time_now=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            sql='@'+dir+'/'+file
            proc.stdin.write(sql)
            (out, err) = proc.communicate()
            with open('excute.log','a') as f:
                print  ('{0}'.format('#'*50))
                print >> f, ('{0}'.format('#'*50))
                print  ('{0} Info: start to excute [{1}] .'.format(time_now,file))
                print >> f, ('{0} Info: start to excute [{1}] .'.format(time_now,file))
                print  ('{0} Info: excute result is [{1}] '.format(time_now,out))
                print >> f, ('{0} Info: excute result is [{1}] '.format(time_now,out))
                with open('Error.log','a') as err_f:
                    if len(err)!=0:
                        print  ('{0} Error: excute {1}'.format(time_now,file)) 
                        print >> err_f, ('{0} Error: excute {1}'.format(time_now,file))
                        print  ('{0} Error: {1}'.format(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),err))
                        print >> err_f, ('{0} Error: {1}'.format(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),err)) 
 

def get_files_list(dir,fileno):
    if len(dir)>=2:
        print ('ERROR: Multiple dir have been found : {0} !'.format(dir))
        print ('There must be only one directory here !')
        sys.exit(1)
    elif len(dir)==0:
        print ('Error : Can not find the directory contain [{0}] .'.format(dir_date))
        sys.exit(1)
    else:
        exc_list=[]
        dir_1=dir[0]
        for i in os.listdir(dir_1):
            k=i.find('-')
            if  i[0:k] in fileno:
                exc_list.append(i)
    return exc_list
    
def running():
    ini_env()
    get_dirlist(dir_date)
    FILES_SQL=get_files_list(DIR_DATE,file_no_list)
    excute_sql(DIR_DATE[0],FILES_SQL,ENV_LIST)

if __name__=='__main__':
    running()
