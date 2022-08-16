from typing import *
# 14. Longest Common Prefix
# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".

class Solution:
    # Runtime: O(N*M) Space Complexity: O(M) where N is the length of strs
    # and M is the length of the shortest string in strs
    # Two Pointer Solution
    def longestCommonPrefix(strs: List[str]) -> str:
        result = ""
        firstWord = strs[0]
        for i in range(0, len(firstWord)):
            for s in strs:
                if i >= len(s) or firstWord[i] != s[i]:
                    return result
            result += s[i]
        return result
