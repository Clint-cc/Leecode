# !D:/Code/python
# -*- coding:utf-8 -*-
# @Author : Clint
# @Question : 二维数组中的查找

# 暴力法
'''
class Solution:
    def findNumberIn2DArray(nums, target):
        if len(nums) ==0 or len(nums[0]) == 0:
            return False
        n = len(nums)
        m = len(nums[0])
        for i in range(n):
            for j in range(m):
                if nums[i][j] == target:
                    return True
        return False
'''


# 二叉树法
class Solution:
    def findNumberIn2DArray(nums, target):
        if len(nums) == 0 or len(nums[0]) == 0:
            return False
        n = len(nums)
        m = len(nums[0])

        row = 0
        column = m - 1
        while row < n and column >= 0:
            if nums[row][column] == target:
                return True
            elif nums[row][column] > target:
                column -= 1
            else:
                row += 1

        return False


print(Solution.findNumberIn2DArray([[1, 4, 7, 11, 15],
                                    [2, 5, 8, 12, 19],
                                    [3, 6, 9, 16, 22],
                                    [10, 13, 14, 17, 24],
                                    [18, 21, 23, 26, 30]
                                    ], 5))
