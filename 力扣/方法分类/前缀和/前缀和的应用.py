# !D:/Code/python
# -*- coding:utf-8 -*-
# @Author : Clint
# @Question : 求和为K的所有连续非空子数组个数
# @Thinking :  优化的前缀和


class Solution:
    def subarraysIsK(self, A, K):
        # 普通的前缀和方法 O(n^2)
        # n = len(A)
        # preSum = [0] * (n + 1)
        # for i in range(n):
        #     preSum[i+1] = preSum[i] + A[i]  # 这里将前缀和的数组构造出来
        # ans = 0
        # for i in range(1, n+1):  # 这里穷举所有的子数组
        #     for j in range(i):
        #         if (preSum[i] - preSum[j]) == K:  # 这里算出sum of A[j:i]
        #             ans += 1
        # return ans

        # 优化后的前缀和方法
        n = len(A)
        from collections import defaultdict
        preSum = defaultdict(int)
        preSum[0] = 1
        ans, sum_i = 0, 0
        for i in range(n):
            sum_i += A[i]
            sum0_j = sum_i - K
            if sum0_j in preSum:
                ans += preSum[sum0_j]

            preSum[sum_i] += 1
        return ans


s = Solution()
print(s.subarraysIsK([2, 2, 2, 2, 4, 4], 4))
