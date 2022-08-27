from typing import *
from queue import Queue
# 102. Binary Tree Level Order Traversal
# Given the root of a binary tree, return the level order traversal of its nodes' values. 
# (i.e., from left to right, level by level).

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # Iterative BFS
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result =  []
        if not root:
            return result
        q = Queue()
        q.put(root)
        while q.qsize() != 0:
            level = []
            for i in range(q.qsize()):
                node = q.get()
                level.append(node.val)
                if node.left:
                    q.put(node.left)
                if node.right:
                    q.put(node.right)
            result.append(level)
        return result