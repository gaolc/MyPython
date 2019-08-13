##问题1：如何修改以下的Python代码，使得下面的代码调用类A的show方法？
class A(object):
    def show(self):
        print 'base show'
        
class B(A):
    def show(self):
        print 'derived show'
        
obj=B()
obj.show()

#答: 这道题的考点是类的继承，只要通过class方法指定类对象就可以了，补充如下代码：
obj.__class__=A
obj.show()

##问题2：如何修改以下Python代码，使得代码能够运行？
class A(object):
    def __init__(self,a,b):
        self.__a=a
        self.__b=b
    def myprint(self):
        print "a=",self.__a ,"b=",self.__b

a1=A(10,20)
a1.myprint()
a1(80)

#答： 此题考查的是方法对象，为了能让对象实例能别直接调用需要实现call方法
class A(object):
    def __init__(self,a,b):
        self.__a=a
        self.__b=b
    def myprint(self):
        print "a=",self.__a ,"b=",self.__b
    def __call__(self,num):
        print 'call:',num + self.__a
        
        
##问题3：下面代码输出是什么
class B(object):
    def fn(self):
        print "B fn"
    def __init__(self):
        print "B INIT"

class A(object):
    def fn(self):
        print "A fn"
    def __new__(cls,a):
        print "NEW",a
        if a>10:
            return super(A,cls).__new__(cls)
        return B()
    def __init__(self,a):
        print "INIT",a
a1=A(5)
a1.fn()
a2=A(20)
a2.fn()

#答：此题考查的是new和init 的用法
>>> a1=A(5)
NEW 5
B INIT
>>> a1.fn()
B fn
>>> a2=A(20)
NEW 20
INIT 20
>>> a2.fn()
A fn

##问题4：下面这段代码输出什么
ls=[1,2,3,4]
list1=[i for i in ls if i>2]
print list1

list2=[i*2 for i in ls if i>2 ]
print list2

dic1={x:x**2 for x in(2,4,6)}
print dic1

dic2={x:'item'+str(x**2) for x in (2,4,6)}
print (dic2)

set1={x for x in 'hello world' if x not in 'low level'}
print (set1)

#答：
>>> print list1
[3, 4]
>>> print list2
[6, 8]
>>> print (dic1)
{2: 4, 4: 16, 6: 36}
>>> print (dic2)
{2: 'item4', 4: 'item16', 6: 'item36'}
>>> print (set1)
{'h', 'r', 'd'}

##问题5： 如何使用一行代码交换两个变量
a=8
b=0
#答： (a,b)=(b,a)

##问题6：如何添加代码，使得没有定义的方法都调用mydefault方法
class A(object):
    def __init__(self,a,b):
        self.a1=a
        self.b1=b
        print 'init'
    def mydefault(self):
        print 'default'
    def __getattr__(self,name):
        return self.mydefault
a1=A(10,20)
a1.fn1()
a1.fn2()
a1.fn3()

>>> a1=A(10,20)
init
>>> a1.fn1()
default
>>> a1.fn2()
default
>>> a1.fn3()
default

#答：此题考查的是python 的默认方法。只有当没有定义的方法调用时，才调用getattr 。当fn1 方法传入参数时，我们可以给mydefault 方法增加一个*args 不定参数来兼容。
class A(object):
    def __init__(self,a,b):
        self.a1=a
        self.b1=b
        print 'init'
    def mydefault(self,*args):
        print 'default' +str(args[0])
    def __getattr__(self,name):
        return self.mydefault
a1=A(10,20)
a1.fn1(33)
a1.fn2('hello')
a1.fn3(10)

>>> a1.fn1(33)
default33
>>> a1.fn2('hello')
defaulthello
>>> a1.fn3(10)
default10

##问题7: 一个包里有三个模块。mod1.py , mod2.py , mod3.py 但是使用from demopack import * 导入模块时如何保证只有mod1 mod3 被导入了
#答：
在包中添加init.py 文件，并在文中添加
__all__=['mod1','mod3']

##问题8：求两个列表的交集、差集、并集
a=[1,2,3,4]
b=[4,3,5,6]
jj1=[i for i in a if i in b ]
jj2=list(set(a).intersection(set(b)))
bj1=list(set(a).union(set(b)))
cj1=list(set(a).difference(set(b)))
cj2=list(set(b).difference(set(a)))

##问题9: 生成0-100的随机数
>>> import random 
>>> random.random()       #生成0-1之间的随机小数
0.744482129922733
>>> 100*random.random()
60.64393457666088
>>> random.choice(range(0,101))     #随机整数
97
>>> random.randint(1,100)           #随机整数
51

## 一行代码实现1-100之和
sum(range(1,101))

##如何在一个函数内部修改全局变量 ，利用global修改全局变量
a=5
def fn():
    global a
    a=4 
fn()

##列出5个python标准库
os
sys
math
re
datetime

