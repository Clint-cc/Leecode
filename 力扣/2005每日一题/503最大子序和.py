# !D:/Code/python
# -*- coding:utf-8 -*-
# @Author : Clint
# @Question : 
# @Thinking : 可以理解为动态规划


class Solution:
    def maxSubArray(self, nums):
        if not nums:
            return 0
        for i in range(1, len(nums)):
            # nums[i] = max(nums[i], nums[i] + nums[i - 1])
            nums[i] += max(nums[i - 1], 0)
        return max(nums)


s = Solution()

print(s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
# [-2,1,-2,4,3,]
