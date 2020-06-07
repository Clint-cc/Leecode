# !D:/Code/python
# -*- coding:utf-8 -*-
# @Author : Clint
# @Question : 给定一个未排序的整数数组，找出最长连续序列的长度。
# @Thinking :
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # from collections import defaultdict
        # dict = defaultdict(int)
        max_len = 0
        set_nums = list(set(nums))
        for num in nums:
            if num - 1 not in set_nums:
                cur = num
                cnt = 1
                while cur + 1 in set_nums:
                    cur += 1
                    cnt += 1
                max_len = max(max_len, cnt)
        return max_len


s = Solution()
print(s.longestConsecutive([7, 6, 100, 8, 2, 9, 10, 200, 3, 1, 4]))
