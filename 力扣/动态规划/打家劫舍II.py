# !D:/Code/python
# -*- coding:utf-8 -*-
# @Author : Clint
# @Question : 房子排列成环的样子，相邻的房子不能同时被抢，求能抢到的最高金额
# @Thinking :

class Solution:
    def rob(self, nums):
        n = len(nums)
        if n == 1: return nums[0]
        return max(self.money(nums, 0, n - 2), self.money(nums, 1, n - 1))

    def money(self, nums, start, end):
        a, b = 0, 0
        res = 0
        for i in range(end, start - 1, -1):
            res = max(a, b + nums[i])
            b = a
            a = res
        return res


s = Solution()
print(s.rob([1, 2, 3, 1, 2]))
