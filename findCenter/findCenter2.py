class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        adjacencyList = defaultdict(list)
        for edge in edges:
            adjacencyList[edge[0]].append(edge[1])
            adjacencyList[edge[1]].append(edge[0])
        for node in adjacencyList:
            if len(adjacencyList[node]) == len(edges):
                return node
        