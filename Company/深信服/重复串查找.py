# !D:/Code/python
# -*- coding:utf-8 -*-
# @Author : Clint
# @Question : 一个重复字符串是由两个相同的字符串首尾拼接而成，例如abcabc便是长度为6的一个重复字符串，而abcba则不存在重复字符串。
#             如：xabcabcx, 返回6; abcba, 返回0
# @Thinking :

class Solution:
    def LongestRepeatedSub(slef, s):
        n = len(s)
        max_len = 0
        for i in range(0, n - 1):  # 'xabcabcx'
            for j in range(i + 1, n):
                if s[i:j] == s[j:(2 * j - i)]:
                    max_len = max(max_len, 2 * (j - i))
        return max_len


s = Solution()
print(s.LongestRepeatedSub(''))
