# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node,sum_):
            if not node:
                return False
            sum_ += node.val
            if not node.left and not node.right:
                return sum_ == targetSum
            return (dfs(node.left,sum_) or dfs(node.right,sum_))
        return dfs(root,0)
            
        