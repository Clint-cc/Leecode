# -*- coding:utf-8 -*-
# @Author  : Clint


def plusone(digits):
    n = 0
    a = []
    for i in digits:
        n = n*10+int(i)
    for j in str(n+1):
        a.append(int(j))
    return a


print(plusone([1, 2, 3]))
