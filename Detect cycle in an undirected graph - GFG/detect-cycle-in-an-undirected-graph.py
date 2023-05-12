from typing import List
class Solution:
    #Function to detect cycle in an undirected graph.
    def dfs(self,child , parent):
        if self.colors[child] == 1:
            return True
        self.colors[child] =1
        for neighbor in self.adj[child]:
            if neighbor != parent:
                if self.dfs(neighbor,child):
                    return True
        return False
            
        
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
		self.colors = [0]*V
		self.adj = adj
		for node in range(V):
		    if self.colors[node] == 0:
		        if self.dfs(node,-1):
		            return True
		return False
		


#{ 
 # Driver Code Starts
if __name__ == '__main__':

	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.isCycle(V, adj)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends