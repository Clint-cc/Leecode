# !D:/Code/python
# -*- coding:utf-8 -*-
# @Author : Clint
# @Question : 排序(正序)
# @Thinking : 一趟遍历最小的数，放到第一个位置，再一趟遍历放到第二个位置，...，知道排序完成


def Select_Sort(nums):
    n = len(nums)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if nums[j] < nums[min_idx]:
                min_idx = j
        nums[i], nums[min_idx] = nums[min_idx], nums[i]
    return nums


print(Select_Sort([0, 1, 3, 4, 8, 7, 9, 5, 6, 2]))
