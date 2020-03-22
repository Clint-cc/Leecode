# -*- coding:utf-8 -*-
# @Author  : Clint
# @File    : calculate_time.py
import time


def cal_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        x = func(*args, **kwargs)
        end_time = time.time()
        print(func.__name__+"的Time cost:", end_time-start_time)
        return x
    return wrapper
