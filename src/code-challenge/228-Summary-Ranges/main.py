#!/usr/bin/env python3

"""
LeetCode: 228
Url: https://leetcode.com/problems/summary-ranges/
"""

import unittest


class Solution:
    def main(self, nums):
        mass = []
        res = f"{nums[0]}"

        if len(nums) < 2:
            return [f"{nums[0]}"]

        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] != 1:
                if res != f"{nums[i-1]}":
                    res += "->"
                    res += f"{nums[i-1]}"

                mass.append(res)
                res = f"{nums[i]}"

            if i == len(nums)-1:
                if res != f"{nums[i]}":
                    res += "->"
                    res += f"{nums[i]}"
                mass.append(f"{res}")

        return mass


class TestSolution(unittest.TestCase):
    def test_main(self):
        s = Solution()
        self.assertEqual(s.main([0,1,2,4,5,7]), ["0->2","4->5","7"])
        self.assertEqual(s.main([0,2,3,4,6,8,9]), ["0","2->4","6","8->9"])
        self.assertEqual(s.main([0,2,3,4,6,8,10]), ["0","2->4","6","8","10"])
        self.assertEqual(s.main([0,1]), ["0->1"])
        self.assertEqual(s.main([0]), ["0"])
        self.assertEqual(s.main([-2147483648, -2147483647, 2147483647]), ["-2147483648->-2147483647", "2147483647"])


if __name__ == "__main__":
    unittest.main()
