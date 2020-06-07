# !D:/Code/python
# -*- coding:utf-8 -*-
# @Author : Clint
# @Question : 
# @Thinking :

class Solution:
    def findNthDigit(self, n: int) -> int:
        # 确定n所在的位数
        digit, start, count = 1, 1, 9
        while n > count:
            n -= count
            start *= 10  # 1, 10, 100, ...
            digit += 1  # 1,  2,  3, ...
            count = 9 * start * digit  # 9, 180, 2700, ...

        num = start + (n - 1) // digit

        s = str(num)  # 转化为 string
        res = int(s[(n - 1) % digit])
        return res


s = Solution()
print(s.findNthDigit(1001))
