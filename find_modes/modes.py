# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findModes(self,root,nodes_freq):
        if not root:
            return 
        nodes_freq[root.val] +=1
        self.findModes(root.left,nodes_freq)
        self.findModes(root.right,nodes_freq)


    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        nodes_freq = defaultdict(int)
        self.findModes(root,nodes_freq)
        max_freq = max(nodes_freq.values())
        modes = []
        for node in nodes_freq:
            if nodes_freq[node] == max_freq:
                modes.append(node)
        return modes