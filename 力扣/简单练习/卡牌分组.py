# !D:/Code/python
# -*- coding:utf-8 -*-
# @Author : Clint
# @Question :


# 暴力算法
def hasGroupsSizesX(deck):
    from collections import Counter  # 内置计数器函数
    count = Counter(deck)
    n = len(deck)
    for X in range(2, N + 1):
        if N % X == 0:
            if all(c % X == 0 for c in count.values()):  # all() 函数用于判断给定的可迭代参数 iterable 中的所有元素是否都为 TRUE
                return True

    return False


# 最大公约数
def hasGroupsSizesX(deck):
    from collections import Counter  # 内置计数器函数
    from functools import reduce
    from math import gcd  # 内置求最大公约数

    counts = Counter(deck).values()
    return reduce(gcd, counts) >= 2
