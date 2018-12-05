#!/usr/bin/python 

def main (n,d):
    if d.get(n) is not None:
        return d[n]
    else:
        if n==0:
            d[n]=0
        elif n==1:
            d[1]=1
        elif n==2:
            d[2]=2
        else:
            d[n]= main(n-1,d) + main(n-2,d)
        return d[n]
        
         
if __name__=="__main__":
    m=raw_input("Pleas in put a number :")
    t={}
    print main(m,t)
       