#!/bin/env python3

"""
LeedCode: 05
Url: https://leetcode.com/problems/longest-palindromic-substring/
"""

import unittest


class Solution:
    def is_palindrom(self, line):
        if len(line) < 2:
            print(f"{line} isn't palindrome")
            return False
        if ( len(str(line)) % 2 ) == 0:
            head_line = line[round(len(line)/2):]
            tail_line = line[:round(len(line)/2)]
        else:
            head_line = line[round(len(line)/2):]
            tail_line = line[:-round(len(line)/2)]
        if head_line == tail_line[::-1]: 
            print(f"True: {line}:{head_line}:{tail_line}")
            return True

    def get_substr(self, line):
        result = []
        for i in range(len(line)):
            if self.is_palindrom(line[i:]):
                result.append(line[i:])
        return result

    def longest(self, line):
        prev = ""
        print(line)
        for i in line:
            if len(prev) < len(i):
                prev = i
        return prev

    def main(self, line):
        prev_maxx = []
        maxx = []
        for i in range(len(line)+1):
            prev_maxx = [ x for x in self.get_substr(line[:i]) ]
            if len(prev_maxx) > 0:
                maxx.append(prev_maxx[0])
        return self.longest(maxx)


class TestSolution(unittest.TestCase):
    def test_main(self):
        s = Solution()
        self.assertEqual(s.main("babad"), "bab")
        self.assertEqual(s.main("cbbd"), "bb")
        self.assertEqual(s.main("aacabdkacaa"), "aca")
        self.assertEqual(s.main("nitinarora"), "nitin")


if __name__ == "__main__":
    unittest.main()
