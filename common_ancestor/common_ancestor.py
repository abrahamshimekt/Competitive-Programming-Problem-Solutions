# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findNode(self,node,root,parent,level):
        if not root:
            return
        if root.val == node.val:
            parent[level] = root.val
            return
        elif node.val < root.val:
            parent[level] =  root.val
            self.findNode(node,root.left,parent,level+1)
        else:
            parent[level] = root.val
            self.findNode(node,root.right,parent,level+1)

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        p_parent = defaultdict(int)
        q_parent = defaultdict(int)
        self.findNode(p,root,p_parent,0)
        self.findNode(q,root,q_parent,0)
        common_ancestors = []
        for node in p_parent:
            if p_parent[node] == q_parent.get(node,None):
                common_ancestors.append( p_parent[node])
        return TreeNode(common_ancestors[-1])
        

        

        


        