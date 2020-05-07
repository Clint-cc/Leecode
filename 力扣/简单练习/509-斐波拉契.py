# -*- coding:utf-8 -*-
# @Author  : Clint

#  0 1 1 2 3 5 8 13 21 34 55 89 ...
'''
fibonaccis = []
def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


for i in range(1, 10):
    fibonaccis.append(fibonacci(i))

print(fibonaccis)
'''


def fib(N):
    i = 0
    j = 1
    if N == 0:
        return 0
    while N >= 2:
        i, j = j, i + j
        N -= 1

    return j


print(fib(5))
