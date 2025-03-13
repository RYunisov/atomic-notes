#!/bin/env python3

#
# https://leetcode.com/problems/majority-element
#

class Solution:
    def majorityElement(self, nums):
        x = 1
        max_element = nums[0]
        while x < len(nums) - 1:
            if nums[x] > nums[x-1]:
                max_element = nums[x]
            x += 1
        return max_element, max(nums)

#nums = [1,2,3,4,115,56,1,0]
#nums = [3,2,3]
nums = [2,2,1,1,1,2,2]

s = Solution()
print(s.majorityElement(nums))

