# !D:/Code/python
# -*- coding:utf-8 -*-
# @Author : Clint
# @Question : 实现一个函数用来匹配包含'. '和'*'的正则表达式, '.'表示任意一个字符; '*'表示它前面的字符可以出现0次和多次。
# @Thinking : dp思路如下：
'''
    1\如果B的最后一个字符是正常字符, 那就是看A[n-1]是否等于B[m-1], 相等则看 A[0,n-2]与B[0, m-2], 不等则是不能匹配,
       这就是子问题。
    2\如果B的最后一个字符是., 它能匹配任意字符, 直接看 A[0, n-2]与B[0, m-2]
    3\如果B的最后一个字符是*, 它代表B[m-2]=c可以重复0次或多次, 它们是一个整体c*:
        情况一：A[n-1]是0个c, B最后两个字符废了, 能否匹配取决于 A[0,n-1]和B[0,m-3]是否匹配;
        情况二：A[n-1]是多个c中的最后一个（这种情况必须 A[n-1]=c或者 c='.',所以A匹配完往前挪一个, B继续匹配，因为可
               以匹配多个, 继续看 A[0,n-2]和B[0, m-1]是否匹配。

    根据以上, 确定转移方程:
        情况1、2合并： dp[i][j] = dp[i-1][j-1]
        情况3分两种情况：
            不看c*, 直接砍掉正则串后面两个: dp[i][j] = dp[i][j-2]
            看c*, 正则串不动, 主串前移动一个, dp[i][j] = dp[i-1][j]

    确定初始条件：
        都为空: dp[0][0] = True
        主串空, 匹配串非空: 不能确定, 如A = '', B = a*b*c
        主串非空, 匹配串空: dp[1][0] = ... = dp[n][0] = False
'''


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n = len(s)
        m = len(p)
        dp = [[False for _ in range(m + 1)] for _ in range(n + 1)]

        for i in range(n + 1):
            for j in range(m + 1):
                # 空正则或者非空正则
                if j == 0:
                    dp[i][j] = (i == 0)
                else:
                    # 非空正则分为两种情况 * 和 非*
                    if p[j - 1] != '*':
                        if i > 0 and (s[i - 1] == p[j - 1] or p[j - 1] == '.'):
                            dp[i][j] = dp[i - 1][j - 1]
                    else:
                        # 碰到 * 了, 分为看和不看两种情况
                        # 不看
                        if j >= 2:
                            dp[i][j] |= dp[i][j - 2]
                        # 看
                        if i >= 1 and j >= 2 and (s[i - 1] == p[j - 2] or p[j - 2] == '.'):
                            dp[i][j] |= dp[i - 1][j]

        return dp[n][m]


s = Solution()
print(s.isMatch("mississippi", "mis*is*p*."))
