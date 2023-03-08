# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return None
        queue = deque()
        queue.append([root])
        level_nodes = [[root.val]]
        while queue:
            nodes = queue.popleft()
            collector = []
            values = []
            for node in nodes:
                if node.left:
                    values.append(node.left.val)
                    collector.append(node.left)
                if node.right:
                    values.append(node.right.val)
                    collector.append(node.right)
            if values:
                level_nodes.append(values)
            if collector:
                queue.append(collector)
        return level_nodes
