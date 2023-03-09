# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findNodes(self,nodes,root,row,col):
        if not root:
            return
        nodes[(row,col)].append(root.val)
        self.findNodes(nodes,root.left,row+1,col-1)
        self.findNodes(nodes,root.right,row+1,col+1)
        
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        nodes = defaultdict(list)
        self.findNodes(nodes,root,0,0)
        
        nodes = dict(sorted(nodes.items(),key=lambda x:x[0][0]))
        
        for node in nodes:
            if len(nodes[node]) > 1:
                nodes[node] = sorted(nodes[node])

        nodes = dict(sorted(nodes.items(),key=lambda x:x[0][1]))
        same_col = defaultdict(list)
        verticalOrder = []
        for node_ in nodes:
            row,col = node_
            for n in nodes[node_]: 
                same_col[col].append(n)
        for node_col in same_col:
            verticalOrder.append(same_col[node_col])
        return verticalOrder


        