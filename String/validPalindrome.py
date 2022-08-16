from typing import *
# 125. Valid Palindrome
# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward.
# Alphanumeric characters include letters and numbers.
# Given a string s, return true if it is a palindrome, or false otherwise.
class Solution:

    # Runtime: O(N) Space: O(1)
    # Two Pointer Solution
    def isPalindrome1(s: str) -> bool:
        i, j = 0, len(s)-1
        while i <= j:
            if isAlphaNumeric(i) and isAlphaNumeric(j):
                if lower(s[i]) != lower(s[j]):
                    return False
                i += 1
                j -= 1
            else:
                if not isAlphaNumeric(s[i]):
                    i += 1
                if not isAlphaNumeric(s[j]):
                    j -= 1
        return True


    def isAlphaNumeric(s: str) -> bool:
        asciiValueOfS = ord(s)
        if (asciiValueOfS >= 48 and asciiValueOfS <= 57) or (asciiValueOfS >= 65 and asciiValueOfS <= 90) or (asciiValueOfS >= 97 and asciiValueOfS <= 122):
            return True
        return False


    def lower(s: str) -> str:
        asciiValueOfS = ord(s)
        if (asciiValueOfS >= 65 and asciiValueOfS <= 90):
            return chr(asciiValueOfS+32)
        else:
            return s

    # Runtime: O(N) Space: O(N)
    # Reverse String Solution
    def isPalindrome2(s: str) -> bool:
        validS = ""
        for c in s:
            if c.isalnum():
                validS += c.lower()
        return validS == validS[::-1]
