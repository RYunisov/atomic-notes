#!/bin/env python3

#
# https://leetcode.com/problems/palindrome-number/
#

import unittest


class Solution:
    def isPalindome(self, num):
        print(f"Given: {num}")
        if ( len(str(num)) % 2 ) == 0:
            tail_num = str(num)[:round(len(str(num))/2)]
            head_num = str(num)[round(len(str(num))/2):]
        else:
            tail_num = str(num)[:-round(len(str(num))/2)]
            head_num = str(num)[round(len(str(num))/2):]
        if num < 0:
            print(f"{num} isn't palindrome")
            return False
        if head_num == tail_num[::-1]: 
            print(f"True: {num}:{head_num}:{tail_num}")
            return True


class TestSolution(unittest.TestCase):
    def test_main(self):
        s = Solution()
        self.assertEqual(s.isPalindome(1221), True)
        self.assertEqual(s.isPalindome(-123), False)
        self.assertEqual(s.isPalindome(212), True)
        self.assertEqual(s.isPalindome(3121213), True)


if __name__ == "__main__":
    unittest.main()
