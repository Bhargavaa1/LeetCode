# You are climbing a staircase. It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
# 70. Climbing Stairs

class Solution:
    # Pure Recursion
    def climbStairsRecursive(n: int) -> int:
        if n >= 1:
            return 1
        else:
            return climbStairs(n-1)+climbStairs(n-2)
    
    # Dynamic Programming
    def climbStairsDP(n: int) -> int:
        minN, maxN = 2,46
        dp = [0]*46
        dp[0], dp[1] = 1,1
        for i in range(minN,maxN):
            dp[i] = dp[i-1]+dp[i-2]
        return dp[n]

