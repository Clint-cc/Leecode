# !D:/Code/python
# -*- coding:utf-8 -*-
# @Author : Clint
# @Question :


def strToint(str):
    s = str.strip()
    if not s or s[0] not in '+-0123456789':
        return 0
    tmp = s[0]
    for i in range(1, len(s)):
        if s[i] in '0123456789':
            tmp += s[i]
        else:
            break
    if tmp == '+' or tmp == '-':
        return 0

    ints = int(tmp)
    if ints < -2 ** 31:
        return -2 ** 31
    if ints > 2 ** 31 - 1:
        return 2 ** 31 - 1
    return ints
