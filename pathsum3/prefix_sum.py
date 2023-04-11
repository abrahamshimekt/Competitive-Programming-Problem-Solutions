# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def calcutePathSum(self,node,curr_sum,prefix_sum):
        if not node:
            return 
        
        curr_sum += node.val
        if curr_sum -  self.targetSum in prefix_sum:
            self.numberOfPath += prefix_sum[curr_sum -  self.targetSum]
        prefix_sum[curr_sum] +=1
       
        self.calcutePathSum(node.left,curr_sum,prefix_sum)
        self.calcutePathSum(node.right,curr_sum,prefix_sum)
        
        prefix_sum[curr_sum] -=1

 
        
        
        
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        prefix_sum = defaultdict(int,{0:1})
        self.numberOfPath = 0
        self.targetSum = targetSum
        self.calcutePathSum(root,0,prefix_sum)
        return self.numberOfPath
