class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        dest = len(graph)-1
        def dfs(node,path,paths):
            if node == dest:
                paths.append(path)
            for neighbor in graph[node]:
                dfs(neighbor,path + [neighbor],paths)
        paths = []
        dfs(0,[0],paths)
        return paths