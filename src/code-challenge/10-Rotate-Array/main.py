#!/bin/env python3

#
# https://leetcode.com/problems/rotate-array
#

class Solution:
    def rotate(self, nums, k):
        print(f"Given: {nums}:{k}")
        x = 0
        while x < k:
            print(f"{x}:{nums}")
            nums.insert(0, nums[-1])
            nums.pop()
            x += 1
        return nums

nums = [1,2,3,4,5,6,7]; k = 3
#nums = [-1,-100,3,99]; k = 2

s = Solution()
print(s.rotate(nums, k))

