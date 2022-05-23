# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        root_queue = deque([root])
        level = 0
        while root_queue:
            for i in range(len(root_queue)):
                node = root_queue.popleft()
                if node.left:
                     root_queue.append(node.left)
                if node.right:  
                    root_queue.append(node.right)
            level +=1
        return level
        