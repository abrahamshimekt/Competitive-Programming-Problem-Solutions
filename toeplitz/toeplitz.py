class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:

        n = len(matrix)
        m = len(matrix[0])


        for index_i in range(n*m-m):

            diff = index_i//m-index_i%m

            for index_j in range(index_i+1,n*m):
                
                if diff ==  index_j//m-index_j%m:
                    if matrix[ index_i//m][index_i%m] != matrix[index_j//m][index_j%m]:
                        return False
        return True