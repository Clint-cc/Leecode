# -*- coding:utf-8 -*-
# @Author  : Clint

a = [1, 3, 5, 0, 0, 0]
b = [2, 4, 6]
c = []


def merg(num1, m, num2, n):
    c = sorted(num1[0:m]+num2)[0:m+n]
    return c


print(merg(a, 3, b, 3))