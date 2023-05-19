class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        reps = {i:i for i in range(n)}

        def find(x):
            while x != reps[x]:
                x = reps[x]
            return x
        
        def union(x,y):
            xrep = find(x)
            while y != reps[y]:
                parent = reps[y]
                reps[y] = xrep
                y = parent
            reps[y] = xrep
        
        for edge in edges:
            x,y = edge
            union(x,y)
        
        return find(source) == find(destination)
        
