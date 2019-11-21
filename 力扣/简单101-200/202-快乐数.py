# -*- coding:utf-8 -*-
# @Author  : Clint


def isHappy(n):  # n = 123   10  14  17  50  25  29  85  89  145  42  20   4  16  37 58  89
    summ = 0
    li = [n, ]
    while n != 1:
        while n != 0:
            n, b = divmod(n, 10)  # n除以10得到除数赋值给n，余数赋值给b
            summ += b ** 2
        if summ == 1:
            return True
        else:
            if summ not in li:
                li.append(summ)
                n = sum
                summ = 0
            else:
                return False


print(isHappy(19))
