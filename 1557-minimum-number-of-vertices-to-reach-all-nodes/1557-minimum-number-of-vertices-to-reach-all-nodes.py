class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        indegree = [0]*n
        ans = []
        for edge in edges:
            indegree[edge[1]] +=1
        for i in range(n):
            if indegree[i] == 0:
                ans.append(i)
        return ans
            
        
        