##字典如何删除键和合并两个字典
#del 和 update 方法
>>> dic={'name':'glc','age':27}
>>> del dic['name']     #删除键
>>> dic
{'age': 27}

>>> dic2={'name':'erchen'}
>>> dic.update(dic2)     #update 合并字典
>>> dic 
{'age': 27, 'name': 'erchen'}

## fun (*args,**kwargs) 中的*args,**kwargs 什么意思
#*args和**kwargs 主要用于函数定义，你可以将不定数量的参数传递给一个函数，这里的不定的意思是：预先不知道函数使用者会会传递多少个参数给你，*args 是用来发送一个非键值对的可变数量的参数列表给一个函数
def demo(args_f,*args_v):
    print '1: ' ,args_f
    for i in args_v :
        print i
        
demo('a','b','c','d')
#**kwargs 允许将不定长度的键值对作为参数传递给一个函数，如果你想在一个函数里面处理一个带名字的参数，你应该使用**kwargs
def demo(**args_v):
    for i,v in args_v.items():
        print i, v
    
demo(name='glc')
>>>OUT:  name':'glc'

###################
import json
s = json.loads('{"name":"test", "type":{"name":"seq", "parameter":["1", "2"]}}')
print s
print s.keys()
print s["name"]
print s["type"]["name"]
print s["type"]["parameter"][1]


#whit open('foo.out') as f:
#python f.read()  f.readline()  f.readlines() 区别
#f.read()  每次读取整个文件,用于将文件内容放到一个字符串变量中
#f.readline() 每次只读取一行，通常比 .readlines() 慢得多。仅当没有足够内存可以一次读取整个文件时，才应该使用 .readline()
#f.readlines()  每次读取整个文件,自动将文件内容分析成一个行的列表


#enumerate()函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中
>>> seasons = ['Spring', 'Summer', 'Fall', 'Winter']
>>> for x,y in enumerate(seasons):
...     print x,y 
... 
0 Spring
1 Summer
2 Fall
3 Winter

#Python 字典的遍历
In [8]: a={'a':'1','b':'2','c':'3'}

In [9]: for k in a.keys():
   ...:     print (k+':'+a[k])
   ...:
a:1
b:2
c:3

In [11]: for value in a.values():
    ...:     print (value)
    ...:
    ...:
1
2
3

In [12]: for k,v in a.items():
    ...:     print (k,v)
    ...:
a 1
b 2
c 3

##计算重复单词个数
a='aabbbbccD'
def duplicate_count(text):
    text=text.lower()
    texts=set(text)
    lists=[]
    for i in texts:
        numbers=text.count(i)
        if numbers !=1:
            lists.append(numbers)
    return len(lists)
l=duplicate_count(a)
print (l)
#OUT: 3

#
n=[{'name':'glc'},{'name':'erchen'},{'name':'wuhan'}]

def namelist(names):
    if len(names)>1:
        return '{} & {}'.format(', '.join(i['name'] for i in names[:-1]),names[-1]['name'])
    elif len(names)==1:
        return names[0]['name']
    else:
        return ''
    
print (namelist(n))  
#OUT: glc, erchen & wuhan

#enumerate()
bag=[1,2,3,4]
for k,v in enumerate(bag):
    print (k,v)
####################
def binary():
    return 1,2,3
  
a,b,c=binary()

#笛卡尔积
#笛卡尔乘积是指在数学中，两个集合X和Y的笛卡尓积（Cartesian product），又称直积，表示为X×Y，第一个对象是X的成员而第二个对象是Y的所有可能有序对的其中一个成员 [3]  。
#假设集合A={a, b}，集合B={0, 1, 2}，则两个集合的笛卡尔积为{(a, 0), (a, 1), (a, 2), (b, 0), (b, 1), (b, 2)}
from itertools import product
for x,y,z in product(['a','b','c'],['d','e','f'],['m','n']):
    print(x,y,z)
len(list(product(['a','b','c'],['d','e','f'],['m','n'])))

#enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标
#enumerate(sequence, [start=0])
>>> list(enumerate(items))
[(0, 'zero'), (1, 'one'), (2, 'two'), (3, 'three')]

#format 进制转换
#10进制转换为其他进制
>>> "int:{0:d} ; hex:{0:x} ; oct:{0:o} ; bin:{0:b}".format(10)
#16进制转换为其他进制
>>> "int:{0:d} ; hex:{0:x} ; oct:{0:o} ; bin:{0:b}".format(0xa,'x')
'int:10 ; hex:a ; oct:12 ; bin:1010'
#8进制转换为其他进制
>>> "int:{0:d} ; hex:{0:x} ; oct:{0:o} ; bin:{0:b}".format(0o12,'o')
'int:10 ; hex:a ; oct:12 ; bin:1010'
#2进制转换为其他进制
>>> "int:{0:d} ; hex:{0:x} ; oct:{0:o} ; bin:{0:b}".format(0b1010,'b')
'int:10 ; hex:a ; oct:12 ; bin:1010






