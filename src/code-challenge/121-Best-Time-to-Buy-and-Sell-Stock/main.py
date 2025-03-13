#!/usr/bin/env python3

#
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock
#

class Solution:
    def maxProfit(self, prices):
        min_price = min(prices)
        min_index = prices.index(min_price)
        max_price = max(prices[min_index:])
        max_index = prices.index(max_price)
        print(f"{min_price}:{min_index}")
        print(f"{max_price}:{max_index}")
        if min_price < max_price:
            return max_price - min_price
        return 0

#prices = [7,1,5,3,6,4]
#prices = [7,6,4,3,1]
prices = [7,6,4,3,1,8]

s = Solution()
print(s.maxProfit(prices))
