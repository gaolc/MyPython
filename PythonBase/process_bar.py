#!/usr/bin/env python
import sys
import time
max_n=50
print ('start')
for i in range(1,51):    
    progress_bar = '[' + '>' * i + '-' * (max_n-i) + ']' + '%.2f' % ((i/float(max_n))*100) +' '+ '%' + '\r'
    time.sleep(1)
    if  i<max_n:
        sys.stdout.write(progress_bar)
    else:
        sys.stdout.write(progress_bar)
        print ('')
    sys.stdout.flush()