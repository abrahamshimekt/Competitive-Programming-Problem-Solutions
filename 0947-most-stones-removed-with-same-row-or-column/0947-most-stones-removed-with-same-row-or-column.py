class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        graphX = defaultdict(list)
        graphY = defaultdict(list)
        for x,y in stones:
            graphX[x].append(y)
            graphY[y].append(x)
        connectedComponent = 0
        visited = set()
        for x,y in stones:
            if (x,y) not in visited:
                q = deque([(x,y)])
                while q:
                    xo,yo = q.popleft()
                    if (xo,yo) not in visited:
                        visited.add((xo,yo))
                        for neiY in graphX[xo]:
                            q.append((xo,neiY))
                        for neiX in graphY[yo]:
                            q.append((neiX,yo))
                connectedComponent += 1
        
        return len(stones)-connectedComponent