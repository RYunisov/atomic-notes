#!/usr/bin/env python3

'''
LeetCode: 167
Url: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
'''

import unittest


class Solution:
    def main(self, nums, target):
        i = 0
        j = len(nums)-1
        while i <= j:
            if nums[i] + nums[j] < target:
                i += 1
            elif nums[i] + nums[j] > target:
                j -= 1
            elif nums[i] + nums[j] == target:
                return [i+1,j+1]


class TestSolution(unittest.TestCase):
    def test_main(self):
        s = Solution()
        self.assertEqual(s.main([2,7,11,15], 9), [1,2])
        self.assertEqual(s.main([2,3,4], 6), [1,3])
        self.assertEqual(s.main([-1,0], -1), [1,2])


if __name__ == "__main__":
    unittest.main()
