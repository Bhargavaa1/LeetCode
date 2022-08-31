from typing import *
# 1672. Richest Customer Wealth
# You are given an m x n integer grid accounts where accounts[i][j] is the amount of money the i​​​​​​​​​​​th​​​​ customer has in the j​​​​​​​​​​​th​​​​ bank. 
# Return the wealth that the richest customer has.
# A customer's wealth is the amount of money they have in all their bank accounts. 
# The richest customer is the customer that has the maximum wealth.
class Solution:
    # Iteration
    # Runtime: O(M*N) Space: O(1)
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxWealth =  0
        for i in range(len(accounts)):
            wealthOfithCustomer = 0
            for j in range(len(accounts)):
                wealthOfithCustomer += accounts[i][j]
            maxWealth = max(maxWealth, wealthOfithCustomer)
        return maxWealth
