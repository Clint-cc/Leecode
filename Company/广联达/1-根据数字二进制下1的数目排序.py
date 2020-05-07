# !D:/Code/python
# -*- coding:utf-8 -*-
# @Author : Clint
# @Question :

# 方法一：
def sortByBits(arr):
    res = []
    d = {}
    for i in arr:
        t = str(bin(i))
        n = t.count('1')
        if n not in d:
            d[n] = []
        d[n].append(i)

    for i in sorted(d):
        res += sorted(d[i])
    return res


# 方法二
def sortByBits(arr):
    return sorted(arr, key=lambda x: (bin(x).count('1'), x))


print(sortByBits([1, 3, 5, 7, 8]))
