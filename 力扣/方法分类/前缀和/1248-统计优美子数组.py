# !D:/Code/python
# -*- coding:utf-8 -*-
# @Author : Clint
# @Question : 给你一个整数数组 nums 和一个整数 k。如果某个连续子数组中恰好有k个奇数数字，我们就认为
#             这个子数组是「优美子数组」。请返回这个数组中「优美子数组」的数目
# @Thinking : 前缀和
from collections import defaultdict


class Solution:
    def numberOfSubarrays(self, nums, k):
        num_odd = defaultdict(int)
        num_odd[0] = 1  # 初始化，奇数个数为0出现1次
        res, cur_odd = 0, 0  # 初始化定义次数结果，记录当前位置的奇数个数
        for i in range(len(nums)):
            if nums[i] % 2 != 0:  # 如果是奇数
                cur_odd += 1  # 当前位置奇数个数更新
            if cur_odd - k in num_odd:  # 如果当前奇数个数和减去k所得到的值在字典中出现
                res += num_odd[cur_odd - k]  # 更新结果次数
            num_odd[cur_odd] += 1  # 将新的奇数个数设为1
        return res


s = Solution()
print(s.numberOfSubarrays([2, 2, 2, 1, 2, 2, 1, 2, 2, 2], 2))
