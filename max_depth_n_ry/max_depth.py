"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def dfs(self,root,depth):
        if not root:
            return 
        self.max_depth = max(self.max_depth,depth)
        for node in root.children:
            self.dfs(node,depth+1)
        
        

    def maxDepth(self, root: 'Node') -> int:
        self.max_depth = 0
        self.dfs(root,1)
        return self.max_depth


        



















        