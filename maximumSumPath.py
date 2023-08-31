# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def dfs(self,root):
            if not root:
                return 0
            currVal = root.val
            leftSum = self.dfs(root.left)
            rightSum = self.dfs(root.right)
            self.maxSum = max(self.maxSum,leftSum+rightSum+currVal,currVal,leftSum+currVal,rightSum+currVal)
            return max(leftSum+currVal,rightSum+currVal,currVal)

    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.maxSum = float("-inf")
        self.dfs(root)
        return self.maxSum
    
