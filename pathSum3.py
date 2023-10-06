# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        pathCount = 0
        prefix = defaultdict(int,{0:1})

        def findPaths(root,currSum):
            nonlocal pathCount
            if not root:
                return

            currSum += root.val
            if currSum - targetSum in prefix:
                pathCount += prefix[currSum-targetSum]
            prefix[currSum] +=1
            findPaths(root.left ,currSum)
            findPaths(root.right,currSum)
            prefix[currSum] -=1
        
        
        findPaths(root,0)
        return pathCount
