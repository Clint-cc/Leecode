# !D:/Code/python
# -*- coding:utf-8 -*-
# @Author : Clint
# @Question : 
# @Thinking :


class Solution:
    def guiwei(self, nums):
        left, right = 0, len(nums) - 1
        while left < right:  # [1,1,1,1,2,2,2,2]
            if ((left + 1) % 2 == 1 and nums[left] % 2 == 0) and ((right + 1) % 2 == 0 and nums[right] % 2 == 1) or \
                    ((left + 1) % 2 == 0 and nums[left] % 2 == 1) and ((right + 1) % 2 == 1 and nums[right] % 2 == 0):
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
                continue

            if (left + 1) % 2 == 1:
                if nums[left] % 2 == 1:
                    left += 1

            elif (left + 1) % 2 == 1:
                if nums[left] % 2 == 1:
                    left += 1

            if (right + 1) % 2 == 1:
                if nums[right] % 2 == 1:
                    right -= 1

            elif (right + 1) % 2 == 0:
                if nums[right] % 2 == 0:
                    right -= 1
        return nums


s = Solution()
print(s.guiwei([3, 3, 3, 3, 2, 2, 2, 2]))
