# !D:/Code/python
# -*- coding:utf-8 -*-
# @Author : Clint
# @Question : 生成每种字符都是奇数个的字符串,字符只是小写英文字母


def generateTheString(n):
    """
    :type n: int
    :rtype: str
    """
    if n % 2 != 0:
        return n * 'x'
    else:
        return (n - 1) * 'x' + 'y'


print(generateTheString(3))
