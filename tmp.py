# !D:/Code/python
# -*- coding:utf-8 -*-
# @Author : Clint
# @Question : 临时测试文件

def sumNums(n):
    sum = n
    if n == 1:
        return 1
    sum += sumNums(n - 1)
    return sum


print(sumNums(50))
