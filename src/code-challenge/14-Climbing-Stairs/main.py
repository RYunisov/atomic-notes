#!/bin/env python3

"""
Problem:
https://leetcode.com/problems/climbing-stairs/
"""

class Solution:
    def climbStairs(self, n):
        print(f"Given: {n}")
        one, two = 1, 1

        for i in range(n - 1):
            temp = one
            one = one + two
            two = temp

        return one


n = 5

s = Solution()
print(s.climbStairs(n))

