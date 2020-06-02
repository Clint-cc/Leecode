# !D:/Code/python
# -*- coding:utf-8 -*-
# @Author : Clint
# @Question : 
# @Thinking :
from typing import List


class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        # 使用队列
        # from collections import deque
        # sorted_nums = deque([])
        # for num in nums:
        #     if num % 2 == 0:
        #         sorted_nums.append(num)
        #     else:
        #         sorted_nums.appendleft(num)
        # return list(sorted_nums)

        # 使用双指针
        left, right = 0, len(nums) - 1
        while left < right:
            if nums[left] % 2 == 0 and nums[right] % 2 == 1:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
            elif nums[left] % 2 == 1 and nums[right] % 2 == 0:
                left += 1
                right -= 1

            elif nums[left] % 2 == 1:
                left += 1

            elif nums[right] % 2 == 0:
                right -= 1

        return nums


s = Solution()
print(s.exchange([1, 2, 3, 4]))
