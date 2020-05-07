# !D:/Code/python
# -*- coding:utf-8 -*-
# @Author : Clint
# @Question : 
# @Thinking : dp，dp，还是dp！！


class Solution:
    def mincostTickets(self, days, costs):
        dp = [0 for _ in range(days[-1] + 1)]
        days_idx = 0  # 标记应该处理days中的哪一个元素
        for i in range(days[0], len(dp)):
            # if i not in days:
            if i != days[days_idx]:  # 当天非处理天数，则费用和前一天相同
                dp[i] = dp[i - 1]
            else:
                dp[i] = min(
                    dp[max(i - 1, 0)] + costs[0],
                    dp[max(i - 7, 0)] + costs[1],
                    dp[max(i - 30, 0)] + costs[2],
                )
                days_idx += 1
        return dp[-1]


s = Solution()
print(s.mincostTickets([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31], [2, 7, 15]))
