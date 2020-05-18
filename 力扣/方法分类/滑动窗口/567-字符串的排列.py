# !D:/Code/python
# -*- coding:utf-8 -*-
# @Author : Clint
# @Question : 给定两个字符串 s1 和 s2，写一个函数来判断 s2 是否包含 s1 的排列。
#             如： s1 = "ab" s2 = "eidbaooo" 返回True
#                  s1= "ab" s2 = "eidboaoo"  返回False
# @Thinking : 滑动窗口

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import defaultdict
        need = defaultdict(int)
        window = defaultdict(int)
        left, right, valid = 0, 0, 0
        for char in s1: need[char] += 1
        while right < len(s2):
            c = s2[right]  # 加入窗口
            right += 1
            if c in need:  # 增加字符串一系列更新操作
                window[c] += 1
                if window[c] == need[c]:
                    valid += 1
            while right - left >= len(s1):
                if valid == len(s1): return True
                d = s2[left]  # 从窗口中删除
                left += 1
                if d in need:  # 删除字符串一系列更新操作
                    if window[d] == need[d]: valid -= 1
                    window[d] -= 1
        return False


s = Solution()
print(s.checkInclusion('ab', 'eidbaoo'))
