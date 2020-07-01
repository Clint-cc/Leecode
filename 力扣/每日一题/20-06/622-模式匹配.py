# !D:/Code/python
# -*- coding:utf-8 -*-
# @Author : Clint
# @Question : 
# @Thinking :


class Solution:
    def patternMatching(self, pattern: str, value: str) -> bool:
        cnt_a, cnt_b = pattern.count('a'), pattern.count('b')
        m = len(value)

        # 预处理
        if cnt_a < cnt_b:
            cnt_a, cnt_b = cnt_b, cnt_a

        # 1、value 为空，那么pattern只有一个字母，或者也为空
        if m == 0:
            return cnt_a == 0 or cnt_b == 0

        # 2、pattern 为空， valeue 不为空，无法匹配
        if cnt_a + cnt_b == 0 and m > 0: return False

        # 3、pattern、value都不为空
        # 'abba', 'docfttdocf'
        for len_a in range(m // cnt_a + 1):  # 枚举a代表字符的可能长度
            rest = m - cnt_a * len_a  # b代表字符的总长度

            if (cnt_b == 0 and rest == 0) or (cnt_b != 0 and rest % cnt_b == 0):
                len_b = 0 if cnt_b == 0 else rest // cnt_b

                pos, correct = 0, True
                value_a, value_b = None, None

                for ch in pattern:
                    if ch == 'a':
                        sub = value[pos:pos + len_a]
                        if not value_a:
                            value_a = sub
                        elif value_a != sub:
                            correct = False
                            break
                        pos += len_a
                    else:
                        sub = value[pos:pos + len_b]
                        if not value_b:
                            value_b = sub
                        elif value_b != sub:
                            correct = False
                            break
                        pos += len_b
                if correct and value_a != value_b:
                    return True

        return False

        # if m % (cnt_a + cnt_b) != 0: return False   # 长度不是a+b的倍数
        # if cnt_a == 0:
        #     return value == pattern.replace('b', value[:m // cnt_b])
        # if cnt_b == 0:
        #     return value == pattern.replace('a', value[:m // cnt_a])


s = Solution()
print(s.patternMatching('abba', 'docfttdocf'))
