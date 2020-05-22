# !D:/Code/python
# -*- coding:utf-8 -*-
# @Author : Clint
# @Question : 给你⼀个数组，返回⼀个等⻓的数组，对应索引存储着下⼀个更⼤元素，如果没有更⼤的元素，就存-1。
#             如：给你⼀个数组 [2,1,2,4,3]，你返回数组 [4,2,4,-1,-1]。
# @Thinking :

class Solution:
    def monotonicStack(self, nums):
        ans = [0] * len(nums)  # 存放答案的数组
        stack = []
        for i in range(len(nums) - 1, -1, -1):  # 倒着往栈里放
            while stack and stack[-1] <= nums[i]:  # 判断谁矮
                stack.pop()
            ans[i] = -1 if not stack else stack[-1]  #
            stack.append(nums[i])
        return ans, stack


s = Solution()
print(s.monotonicStack([2, 1, 2, 4, 3]))
