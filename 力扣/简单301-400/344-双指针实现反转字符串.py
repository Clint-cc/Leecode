# -*- coding:utf-8 -*-
# @Author  : Clint

# 对双指针的理解
strs = ['w', 'e', 'a', 'r', 'y']


def reverseString(s):
    i = 0
    j = len(s)-1
    while i < j:
        s[i], s[j] = s[j], s[i]
        i += 1
        j -= 1
    return s


print(reverseString(strs))