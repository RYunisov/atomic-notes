#!/bin/env python3

#
# https://leetcode.com/problems/partition-equal-subset-sum/
#

class Solution:
    def canPartition(self, nums):
        m = max(nums)
        summ = 0
        for x in nums:
            if x != m:
                summ = summ + x

        if summ == m:
            return True

        return False

#nums = [1,2,3,5]
#nums = [1,5,11,5]
nums = [1,1,1,1,1,5]

s = Solution()
print(s.canPartition(nums))

