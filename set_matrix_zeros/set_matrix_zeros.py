class Solution:
    def move_up(self,matrix,row,col):
        while row >-1:
            matrix[row][col] = 0
            row -=1
        
    def move_down(self,matrix,row,col):
        n = len(matrix)
        while row < n:
            matrix[row][col] = 0
            row +=1

    def move_left(self,matrix,row,col):
        while col > -1:
            matrix[row][col] = 0
            col -=1
    def move_right(self,matrix,row,col):
        m = len(matrix[0])
        while col < m:
            matrix[row][col] = 0
            col +=1
    

    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        m = len(matrix[0])
        zeros_position = {0:[]}
        zeros_count = 0

        for row in range(n):
            for col in range(m):
                if matrix[row][col] == 0:
                   zeros_position[0].append((row,col))
                   zeros_count +=1

        if zeros_count == n*m:
            return matrix
            
        else:
            for row_ , col_ in zeros_position[0]:

                self.move_up(matrix,row_,col_)
                self.move_down(matrix,row_,col_)
                self.move_left(matrix,row_,col_)
                self.move_right(matrix,row_,col_)
                
            return matrix
