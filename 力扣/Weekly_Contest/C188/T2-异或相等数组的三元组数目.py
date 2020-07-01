# !D:/Code/python
# -*- coding:utf-8 -*-
# @Author : Clint
# @Question : 
# @Thinking :


class Solution:
    # 暴力法，o(n^3), 超出时间限制
    def countTriplets(self, arr):
        n = len(arr)
        res = 0
        # tup_res = []
        for i in range(n - 1):
            for j in range(i + 1, n):
                a = 0
                a ^= arr[i]
                tmp = j - 1
                while tmp > i:
                    a ^= arr[tmp]
                    tmp -= 1

                for k in range(j, n):
                    b = 0
                    b ^= arr[j]
                    tmp2 = k
                    while tmp2 > j:
                        b ^= arr[tmp2]
                        tmp2 -= 1
                    if a == b:
                        res += 1
                        # tup_res.append((i,j,k))
        return res  # , tup_res

    # o(n^2)


s = Solution()
print(s.countTriplets([2, 3, 1, 6, 7]))
print(s.countTriplets([1, 1, 1, 1, 1]))
print(s.countTriplets([2, 3]))
print(s.countTriplets([3, 3]))
print(s.countTriplets([1, 3, 5, 7, 9]))
print(s.countTriplets([7, 11, 12, 9, 5, 2, 7, 17, 22]))
