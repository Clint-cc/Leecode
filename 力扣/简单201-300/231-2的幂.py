# -*- coding:utf-8 -*-
# @Author  : Clint


def isPowerOfTwo(n):
    x = 1
    while 2**x < n:
        x += 1
    if 2**x == n:
        return True
    else:
        return False


print(isPowerOfTwo(17))