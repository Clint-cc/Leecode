# !D:/Code/python
# -*- coding:utf-8 -*-
# @Author : Clint
# @Question : 输入一个字符串，打印出该字符串中字符的所有排列。
#             你可以以任意顺序返回这个字符串数组，但里面不能有重复元素。


def permutation(s):
    if len(s) == 1:
        return [s]
    res = []
    for i, x in enumerate(s):
        n = s[:i] + s[i + 1:]
        for y in permutation(n):
            res.append(x + y)

    return list(set(res))


print(permutation('aac'))
