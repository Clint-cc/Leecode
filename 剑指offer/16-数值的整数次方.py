# -*- coding:utf-8 -*-
# @Author : Clint
# @Question : 实现函数double Power(double x, int n)，求x的n次方。不准使用库函数，同时不需要考虑大数问题。
# @Thinking :


class Solution:
    def myPow(self, x, n):
        if x == 0: return 0  # 0的任意次方都得0
        res = 1
        if n < 0: x, n = 1 / x, -n
        while n:
            if n & 1: res *= x  # 最后一位为1的话，就乘以res
            x *= x
            n >>= 1
        return res


s = Solution()
print(s.myPow(2, -2))
