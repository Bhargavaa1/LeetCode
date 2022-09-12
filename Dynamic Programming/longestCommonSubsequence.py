from typing import *
# 1143. Longest Common Subsequence
# Given two strings text1 and text2, return the length of their longest common subsequence. 
# If there is no common subsequence, return 0.
# A subsequence of a string is a new string generated from the original string 
# with some characters (can be none) deleted without changing the relative order of the remaining characters.
# For example, "ace" is a subsequence of "abcde".
# A common subsequence of two strings is a subsequence that is common to both strings.

class Solution:
    # Recursive Solution
    def longestCommonSubsequenceRecursive(self, text1: str, text2: str) -> int:
        if not text1 or not text2:
            return 0
        elif text[-1] == text2[-1]:
            return 1+self.longestCommonSubsequenceRecursive(text1[:-1], text2[:-1])
        else:
            option1 = self.longestCommonSubsequenceRecursive(text1, text2[:-1])
            option2 = self.longestCommonSubsequenceRecursive(text1[:-1], text2)
            return max(option1,option2)
    
    # Dynamic Programming Solution
    def longestCommonSubsequenceDP(self, text1: str, text2: str) -> int:
        m,n = len(text2), len(text1)
        DP = [[0]*(n+1) for col in range(m+1)]
        for col in range(n+1):
            DP[0][col] = 0
        for row in range(m+1):
            DP[row][0] = 0
        for row in range(1,m+1):
            for col in range(1,n+1):
                if text1[col-1] == text2[row-1]:
                    DP[row][col] = 1+DP[row-1][col-1]
                else:
                    DP[row][col] = max(DP[row-1][col],DP[row][col-1])
        return DP[m][n]

