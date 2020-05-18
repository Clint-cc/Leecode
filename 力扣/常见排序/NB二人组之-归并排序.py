# !D:/Code/python
# -*- coding:utf-8 -*-
# @Author : Clint
# @Question : 
# @Thinking : -----如下：------
'''
    1.将列表越分越小，直至分成一个元素；
　　2.把一个元素理解成是是有序的；
　　3.合并：将两个有序列表归并，列表越来越大；
'''


# import sys
# sys.setrecursionlimit(1000)


def One_Merge(nums, low, mid, high):  # 一次归并
    i, j, lda = low, mid + 1, []

    while i <= mid and j <= high:
        if nums[i] < nums[j]:
            lda.append(nums[i])
            i += 1
        else:
            lda.append(nums[j])
            j += 1
    while i <= mid:
        lda.append(nums[i])
        i += 1
    while j <= high:
        lda.append(nums[j])
        j += 1
    nums[low:high + 1] = lda


def Merge_Sort(nums, low, high):  # 合并排序 O(nlogn)
    if low < high:
        mid = (low + high) // 2
        Merge_Sort(nums, low, mid)  # 递归实现
        Merge_Sort(nums, mid + 1, high)
        One_Merge(nums, low, mid, high)


nums = [7, 1, 3, 4, 8, 0, 9, 5, 6, 2]
Merge_Sort(nums, 0, len(nums) - 1)
print(nums)
