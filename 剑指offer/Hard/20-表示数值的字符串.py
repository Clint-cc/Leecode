# !D:/Code/python
# -*- coding:utf-8 -*-
# @Author : Clint
# @Question : 
# @Thinking :


import re


class Solution:
    # 关于正则的说明：
    '''
        ?:匹配0个或1个前面的字符
        \d+:匹配1个或多个数字
        \d*:匹配0个或多个数字
    '''

    def isNumber(self, s: str) -> bool:
        p = re.compile(r'^[+-]?(\.\d+|\d+\.?\d*)([eE][+-]?\d+)?$')
        return bool(p.match(s.strip()))
