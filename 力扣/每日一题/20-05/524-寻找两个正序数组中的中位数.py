# !D:/Code/python
# -*- coding:utf-8 -*-
# @Author : Clint
# @Question : 
# @Thinking :


class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        # 暴力排序合并查找，O((m+n)log(m+n))
        num = sorted(nums1 + nums2)
        print(num)
        n = len(num)
        if n % 2 == 0:
            return (num[n // 2] + num[n // 2 - 1]) / 2
        else:
            return format(num[n // 2], '.1f')

        # 二分查找，O(log(m+n))
        # ...


s = Solution()
print(s.findMedianSortedArrays([1, 4, 5, 8, 9], [2, 7]))
