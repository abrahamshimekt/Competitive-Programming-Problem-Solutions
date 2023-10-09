class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        visited= set()
        for a,b,price in flights:
            graph[a].append((b,price))
        minheap = [(0,0,src)]
        while minheap:
            price,level,city = heappop(minheap)
            if city == dst:
                return price
            if level > k : continue
            if (city,price) in visited: continue
            visited.add((city,price))
            for b,p in graph[city]:
                heappush(minheap,(price+ p,level+1,b))
        return -1
        
        
