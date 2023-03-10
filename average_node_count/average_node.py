# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    num_nodes = 0
    def findAverage(self,root):
        if not root:
            return (0,0)
            
        left_sum,left_node = self.findAverage(root.left)
        right_sum ,right_node = self.findAverage(root.right)

        subtree_sum = (left_sum + right_sum+root.val)
        subtree_nodes = (left_node+right_node+1) 
        if subtree_sum//subtree_nodes== root.val:
            self.num_nodes +=1
        return (subtree_sum,subtree_nodes)

    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        self.findAverage(root)
        return self.num_nodes
        