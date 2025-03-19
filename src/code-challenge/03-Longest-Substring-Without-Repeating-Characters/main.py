#!/bin/env python3

"""
LeetCode: 03
Url: https://leetcode.com/problems/longest-substring-without-repeating-characters/
"""

import unittest


class Solution:
    def get_dupl(self, line):
        for i in range(len(line)):
            if line.count(line[i]) > 1:
                return False
        return True

    def get_substr(self, line):
        res = []
#        print("DEBUG: ", line)

        for i in range(len(line)):
            if self.get_dupl(line[i:]):
                res.append(line[i:])
#            print("DEBUG: ", res)
        return res

    def main(self, line):
        maxx = 0
        prev_maxx = 0
        for i in range(len(line)+1):
            prev_maxx = [ len(x) for x in self.get_substr(line[:i]) ]
            prev_maxx = max(prev_maxx, default=0)
            if maxx < prev_maxx:
                maxx = prev_maxx
        return maxx


class TestSolution(unittest.TestCase):
    def test_main(self):
        s = Solution()
        self.assertEqual(s.main("abcabcbb"), 3)
        self.assertEqual(s.main("bbbbb"), 1)
        self.assertEqual(s.main("pwwkew"), 3)
        self.assertEqual(s.main("anviaj"), 5)
        self.assertEqual(s.main("jbpnbwwd"), 4)
        self.assertEqual(s.main("dvdf"), 3)


if __name__ == "__main__":
    unittest.main()

