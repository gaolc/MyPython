import time
import os 
from multiprocessing import Pool
 

def get_time(func):
    def wrapper(*args, **kwargs):
        startTime = time.time()
        func(*args, **kwargs)
        endTime = time.time()
        ms = (endTime - startTime)
        print("This progream the time of using is %d s" %ms)
    return wrapper

def ana_log (data_file):
    f_name=data_file.split('/')[-1]
    write_file_open=open('./result/'+f_name,'a')
    with open(data_file) as file:
        for line in file:
            if line[78:89] == r'sendSymbol:':
                data_l = line[90:len(line)-2]
                Line_list=data_l.split(', ')
                dic_={'-1':'','875':'','1010':'','22':'','25':''}
                for i in Line_list:
                    n=i.find('=')
                    dic_[i[0:n]]=i[n+1:]
                print_patter='%s,%s,%s,%s,%s,\n'%(dic_['-1'],dic_['875'],dic_['1010'],dic_['22'],dic_['25'])
                write_file_open.write(print_patter)                     		
    write_file_open.close()

@get_time
def main():
    files = [r'data/' + i for i in os.listdir('data') if  os.path.isfile(r'data/' + i) ]
    pool = Pool(5)
    for file in files:
        pool.apply_async(ana_log, (file,))
    pool.close()
    pool.join()
    
if __name__=='__main__':
    main()