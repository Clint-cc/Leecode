# -*- coding:utf-8 -*-
# @Author  : Clint

'''
    stack = []
    a = ""
    for i in s:
        if i != ' ':
            stack.append(i)
        else:
            for j in list(reversed(stack)):
                a += j
            a += " "
            stack = []
    for k in list(reversed(stack)):
        a += k
    a += " "
    return a
'''


def reverseWords(s):      # s = 'I am the man'

    return " ".join(ss[::-1] for ss in s.split())


print(reverseWords('I am the man'))
