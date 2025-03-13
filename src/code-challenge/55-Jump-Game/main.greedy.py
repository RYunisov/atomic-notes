#!/bin/env python3

'''
Leetcode 55
Greedy version
https://leetcode.com/problems/jump-game/
'''

class Solution:
    def canJump(self, nums):
        print(f"Given: {nums}")
        goal = len(nums) - 1
        for x in range(len(nums)-1, -1, -1):
            print(f"I:{x}, J:{nums[x]}, goal: {goal}")
            if x + nums[x] >= goal:
                goal = x

        return goal == 0        

nums = [2,3,1,1,4]
nums = [3,2,1,0,4]
#nums = [2,3,0,1,4]
#nums = [2,5,0,0]

s = Solution()
print(s.canJump(nums))

