#!/bin/env python3

class Solution:
    def removeDuplicates(self, nums):
        x = 0
        while x < len(nums):
            if nums.count(nums[x]) > 1 and type(nums[x]) == int:
                nums.pop(x)
                nums.append('_')
                x -= 1
            x += 1
        return len(nums) - nums.count("_"), nums

nums = [1,1,2]
#nums = [0,0,1,1,1,2,2,3,3,4]

s = Solution()
print(s.removeDuplicates(nums))

