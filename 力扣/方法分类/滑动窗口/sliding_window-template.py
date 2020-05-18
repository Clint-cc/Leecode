# !D:/Code/python
# -*- coding:utf-8 -*-
# @Author : Clint
# @Question : 
# @Thinking :
from collections import defaultdict


# 这里是滑动窗口的代码框架
def sliding_window(s, t):
    need = defaultdict(int)
    for s_char in t:
        need[s_char] += 1
    left, right = 0, 0
    valid = 0

    while right < len(s):
        c = s[right]  # c是将移入窗口的字符
        right += 1  # 右移窗口

        # 进⾏窗⼝内数据的⼀系列更新
        # ...

        # 判断左侧窗口是否要收缩
        '''
         while (window needs shrink):
            d = s[left]  # 将要移除窗口的字符
            left += 1  # 左移窗口
            
            # 进⾏窗⼝内数据的⼀系列更新
            # ... 
        '''
