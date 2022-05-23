# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        level = 0
        stack = [[root,1]]
        while stack:
            node,depth = stack.pop()
            if node:
                level = max(level,depth)
                stack.append([node.left,depth+1])
                stack.append([node.right,depth+1])
        return level
        