from typing import *
# 3. Longest Substring Without Repeating Characters
# Given a string s, find the length of the longest substring without repeating characters.

class Solution:
    # Runtime: O(N) Space: O(1)
    # Sliding Window And Hash Set
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        left, result = 0,0
        for right in range(len(s)):
            while s[right] in charSet:
                charSet.remove(s[left])
                left += 1
            charSet.add(s[right])
            result = max(result, right-left+1)
        return result