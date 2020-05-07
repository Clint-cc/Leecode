# !D:/Code/python
# -*- coding:utf-8 -*-
# @Author : Clint
# @Question : [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

def sort_num(nums):
    nums.sort(key=lambda x: (-x[0], x[1]))
    out = []
    for p in nums:
        out.insert(p[1], p)
    return out
    # out = [[5,0][7,0],[5,2],[5,3],[4,4],[6,1],[7,1]]


print(sort_num([[7, 0], [5, 3], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]))

# [[5, 0], [7, 0], [5, 2], [5, 3], [4, 4], [6, 1], [7, 1]]
