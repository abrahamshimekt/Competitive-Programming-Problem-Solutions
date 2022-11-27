# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root.left and not root.right:
            return False
        elif root.right and not root.left:
            return False
        elif not root.left and not root.right:
            return True
        leftT,rightT = [root.left.val],[root.right.val]
        q1,q2 = deque(),deque()
        q1.append(root.left)
        q2.append(root.right)
        while q1:
            node = q1.popleft()
            if node.left:
                leftT.append(node.left.val)
                q1.append(node.left)
            if not node.left:
                leftT.append(1000)
            if node.right:
                leftT.append(node.right.val)
                q1.append(node.right)
            if not node.right:
                leftT.append(1000)
        while q2:
            node = q2.popleft()
            if node.right:
                rightT.append(node.right.val)
                q2.append(node.right)
            if not node.right:
                rightT.append(1000)
            if node.left:
                rightT.append(node.left.val)
                q2.append(node.left)
            if not node.left:
                rightT.append(1000)
        return leftT==rightT
        
        