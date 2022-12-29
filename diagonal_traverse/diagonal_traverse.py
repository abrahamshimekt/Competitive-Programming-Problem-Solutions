class Solution:
    """find all elements above the main diagonal including the diagonals"""
    def above_diagonal(self,m,n,mat):

        above_diagonal = []
        for column in range(n):

            row  = 0
            left_column = column
            diagonal = []

            while row < m and left_column > -1:

                diagonal.append(mat[row][left_column])
                row +=1
                left_column -=1

            # starting column 0 all even indexed columns would be reversed their order 
            # since I have a fixed starting point to traverse elements starting from
            #  right to bottom left

            if column %2 ==0:
                diagonal = diagonal[::-1]
            above_diagonal += diagonal

        return above_diagonal
    """find all elements below the main diagonal not including the main diagonal """
    def below_diagonal(self,m,n,mat):

        below_diagonal = []
        for row in range(1,m):

            below_row = row 
            left_column = n-1
            diagonal = [] 

            while below_row < m and left_column >-1:
                diagonal.append(mat[below_row][left_column])
                below_row +=1
                left_column -=1

            # if the last column was traversed from bottom left to right upward 
            # then the diagonal elements should be reversed 
            
            if (n + row)% 2 != 0:
                diagonal = diagonal[::-1]

            below_diagonal += diagonal

        return below_diagonal
            

    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:

        m = len(mat)
        n = len(mat[0])

        return self.above_diagonal(m,n,mat) + self.below_diagonal(m,n,mat)




