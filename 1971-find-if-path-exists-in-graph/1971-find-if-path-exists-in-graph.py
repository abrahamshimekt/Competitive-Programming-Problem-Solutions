class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:  
    
        if not edges: 
            return True
        adj = [[] for _ in range(n)]
        
        for v, e in edges:
            adj[v].append(e)
            adj[e].append(v)
        def dfs(v):
            if v == destination:
                return True
            while adj[v]:
                if dfs(adj[v].pop()):
                    return True
            return False
            
        return dfs(source)