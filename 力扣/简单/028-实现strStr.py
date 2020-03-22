# !D:/Code/python
# -*- coding:utf-8 -*-
# @Author : Clint


def strStr(haystack, needle):
    if not haystack or not needle:
        return 0
    else:
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:(i + len(needle))] == needle:
                return i
        return -1


print(strStr('aaaaa', 'bba'))
