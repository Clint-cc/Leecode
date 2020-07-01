# !D:/Code/python
# -*- coding:utf-8 -*-
# @Author : Clint
# @Question :  '.' 匹配任意单个字符； '*' 匹配零个或者多个前面的一个元素
# @Thinking : dp


class Solution1:
    def isMatch(self, s: str, p: str) -> bool:
        '''
        状态： dp[i][j]表示s的前i个是否能被p的前j个匹配
        转移方程：假设已经求出  dp[i-1][j-1]，再加上已知 s[i]、p[j]，就是怎么去求 dp[i][j]
            对于新的一位p[j] s[i]情况，需要 分情况讨论：
                1、如果p[j] == s[i], 则 dp[i][j] = dp[i-1][j-1]
                2、p[j] == ".", 一样，dp[i][j] = dp[i-1][j-1]
                3、p[j] == "*": 匹配零个或多个前面的那一个元素，所以要考虑他前面的元素 p[j-1]
                所以按照 p[j-1] 和 s[i] 是否相等，我们分为两种情况：
                    3.1、p[j-1] != s[i] ：
                        dp[i][j] = dp[i][j-2]
                    3.2、p[j-1] == s[i] or p[j-1] == "."：
                        dp[i][j] = dp[i-1][j] or \
                        dp[i][j] = dp[i][j-1] or \
                        dp[i][j] = dp[i][j-2]
        '''
        if not s or not p: return False

        dp = [[False for _ in range(len(p) + 1)] for _ in range(len(s) + 1)]

        # 初始化
        dp[0][0] = True
        for i in range(len(p)):
            if p[i] == '*' and dp[0][i - 1]:
                dp[0][i + 1] = True

        for i in range(len(s)):
            for j in range(len(p)):
                # 情况1和情况2可以合并
                if p[j] == s[i] or p[j] == ".":
                    dp[i + 1][j + 1] = dp[i][j]

                # 情况3
                if p[j] == "*":
                    if p[j - 1] != s[i] and p[j - 1] != ".":
                        dp[i + 1][j + 1] = dp[i + 1][j - 1]
                    else:
                        dp[i + 1][j + 1] = (dp[i][j + 1] or dp[i + 1][j] or dp[i + 1][j - 1])

        return dp[len(s)][len(p)]


class Solution2:
    def isMatch(self, s: str, p: str) -> bool:
        if not p: return not s
        if not s and len(p) == 1: return False

        n, m = len(s), len(p)
        dp = [[False for _ in range(m + 1)] for _ in range(n + 1)]
        # 初始化
        dp[0][0] = True
        for i in range(m):
            if p[i] == '*' and dp[0][i - 1]:
                dp[0][i + 1] = True
        for i in range(n):
            for j in range(m):
                if p[j] == s[i] or p[j] == ".":  # 情况1和情况2可以合并
                    dp[i + 1][j + 1] = dp[i][j]
                if p[j] == "*":
                    if p[j - 1] != s[i] and p[j - 1] != ".":  # 情况3.1
                        dp[i + 1][j + 1] = dp[i + 1][j - 1]
                    else:  # 情况3.2
                        dp[i + 1][j + 1] = (dp[i][j + 1] or dp[i + 1][j] or dp[i + 1][j - 1])
        return dp[n][m]


s = Solution2()
print(s.isMatch("aab", "c*a*b"))
