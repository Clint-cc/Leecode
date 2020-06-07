# !D:/Code/python
# -*- coding:utf-8 -*-
# @Author : Clint
# @Question : 
# @Thinking :
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # res = []
        # while matrix:
        #     res += matrix.pop(0)
        #     matrix = list(zip(*matrix))[::-1]
        # return res

        if len(matrix) == 0 or len(matrix[0]) == 0: return []
        row, col = len(matrix), len(matrix[0])
        start, res = 0, []

        while col > start * 2 and row > start * 2:  # 进行下一圈的条件
            self.printMatrinx(matrix, row, col, start, res)  # 打印一圈
            start += 1
        return res

    def printMatrinx(self, matrix, row, col, start, res):
        endx = row - 1 - start
        endy = col - 1 - start

        # 1、从左到右打印一行，这一步是一定有的，
        for i in range(start, endy + 1):
            res.append(matrix[start][i])

        # 2、从上到下打印一列：终止行号打大于起始行号
        if start < endx:
            for i in range(start + 1, endx + 1):
                res.append(matrix[i][endy])

        # 3、从右到左打印一行：至少是两行两列（也就是终止行号大于起始行号 and 终止列号大于起始列号）
        if start < endx and start < endy:
            for i in range(endy - 1, start - 1, -1):
                res.append(matrix[endx][i])

        # 4、从下到上打印一列：至少三行两列（终止行号比起始行号大2 and 终止列号大于起始列号）
        if start < endx - 1 and start < endy:
            for i in range(endx - 1, start, -1):
                res.append(matrix[i][start])


s = Solution()
print(s.spiralOrder([[1, 2, 3, 4],
                     [5, 6, 7, 8],
                     [9, 10, 11, 12]
                     ])
      )
