# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        queue = deque()
        queue.append((root,1))
        maxWidth = 0
        while queue:
            maxWidth = max(maxWidth,queue[-1][1]-queue[0][1]+1)
            secondQueue = deque()
            while queue:
                node,label = queue.popleft()
                if node.left :
                    secondQueue.append((node.left,label*2))
                if node.right :
                    secondQueue.append((node.right,label*2 + 1))
            queue = secondQueue
        return maxWidth

                

        
