# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self,root):
        nodes = []
        if root:
            nodes += self.inorderTraversal(root.left)
            nodes.append(root.val)
            nodes += self.inorderTraversal(root.right)
        return nodes
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        nodes = self.inorderTraversal(root)
        return nodes[k-1]
        