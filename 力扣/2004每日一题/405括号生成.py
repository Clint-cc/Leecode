# !D:/Code/python
# -*- coding:utf-8 -*-
# @Author : Clint
# @Question : 数字n代表生成括号的对数，设计一个函数用于能够生成所有可能的并且有效的括号组合。
# @Thinking : dfs,

'''
括号是否有效：
def isValid(parentheses):
    stack = []
    for i in parentheses:
        if i == '(':
            stack.append(i)
        else:
            if not len(stack):
                return False
            stack.pop()
    return True
'''


class Solution():
    def generateParenthesis(self, n):
        res = []
        self.dfs(res, n, n, '')
        return res

    def dfs(self, res, left, right, path):
        if left == 0 and right == 0:
            res.append(path)
            return

        if left > 0:
            self.dfs(res, left - 1, right, path + '(')

        if left < right:
            self.dfs(res, left, right - 1, path + ')')


s = Solution()
print(s.generateParenthesis(3))
