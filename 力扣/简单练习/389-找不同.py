# !D:/Code/python
# -*- coding:utf-8 -*-
# @Author : Clint


def findthediff(s, t):
    n = len(s)
    while n:
        for i in t:
            if i in s:
                t = t.strip(i)
            else:
                continue
        n -= 1
    print(t)


findthediff("acdb", "abadc")
