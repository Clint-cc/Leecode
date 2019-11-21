# -*- coding:utf-8 -*-
# @Author  : Clint
x = [2, 2, 1, 1, 1, 2, 2]


def majorityElement(nums):
    dictt = {}
    for i in nums:
        if i not in dictt:
            pass
        else:
            dictt['i'] += 1
    print(dictt)


majorityElement(x)