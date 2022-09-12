from typing import *
# 1143. Longest Common Subsequence
# Given two strings text1 and text2, return the length of their longest common subsequence. 
# If there is no common subsequence, return 0.
# A subsequence of a string is a new string generated from the original string 
# with some characters (can be none) deleted without changing the relative order of the remaining characters.
# For example, "ace" is a subsequence of "abcde".
# A common subsequence of two strings is a subsequence that is common to both strings.

class Solution:
    def longestCommonSubsequenceRecursive(self, text1: str, text2: str) -> int:
        if not text1 or not text2:
            return 0
        elif text[-1] == text2[-1]:
            return 1+self.longestCommonSubsequence(text1[:-1], text2[:-1])
        else:
            option1 = self.longestCommonSubsequence(text1, text2[:-1])
            option2 = self.longestCommonSubsequence(text1[:-1], text2)
            return max(option1,option2)
    
    # def longestCommonSubsequenceDP(self, text1: str, text2: str) -> int:
