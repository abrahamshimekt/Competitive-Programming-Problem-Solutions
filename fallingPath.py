class Solution(object):
    def minFallingPathSum(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        N = len(matrix)
        dp = {}
        movements = [(1,-1),(1,0),(1,1)]
        def findSum(row,col):
            if not (0<= row < N and 0<= col< N):
               
                return float('inf')
            if row == N-1:
                dp[(row,col)] = matrix[row][col]
                return matrix[row][col]
            
            if (row,col) in dp:
               
                return dp[(row,col)]
            minSum = float("inf")
            for movement in movements:
                newRow,newCol = row + movement[0],col+movement[1]
                minSum = min(minSum, findSum(newRow,newCol))
            dp[(row,col)] = matrix[row][col] + minSum 
            return dp[(row,col)]
        
        for index in range(N):
            findSum(0,index)
         
        minimumSum = float('inf')
        for col in range(N):
            minimumSum = min(minimumSum,dp[(0,col)])
        return minimumSum


