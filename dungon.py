class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m = len(dungeon)
        n = len(dungeon[0])
        healths = [[float('-inf') for col in range(n)] for row in range(m)]

        def findInitialHealth(row,col):
            if row >= m or col >= n:
                return float('-inf')
            if row == m-1 and col == n-1:
                return min(dungeon[row][col],0)
            if healths[row][col] != float('-inf'):
                return healths[row][col]
            
            rightMove = min(findInitialHealth(row,col+1) +  dungeon[row][col],0)
            downMove = min(findInitialHealth(row+1,col) +  dungeon[row][col],0)
            healths[row][col] = max(rightMove,downMove)
            return healths[row][col]
        return abs(findInitialHealth(0,0)) + 1




        
