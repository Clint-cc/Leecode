# !D:/Code/python
# -*- coding:utf-8 -*-
# @Author : Clint
# @Question :


def compressString(s):
    count = 1
    res = ''
    res += s[0]
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            res += str(count)
            res += s[i]
            count = 1
    res += str(count)
    if len(res) >= len(s):
        return s
    return res


print(compressString('abcccccaaavbvvbvvvvrrrrraaaaaabbbb'))
