class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        prefixRow1, prefixRow2 = grid[0][:],grid[1][:]
        N = len(grid[0])
        
        for j in range(1,N):
            prefixRow1[j] += prefixRow1[j-1]
            prefixRow2[j] += prefixRow2[j-1]
            
        result = float("inf")

        for index in range(N):

            row1Point = prefixRow1[-1]- prefixRow1[index]
            row2Point = prefixRow2[index-1] if index > 0 else 0

            secondRobot = max(row1Point,row2Point)

            result = min(result,secondRobot)

        return result