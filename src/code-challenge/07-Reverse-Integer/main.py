#!/usr/bin/env python3

"""
LeetCode: 07
Url: https://leetcode.com/problems/reverse-integer/
"""

import unittest


class Solution:
    def main(self, num):
        minus = ""
        min_num = -2**31
        max_num = 2**31 - 1

        if str(num)[0] == '-':
            minus = "-"
            num = int(str(num)[1::])

        reverse_num = int(minus+str(num)[::-1])

        if reverse_num <= min_num or reverse_num >= max_num:
            return 0

        return reverse_num


class TestSolution(unittest.TestCase):
    def test_main(self):
        s = Solution()
        self.assertEqual(s.main(123), 321)
        self.assertEqual(s.main(-123), -321)
        self.assertEqual(s.main(120), 21)
        self.assertEqual(s.main(1534236469), 0)


if __name__ == "__main__":
    unittest.main()

