# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def helper(node):
            if not node:
                return 0
            l = node.left
            r = node.right
            lDepth  = helper(l) +1
            rDepth = helper(r) +1
            return lDepth + rDepth 
        return helper(root)//2
            
        
            
            