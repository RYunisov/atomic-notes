#!/usr/bin/env python3

"""
LeetCode: 08
Url: https://leetcode.com/problems/string-to-integer-atoi/
"""


import unittest


class Solution:
    def atoi(self, sym):
        try:
            if int(sym) or int(sym) == 0:
                num = sym
            return num
        except:
            return False

    def main(self, line):
        temp_num = "0"
        minus = False

        s_num = line.strip()

        if s_num[0] == '-':
            s_num = s_num[1::]
            minus = True

        for k, v in enumerate(s_num):
            print(f"DEBUG: {temp_num}, {s_num}, {k}: {self.atoi(v)}")

            if self.atoi(v):
                temp_num += v
            else:
                break

        if minus:
            temp_num = "-" + temp_num

        return int(temp_num)


class TestSolution(unittest.TestCase):
    def test_main(self):
        s = Solution()
        self.assertEqual(s.main("42"), 42)
        self.assertEqual(s.main(" -042"), -42)
        self.assertEqual(s.main("1337c0d3"), 1337)
        self.assertEqual(s.main("0-1"), 0)
        self.assertEqual(s.main("words and 987"), 0)


if __name__ == "__main__":
    unittest.main()

