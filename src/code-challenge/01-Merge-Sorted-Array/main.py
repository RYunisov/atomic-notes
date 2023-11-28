#!/bin/env python3

# 1 2 3 
# 2 5 6 
# [1, 2, 3]

class Solution:
    def merge(self, nums1, m, nums2, n):
        nums_temp = []
        if n == 0:
           return nums1
        elif m == 0:
           nums1 = nums2
           return nums1
        nums1 = nums1[:m]
        for i in nums2:
            nums1.append(i)
        return sorted(nums1)

nums1 = [1,2,3,0,0,0]
m = 3 
nums2 = [2,5,6]
n = 3

#nums1 = [1]
#m = 1 
#nums2 = [] 
#n = 0

#nums1 = [0] 
#m = 0 
#nums2 = [1] 
#n = 1

solution = Solution()
print(solution.merge(nums1, m, nums2, n))

