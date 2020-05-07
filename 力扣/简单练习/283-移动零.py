# -*- coding:utf-8 -*-
# @Author  : Clint


def moveZeroes(nums):
    for i in range(len(nums)):
        if nums[i] == 0:

            nums.remove(0)
            nums.append(0)
        else:
            continue
    return nums


print(moveZeroes([2, 3, 0, 0, 1, 0]))
