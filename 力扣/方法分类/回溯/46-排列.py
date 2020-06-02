# !D:/Code/python
# -*- coding:utf-8 -*-
# @Author : Clint
# @Question : 
# @Thinking :


class Solution:
    # def permutation(self, nums):
    #     res = []
    #     cnt = 0
    #     def backTrack(nums, track):
    #         if len(nums) == len(track):
    #             res.append(track)
    #
    #             return
    #         for i in range(len(nums)):
    #             if nums[i] in track:
    #                 continue
    #             backTrack(nums, track + [nums[i]])
    #
    #     backTrack(nums, [])
    #     return res

    def per_N(self, n):
        res = []

        def backTrack(n, track):
            if n == len(track):
                res.append(track)
                return
            for i in range(1, n + 1):
                if str(i) in track:
                    continue
                backTrack(n, track + str(i))

        backTrack(n, '')
        return res


s = Solution()
# print(s.permutation([1,2,3]))
# print(len(s.permutation([1,2,3])))
print(s.per_N(3))
