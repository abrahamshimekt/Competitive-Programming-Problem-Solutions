class Solution(object):
    def knightProbability(self, n, k, row, column):
        """
        :type n: int
        :type k: int
        :type row: int
        :type column: int
        :rtype: float
        """
        dp = {}
        movements = [(1,2),(-1,2),(1,-2),(-1,-2),(2,1),(2,-1),(-2,1),(-2,-1)]
        
        def KnightMove(row,col,k):
          
            if k == 0:
                return 1.0
            if (k,row,col) in dp:
                return dp[(k,row,col)]
           
            probability = 0
            for movement in movements:
                x,y = row+movement[0],col + movement[1]
                if 0<=x<n and 0<=y<n:
                    probability += KnightMove(x,y,k-1)/8.0
           
            dp[(k,row,col)] =probability

            return probability
        
    
        return KnightMove(row, column,k)
        

        
