# !D:/Code/python
# -*- coding:utf-8 -*-
# @Author : Clint
# @Question : 
# @Thinking :

class Solution:
    def buildArray(self, target, n):
        res = []
        for i in range(1, target[-1] + 1):
            res.append('Push')
            if i not in target:
                res.append('Pop')
        return res


s = Solution()
print(s.buildArray([1, 3, 5, 7], 9))
