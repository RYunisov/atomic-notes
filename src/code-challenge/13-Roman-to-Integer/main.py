#!/bin/env python3

"""
LeetCode: 13
Url: https://leetcode.com/problems/roman-to-integer/
"""

import unittest


class Solution:
    def edge_roman(self, result, curr_num, prev_num):
        result = result - prev_num + curr_num
        return result, True, ""

    def main(self, roman_num):
        i = 0
        buff = False
        prev_roman = ""
        result = 0

        roman_dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        while i < len(roman_num):
            buff = False

            if roman_num[i] == "V" and prev_roman == "I":
                result, buff, prev_roman = self.edge_roman(result, 4, roman_dict[prev_roman])
            if roman_num[i] == "X" and prev_roman == "I":
                result, buff, prev_roman = self.edge_roman(result, 9, roman_dict[prev_roman])
            if roman_num[i] == "L" and prev_roman == "X":
                result, buff, prev_roman = self.edge_roman(result, 40, roman_dict[prev_roman])
            if roman_num[i] == "C" and prev_roman == "X":
                result, buff, prev_roman = self.edge_roman(result, 90, roman_dict[prev_roman])
            if roman_num[i] == "D" and prev_roman == "C":
                result, buff, prev_roman = self.edge_roman(result, 400, roman_dict[prev_roman])
            if roman_num[i] == "M" and prev_roman == "C":
                result, buff, prev_roman = self.edge_roman(result, 900, roman_dict[prev_roman])
                    
            if not buff:
                result += roman_dict[roman_num[i]]
                prev_roman = roman_num[i]

            print("END: ", i, roman_num[i], prev_roman, result)
            
            i += 1

        return result


class TestSolution(unittest.TestCase):
    def test_main(self):
        s = Solution()
        self.assertEqual(s.main("IV"), 4)
        self.assertEqual(s.main("III"), 3)
        self.assertEqual(s.main("LVIII"), 58)
        self.assertEqual(s.main("XCVIII"), 98)
        self.assertEqual(s.main("MCMXCIV"), 1994)
        self.assertEqual(s.main("MCMLXXXVIII"), 1988)


if __name__ == "__main__":
    unittest.main()
