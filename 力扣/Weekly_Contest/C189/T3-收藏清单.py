# !D:/Code/python
# -*- coding:utf-8 -*-
# @Author : Clint
# @Question : 
# @Thinking :
from typing import List
from collections import defaultdict


class Solution:
    # 暴力法, 超出时间限制
    # def is_sub_array(self, s, t):
    #     for i in s:
    #         if i not in t:
    #             return False
    #     return True

    # def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
    #
    #     n = len(favoriteCompanies)
    #     res = [i for i in range(n)]
    #     for i in range(n):
    #         for j in range(n):
    #             if j == i:  # 跳过判断是否是自己的子集
    #                 continue
    #             if self.is_sub_array(favoriteCompanies[i], favoriteCompanies[j]):
    #                 res.remove(i)
    #                 break
    #     return res

    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        # 优化后的暴力，优化思路如下：
        # 1、将字符串列表转为数字列表
        # 2、将数字列表进行排序
        # 3、进行比较
        n = len(favoriteCompanies)
        fc_num = defaultdict(int)
        for i in range(n):
            for j in favoriteCompanies[i]:
                if j not in fc_num:
                    fc_num[j] = len(fc_num)

        fc_nums = [[] for _ in range(n)]
        for i in range(n):
            for j in favoriteCompanies[i]:
                fc_nums[i].append(fc_num[j])
            fc_nums[i].sort()

        res = [i for i in range(n)]
        for i in range(n):
            for j in range(n):
                if j == i:  # 跳过判断是否是自己的子集
                    continue
                if self.is_substr(fc_nums[i], fc_nums[j]):
                    res.remove(i)
                    break
        return res

    def is_substr(self, a, b):
        if len(a) > len(b):
            return False
        for i in a:
            if i not in b:
                return False
        return True


s = Solution()
print(s.peopleIndexes([["leetcode", "google", "facebook"], ["leetcode", "amazon"], ["facebook", "google"]]))
t = [["leetcode", "google", "facebook"], ["google", "microsoft"], ["google", "facebook"], ["google"], ["amazon"]]
print(s.peopleIndexes(t))
