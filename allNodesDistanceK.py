# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        
        adjList = defaultdict(list)
        queue =deque()
        queue.append(root)
        while queue:
            currNode = queue.popleft()
            if currNode.left:
                adjList[currNode.val].append(currNode.left.val)
                adjList[currNode.left.val].append(currNode.val)
                queue.append(currNode.left)
            if currNode.right:
                adjList[currNode.val].append(currNode.right.val)
                adjList[currNode.right.val].append(currNode.val)
                queue.append(currNode.right)

        nodes = []
        queue = deque()
        queue.append((target.val,0))
        visited = {target.val}
        while queue:
            node,level = queue.popleft()
            
            if level==k:
               
                nodes.append(node)
            for child in adjList[node]:
                if child not in visited:
                    queue.append((child,level+1))
                    visited.add(child)
        return nodes




