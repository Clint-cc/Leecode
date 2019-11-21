# -*- coding:utf-8 -*-
# @Author  : Clint

# 递归方法：
'''
def adddigits(num):
    if num >= 10:
        sum = 0
        while num > 0:
            sum += num % 10         # 1238
            num = num // 10

        if sum >= 10:
            adddigits(sum)

        else:
            return sum

    else:
        return num
'''

# 找规律方法：
def adddigits(num):
    if num <= 9:
        return num
    else:
        return num % 9


print(adddigits(10))
