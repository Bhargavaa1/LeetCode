from typing import *
#  110. Balanced Binary Tree
# Given a binary tree, determine if it is height-balanced.
# For this problem, a height-balanced binary tree is defined as:
#     a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # Helper Recursive Function Solution
    # Runtime: O(N) Space: O(N)
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root: Optional[TreeNode]) -> [bool,int]:
            if not root:
                return [True, 0]
            left,right = dfs(root.left), dfs(root.right)
            balanced = (left[0] and right[0]) and (abs(left[1]-right[1]) <= 1)
            height = 1+max(left[1],right[1])
            return [balanced, height]
        return dfs(root)[0]