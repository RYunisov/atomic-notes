#!/bin/env python3

"""
Url: ?
"""

class Solution:
    def sum(self, int1, int2):
        int1, int2 = self.equal_length(int1, int2)
        x = len(int1) - 1
        temp = 0
        int3 = ""
        while x >= 0 :
            num = int(int1[x]) + int(int2[x])
            if temp > 0:
                num += temp
                temp = 0
            #print(f"{num}")
            if num >= 10:
                temp += 1
                num = num - 10
            int3 = f"{num}{int3}"
            x -= 1
        print(int3)
        return int1, int2

    def equal_length(self, int1, int2):
        length = len(int1) - len(int2)
        #print(f"{length}")
        if length > 0:
            int2 = "0" * length + int2
        if length < 0:
            int1 = "0" * abs(length) + int1
        return int1, int2

int1 = "983"
int2 = "1138"

s = Solution()
print(s.sum(int1, int2))

