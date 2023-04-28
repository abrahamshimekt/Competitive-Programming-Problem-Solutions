class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] ==1:
            return -1
        N = len(grid)
        queue = deque()
        queue.append((0,0))
        visited = {(0,0)}
        directions = [(0,-1),(0,1),(1,0),(-1,0),(-1,1),(-1,-1),(1,-1),(1,1)]
        parent = {}
       
        while queue:
            currRow,currCol = queue.popleft()
            if (currRow,currCol) == (N-1,N-1):
                paths = 0
                cell = (currRow,currCol)
                while cell:
                    paths +=1
                    cell = parent.get(cell,None)
                return paths


            for direction in directions:
                newRow,newCol = currRow + direction[0],currCol + direction[1]
                if 0<= newRow < N and 0 <= newCol < N:
                    if (newRow,newCol) not in visited and grid[newRow][newCol] == 0:
                        visited.add((newRow,newCol))
                        parent[(newRow,newCol)] = (currRow,currCol)
                        queue.append((newRow,newCol))
        return -1
                
                



