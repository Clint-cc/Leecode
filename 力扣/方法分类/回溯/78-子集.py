# !D:/Code/python
# -*- coding:utf-8 -*-
# @Author : Clint
# @Question : 
# @Thinking :


class Solution:
    def subsets(self, nums):
        res = []

        def backtrack(start, track):
            if track not in res:
                res.append(track)
            for i in range(start, len(nums)):
                backtrack(i + 1, track + [nums[i]])

        backtrack(0, [])

        return res


s = Solution()
print(s.subsets([1, 2, 2]))
