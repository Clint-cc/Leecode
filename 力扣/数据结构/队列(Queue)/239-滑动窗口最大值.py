# !D:/Code/python
# -*- coding:utf-8 -*-
# @Author : Clint
# @Question : 给定一个数组nums，有一个大小为k的滑动窗口从数组的最左侧移动到数组的最右侧，你只可以看到
#             在滑动窗口内的k个数字。滑动窗口每次只向右移动一位。返回滑动窗口中的最大值。
# @Thinking : 要求线性时间,单调队列

class Solution:
    def maxSlidingWindow1(self, nums, k):
        from collections import deque
        window, res = deque(), []
        for i in range(len(nums)):
            if i < k - 1:  # 填满前 k - 1个元素的窗口
                window.append(nums[i])
            else:
                window.append(nums[i])  # 开始向前移动
                # 这里需要计算window中的最大值,并添加到res中
                res.append(max(window))

                window.popleft()
        return res

    def maxSlidingWindow2(self, nums, k):
        from collections import deque
        window, res = deque(), []
        for i in range(len(nums)):
            if i < k - 1:
                # 单调对列的push操作
                while window and window[-1] < nums[i]:
                    window.pop()
                window.append(nums[i])
            else:
                # 单调对列的push操作
                while window and window[-1] < nums[i]:
                    window.pop()
                window.append(nums[i])

                # 一步一步的录入结果
                res.append(window[0])

                # 单调对列的pop操作
                if window and window[0] == nums[i - k + 1]:
                    window.popleft()
        return res


s = Solution()
print(s.maxSlidingWindow1([1, 3, -1, -3, 5, 3, 6, 7], 3))
# print(s.maxSlidingWindow2([1,3,-1,-3,5,3,6,7], 3))
