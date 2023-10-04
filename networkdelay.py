class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        signalTime = {node: float('inf') for node in range(1,n+1)}
        graph = defaultdict(list)
        for u,v,w in times:
            graph[u].append((v,w))
        def djkistr(k):
            signalTime[k] = 0
            minheap = [(0,k)]
            while minheap:
                time , node = heappop(minheap)
                for v,w in graph[node]:
                    if time + w < signalTime[v]:
                        signalTime[v] = time + w
                        heappush(minheap,(time+w,v))
        djkistr(k)
        maxTime = 0
        for node in signalTime:
            maxTime = max(maxTime,signalTime[node])
        if maxTime == float('inf'):
            return -1
        return maxTime


        
