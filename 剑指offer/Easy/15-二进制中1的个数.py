# !D:/Code/python
# -*- coding:utf-8 -*-
# @Author : Clint
# @Question : 请实现一个函数，输入一个整数，输出该数二进制表示中1的个数。例如，把9表示成二进制是1001，
#             有2位是1。因此，如果输入9，则该函数输出2。
# @Thinking :


class Solution:
    def hammingWeight(self, n):
        # 无符号的二进制串输入，右移位与运算
        count = 0
        while n:
            if n & 1: count += 1
            n = n >> 1  # 这里除2是等价的，但移位的效率更高
        return count

        # 注意无符号和有符号的区别，避免死循环


s = Solution()
print(s.hammingWeight(0b10001))
