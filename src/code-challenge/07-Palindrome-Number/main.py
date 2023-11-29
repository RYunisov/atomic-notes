#!/bin/env python3

#
# https://leetcode.com/problems/palindrome-number/
#

class Solution:
    def isPalindome(self, num):
        print(f"Given: {num}")
        if ( len(str(num)) % 2 ) == 0:
            tail_num = str(num)[:round(len(str(num))/2)]
            head_num = str(num)[round(len(str(num))/2):]
        else:
            tail_num = str(num)[:round(len(str(num))/2)-1]
            head_num = str(num)[round(len(str(num))/2):]
        if num < 0:
            print(f"{num} isn't palindrome")
            return False
        if head_num == tail_num[::-1]: 
            print(f"True: {num}:{head_num}:{tail_num}")
            return True

#num = 1221
#num = -123
num = 212
#num = 3121213

s = Solution()
s.isPalindome(num)

