from typing import *
# Given a binary search tree (BST), 
# find the lowest common ancestor (LCA) node of two given nodes in the BST.
# According to the definition of LCA on Wikipedia: 
# “The lowest common ancestor is defined between two nodes p and q as the 
# lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”
# 235. Lowest Common Ancestor of a Binary Search Tree

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val:int = 0, left:TreeNode = None, right:TreeNode = None):
        self.val = x
        self.left = None
        self.right = None
        
class Solution:
    # Traversal Solution
    # Runtime: O(log N) Space: O(1)
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        curr = root
        while curr:
            if p.val < curr.val and q.val < curr.val:
                curr = curr.left
            elif p.val > curr.val and q.val > curr.val:
                curr = curr.right
            else:
                return curr