# -*- coding:utf-8 -*-
# @Author  : Clint
# @File    : Calculate_Time.py

# import sys
# sys.setrecursionlimit(10000)     # 将递归数设置为10000
import time


def cal_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        x = func(*args, **kwargs)
        end_time = time.time()
        print(func.__name__ + "的Time cost:", end_time - start_time)
        return x

    return wrapper
