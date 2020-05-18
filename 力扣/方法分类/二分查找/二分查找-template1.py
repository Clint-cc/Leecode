# !D:/Code/python
# -*- coding:utf-8 -*-
# @Author : Clint
# @Question : 寻找一个数，（基本的二分查找）
# @Thinking : 不出现else，把每个情况都用elif写清楚，这样可以很好的展示细节


# 基本的二分查找
def Binary_Search(nums, target):
    # 确定查找的上下界
    low, high = 0, len(nums) - 1

    while low <= high:  # 当low == high时还剩下最后一个值需要进行检验
        # mid = (low + high) // 2
        mid = low + (high - low) // 2  # 不用上面的写法为了防止溢出
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid + 1  # +1是因为mid已经验证过不符合条件，新的区间又mid+1开始
        elif nums[mid] > target:
            high = mid - 1  # 这里+1同上面原因相同
    return -1  # 执行结束但是没有找到


nums, target = [-1, 0, 3, 5, 9, 12], 9
print(Binary_Search(nums, target))
