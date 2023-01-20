class Solution:
    def row_sum(self,grid,row,col):
        distnict = set()
        rows_sum = []
        for r in range(row,row+3):
            total = 0
            for c in range(col,col+3):
                if grid[r][c] > 9 or grid[r][c] < 1:
                    total = 0
                    break
                elif grid[r][c] in distnict:
                    total = 0
                    break
                else:
                    total += grid[r][c]
                    distnict.add(grid[r][c])
            if not total:
                break
            else:
                rows_sum.append(total)
        return rows_sum

    def col_sum (self,grid,row,col):
        distnict = set()
        cols_sum = []
        for c in range(col,col+3):
            total = 0
            for r in range(row,row+3):
                if grid[r][c] >9 or grid[r][c] < 1:
                    total = 0
                    break
                elif grid[r][c] in distnict:
                    total = 0
                    break
                else:
                    total += grid[r][c]
                    distnict.add(grid[r][c])
            if not total:
                break
            else:
                cols_sum.append(total)
        return cols_sum

    def digonal_sum (self,grid,row,col):
        if (grid[row][col] == grid[row+1][col+1]) or  (grid[row][col] == grid[row+2][col+2]) or (grid[row+1][col+1] == grid[row+2][col+2]):
            return []
        elif (grid[row][col+2] == grid[row+1][col+1]) or (grid[row][col+2] == grid[row+2][col]) or (grid[row+1][col+1] == grid[row+2][col]):
            return []
        else:
            diagonal_sum = [grid[row][col] + grid[row+1][col+1] + grid[row+2][col+2],
            grid[row][col+2]+grid[row+1][col+1]+grid[row+2][col]]

        return diagonal_sum

        
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:

        m = len(grid)
        n = len(grid[0])
        magic_count = 0
        for row in range(m-2):
            for col in range(n-2):
                rows_sum = self.row_sum(grid,row,col)
                cols_sum = self.col_sum(grid,row,col)
                diagonal_sum = self.digonal_sum(grid,row,col)
               
                if (rows_sum and cols_sum and diagonal_sum) and (rows_sum == cols_sum )and (diagonal_sum[0] == diagonal_sum[1]) and (diagonal_sum[0] == rows_sum[0]):
                    magic_count +=1
        return magic_count 




       

        