# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def calcutePathSum(self,node,curr_sum):
        if not node:
            return 
        
        curr_sum += node.val
        if curr_sum == self.target:
            self.numberOfPath +=1
            
        self.calcutePathSum(node.left,curr_sum)
        self.calcutePathSum(node.right,curr_sum)

    def traverse(self,root):
        if not root:
            return
        self.calcutePathSum(root,0)
        self.traverse(root.left)
        self.traverse(root.right)
        
        
        
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.numberOfPath = 0
        self.target = targetSum
        self.traverse(root)
        return self.numberOfPath
