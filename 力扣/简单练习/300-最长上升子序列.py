# !D:/Code/python
# -*- coding:utf-8 -*-
# @Author : Clint
# @Question : 给定一个无序的整数数组，找到其中最长上升子序列的长度。


def lengthOfLIS(nums):
    '''
    思路：遍历数组，当前的下一个元素大于当前,count+1,当不大于时比较count和max_count,
          最后输出max_count
    这题有坑： 输入[10,9,2,5,3,7,101,18]，输出4，解释：最长的上升子序列是 [2,3,7,101]，它的长度是 4
    :param nums:
    :return:
    '''
    count = 1
    max_count = 1
    for i in range(len(nums) - 1):
        if nums[i + 1] >= nums[i]:
            count += 1
        else:
            if count > max_count:
                max_count = count
                count = 1
            else:
                count = 1
    if max_count < count:
        max_count = count
    return max_count


# 动态规划
def lengthOfLIS(nums):
    if not nums:
        return 0
    dp = [1] * len(nums)
    for i in range(len(nums)):
        for j in range(i):
            if nums[j] < nums[i]:  # 如果要求非严格递增，将此行 '<' 改为 '<=' 即可。
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)


# 二分查找
def lengthOfLIS(nums):
    d = []
    for n in nums:
        if not d or n > d[-1]:
            d.append(n)
        else:
            l, r = 0, len(d) - 1
            loc = r
            while l <= r:
                mid = (l + r) // 2
                if d[mid] >= n:
                    loc = mid
                    r = mid - 1
                else:
                    l = mid + 1
            d[loc] = n
    return len(d)


print(lengthOfLIS([1, 2, 5, 3, 7, 11, 18]))
