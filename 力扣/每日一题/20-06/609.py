# !D:/Code/python
# -*- coding:utf-8 -*-
# @Author : Clint
# @Question : 
# @Thinking :


class Solution(object):
    def translateNum(self, num):
        num = str(num)
        dp = [1 for _ in range(len(num))]
        # 9876543
        for i in range(1, len(num)):
            if num[i - 1] != '0' and (26 > int(num[i - 1:i + 1]) >= 10):
                dp[i] = dp[i - 1] + dp[i - 2]
            else:
                dp[i] = dp[i - 1]

        return dp[-1]


s = Solution()
print(s.translateNum(98765))
