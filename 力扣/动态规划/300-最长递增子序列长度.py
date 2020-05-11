# !D:/Code/python
# -*- coding:utf-8 -*-
# @Author : Clint
# @Question : 
# @Thinking :

class Solution:
    def lengthOfLIS(self, nums):
        dp = [0 for i in range(len(nums))]
        m = 1
        for i in range(0, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

            #         max_l += 1
            #     j -= 1
            # max_l = 1
            # j = i
            # while j > 0:
            #     if nums[i] > nums[j-1]:
            #         max_l += 1
            #     j -= 1
            m = max(m, max_l)
        return m


s = Solution()
print(s.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))
