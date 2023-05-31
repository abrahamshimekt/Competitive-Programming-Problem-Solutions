class Solution:
    def isBound(self,row,col):
        return 0<= row < self.m and 0<= col < self.n
    def dfs(self,row,col):
        stack = [(row,col)]
        isSubset = True
        while stack:
            currRow,currCol = stack.pop()
            self.grid2[currRow][currCol] = 0
            for direction in self.directions:
                newRow,newCol = currRow + direction[0], currCol + direction[1]
                if self.isBound(newRow,newCol) and self.grid2[newRow][newCol] == 1:
                    stack.append((newRow,newCol))
        



    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:

        self.grid1 = grid1
        self.grid2 = grid2
        self.m = len(self.grid1)
        self.n = len(self.grid1[0])
        self.directions = [(0,-1),(0,1),(-1,0),(1,0)]
        for row in range(self.m):
            for col in range(self.n):
                if grid2[row][col]==1 and grid1[row][col]==0:
                    self.dfs(row,col)

        count = 0

        for row in range(self.m):
            for col in range(self.n):
                  if self.grid2[row][col] == 1:
                    self.dfs(row,col)
                    count +=1
        return count
        
