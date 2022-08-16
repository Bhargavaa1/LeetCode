from typing import *
from queue import Queue
# 104. Maximum Depth of Binary Tree
# Given the root of a binary tree, return its maximum depth.
# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # Recursive DFS
    def maxDepthDFSRecursive(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        else:
            leftTraversal = 1+self.maxDepthDFSRecursive(root.left)
            rightTraversal = 1+self.maxDepthDFSRecursive(root.right)
            return max(leftTraversal,rightTraversal)
    
    # Iterative DFS
    def maxDepthDFSIterative(self, root: TreeNode) -> int:
        if not root:
            return 0
        res = 1
        stack = [[root,1]]
        while stack:
            node,depth = stack.pop()
            res = max(res,depth)
            if node.left:
                stack.append([node.left,depth+1])
            if node.right:
                stack.append([node.right,depth+1])
        return res

    # BFS
    def maxDepthBFS(self, root: Optional[TreeNode]) -> int:
        level = 0
        if not root:
            return level
        q = Queue()
        q.put(root)
        while q.qsize() != 0:
            for i in range(0,q.qsize()):
                node = q.get()
                if node.left:
                    q.put(node.left)
                if node.right:
                    q.put(node.right)
            level += 1
        return level

