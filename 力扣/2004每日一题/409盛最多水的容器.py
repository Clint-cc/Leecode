# !D:/Code/python
# -*- coding:utf-8 -*-
# @Author : Clint
# @Question : 给你n个非负整数a1，a2，...，an，每个数代表坐标中的一个点(i, ai) 。在坐标内画n条垂直线，垂直线i的两个端点
#             分别为 (i, ai)和(i, 0)。找出其中的两条线，使得它们与x轴共同构成的容器可以容纳最多的水；
# @Thinking : 双指针


class Solution:
    def maxArea(self, nums):
        i, j = 0, len(nums) - 1
        cur_area, res = 0, 0
        while i < j:
            if nums[i] <= nums[j]:
                cur_area = (j - i) * nums[i]
                i += 1
            else:
                cur_area = (j - i) * nums[j]
                j -= 1
            res = max(res, cur_area)
        return res


s = Solution()
print(s.maxArea([8, 1, 6, 2, 5, 4, 8, 3, 7]))
