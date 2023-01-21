class Solution:
    def top_row(self,grid,top,left,right):
        curr_row = []
        for col in range(left,right+1):
            curr_row.append((top,col,grid[top][col]))
        return curr_row
    def bottom_row(self,grid,bottom,left,right):
        curr_row = []
        for col in range(right,left-1,-1):
            curr_row.append((bottom,col,grid[bottom][col]))
        return curr_row
    def left_col(self,grid,left,top,bottom):
        curr_col = []
        for row in range(bottom,top-1,-1):
            curr_col.append((row,left,grid[row][left]))
        return curr_col
    def right_col(self,grid,right,top,bottom):
        curr_col = []
        for row in range(top,bottom+1):
            curr_col.append((row,right,grid[row][right]))
        return curr_col


    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        top = 0
        left = 0
        right  = m-1
        bottom  = m-1
        while left < right and top < bottom:
            t_row = self.top_row(matrix,top,left,right)
            r_col =  self.right_col(matrix,right,top,bottom)
            b_row = self.bottom_row(matrix,bottom,left,right)
            l_col = self.left_col(matrix,left,top,bottom)
            for index in range(len(t_row)):
                matrix[r_col[index][0]][r_col[index][1]] = t_row[index][2]
                matrix[b_row[index][0]][b_row[index][1]] = r_col[index][2]
                matrix[l_col[index][0]][l_col[index][1]] = b_row[index][2]
                matrix[t_row[index][0]][t_row[index][1]] = l_col[index][2]
            left +=1
            top +=1
            right -=1
            bottom -=1
        


            


        
            

        