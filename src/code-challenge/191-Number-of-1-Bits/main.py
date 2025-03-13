#!/bin/env python3

#
# https://leetcode.com/problems/number-of-1-bits
#

class Solution:
    def hammingWeight(self, n):
        if len(n) == 32:
            print(f"{n.count('1')}")
        print("The length of binary string less then 32 symbols")
        return False

#n = "00000000000000000000000000001011"
#n = "00000000000000000000000010000000"
#n = "11111111111111111111111111111101"
n = "1111111111111111111111111111110"

s = Solution()
s.hammingWeight(n)

