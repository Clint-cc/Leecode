# !D:/Code/python
# -*- coding:utf-8 -*-
# @Author : Clint


def trailingZeroes(n):
    k = 0
    while n >= 5:
        k += n % 5
        n = n // 5
    return k


print(trailingZeroes(24))
