from typing import *
# 102. Binary Tree Postorder Traversal
# Given the root of a binary tree, return the postorder traversal of its nodes' values.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # Recursive
    def postorderTraversalRecursive(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        else:
            left = self.postorderTraversalRecursive(root.left)
            right = self.postorderTraversalRecursive(root.right)
            return left + right + [root.val]
    
    # Iterative Using Stack
    def postorderTraversalIterative(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        if not root:
            return result
        stack = [root]
        while stack:
            node = stack.pop()
            result.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return result[::-1]