# !D:/Code/python
# -*- coding:utf-8 -*-
# @Author : Clint
# @Question : 给你一个m*n的矩阵，矩阵中的元素不是0就是1，请你统计并返回其中完全由1组成的正方形子矩阵的个数
# @Thinking : dp


class Solution:
    def countSquares(self, matrix):
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        rows, cols = len(matrix), len(matrix[0])
        dp = [[0] * cols for _ in range(rows)]
        square_counts = 0
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 1:
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1], dp[i][j - 1]) + 1
                square_counts += dp[i][j]
        return square_counts


s = Solution()
print(s.countSquares([[0, 1, 1, 1],
                      [1, 1, 1, 1],
                      [0, 1, 1, 1]]
                     )
      )
