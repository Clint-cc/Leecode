# !D:/Code/python
# -*- coding:utf-8 -*-
# @Author : Clint
# @Question : 给定一个整数数组和一个整数 k，你需要找到该数组中和为 k 的连续的子数组的个数。
# @Thinking :
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # 暴力: O(n^2)
        # if not nums: return 0
        # res, n = 0, len(nums)
        # for i in range(n):
        #     summ = nums[i]
        #     if summ == k:
        #         res += 1
        #     for j in range(i+1, n):
        #         summ += nums[j]
        #         if summ == k:
        #             res += 1
        # return res

        # 前缀和： O(n^2)
        from collections import defaultdict
        nums_times = defaultdict(int)
        nums_times[0] = 1
        cur_sum = 0
        res = 0
        for i in range(len(nums)):
            cur_sum += nums[i]
            if cur_sum - k in nums_times:
                res += nums_times[cur_sum - k]
            nums_times[cur_sum] += 1
        return res


s = Solution()
print(s.subarraySum([1, 1, 0, 1, 2], 2))
