# !D:/Code/python
# -*- coding:utf-8 -*-
# @Author : Clint


def containsDuplicate(nums):
    b = []
    for i in nums:
        if i not in b:
            b.append(i)
        else:
            return True
            break
    return False


print(containsDuplicate([1, 2, 3, 4]))
