# !D:/Code/python
# -*- coding:utf-8 -*-
# @Author : Clint
# @Question : 
# @Thinking :


class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        vowel = {'a': 2, 'e': 2, 'i': 2, 'o': 2, 'u': 2}
        left, right = 0, 0
        max_ans = 0
        # from collections import defaultdict
        # window = defaultdict(int)
        while right < len(s):
            right += 1
            t = s[left:right]
            if t.count('a') % 2 == 0 and t.count('e') % 2 == 0 and t.count('i') % 2 == 0 \
                    and t.count('o') % 2 == 0 and t.count('u') % 2 == 0:
                max_ans = right - left
            else:
                left += 1
        return max_ans


s = Solution()
print(s.findTheLongestSubstring("eleetminicoworoep"))
