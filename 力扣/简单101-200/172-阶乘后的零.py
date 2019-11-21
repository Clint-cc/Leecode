# -*- coding:utf-8 -*-
# @Author  : Clint


def trailingZeroes(n):    # 24  ---->   2 5   10   20    15
    k = 0
    while n >= 5:
        k += n % 5
        n = n // 5
    return k


print(trailingZeroes(24))
