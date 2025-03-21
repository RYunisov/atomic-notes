#!/bin/env python3

"""
LeetCode: 01
Url: https://leetcode.com/problems/two-sum/
"""

import unittest


class Solution:
    def main(self, nums, target):
        for i in range(0, len(nums)):
            for y in range(1, len(nums)):
                if nums[i] + nums[y] == target:
                    return [i, y]
        return ""


class TestSolution(unittest.TestCase):
    def test_main(self):
        s = Solution()
        self.assertEqual(s.main([2,7,11,15], 9), [0,1])
        self.assertEqual(s.main([3,2,4], 6), [1,2])
        self.assertEqual(s.main([3,3], 6), [0,1])
        self.assertEqual(s.main([3,4], ""), "")


if __name__ == "__main__":
    unittest.main()

