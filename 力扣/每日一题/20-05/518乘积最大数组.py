# !D:/Code/python
# -*- coding:utf-8 -*-
# @Author : Clint
# @Question : 
# @Thinking :
from typing import List
import math


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums: return 0

        # [2,0,3,-2,4,-2]
        dp_max, dp_min = 1, 1
        res = -math.inf
        for i in range(len(nums)):
            if nums[i] < 0:
                dp_max, dp_min = dp_min, dp_max

            dp_max = max(dp_max * nums[i], nums[i])
            dp_min = min(dp_min * nums[i], nums[i])

            res = max(dp_max, res)
        return res


s = Solution()
print(s.maxProduct([2, 0, 3, -2, 4, -2]))
