# !D:/Code/python
# -*- coding:utf-8 -*-
# @Author : Clint
# @Question : 排序(正序)
# @Thinking : 列表分为有序区和无序区，最初有序区只有一个元素，每次从无序区选择一个元素，插入到有序区
#             的位置，直到无序区变空


def Insert_Sort(nums):
    n = len(nums)
    for i in range(1, n):
        tmp = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > tmp:
            nums[j + 1], nums[j] = nums[j], tmp
            j -= 1
    return nums


print(Insert_Sort([6, 8, 7, 1, 3, 4, 9, 5, 0, 2]))
