# You are climbing a staircase. It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
# 70. Climbing Stairs
class Solution:
    # Memory: O(N) Space Complexity: O(N)
    # Pure Recursion
    def climbStairs(n: int) -> int:
        if n >= 1:
            return 1
        else:
            return climbStairs(n-1)+climbStairs(n-2)
