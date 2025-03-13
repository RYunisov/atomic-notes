#!/bin/env python3

# Num: 12
# Url: https://leetcode.com/problems/integer-to-roman/
#

import unittest

class Solution:
    def get_from_dict(self, digit, romans):
        roman_dict = {
            1: "I",
            4: "IV",
            5: "V",
            9: "IX",
            10: "X",
            40: "XL",
            50: "L",
            90: "XC",
            100: "C",
            400: "CD",
            500: "D",
            900: "CM",
            1000: "M"
        }

        for i in reversed(roman_dict.keys()):
            if digit >= i:
                #print(digit, i, roman_dict[i], romans)
                romans.append(roman_dict[i])
                return self.get_from_dict(digit-i, romans)

        return romans

    def int_to_roman(self, nums):
        romans = []

        if nums > 3999:
            return False

        romans.append(self.get_from_dict(nums, romans))

        return ''.join(romans[:-1])


class TestSolution(unittest.TestCase):
    def test_main(self):
        s = Solution()
        self.assertEqual(s.int_to_roman(2234), "MMCCXXXIV")
        self.assertEqual(s.int_to_roman(3749), "MMMDCCXLIX")
        self.assertEqual(s.int_to_roman(58), "LVIII")
        self.assertEqual(s.int_to_roman(1994), "MCMXCIV")
        self.assertEqual(s.int_to_roman(1988), "MCMLXXXVIII")


if __name__ == '__main__':
    unittest.main()
