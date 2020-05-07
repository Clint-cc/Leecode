# !D:/Code/python
# -*- coding:utf-8 -*-
# @Author : Clint
# @Question : 
# @Thinking :


class Solution:
    def substr_match(self, s, sub_s):
        n, sn = len(s), len(sub_s)
        if not s or not sub_s:
            return 0
        if sn > n:
            return -1
        if sub_s[0] != '?' and s[0] != s[0]:
            return -1
        # 指定两个指针，初始化指向第一个字符
        j, sj, res = 0, 0, -1
        while j < n and sj < sn:
            # 子串字符非?时，不相等直接跳出
            if sub_s[sj] != '?' and s[j] != sub_s[sj]:
                break
            elif s[j] == sub_s[sj]:
                j += 1
                sj += 1
            elif sub_s[sj] == '?':
                if j - sj > 3:
                    res = -1
                    break
                if sub_s[sj + 1] == s[j + 1]:
                    j += 2
                    sj += 2
                else:
                    j += 1
        # 若匹配字符串指针已经指向尾部（完全匹配）且结果数小于新的匹配数，则更新
        if sj >= sn and j <= n and j > res:
            res = j
        return res


so = Solution()
print(so.substr_match('aabdddefg', 'aab?'))
