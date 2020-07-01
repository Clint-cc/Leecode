# !D:/Code/python
# -*- coding:utf-8 -*-
# @Author : Clint
# @Question : 元素计数
# @Thinking :
from typing import List


class Solution:
    def countElements(self, arrs: List[int]):
        element_set = set(arrs)
        cnt = 0
        for arr in arrs:
            if arr + 1 in element_set:
                cnt += 1
        return cnt


'''
        hash_table = defaultdict(int)
        # 得到巧克力的小朋友数  
        num = 0
        for i in arr: 
            # 统计拿到数字i的小朋友人数            
            hash_table[i] += 1
        for i in hash_table: 
            # 判断是否有拿到i+1的小朋友            
            if i + 1 in hash_table: 
                # 如果有，拿到i的小朋友每发巧克力一块！
                num += hash_table[i]
        
        # 总共有多少个小朋友拿到巧克力呢？        
        return num
'''

s = Solution()
print(s.countElements([1, 1, 2, 2]))
