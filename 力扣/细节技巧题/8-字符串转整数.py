# !D:/Code/python
# -*- coding:utf-8 -*-
# @Author : Clint
# @Question : 
# @Thinking :


class Solution:
    def myAtoi(self, s):
        # 正则表达式
        return max(min(int(*re.findall('^[\+\-]?\d+', s.lstrip())), 2 ** 31 - 1), -2 ** 31)
        '''
        	i = int(*re.findall('^[\+\-]?\d+', s.lstrip())),相当于result = re.findall('^[\+\-]?\d+', s.lstrip())
            i = int(*result),这个result是一个列表，而int接受的是单个的参数，所以需要通过*的unpack运算将它转换为元组。
            int(*result)其实就是 int(result[0])。
            
            max(min(数字, 2**31 - 1), -2**31)  # 防止结果越界
        '''
