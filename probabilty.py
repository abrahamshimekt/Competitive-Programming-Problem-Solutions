class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        probability = {node: 0 for node in range(n)}
        graph = defaultdict(list)
        for i in range(len(edges)):
            u, v = edges[i]
            graph[u].append((v, succProb[i]))
            graph[v].append((u, succProb[i]))
        
        def dijkstras(start, end):
            minheap = [(-1, start)] 
            visited = set()
            
            while minheap:
                currProb, currNode = heappop(minheap)
                currProb *= -1 
                if currNode == end:
                    return currProb
                if currNode in visited:
                    continue
                visited.add(currNode)
                for v, pr in graph[currNode]:
                    prob = currProb * pr
                    if prob > probability[v]:
                        probability[v] = prob
                        heappush(minheap, (-prob, v))  
            
            return 0
        
        return dijkstras(start_node, end_node)
                    

        
