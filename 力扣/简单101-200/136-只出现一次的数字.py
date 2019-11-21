# -*- coding:utf-8 -*-
# @Author  : Clint

a = [3, 5, 7, 4, 3, 7, 4]


def singleNumber(nums):
    b = []
    for i in nums:
        if i not in b:
            b.append(i)
        else:
            b.remove(i)
    return b[0]


print(singleNumber(a))

