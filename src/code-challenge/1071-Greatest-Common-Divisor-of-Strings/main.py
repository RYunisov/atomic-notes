#!/usr/bin/env python3

"""
LeetCode: 1071
Url: https://leetcode.com/problems/greatest-common-divisor-of-strings/
"""


import unittest


class Solution:
    def largestString(self, n1, n2):
        if n2 == 0:
            return n1
        return self.largestString(n2, n1 % n2)

    def main(self, str1, str2):
        if not str1+str2 == str2+str1:
            return ""

        gcd = 0
        n1 = len(str1)
        n2 = len(str2)

        if n1 > n2:
            gcd = self.largestString(n1, n2)
        else:
            gcd = self.largestString(n2, n1)

        return str1[0:gcd]


class TestSolution(unittest.TestCase):
    def test_main(self):
        s = Solution()
        self.assertEqual(s.main("ABCABC", "ABC"), "ABC")
        self.assertEqual(s.main("ABABAB", "ABAB"), "AB")
        self.assertEqual(s.main("LEET", "CODE"), "")
        self.assertEqual(s.main("ABCDEF", "ABC"), "")
        self.assertEqual(s.main("TAUXXTAUXXTAUXXTAUXXTAUXX", "TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX"), "TAUXX")


if __name__ == "__main__":
    unittest.main()
