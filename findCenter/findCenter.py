class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        adjacencyList = defaultdict(list)
        for edge in edges:
            adjacencyList[edge[0]].append(edge[1])
            adjacencyList[edge[1]].append(edge[0])
            if len(adjacencyList[edge[0]]) >=2  :
                return edge[0]
            elif len(adjacencyList[edge[1]]) >=2:
                return edge[1]
        
        