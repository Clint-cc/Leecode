# !D:/Code/python
# -*- coding:utf-8 -*-
# @Author : Clint


def isprime(num):
    import math
    n = int(math.sqrt(num))
    for i in range(2, n + 1):
        if num % i == 0:
            return False
    return True


def countPrime(num):
    count = 0
    a = []
    for i in range(2, num):
        if isprime(i):
            count += 1
            a.append(i)
    print(a)
    return count


print(countPrime(999983))
