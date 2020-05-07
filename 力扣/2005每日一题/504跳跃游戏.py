# !D:/Code/python
# -*- coding:utf-8 -*-
# @Author : Clint
# @Question : 
# @Thinking :

class Solution:
    def jump(self, nums):
        if len(nums) < 2:
            return 0  # 长度为0或1表示不用跳，直接返回0

        cur_max = nums[0]  # 记录从远点开始最远可以跳多远(初始化为nums[0])
        end = nums[0]  # 记录用最少的跳跃次数可以跳多远(初始化为nums[0])
        res = 1  # 记录返回值即最少跳跃次数

        if end >= len(nums) - 1:  # 如果第一次跳跃已经到达末尾，则直接返回，否则进入for循环
            return res
            # [2,3,1,1,4]
        for i in range(1, len(nums)):
            cur_max = max(cur_max, i + nums[i])  # 更新可以到达的最远位置
            if i == end:  # 如果i走到了上一次跳跃可达到的最远点
                if end < len(nums) - 1:  # 如果这个end还没达到最后一个位置，就跳一步，同时更新res和end，当更新完end立刻判断和最后一个位置的关系
                    res += 1
                    end = cur_max
                    if end >= len(nums) - 1:
                        return res
                else:  # 如果end已经达到末尾，直接返回
                    return res


s = Solution()
print(s.jump([2, 3, 1, 1, 4]))
