# !D:/Code/python
# -*- coding:utf-8 -*-
# @Author : Clint
# @Question : 数组中的每个元素代表你在该位置可以跳跃的最大长度,判断你是否能够到达最后一个位置
# @Thinking : 尽可能到达最远位置（贪心）


class Solution:
    def canJump(self, nums):
        max_res = 0
        for i in range(len(nums)):
            if max_res >= i:
                max_res = max(i + nums[i], max_res)
        if max_res >= i:
            return True
        else:
            return False

s = Solution()
print(s.canJump([3, 2, 1, 0, 4]))
