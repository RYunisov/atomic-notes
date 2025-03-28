#!/usr/bin/env python3

"""
LeetCode: 10
Url: https://leetcode.com/problems/regular-expression-matching/
"""

import unittest
import re


class Solution:
    def main(self, line, pattern):
        p = re.compile(pattern)
        if p.fullmatch(line):
            return True
        return False


class TestSolution(unittest.TestCase):
    def test_main(self):
        s = Solution()
        self.assertEqual(s.main("aa", "a"), False)
        self.assertEqual(s.main("aa", "a*"), True)
        self.assertEqual(s.main("aa", ".*"), True)
        self.assertEqual(s.main("aab", "c*a*b"), True)


if __name__ == "__main__":
    unittest.main()

