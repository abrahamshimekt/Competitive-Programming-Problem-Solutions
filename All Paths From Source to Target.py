class Solution:
    def dfs(self,source,destination,path):
        
        if source==destination:
            self.paths.append(path[:])
            return 

        for adjacent in self.graph[source]:
           self.dfs(adjacent,destination,path+[adjacent])

    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        self.paths = []
        self.graph = graph
        self.dfs(0,len(graph)-1,[0])

        return  self.paths
