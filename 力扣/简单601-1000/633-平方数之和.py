# -*- coding:utf-8 -*-
# @Author  : Clint
import math

'''
def judgeSquareSum(c):          # 时间复杂度太高
    n = int(math.sqrt(c))
    for i in range(0, n+1):
        for j in range(n, -1, -1):
            if i**2+j**2 == c:
                # print(i, j)
                return True
    return False    #  #
'''


def judgeSquareSum(c):
    a = 0
    b = int(math.sqrt(c))
    while a <= b:
        if a ** 2 + b ** 2 == c:
            return True
        elif a ** 2 + b ** 2 > c:
            b -= 1
        else:
            a += 1
    return False


print(judgeSquareSum(6))