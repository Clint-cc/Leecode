# !D:/Code/python
# -*- coding:utf-8 -*-
# @Author : Clint
# @Question : 求base的exponent次方。不得使用库函数，同时不需要考虑大数问题。


def myPow(x, n):
    if n > 0:
        return x ** n
    else:
        return 1 / (x ** (-n))


print('%.5f' % myPow(2.00000, 10))
