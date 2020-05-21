# !D:/Code/python
# -*- coding:utf-8 -*-
# @Author : Clint
# @Question : 
# @Thinking :

class Solution:
    def findAnagrams(self, s: str, p: str):
        from collections import defaultdict
        need, window = defaultdict(int), defaultdict(int)
        for i in p:
            need[i] += 1

        left, right, valid = 0, 0, 0
        res = []

        while right < len(s):
            c = s[right]
            right += 1
            if c in need:
                window[c] += 1
                if window[c] <= need[c]:
                    valid += 1

            while valid >= len(p):
                if right - left == len(p):
                    res.append(left)

                d = s[left]
                left += 1

                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1
        return res


s = Solution()
print(s.findAnagrams("baa", "aa"))
