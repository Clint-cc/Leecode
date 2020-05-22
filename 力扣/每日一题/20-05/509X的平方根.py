# !D:/Code/python
# -*- coding:utf-8 -*-
# @Author : Clint
# @Question : 实现int sqrt(int x)函数。计算并返回x的平方根，结果只保留整数的部分，其中x是非负整数。
# @Thinking : 二分查找、暴力、牛顿法、内置函数


class Solution:
    def mySqrt(self, x):
        #
        left, right = 0, x
        while left <= right:
            mid = (left + right) // 2
            if mid ** 2 == x:
                return mid
            elif mid ** 2 > x:
                right = mid - 1
            else:
                left = mid + 1
        return right


s = Solution()
print(s.mySqrt(0))
