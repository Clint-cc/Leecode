# !D:/Code/python
# -*- coding:utf-8 -*-
# @Author : Clint
# @Question : 
# @Thinking :
from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # 暴力解法
        # n = len(heights)
        # ans = 0
        # for i in range(n):
        #     left, right = i-1, i + 1
        #     while left >= 0 and heights[left] >= heights[i]:
        #        left -= 1
        #     while right < n and heights[right] >= heights[i]:
        #         right += 1
        #     ans = max(ans, heights[i] * (right - left - 1))
        # return ans

        # 单调栈
        stack = []
        heights = [0] + heights + [0]  # [0,2,1,5,6,2,3,0]
        res = 0
        for i in range(len(heights)):
            print(stack)
            while stack and heights[stack[-1]] > heights[i]:
                tmp = stack.pop()
                res = max(res, (i - stack[-1] - 1) * heights[tmp])
            stack.append(i)
        return res


s = Solution()
print(s.largestRectangleArea([2, 1, 5, 6, 2, 3]))
