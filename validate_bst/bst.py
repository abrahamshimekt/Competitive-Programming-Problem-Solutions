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
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        nodes = self.inorderTraversal(root)
        for index in range(len(nodes)-1):
            if nodes[index] >= nodes[index+1]:
                return False
        return True
        