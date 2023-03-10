# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def backTrack(self,root,path):
        if not root.left and not root.right:
            path.append(str(root.val))
            self.paths.append("->".join(path))
            return
        path.append(str(root.val))
        if root.left:
            self.backTrack(root.left,path.copy())
        if root.right:
            self.backTrack(root.right,path.copy())
        

    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        self.paths = []
        self.backTrack(root,[])
        return self.paths     