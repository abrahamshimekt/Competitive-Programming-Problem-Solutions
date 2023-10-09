# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def dfs(self, root, target, path):
        if not root:
            return None

        if root.val == target.val:
            return path+[root.val]

        path.append(root.val)
        result = self.dfs(root.left, target, path)
        if result is not None:
            return result

        result = self.dfs(root.right, target, path)
        if result is not None:
            return result

        path.pop()
        return None
            
        
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
       
        pParent = self.dfs(root,p,[])
        
        qParent = self.dfs(root,q,[])
        n = len(pParent)
        m = len(qParent)
        i = 0
        j = 0
        LCA = root.val
        while i < n and j < m:
            if pParent[i] == qParent[j]:
                 LCA = pParent[i]
                 i +=1
                 j +=1
            else:
                break
        return  TreeNode(LCA)
