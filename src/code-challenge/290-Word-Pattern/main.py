#!/usr/bin/env python

"""
LeetCode: 290
Url: https://leetcode.com/problems/word-pattern
"""

import unittest


class Solution:
    def main(self, pattern, s):
        hash = {}

        for k, v in enumerate(pattern):
            value = s.split(" ")[k]
            if v in hash:
                if hash[v] != value:
                    return False
            else:
                hash[v] = value
        return True


class TestSolution(unittest.TestCase):
    def test_main(self):
        s = Solution()
        self.assertEqual(s.main('abba', 'dog cat cat dog'), True)
        self.assertEqual(s.main('abba', 'dog cat cat fish'), False)
        self.assertEqual(s.main('aaaa', 'dog cat cat dog'), False)
        self.assertEqual(s.main('aaab', 'cat cat cat dog'), True)


if __name__ == '__main__':
    unittest.main()
