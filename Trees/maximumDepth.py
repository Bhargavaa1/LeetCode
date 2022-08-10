# 104. Maximum Depth of Binary Tree
# Given the root of a binary tree, return its maximum depth.
# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Recursive/DFS
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        elif root.left == None and root.right == None:
            return 1
        else:
            leftTraversal = 1+self.maxDepth(root.left)
            rightTraversal = 1+self.maxDepth(root.right)
            return max(leftTraversal,rightTraversal)