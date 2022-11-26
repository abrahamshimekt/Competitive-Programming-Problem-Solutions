# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        q = deque()
        q.append(root)
        q2 = deque()
        ans = []
        while q:
            n = len(q)
            sum_val = 0
            while q:
                temp = q.popleft()
                sum_val += temp.val
                if temp.left:
                    q2.append(temp.left)
                if temp.right:
                    q2.append(temp.right)
            ans.append(sum_val/n)
            q = q2
            q2 = deque()
        return ans
        