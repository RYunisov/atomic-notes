#!/usr/bin/env python3

"""
LeetCode: 06
Url: https://leetcode.com/problems/zigzag-conversion/
"""

import unittest


class Solution:
    def main(self, line, num):
        if num == 1:
            return line

        arr = [""] * num
        row_idx = 1
        is_up   = True

        for i in line:
            print(arr, row_idx, is_up)
            row_arr[row_idx - 1] += i
            if row_idx == num:
                is_up = False
            elif row_idx == 1:
                is_up = True

            if is_up:
                row_idx += 1
            else:
                row_idx -= 1

        return "".join(row_arr)


class TestSolution(unittest.TestCase):
    def test_main(self):
        s = Solution()
        self.assertEqual(s.main("A", 1), "A")
        self.assertEqual(s.main("PAYPALISHIRING", 3), "PAHNAPLSIIGYIR")
        self.assertEqual(s.main("PAYPALISHIRING", 4), "PINALSIGYAHRPI")


if __name__ == "__main__":
    unittest.main()
 
