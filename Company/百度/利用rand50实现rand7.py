# !D:/Code/python
# -*- coding:utf-8 -*-
# @Author : Clint
# @Question : 函数random50能够产生1到50之间的随机数，如何利用random50实现出来random7；
# @Thinking : 如果是random10实现random7，那么当得到8-10，就继续调用，直到处于1-7，当random-n
#             的n比较大时，如50，则可以取余，1-49映射到1-7,50就继续调用；

def random50():
    s = [i for i in range(1, 51)]
    import random
    return random.choice(s)


def random7():
    num = random50()
    while num == 50:
        num = random50()
    return 1 + num % 7


print(random7())
