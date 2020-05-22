# !D:/Code/python
# -*- coding:utf-8 -*-
# @Author : Clint
# @Question :
# @Thinking : 滑动窗口


class Solution:
    def lengthOfLongestSubstring(self, s: str):
        if not s:
            return 0
        slide_window, max_len, j = set(), 0, 0
        for i in range(len(s)):
            while s[i] in slide_window:
                slide_window.remove(s[j])
                j += 1
            max_len = max(max_len, i + 1 - j)
            slide_window.add(s[i])
        return max_len


s = Solution()
print(s.lengthOfLongestSubstring('abccabcbb'))
