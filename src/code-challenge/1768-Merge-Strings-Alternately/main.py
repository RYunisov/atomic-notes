#!/usr/bin/env python3

"""
LeetCode: 1768
Url: https://leetcode.com/problems/merge-strings-alternately/
"""


import unittest


class Solution:
    def main(self, s1, s2):
        res = ""
        i = 0
        maxx = max(len(s1), len(s2))

        while i < maxx:
            if i < len(s1) and i < len(s2):
                print(f"DEBUG01: {i} {s1}, {s2}, {res}")
                res += s1[i]
                res += s2[i]

            if i < len(s1) and i > len(s2):
                print(f"DEBUG02: {i} {s1}, {s2}, {res}")
                res += s1[i-1::]

            if i < len(s2) and i > len(s1):
                print(f"DEBUG03: {i} {s1}, {s2}, {res}")
                res += s2[i-1::]

            i += 1

        return res


class TestSolution(unittest.TestCase):
    def test_main(self):
        s = Solution()
        self.assertEqual(s.main("abc", "pqr"), "apbqcr")
        self.assertEqual(s.main("ab", "pqrs"), "apbqrs")
        self.assertEqual(s.main("abcd", "pq"), "apbqcd")


if __name__ == "__main__":
    unittest.main()
