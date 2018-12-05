1.函数的对象特征
函数对象有3个特征
身份，类型，值
>>> def func():
...     print ("Hi,I'm fun")
... 
>>> print (type(func))
<type 'function'>
>>> print (func)
<function func at 0x7f9ba7d99410>
>>> print(id(func))
140306512712720
函数 func 有类型：它的类型是class
函数 func 有值：有内存的地址
函数 func 有身份：140306512712720
2.函数可以赋值
>>> def func1():
...     print ("Hi,I'm fun")
... 
>>> func2=func1
>>> print (func1)
<function func1 at 0x7f9ba7d996e0>
>>> print (func2)
<function func1 at 0x7f9ba7d996e0>
>>> func2()
Hi,I'm fun

3.函数可以当参数传递
def fun():
    print ('Hello,I am func')
    
def another_fun(func):
    print ('Hello,I am another func')
    func()
    
another_fun(fun)
#out: Hello,I am another func
#out：Hello,I am func

4.返回值也可以是函数
Python 返回值已经设置的比较灵活了，比如可以返回单个，也可以返回多个，函数也可以当返回值返回，小伙伴不要惊讶，你经常玩的闭包，装饰器就是这样玩的
def show_name(name):
    def inner(age):
        print ('My name is : {0}'.format(name))
        print ('My age is : {0}'.format(age))
    return inner
   
f=show_name('glc')
f('18')
#out: My name is : glc
#out: My age is : 29
我们定义了一个show_name,这个函数的返回值是一个函数。也就是说变量f就是返回的inner函数。所以我们就可以用f('18')来执行函数

5.函数可以在字典中使用
函数可以在容器中使用，比如列表，字典里面像参数一样使用
def show_apple(price):
    print ('This is apple.price is:',price)
def show_orange(price):
    print ('This is orange.price is :',price)
switch={'apple':show_apple,'orange':show_orange}
def process(yoour_choice,price):
    switch[yoour_choice](price)
process('apple',5)
process('orange',6)
#out: ('This is apple.price is:', 5)
#out: ('This is orange.price is :', 6)