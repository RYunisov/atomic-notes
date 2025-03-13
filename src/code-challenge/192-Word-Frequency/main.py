#!/bin/env python3

"""
Num: 192
Url: https://leetcode.com/problems/word-frequency/description/
"""

import unittest

class Solution:
    def main(self):
        dictionary = {}

        with open("words.txt") as file:
            lines = file.readlines()

        for line in lines:
            for word in line.split(" "):
                word = word.strip()
                if dictionary.get(word):
                    dictionary[word] += 1
                else:
                    dictionary[word] = 1

        return dictionary


class TestSolution(unittest.TestCase):
    def test_main(self):
        s = Solution()
        want = {"the": 4, "is": 3, "sunny": 2, "day": 1}
        self.assertEqual(s.main(), want)


if __name__ == "__main__":
    unittest.main()

