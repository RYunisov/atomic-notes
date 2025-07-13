#!/usr/bin/env python3

'''
LeetCode: 303
Url: https://leetcode.com/problems/range-sum-query-immutable
'''

import unittest


class Solution:
    def main(self, nums, indexes):
        arr = nums[indexes[0]:indexes[1]+1]
        return sum(arr)


class TestSolution(unittest.TestCase):
    def test_main(self):
        s = Solution()
        nums = [-2,0,3,-5,2,-1]
        self.assertEqual(s.main(nums, [0,2]),1)
        self.assertEqual(s.main(nums, [2,5]),-1)
        self.assertEqual(s.main(nums, [0,5]),-3)


if __name__ == "__main__":
    unittest.main()
