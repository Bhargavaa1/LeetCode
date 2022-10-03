from typing import *
# 20. Valid Parentheses
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
#     Open brackets must be closed by the same type of brackets.
#     Open brackets must be closed in the correct order.

class Solution:
    # Runtime: O(N) Space: O(N)
    # Stack Of Open Characters Solution
    def isValid(self, s: str) -> bool:
        stack = []
        parenDict = {')': '(', '}': '{', ']': '['}
        for i in s:
            if i in parenDict.values():
                stack.append(i)
            elif len(stack) == 0 or stack.pop() != parenDict[i]:
                return False
        return len(stack) == 0
