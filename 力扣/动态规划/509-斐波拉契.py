# !D:/Code/python
# -*- coding:utf-8 -*-
# @Author : Clint
# @Question : 斐波那契第n项的值
# @Thinking : dp、带备忘录的dp（剪枝）、dp table


class Solution:
    # dp
    def fib(self, N):
        if N == 1 or N == 2:
            return 1
        else:
            return self.fib(N - 1) + self.fib(N - 2)

    # 带demo的dp（自顶向下）
    def memo_fib(self, N):
        # memo = {}   # 字典形式的memo
        # for i in range(1, N + 1)
        #     memo.setdefault(i, 0) for i in range(1, N + 1)
        memo = [0 for _ in range(N + 1)]  # 列表形式的memo
        return self.memo_helper(memo, N)

    def memo_helper(self, memo, N):
        if N == 1 or N == 2:
            return 1
        if memo[N] != 0:
            return memo[N]
        memo[N] = self.memo_helper(memo, N - 1) + self.memo_helper(memo, N - 2)
        return memo[N]

    # dp table
    def dp_table_fib(self, N):
        dp_table = [0 for _ in range(N + 1)]
        if N == 1:
            return 1
        dp_table[1] = dp_table[2] = 1
        for i in range(3, N + 1):
            dp_table[i] = dp_table[i - 1] + dp_table[i - 2]
        return dp_table[N]

    # 细节优化，状态转移方程只需要存之前两个状态就行
    def opt_fib(self, N):
        if N == 1 or N == 2:
            return 1
        pre, cur = 1, 1
        for i in range(3, N + 1):
            summ = pre + cur
            pre = cur
            cur = summ
        return cur


s = Solution()
print("带备忘录的dp：")
for i in range(1, 21):
    print(s.memo_fib(i), end='    ')

print("\ndp_table：")
for i in range(1, 21):
    print(s.dp_table_fib(i), end='    ')

print("\n优化后的状态转移：")
for i in range(1, 21):
    print(s.opt_fib(i), end='    ')
