class Solution:

    def solve(self, board: List[List[str]]) -> None:
    
        m = len(board) 
        n = len(board[0])  
        directions = [(0,-1),(0,1),(-1,0),(1,0)]

        # DFS function to mark cells as Escape ('E')
        def dfs(row, col):
            
            board[row][col] = 'E'  # Mark cell as Escape
           
            for direction in directions:
                newRow,newCol = row+direction[0],col + direction[1]
                if (0<= newRow < m and 0 <= newCol < n) and board[newRow][newCol] == "O":
                    dfs(newRow,newCol)

        # Mark 'o's on the boundary and those reachable from the boundary
        for col in range(n):
            if board[0][col] == "O":
                dfs(0,col)
            if board[m-1][col] == "O":
                dfs(m-1,col)
        for row in range(m):
            if board[row][0] == 'O':
                dfs(row,0)
            if board[row][n-1] == "O":
                dfs(row,n-1)
            
        # Capture regions and convert back Escape cells into 'o's
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'E':
                    board[i][j] = 'O'

        return board
 
 
 
class Solution:
    def dfs(self,row,col):

        self.board[row][col] = "B"

        for direction in self.directions:
            
            newRow,newCol = row + direction[0],col + direction[1]
            if (0<= newRow < self.N and 0 <= newCol < self.M ) and self.board[newRow][newCol] == "O":

                self.dfs(newRow,newCol)

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.board = board
        self.N = len(self.board)
        self.M = len(self.board[0])
        self.directions = [(0,-1),(0,1),(-1,0),(1,0)]
        
        for row in range(self.N):
            for col in range(self.M):
                if (row == 0 or row == self.N -1 or col == 0 or col == self.M-1) and self.board[row][col] == "O" :
                    self.dfs(row,col)
        
        for row in range(self.N):
            for col in range(self.M):
                if self.board[row][col] == "B":
                    self.board[row][col] = "O"
                elif self.board[row][col] == "O":
                    self.board[row][col] = "X"
                    
        return self.board

