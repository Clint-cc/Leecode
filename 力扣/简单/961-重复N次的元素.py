# -*- coding:utf-8 -*-
# @Author  : Clint


def repeateNs(li):
    for i in li:
        if li.count(i) == len(li) // 2:
            return i


print(repeateNs([5, 1, 5, 2, 5, 3, 5, 4]))
