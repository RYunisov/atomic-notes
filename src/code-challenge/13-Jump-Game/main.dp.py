#!/bin/env python3

'''
Leetcode 55 
Dynamic Programming Version
https://leetcode.com/problems/jump-game/
'''

class Solution:
    def canJump(self, nums):
        print(f"Given: {nums}")
        n = len(nums) - 1
        maxum = n
        
        while n > 0:
            print(f"ID:{n} Num:{nums[n]}")
            if nums[n-1] >= maxum - (n - 1):
                print(f"BF: {n} {maxum} {nums[n-1]}")
                maxum = n - 1
                print(f"AF: {n} {maxum} {nums[n-1]}")
            n -= 1

        return maxum == 0

nums = [2,3,1,1,4]
nums = [3,2,1,0,4]
nums = [2,3,0,1,4]
nums = [1,1,1,1,4]
#nums = [2,5,0,0]
#nums = [4,0,0,0,0]

s = Solution()
print(s.canJump(nums))

