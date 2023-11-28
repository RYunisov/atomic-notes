#!/bin/env python3

#
# https://leetcode.com/problems/remove-element/?envType=study-plan-v2&envId=top-interview-150
#

class Solution:
    def removeElement(self, nums, n):
        k = 0

        while k < len(nums):
            if nums[k] == n:
                nums.pop(k)
                nums.append("_")
                k -= 1
            k += 1
        
        res = len(nums) - nums.count("_")
        return res, nums

#nums = [3,2,2,3]
#val = 3

nums = [0,1,2,2,3,0,4,2]
val = 2

s = Solution()
print(s.removeElement(nums, val))

