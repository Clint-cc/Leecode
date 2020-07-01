# !D:/Code/python
# -*- coding:utf-8 -*-
# @Author : Clint
# @Question : 
# @Thinking : -----如下：------
'''
    堆：
　　　　大根堆：一颗完全二叉树，满足任一节点都比其孩子节点大
　　　　小根堆：一颗完全二叉树，满足任一节点都比其孩子节点小
    1.建立堆（sift）；
    2.得到堆顶，为最大元素
    3.去掉堆顶，将堆最后一个元素放到堆顶，此时可通过一次调整重新使堆有序；
    4.堆顶元素为第二大元素；
    5.重复步骤3，直到堆变空；
'''




# 升序 建大根堆
def sift(nums, size):
    last_p = (size - 1) // 2
    for i in range(last_p, -1, -1):
        ma = i
        left = i * 2 + 1
        right = i * 2 + 2

        if (left < size and nums[left] > nums[ma]):
            ma = left
        if (right < size and nums[right] > nums[ma]):
            ma = right
        if ma != i:
            nums[i], nums[ma] = nums[ma], nums[i]


def heap_sort(nums):
    n = len(nums)

    for i in range(n - 1, -1, -1):
        sift(nums, i + 1)
        nums[0], nums[i] = nums[i], nums[0]
    print(nums)


nums = [7, 1, 3, 4, 8]
heap_sort(nums)
