# !D:/Code/python
# -*- coding:utf-8 -*-
# @Author : Clint
# @Question : 
# @Thinking :
from typing import List


class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        if k == 0 or not arr: return []

        res = arr[:k]  # 记录结果
        print(res)
        self.heap_sort(res)

        for i in range(k, len(arr)):
            if arr[i] < res[-1]:
                res.pop()
                res.append(arr[i])
                self.heap_sort(res)
                print(res)
            else:
                continue;
        return res

    # 这里调用大根堆API
    def sift(self, data_list, low, high):  # 升序 建大根堆
        i = low  # 最开始的父节点
        j = 2 * i + 1  # 最开始的左子节点
        tmp = data_list[i]
        while j < high:  # 如果子节点没到子树的最后，那么继续
            if data_list[j] < data_list[j + 1] and j + 1 <= high:
                j += 1
            if tmp < data_list[j]:  # 如果父节点比子节点小
                data_list[i] = data_list[j]  # 那么父子节点互换
                i = j  # 字节点成为父节点
                j = 2 * i + 1  # 新子节点
            else:
                break
        data_list[i] = tmp

    def heap_sort(self, data_list):
        n = len(data_list)
        for i in range(n // 2 - 1, -1, -1):
            self.sift(data_list, i, n - 1)
        # 堆建好了
        for i in range(n - 1, -1, -1):  # i指向堆的最后
            data_list[0], data_list[i] = data_list[i], data_list[0]  # 父节点出局，堆的最后叶子节点上位
            self.sift(data_list, 0, i - 1)  # 调整出新的父节点


s = Solution()
print(s.getLeastNumbers([0, 1, 1, 2, 4, 4, 1, 3, 3, 2], 6))
