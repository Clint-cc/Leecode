# !D:/Code/python
# -*- coding:utf-8 -*-
# @Author : Clint
# @Question : 
# @Thinking :


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        from collections import defaultdict
        window = defaultdict(int)
        left, right, res = 0, 0, 0

        while right < len(s):
            c = s[right]
            right += 1
            window[c] += 1  # 增加更新窗口
            while window[c] > 1:  # 判断左侧是否要收缩
                d = s[left]
                left += 1
                window[d] -= 1  # 删除更新窗口
            res = max(right - left, res)
        return res


s = Solution()
print(s.lengthOfLongestSubstring("pwwkew"))
