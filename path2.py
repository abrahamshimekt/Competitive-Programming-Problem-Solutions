# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        answer = []
        def backTrack(root,currSum,path):
            if not root:
                return
           
            currSum += root.val
            path.append(root.val)
            
            if (currSum == targetSum) and (not root.left and not root.right):
                answer.append(path[:])
        
            backTrack(root.left, currSum, path)
            backTrack(root.right, currSum, path)
            
            path.pop()
            currSum -= root.val
        
        backTrack(root, 0, [])
        return answer

