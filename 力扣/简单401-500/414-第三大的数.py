# -*- coding:utf-8 -*-
# @Author  : Clint


def thirdmax(nums):
    n = len(nums)
    if n <= 3:
        return min(nums)
    else:
        if len(set(nums)) < 3:
            return max(nums)
        else:
            return list(set(nums))[-3]


print(thirdmax([3,2,1,1,4,0,9,11,898,765,242,11,45,232,655]))