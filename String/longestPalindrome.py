from typing import *
# 409. Longest Palindrome
# Given a string s which consists of lowercase or uppercase letters, 
# return the length of the longest palindrome that can be built with those letters.
# Letters are case sensitive, for example, "Aa" is not considered a palindrome here.

class Solution:
    # Runtime: O(N) Space: O(1)
    # Character Counting Definition of Palindrome
    def longestPalindrome(self, s: str) -> int:
        sCharCount = {}
        for i in s:
            if i not in sCharCount:
                sCharCount[i] = 1
            else:
                sCharCount[i] += 1
        result,odd = 0,False
        for j in sCharCount:
            if sCharCount[j] % 2 == 0:
                result += sCharCount[j]
            else:
                odd = True 
                result += (sCharCount[j]-1)
        if odd:
            result += 1
        return result