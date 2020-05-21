# !D:/Code/python
# -*- coding:utf-8 -*-
# @Author : Clint
# @Question : 
# @Thinking :


class Solution:
    def longestPalindrome(self, s: str) -> str:
        #     n = len(s)    # 日常暴力超时
        #     res, ans = 0, ""
        #     for left in range(n):
        #         for right in range(left, n):
        #             if self.is_Palindrome(s[left:(right + 1)]):
        #                 if right + 1 - left > res:
        #                     res, ans = right + 1 - left, s[left:(right + 1)]
        #     return ans
        # def is_Palindrome(self, s):
        #     return s[::] == s[::-1]

        # dp算法，
        n = len(s)
        dp = [[False for _ in range(n)] for _ in range(n)]  # dp[i][j] 表示s[i...j] 是否是回文串
        # 初始化结果
        maxlen, begin = 1, 0
        for j in range(1, n):
            for i in range(j):
                if s[i] != s[j]:
                    dp[i][j] = False
                elif j - i < 3:
                    dp[i][j] = True
                else:
                    dp[i][j] = dp[i + 1][j - 1]

                if dp[i][j] and j - i + 1 > maxlen:
                    maxlen = j - i + 1
                    begin = i

        return s[begin:begin + maxlen]


s = Solution()
print(s.longestPalindrome("babad"))
