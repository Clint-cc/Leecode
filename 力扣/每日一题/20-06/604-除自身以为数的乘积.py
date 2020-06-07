# !D:/Code/python
# -*- coding:utf-8 -*-
# @Author : Clint
# @Question : 
# @Thinking :
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # L, R = [0] * len(nums), [0] * len(nums)
        # res = []
        # n = len(nums)
        # L[0] = 1
        # for i in range(n - 1):
        #     L[i + 1] = L[i] * nums[i]
        #
        # R[n - 1] = 1
        # for i in reversed(range(0, n-1)):
        #     R[i] = R[i+1] * nums[i+1]
        #
        # for i in range(n):
        #     res.append(L[i] * R[i])
        # return res

        res = []
        n = len(nums)
        left, right = 1, 1
        for i in range(n):
            res.append(left)
            left *= nums[i]
        print(res)

        for i in reversed(range(n)):
            res[i] = res[i] * right
            right *= nums[i]

        return res


s = Solution()
print(s.productExceptSelf([1, 2, 3, 4]))
