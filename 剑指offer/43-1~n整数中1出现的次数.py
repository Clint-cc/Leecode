# !D:/Code/python
# -*- coding:utf-8 -*-
# @Author : Clint
# @Question : 输入一个整数 n ，求1～n这n个整数的十进制表示中1出现的次数。


def countDigitOne(n):
    count = 0
    for i in range(1, n + 1):
        tmp_str = str(i)
        count += tmp_str.count('1')
    return count


print(countDigitOne(122))
