# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        q1,q2 = deque(),deque()
        q1.append(original)
        q2.append(cloned)
        while q1:
            node_original = q1.popleft()
            node_cloned = q2.popleft()
            if node_original.val == target.val:
                return node_cloned
            if node_original.left:
                q1.append(node_original.left)
                q2.append(node_cloned.left)
            if node_original.right:
                q1.append(node_original.right)
                q2.append(node_cloned.right)
                
        