# !D:/Code/python
# -*- coding:utf-8 -*-
# @Author : Clint
# @Question : 给定一个可包含重复数字的序列，返回所有不重复的全排列
# @Thinking : 回溯法 + 剪枝
from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        visited = [False for _ in range(n)]

        def backtrack(nums, track):
            if len(track) == n:  # 满足条件
                res.append(track)
                return

            for i in range(n):

                # 在回溯前后需要进行是否剪枝判断
                if i > 0 and nums[i] == nums[i - 1] and not visited[i - 1] == False:  # 剪枝
                    continue
                if visited[i]:  # 如果已经访问过，也跳过
                    continue

                visited[i] = True
                backtrack(nums, track + [nums[i]])
                visited[i] = False

        nums.sort()
        backtrack(nums, [])
        return res


s = Solution()
print(s.permuteUnique([1, 1, 1, 3]))
