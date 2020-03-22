# !D:/Code/python
# -*- coding:utf-8 -*-
# @Author : Clint
# @Question : 把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
#             输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。例如，
#             数组 [3,4,5,1,2] 为 [1,2,3,4,5] 的一个旋转，该数组的最小值为1。


def minArray(numbers):
    '''
    思路：二分法，只是多出判断，如果mid>right,那最小值一定在右边
    :param numbers: [7,0,1,1,1,1,2,3,4]
    '''
    left, right = 0, len(numbers) - 1
    while left < right:
        mid = (left + right) // 2
        if numbers[mid] < numbers[right]:
            right = mid
        elif numbers[mid] > numbers[right]:
            left = mid + 1
        else:
            right -= 1
    return numbers[left]


print(minArray([7, 0, 1, 1, 1, 1, 2, 3, 4]))
