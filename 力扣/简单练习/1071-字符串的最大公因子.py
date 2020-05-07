# !D:/Code/python
# -*- coding:utf-8 -*-
# @Author : Clint
# @Question : 对于字符串S和T，只有在S=T+...+T（T与自身连接1次或多次）时，我们才认定“T能除尽S”。


# 思路：最大公约数
def gcdOfStrings(str1, str2):
    a = len(str1)
    b = len(str2)
    if a == 0 or b == 0 or str1 + str2 != str2 + str1:
        return ""
    if a > b:
        a, b = b, a
    while a != 0:
        a, b = b % a, a
    return str1[0:b]


print(gcdOfStrings("ABC", "ABCABC"))
