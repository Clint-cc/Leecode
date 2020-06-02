# !D:/Code/python
# -*- coding:utf-8 -*-
# @Author : Clint
# @Question : 
# @Thinking :

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for i in s:
            if i != ']':
                stack.append(i)
            else:
                subs = ''
                while stack[-1] != '[':  # 将括号的字符推出栈
                    tmp = stack.pop()
                    if len(tmp) == 1:
                        subs += tmp
                    elif len(tmp) > 1:
                        subs += tmp[::-1]
                stack.pop()  # 删除左括号

                num = ''
                while stack and stack[-1].isdigit():
                    num += stack.pop()
                stack.append(subs[::-1] * int(num[::-1]))

        return ''.join(s for s in stack)


s = Solution()
print(s.decodeString("3[z]2[2[y]pq4[2[jk]e1[f]]]ef"))
