class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        spiral =[]
        left ,top = 0,0
        right , bottom = len(matrix[0]), len(matrix)

        while left < right and top < bottom:
            
            for i in range(left,right):
                spiral.append(matrix[top][i])
            top +=1

            for j in range(top,bottom):
                spiral.append(matrix[j][right-1])
            right -=1
            
            if not (left <right and top <bottom):
                break

            for k in range(right-1,left-1,-1):
                spiral.append(matrix[bottom-1][k])

            bottom -=1

            for l in range(bottom-1, top-1,-1):
                spiral.append(matrix[l][left])
            left +=1

        return spiral
                
        
        