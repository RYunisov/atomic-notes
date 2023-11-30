#!/bin/env python3

#
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii
#

class Solution:
    def maxProfit(self, prices):
        print(f"Given: {prices}")
        min_el = min(prices)
        ind_el = prices.index(min_el)
        profit_single = max(prices[ind_el:]) - min_el
        print(f"PI:{profit_single}")
        profit_stages = self.multiStages(prices)
        print(f"PIS:{profit_stages}")
        if profit_single > profit_stages:
            print(f"Single: {profit_single}")
        else:
            print(f"Stages: {profit_stages}")

    def multiStages(self, prices):
        profit = 0
        min_el = min(prices)
        id_min_el = prices.index(min_el)
        while id_min_el < len(prices) - 1:
            print(f"Given: {prices}")
            if prices[id_min_el] < prices[id_min_el+1] and (prices[id_min_el+1] - prices[id_min_el]) > 1:
                profit += prices[id_min_el+1] - prices[id_min_el]
                print(f"PII:{prices[id_min_el+1]}-{prices[id_min_el+1]}={profit}")
            # self.multiStages(prices[id_min_el+1:])
            id_min_el += 1
        return profit
            

prices = [7,1,5,3,6,4]
prices = [1,2,3,4,5]
prices = [7,6,4,3,1]

s = Solution()
s.maxProfit(prices)

