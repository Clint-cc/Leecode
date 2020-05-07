# !D:/Code/python
# -*- coding:utf-8 -*-
# @Author : Clint
# @Question : 找出和为目标数的连续数组


class Solution:
    def findContinuousSequence(target):
        # target = int(input("请输入目标数："))
        b = []
        for i in range(1, int(target / 2) + 1):
            sums = 0
            for j in range(i, int(target / 2) + 2):
                sums += j
                if sums < target:
                    continue
                elif sums == target:
                    a = []
                    for k in range(i, j + 1):
                        a.append(k)
                    b.append(a)
                else:
                    break
        return b


print(Solution.findContinuousSequence(9))
