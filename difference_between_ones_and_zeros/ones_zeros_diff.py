class Solution:
    """count the number of ones and zeros for each row
    and count them in a dictionary 
    """
    def ones_zeros_row(self,m,n,grid):

        ones_zeros = {}
        for index_i in range(m):

            ones = 0
            zeros = 0

            for index_j in range(n):
                # count ones and zeros in a row
                if grid[index_i][index_j] == 0:
                    zeros +=1
                else:
                    ones +=1 

            ones_zeros[index_i] = [ones,zeros]

        return ones_zeros

    """count the number of ones and zeros for each column in a dictionary"""

    def ones_zeros_col(self,m,n,grid):

        ones_zeros ={}
        for index_i in range(n):

            ones = 0
            zeros = 0

            for index_j in range(m):
                # count zeros and ones in a column
                if grid[index_j][index_i] == 0:
                    zeros +=1
                else:
                    ones +=1
            ones_zeros[index_i] = [ones,zeros]

        return ones_zeros

    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:

        m = len(grid)
        n = len(grid[0])

        # dictionaries for look up
        row_ones_zeros = self.ones_zeros_row(m,n,grid)
        col_ones_zeros = self.ones_zeros_col(m,n,grid)

        diff_matrix = []

        for index_i in range(m):

            diff_row = []
            for index_j in range(n):
                # calculate the what is asked in the question that is
                # difference between ones and zeros
               diff = row_ones_zeros[index_i][0] + col_ones_zeros[index_j][0]-(row_ones_zeros[index_i][1] + col_ones_zeros[index_j][1])

               diff_row.append(diff)

            diff_matrix.append(diff_row)

        return diff_matrix


