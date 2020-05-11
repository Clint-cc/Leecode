# !D:/Code/python
# -*- coding:utf-8 -*-
# @Author : Clint
# @Question : 给你两个单词word1和word2，请你计算出将word1转换成word2所使用的最少操作数
#             你可以对一个单词进行如下三种操作：
#                插入一个字符
#                删除一个字符
#                替换一个字符
# @Thinking :


class Solution:
    def edit_distance(self, s1, s2):
        rows, cols = len(s1), len(s2)
        dp = [[0] * (cols + 1) for _ in range(rows + 1)]
        # 初始化
        for i in range(cols + 1):
            dp[0][i] = i
        for j in range(rows + 1):
            dp[j][0] = j

        # 状态转移
        for i in range(1, rows + 1):
            for j in range(1, cols + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1

        return dp[-1][-1]


s = Solution()
print(s.edit_distance('horse', 'ros'))
