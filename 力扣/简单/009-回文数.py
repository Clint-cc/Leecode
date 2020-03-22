# !D:/Code/python
# -*- coding:utf-8 -*-
# @Author : Clint


def reverse_num(num):
    initial_num = num
    if num > 0:
        a = len(str(num))  # a=3
        n = len(str(num)) - 1  # n=2
        sum = 0
        while n >= 0:
            s = num // 10 ** n
            s = s * 10 ** (a - 1 - n)
            num = num % 10 ** n
            sum += s
            n -= 1
        if sum == initial_num:
            return True
        else:
            return False
    else:
        return False


print(reverse_num(-101))
