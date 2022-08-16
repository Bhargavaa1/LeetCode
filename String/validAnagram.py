from collections import Counter
from typing import *
#  242. Valid Anagram
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
# typically using all the original letters exactly once.

class Solution:
    # Runtime: O(N) Space: O(1)
    # Custom Character Counter Solution
    def isAnagram1(s: str, t: str) -> bool:
        sCharCount = {}
        for chr in s:
            if chr not in sCharCount.keys():
                sCharCount[chr] = 1
            else:
                sCharCount[chr] += 1
        for chr in t:
            if chr not in sCharCount.keys():
                return False
            else:
                sCharCount[chr] -= 1
        for chr in sCharCount.keys():
            if sCharCount[chr] != 0:
                return False
        return True

    # Runtime: O(N log N) Space: O(N)
    # Sorting Solution
    def isAnagram2(s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

    # Runtime: O(N) Space: O(1)
    # Python's Character Counter Solution
    def isAnagram3(s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
