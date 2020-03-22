# !D:/Code/python
# -*- coding:utf-8 -*-
# @Author : Clint

from 力扣 import calculate_time as cal

# 方法一：
'''  

@cal.cal_time
def isPowerOftwo(num):        
    x = 0
    while 4 ** x <= num:
        if 4 ** x == num:
            return True
        else:
            x += 1
    return False


print(isPowerOftwo(1048576))
'''

# 方法二：一行代码
'''
def isPowerOfFour(num):
    return num>0 and (num & num - 1)==0 and (num & 0x55555555)== num


print(isPowerOfFour(1))
'''


# 方法三：
def isPowerOfFour(num):
    if num % 3 == 1:
        return True
    else:
        return False


print(isPowerOfFour(10))
