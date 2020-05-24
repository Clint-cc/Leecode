# !D:/Code/python
# -*- coding:utf-8 -*-
# @Author : Clint
# @Question : K中颜色小球，每个小球若干个 总数小于100，一个盒子能放N（N<=8）个小球
# @Thinking :

class Solution:
    def pick_ball_allways(self, K, N, nums):
        # 一定是用DFS
        ans = []
        self.dfs(0, N, 0, nums, [], ans)
        return ans

    def dfs(self, cur_count, N, index, nums, path, ans):
        '''
        :param cur_count: 当前盒子里放球的数目
        :param N: 小盒子能放球的数目
        :param index: 小球颜色的索引
        :param nums: 每一种颜色小球的个数,它的长度就是颜色种类数目
        :param path: 一种结果
        :param ans: 所有结果
        :return:
        '''

        # 条件满足时, 更新结果，进行下一次遍历
        if cur_count == N:
            path = path + [0] * (len(nums) - index)
            ans.append(path)
            return

        # 条件不满足时, 直接进行下一次遍历
        if cur_count > N or index >= len(nums):
            return

        for i in range(nums[index] + 1):
            self.dfs(cur_count + i, N, index + 1, nums, path[:] + [i], ans)


s = Solution()
print(s.pick_ball_allways(3, 3, [1, 2, 3]))
