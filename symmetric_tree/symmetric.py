# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkSymmetry(self,left_sub_tree,right_sub_tree):
        if not left_sub_tree and not right_sub_tree:
            return True
        elif not left_sub_tree or not right_sub_tree:
            return False
        elif left_sub_tree.val != right_sub_tree.val:
            return False
        left_symmetric = self.checkSymmetry(left_sub_tree.left,right_sub_tree.right)
        right_symmetric = self.checkSymmetry(left_sub_tree.right,right_sub_tree.left)
        return left_symmetric and right_symmetric
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        left_sub_tree = root.left
        right_sub_tree = root.right
        return self.checkSymmetry(left_sub_tree,right_sub_tree)
        