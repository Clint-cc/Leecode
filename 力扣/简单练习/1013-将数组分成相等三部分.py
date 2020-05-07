# !D:/Code/python
# -*- coding:utf-8 -*-
# @Author : Clint
# @Question : 给你一个整数数组 A，只有可以将其划分为三个和相等的非空部分时才返回 true，
#             否则返回 false。

# 此方法超出时间限制
'''
def canThreePartsEqualSum(nums):   # [0,-1,1,-1,1]
    if sum(nums) % 3 == 0:
        a, b, c= [], [], []
        k = int(sum(nums) / 3)

        for i in nums:
            if sum(a) != k or not a:
                a.append(i)
            elif sum(b) != k or not b:
                b.append(i)
            else:
                c.append(i)
        if not c:
            return False
        else:
            return True
    else:
        return False
'''


#  [0,2,1,-6,6,-7,9,1,2,0,1]
#   0 1 2  3 4  5 6 7 8 9 10

# 迫不得已只能用双指针
def canThreePartsEqualSum(nums):  # [3,3,6,5,-2,2,5,1,-9,4]
    if sum(nums) % 3 == 0:
        i, j = 0, len(nums) - 1
        tmp1, tmp2 = nums[i], nums[j]
        k = int(sum(nums) / 3)
        while i < j:
            if tmp1 != k:
                i += 1
                tmp1 += nums[i]

            if tmp2 != k:
                j -= 1
                tmp2 += nums[j]

            if tmp1 == k and tmp2 == k:
                return True
                break
        return False
    else:
        return False


print(canThreePartsEqualSum([1, -1, 1, -1]))
