#!/usr/bin/env python3

"""
You can one time remove, update or change an one symbol.
Examples:
["cat", "dogs"] => False
["cat", "cats"] => True
["cat", "cut"]  => True
["cat", "at"]   => True
["cat", "cast"] => False
"""

import unittest


class Solution:
    def main(self, first, other):
        l = 0
        r = len(other) - 1
        changed = 0

        if len(first) < len(other):
            changed += 1
            r -= 1

        if len(first) > len(other):
            changed += 1
            l += 1

        while l < r:
            if first[l] != other[l]:
                changed += 1
            if first[r] != other[r]:
                changed += 1
            r -= 1
            l += 1

        if changed > 1:
            return False

        return True


class TestSolution(unittest.TestCase):
    def test_main(self):
        s = Solution()
        self.assertEqual(s.main("cat", "dog"), False)
        self.assertEqual(s.main("cat", "cats"), True)
        self.assertEqual(s.main("cat", "cut"), True)
        self.assertEqual(s.main("cat", "at"), True)
        self.assertEqual(s.main("cat", "cast"), False)
        self.assertEqual(s.main("cat", "catt"), True)

if __name__ == "__main__":
    unittest.main()