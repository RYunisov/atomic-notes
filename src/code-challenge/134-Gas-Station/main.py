#!/bin/env python3

"""
LeetCode: 134
Url: https://leetcode.com/problems/gas-station
"""

import unittest


class Solution:
    def upd_position(self, gas, cost, pos):
        res_position = 0

        if pos != 0:
            new_gas = gas[pos:] + gas[:pos] 
            new_cost = cost[pos:] + cost[:pos] 
        else:
            new_gas = gas
            new_cost = cost

        print("Updated: ", new_gas, new_cost, pos)

        for i in range(0, len(new_gas)):
            if i == 0:
                print(f"{i}, {res_position} - 0 + {new_gas[i]}")
                res_position = res_position + new_gas[i]
            else:
                tank = (res_position - new_cost[i-1]) 
                print(f"{i}, {res_position} - {new_cost[i-1]} + {new_gas[i]}")
                if tank > 0:
                    res_position = tank + new_gas[i]
                else:
                    res_position = -1

            if res_position < 0:
                return -1

        return res_position


    def main(self, gas, cost):
        position = -1

        for i in range(0, len(gas)):
            res = self.upd_position(gas, cost, i)
            if res > 0:
                position = i

        return position


class TestSolution(unittest.TestCase):
    def test_main(self):
        s = Solution()
        self.assertEqual(s.main([1,2,3,4,5],[3,4,5,1,2]), 3)
        self.assertEqual(s.main([2,3,4],[3,4,3]), -1)
        self.assertEqual(s.main([1,2,3,4,5,6,7,8],[1,2,3,4,5,6,7,8]), -1)


if __name__ == '__main__':
    unittest.main()

