# !D:/Code/python
# -*- coding:utf-8 -*-
# @Author : Clint
# @Question : 
# @Thinking :


class Solution:
    # 为考虑大数问题
    def printNumbers(self, n: int):
        return [i for i in range(1, 10 ** n)]


s = Solution()
print(s.printNumbers(2))
