#!/bin/env python3

#
# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii
#

class Solution:
    def removeDuplicates(self, nums):
        print(f"Given: {nums}")
        x = 0
        count = 1
        while x < len(nums) - 1:
            if nums[x] == nums[x-1] and nums[x] != "_":
                if count >= 2:
                    nums.pop(x)
                    nums.append("_")
                    x -= 1
                count += 1
            else:
                count = 1
            x += 1
        return len(nums) - str(nums).count('_'), nums

#nums = [1,1,1,2,2,3]
nums = [0,0,1,1,1,1,2,3,3]
#nums = [0,0,0,0,0,0,0,1,2,3,3,3,3,4,4,4,5,6,6,7,7,7]

s = Solution()
print(s.removeDuplicates(nums))

