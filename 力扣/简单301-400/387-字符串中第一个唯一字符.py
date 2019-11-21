# -*- coding:utf-8 -*-
# @Author  : Clint


def firstUniqChar(s):
    """
    :type s: str
    :rtype: int
    """
    if not len(s):
        return -1
    for i in range(len(s)):
        if s.find(s[i], i + 1) == -1 and s.count(s[i]) == 1:
            return i
    return -1
