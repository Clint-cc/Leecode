# !D:/Code/python
# -*- coding:utf-8 -*-
# @Author : Clint
# @Question : 给定无序整数数组，找到最长上升子序列的长度
# @Thinking : 注：子序列和子串不同；子序列可以不连续

class Solution:
    def lengthOfLIS(self, nums):
        dp = [1 for i in range(len(nums))]
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)


s = Solution()
print(s.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))
