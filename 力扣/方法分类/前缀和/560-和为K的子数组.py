# !D:/Code/python
# -*- coding:utf-8 -*-
# @Author : Clint
# @Question : 
# @Thinking :
from typing import List
from collections import defaultdict  # 当key值不存在，不会报错，会返回默认值


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # 前缀和
        nums_time = defaultdict(int)  # 存储‘前缀和’出现的次数
        nums_time[0] = 1  # 初始化，前缀和为0出现1次
        res, cur_sum = 0, 0  # 初始化定义次数结果， 记录当前位置的前缀和
        for i in range(len(nums)):
            cur_sum += nums[i]  # 计算当前前缀和
            if cur_sum - k in nums_time:  # 如果前缀和减去k所得到的值在字典中出现即当前位置前缀和减去之前某一位的前缀和等于目标值
                res += nums_time[cur_sum - k]
            # 下面一句实际上对应两种情况，一种是某cur_sum之前出现过（直接在原来出现的次数上+1即可），
            # 另一种是某cur_sum没出现过（理论上应该设为1，但是因为此处用defaultdict存储，如果cur_sum这个key不存在将返回默认的int，也就是0）
            # 返回0加上1和直接将其置为1是一样的效果。所以这里统一用一句话包含上述两种情况
            nums_time[cur_sum] += 1
        return res


s = Solution()
print(s.subarraySum([1, 1, 0, 1, 2], 2))
