# !D:/Code/python
# -*- coding:utf-8 -*-
# @Author : Clint
# @Question : 
# @Thinking :

class Solution:
    def subarraysDivByK(self, A, K):
        # 先试下暴力
        # n = len(A)
        # res = 0
        # for i in range(n):
        #     for j in range(i+1, n+1):
        #         if sum(A[i:j]) % K == 0:
        #             res +=1
        # return res

        # 理解前缀和，并套用模板
        # n = len(A)
        # preSum = [0] * (n + 1)
        # for i in range(n):
        #     preSum[i+1] = preSum[i] + num[i]

        # 优化后模板，此题有变化，需要灵活运用
        from collections import defaultdict
        ans = 0
        dict = defaultdict(int)
        dict[0] = 1
        sum_i = 0
        for num in A:
            sum_i += num
            sum_j = sum_i % K
            ans += dict[sum_j]

            dict[sum_j] += 1
        return ans


'''
    回到本题, 相比于和为K, 我们知道当前子数组为x之后，只需要去查询之前出现的子数组中出现过多少次和为K-x, 
    然后就可以得到在当前子数组里面和为K的子数组数量了。那么，对于本题来说, 我们是要查找和可被K整除的子数
    组, 看样子好像不能直接去查字典了,是不是要去挨个遍历字典呢? 其实Duck不必, 因为有如下公式
    ((a*K+c)-(b*K+c)) % K = 0一定成立。所以，我们每次只需要在字典中保存当前子数组的和除以K取余数的结果
    出现的次数即可, 然后每次查询最新子数组除以K取余数的结果在字典中已经出现的次数, 这个就是可以目前新增的
    可以构建出和可被K整除的子数组数量。
'''
s = Solution()
print(s.subarraysDivByK([4, 5, 0, -2, -3, 1], 5))
