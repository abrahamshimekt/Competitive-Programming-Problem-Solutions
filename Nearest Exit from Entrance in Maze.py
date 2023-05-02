class Solution:
    def bfs(self,row,col):
        queue = deque()
        queue.append(((row,col),0))
        self.maze[row][col] = "+"
        while queue :
            cell,steps = queue.popleft()
           
            if cell != (row,col) and (cell[0] == 0 or cell[0] == self.M-1 or cell[1]==0 or cell[1]==self.N-1):
                return steps
            for direction in self.directions:
                newRow,newCol = cell[0]+direction[0],cell[1]+direction[1]
                if 0<= newRow < self.M and 0<= newCol < self.N:
                    if self.maze[newRow][newCol] == ".":
                        self.maze[newRow][newCol] = "+"
                        queue.append(((newRow,newCol),steps+1))
        return -1
                    
                
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        self.directions = [(0,-1),(0,1),(-1,0),(1,0)]
       
        self.maze = maze 
        self.M = len(self.maze)
        self.N = len(self.maze[0])
        return self.bfs( entrance[0],entrance[1])
    
        
