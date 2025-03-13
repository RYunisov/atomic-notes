#!/bin/env python3

import unittest

'''
LeetCode 45 Jump Game II
Greedy version
https://leetcode.com/problems/jump-game-ii/
'''

class Solution:
    def jump(self, nums):
        print(f'Given: {nums}')
        n = len(nums) - 1
        steps = 0
        maxx = 0 

        x = 0

        while x <= n-1:
            print(f"{x}")
            x += 1

        print(f"FINAL: {steps}, {x}, {nums[x]}")
        return steps

class TestSolution(unittest.TestCase):
    def test_result(self):
        s = Solution()
        self.assertEqual(s.jump([1,1,1,1,4]), 4)
        self.assertEqual(s.jump([2,2,1,1,4]), 3)
        self.assertEqual(s.jump([2,3,1,1,4]), 2)
        self.assertEqual(s.jump([2,3,0,1,4]), 2)
        self.assertEqual(s.jump([2,5,0,0,0]), 2)
        self.assertEqual(s.jump([3,2,1,0,4]), 0)

if __name__ == '__main__':
    unittest.main()

