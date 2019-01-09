#!/usr/bin/env python3
# - * - coding: UTF-8 - * -


"""
a,b = 0,1
while b < 1000:     #while语句
    print(b, end=',')
    a,b = b,a+b
    

x= int(input("Please enter an integer: "))
if x < 0:             #if语句
    x = 0
    print('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')



a = ['cat','window','defenestrate']
for x in a:     #for语句
    print(x, len(x))

a = ['cat','window','defenestrate']
for x in a[:]:     #创建一个切片副本，在迭代过程中修改迭代序列不安全
    if len(x) >6:
        a.insert(0,x)
print(a)

for i in range(5): #range(起始点，终止点，步进)创建等差级数链表
    print(i)
list(range(5))  #range创建的是链表，不能直接用print，可用list将其转化为一个列表
print(list(range(5)))

a = ['mary','had','a','little','lamb']
for i in range(len(a)):   #创建迭代链表索引
    print(i, a[i])


for n in range(2,100):
    for x in range(2,n):
        if n % x == 0:
            print(n, 'equals', x, "*", n//x)
            break    #求素数，break用于跳出最近的一级 for 或 while 循环。
    else:
        print(n, 'is a prime number')


for num in range(2,10):
    if num % 2 == 0:
        print('found an even number', num)
        continue      #用于循环继续执行下一次迭代,后面的不管了
    print('found a number', num)

for num in range(2,10):  #上面这个也可以这样表达
    if num % 2 == 0:
        print('found an even number', num)
    elif num % 2 != 0:
        print('found a number', num)


while True:
    pass  #什么也不做，等待Ctr+C退出



def fib(n):  #不带返回值，实际返回None
    """函数的文档字符串：print a Fibonacci series up to n."""
    a,b = 0,1
    while a < n:
        print(a, end=' ')
        a,b = b,a+b
fib(1000)
print('\n',fib(1000))

def fib2(n):
    """函数的文档字符串：print a Fibonacci series up to n."""
    result = []
    a,b = 0,1
    while a < n:
        result.append(a)
        a,b = b,a+b
    return result
print('\n',fib2(1000))
"""


    
