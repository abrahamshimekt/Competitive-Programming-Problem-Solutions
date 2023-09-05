class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:

        adjList = defaultdict(set)
        apples = set()
        for edge in edges:
            a,b = edge
            adjList[b].add(a)
            adjList[a].add(b)
            if hasApple[a]:
                apples.add(a)
            if hasApple[b]:
                apples.add(b)
        
        stack = [0]
        visited = {0}
        while stack:
            node = stack.pop()
            for child in adjList[node]:
                if child in visited:
                    adjList[child].remove(node)
                else:
                    stack.append(child)
                    visited.add(child) 

        paths = set()
        def dfs(apple):
            nonlocal paths
            stack = [apple]
            while stack:
                node = stack.pop()
                paths.add(node)
                for parent in adjList[node]:
                    stack.append(parent)

        apples = list(apples)
        for apple in apples:
            dfs(apple)
       
        pathesTaken = len(paths)
        return (pathesTaken-1)*2 if pathesTaken != 0 else 0

        

        
