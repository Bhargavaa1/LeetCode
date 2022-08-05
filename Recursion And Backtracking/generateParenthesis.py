# https://leetcode.com/problems/generate-parentheses/
# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
# 22. Generate Parentheses

# Enumerative Backtracking
def generateParenthesis(self, n: int) -> List[str]:
    result = []
    stack = []

    def generateParenthesisHelper(openN: int, closedN: int):
        if closedN == openN == n:
            result.append("".join(stack))
        if openN < n:
            stack.append("(")
            generateParenthesisHelper(openN+1, closedN)
            stack.pop()
        if closedN < openN:
            stack.append(")")
            generateParenthesisHelper(openN, closedN+1)
            stack.pop()
    generateParenthesisHelper(0, 0)
    return result
