class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        m = len(matrix)
        n = len(matrix[0])
        self.sumregion = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for i in range(1,m+1):
            for j in range(1,n+1):
                # self.sumregion[i][j] = matrix[i-1][j-1] + self.sumregion[i][j-1]
                self.sumregion[i][j] = self.sumregion[i-1][j] + self.sumregion[i][j-1] -self.sumregion[i-1][j-1] +matrix[i-1][j-1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.sumregion[row2 +1][col2 +1] -self.sumregion[row1][col2 +1] - self.sumregion[row2 +1][col1] + self.sumregion[row1][col1]
#         output =0
#         for r in range(row1 +1, row2 +2):
#             output +=self.sumregion[r][col2 +1] - self.sumregion[r][col1]
#         return output
        
        
# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)