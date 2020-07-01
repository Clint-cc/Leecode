# !D:/Code/python
# -*- coding:utf-8 -*-
# @Author : Clint
# @Question : 
# @Thinking :

class Solution:
    # 这是一个小树建堆的过程
    '''
    def heapify(self, nums, size, i):  # size表示数据的长度， 对第i个节点进行heapify
        left = 2 * i + 1
        right = 2 * i + 2
        max = i
        if (left < size and nums[left] > nums[max]):  # 注意条件，如果是叶子节点了，就无需判断了
            max = left
        if (right < size and nums[right] > nums[max]):
            max = right

        if max != i:
            nums[i], nums[max] = nums[max], nums[i]
    '''

    # 对整个数组进行建堆
    def build_heap(self, nums, size):
        # 这里采用for循环heapify，将所有父节点建堆
        # 也可以用递归进行heapify
        last_index = size - 1
        for i in range((last_index - 1) // 2, -1, -1):  # 这里只需要遍历到最后一个父结点就行
            # self.heapify(nums, size, i)
            left = 2 * i + 1
            right = 2 * i + 2
            max = i
            if (left < size and nums[left] > nums[max]):  # 注意条件，如果是叶子节点了，就无需判断了
                max = left
            if (right < size and nums[right] > nums[max]):
                max = right

            if max != i:
                nums[i], nums[max] = nums[max], nums[i]

    def heap_sort(self, nums):
        # nums = [4, 10, 3, 5, 1, 2]
        size = len(nums)

        # 1、建堆
        # self.build_heap(nums, size)

        # 2、交换
        for i in range(size - 1, -1, -1):
            self.build_heap(nums, i + 1)
            nums[i], nums[0] = nums[0], nums[i]
            # self.build_heap(nums, i)

        print(nums)


s = Solution()
s.heap_sort([7, 1, 3, 9, 10, 5, 6, 2, 13])
