# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self,root):
        
        stack = [(root,"root")]
        while stack:
            node,label = stack.pop()
            if label == "left" :
                if not node.left and not node.right:
                    self.leftSum += node.val
            if node.left:
                stack.append((node.left,"left"))
            if node.right:
                stack.append((node.right,"right"))
        


    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        self.leftSum = 0
        self.dfs(root)
        return  self.leftSum