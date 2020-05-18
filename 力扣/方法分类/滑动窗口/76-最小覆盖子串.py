# !D:/Code/python
# -*- coding:utf-8 -*-
# @Author : Clint
# @Question : 
# @Thinking :
from collections import defaultdict
import math


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = defaultdict(int)
        window = defaultdict(int)
        for s_char in t:
            need[s_char] += 1

        left, right = 0, 0
        valid = 0  # 表⽰窗⼝中满⾜need条件的字符个数
        start, le = 0, math.inf

        while right < len(s):
            c = s[right]  # c是将移入窗口的字符
            right += 1  # 右移窗口

            # 进⾏窗⼝内数据的⼀系列更新
            if c in need:
                window[c] += 1
                if window[c] == need[c]:
                    valid += 1

            # 判断左侧窗口是否要收缩
            while valid == len(need):
                # 更新最小覆盖子串
                if right - left < le:
                    start = left
                    le = right - left

                d = s[left]  # 将要移除窗口的字符
                left += 1  # 左移窗口

                # 进⾏窗⼝内数据的⼀系列更新
                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1

        return s[start:(start + le)] if le != math.inf else ""


s = Solution()
print(s.minWindow("ABC", "B"))
