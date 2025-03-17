#!/bin/env python3

"""
LeetCode: 02
Url: https://leetcode.com/problems/add-two-numbers/description/
"""

import unittest


class Solution:
    def main(self, l1, l2):
        rev_l1 = l1[::-1]
        rev_l2 = l2[::-1]

        print(rev_l1)
        print(rev_l2)

        # Converting the list of Int into single Int
        rev_l3 = int(''.join(map(str, rev_l1))) + int(''.join(map(str, rev_l2)))

        # Converting the single Int into the list of Int
        rev_l3 = [ int(x) for x in str(rev_l3) ]

        print(rev_l3[::-1])
        return rev_l3[::-1]


class TestSolution(unittest.TestCase):
    def test_main(self):
        s = Solution()
        self.assertEqual(s.main([2,4,3],[5,6,4]), [7,0,8])
        self.assertEqual(s.main([0],[0]), [0])
        self.assertEqual(s.main([2,4,9],[5,6,4,9]), [7,0,4,0,1])
        self.assertEqual(s.main([9,9,9,9,9,9,9],[9,9,9,9]), [8,9,9,9,0,0,0,1])


if __name__ == "__main__":
    unittest.main()

