 def uniquePaths(self, m: int, n: int) -> int:
        def isInbound(row,col):
            return 0<= row < m and 0 <= col < n

        matrix = [[0 for col in range(n)] for row in range(m)]
        matrix[-1][-1] = 1

        for row in range(m-1,-1,-1):
            for col in range(n-1,-1,-1):
                if isInbound(row+1,col):
                    matrix[row][col] += matrix[row+1][col]
                if isInbound(row,col+1):
                    matrix[row][col] += matrix[row][col + 1]

        return matrix[0][0]
