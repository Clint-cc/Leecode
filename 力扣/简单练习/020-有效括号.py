# !D:/Code/python
# -*- coding:utf-8 -*-
# @Author : Clint


def isValid(s):
    stack = []
    a = {
        '{': '}',
        '[': ']',
        '(': ')'
    }
    for i in s:
        if i in a:
            stack.append(i)
        else:
            if stack and a[stack[-1]] == i:
                stack.pop()
            else:
                return False
    if len(stack) == 0:
        return True
    else:
        return False


print(isValid(']}'))
