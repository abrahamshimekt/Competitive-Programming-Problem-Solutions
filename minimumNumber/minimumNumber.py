class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        indegree = set()
        for edge in edges:
            indegree.add(edge[1])
        smallestSet = []
        for vertex in range(n):
            if vertex not in indegree:
                smallestSet.append(vertex)
        return smallestSet