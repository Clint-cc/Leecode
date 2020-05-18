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

nums = [7, 1, 3, 4, 8, 0, 9, 5, 6, 2]


# 升序 建大根堆
def sift(nums, low, high):
    i = low  # 最开始的父节点
    j = 2 * i + 1  # 最开始的左子节点
    tmp = nums[i]
    while j <= high:  # 如果子节点没到子树的最后，那么继续
        if nums[j] < nums[j + 1] and j + 1 <= high:
            j += 1
        if tmp < nums[j]:  # 如果父节点比子节点小
            nums[i] = nums[j]  # 那么父子节点互换
            i = j  # 字节点成为父节点
            j = 2 * i + 1  # 新子节点
        else:
            break
    nums[i] = tmp


def heap_sort(nums):
    n = len(nums)
    for i in range(n // 2 - 1, -1, -1):
        sift(nums, i, n - 1)
    # 堆建好了
    for i in range(n - 1, -1, -1):  # i指向堆的最后
        nums[0], nums[i] = nums[i], nums[0]  # 父节点出局，堆的最后叶子节点上位
        sift(nums, 0, i - 1)  # 调整出新的父节点


heap_sort(nums)
print(nums)  # 升序排列，若要降序排列，则建小根堆即
