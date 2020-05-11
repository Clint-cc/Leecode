# !D:/Code/python
# -*- coding:utf-8 -*-
# @Author : Clint
# @Question : 在一个由0和1组成的二维矩阵内，找到只包含1的最大正方形，并返回其面积。
# @Thinking :

'''
# 暴力求解
class Solution:
    def maximalSquare(self, matrix):
        # 矩形长度或者宽度只有1
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0

        max_side = 0
        row, col = len(matrix), len(matrix[0])
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 1:
                    # 遇到1，就作为正方形的左上角
                    max_side = max(max_side, 1)
                    # 计算可能的正方形边长
                    curmaxside = min(row - i, col - j)
                    for k in range(1, curmaxside):
                        # 判断新增的一行一列是否均为1
                        flag = True
                        if matrix[i + k][j + k] == 0:
                            break
                        for m in range(k):
                            if matrix[i+k][j+m] == 0 or matrix[i+m][j+k] == 0:
                                flag = False
                                break
                        if flag:
                            max_side = max(max_side, k+1)
                        else:
                            break
        return max_side * max_side
'''


# 动态规划
class Solution:
    def maximalSquare(self, matrix):
        # 矩形长度或者宽度只有1
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0

        maxside = 0
        rows, cols = len(matrix), len(matrix[0])
        dp = [[0] * cols for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 1:
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                    maxside = max(maxside, dp[i][j])

        return maxside * maxside


s = Solution()
print(s.maximalSquare([[1, 0, 1, 0, 0],
                       [1, 0, 1, 1, 1],
                       [1, 1, 1, 1, 1],
                       [1, 0, 0, 1, 0]])
      )
