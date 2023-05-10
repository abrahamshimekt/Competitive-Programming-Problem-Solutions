class Solution:
    def dfs(self,node):
       
        if self.colors[node]== 1:
            
            return False
        self.colors[node] = 1
        
        for neighbor in self.graph[node]:
            if self.colors[neighbor] != 2:
                
                if not self.dfs(neighbor):
                    return False
        
        self.colors[node] = 2
        self.orders.append(node)
        return True

            
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        
        self.colors = [0 for _  in range(len(graph))]
        self.orders = []
        self.graph = graph
        for node in range(len(graph)):
            if self.colors[node] == 0:
                self.dfs(node)

        return sorted(self.orders)
