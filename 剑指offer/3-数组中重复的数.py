# !D:/Code/python
# -*- coding:utf-8 -*-
# @Author : Clint
# @Question : 面试题03. 数组中重复的数字
# @Thinking :


class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        # nums = sorted(nums)
        # pre = nums[0]
        # for i in range(1,len(nums)):
        #     if nums[i] == pre:
        #         return nums[i]
        #     else:
        #         pre = nums[i]

        from collections import defaultdict  # 哈希表
        dict = defaultdict(int)
        for num in nums:
            dict[num] += 1
            if dict[num] > 1:
                return num

        # 原地置换法

        # 不修改数组，二分法


s = Solution()
print(s.findRepeatNumber([2, 3, 1, 0, 2, 5, 3]))
