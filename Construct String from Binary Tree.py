# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if not root:
            return  ""
        result = [str(root.val)]
        left = self.tree2str(root.left)
        right = self.tree2str(root.right)
        if not left and right:
            result += ['()']
        if left:
            result += [f"({left})"]
        if right:
             result += [f"({right})"]
        return ''.join(result)
