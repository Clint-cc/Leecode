# !D:/Code/python
# -*- coding:utf-8 -*-
# @Author : Clint
# @Question : 房子排成一列，相邻的房子不能同时被抢，求能抢到的最高金额
# @Thinking :

class Solution:
    # 方法一
    # def rob(self, nums):  # 线性递归
    #     n = len(nums)
    #     # 记录 dp[i+1] 和 dp[i+2]
    #     dp_i_1, dp_i_2 = 0, 0
    #     # 记录 dp[i]
    #     dp_i = 0;
    #     for i in range(n - 1, -1, -1):
    #         dp_i = max(dp_i_1, nums[i] + dp_i_2);
    #         dp_i_2 = dp_i_1;
    #         dp_i_1 = dp_i;
    #     return dp_i;

    def memo_rob(self, nums):  # 带备忘录的dp
        memo = [-1 for _ in range(len(nums))]
        return self.dp(nums, memo, 0)

    def dp(self, nums, memo, start):
        if start >= len(nums): return 0

        if memo[start] != -1:  # 做备忘录避免重复计算
            return memo[start]
        # 转态转移方程
        res = max(self.dp(nums, memo, start + 1), nums[start] + self.dp(nums, memo, start + 2))
        memo[start] = res  # 记入备忘录
        return res


s = Solution()
print(s.memo_rob([2, 7, 9, 3, 1]))
