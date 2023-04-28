class Solution:
   
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
        M = len(mat)
        N = len(mat[0])
        queue = deque()
        for row in range(M):
            for col in range(N):
                if mat[row][col] == 1:
                    mat[row][col] = float("inf")
                else:
                    queue.append((row,col))
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        
        while queue:

            row,col = queue.popleft()
            for direction in directions:
                newRow,newCol = row+ direction[0],col + direction[1]
                if 0 <= newRow < M and 0 <= newCol < N:
                    if mat[row][col]+1 < mat[newRow][newCol]:
                        mat[newRow][newCol] = mat[row][col]+1
                        queue.append((newRow,newCol))
        return mat

                
        


        
