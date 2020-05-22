# !D:/Code/python
# -*- coding:utf-8 -*-
# @Author : Clint
# @Question : 
# @Thinking :


class Solution:
    def validPalindrome(self, s):
        # 来自题解
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                case1, case2 = s[left:right], s[left + 1:right + 1]
                return case1 == case1[::-1] or case2 == case2[::-1]
            left += 1
            right -= 1
        return True


s = Solution()
print(s.validPalindrome('abbbcdcba'))
