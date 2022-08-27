from typing import *
# 102. Binary Tree Preorder Traversal
# Given the root of a binary tree, return the preorder traversal of its nodes' values.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # Recursive
    def preorderTraversalRecursive(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        else:
            left = self.preorderTraversalRecursive(root.left)
            right = self.preorderTraversalRecursive(root.right)
            return [root.val] + left + right
    
    # Iterative Using Stack
    def preorderTraversalIterative(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        if not root:
            return result
        stack = [root]
        while stack:
            node = stack.pop()
            result.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return result