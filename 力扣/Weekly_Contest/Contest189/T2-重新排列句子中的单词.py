# !D:/Code/python
# -*- coding:utf-8 -*-
# @Author : Clint
# @Question : 
# @Thinking :


class Solution:
    def arrangeWords(self, text):
        text = text.lower().split(' ')
        text.sort(key=lambda x: (len(x)))
        res = ' '.join(text)
        return res.capitalize()


s = Solution()
print(s.arrangeWords("Leetcode is cool"))
