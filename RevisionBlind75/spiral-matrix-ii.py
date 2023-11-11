class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[1 for _ in range(n) ] for _ in range(n)]
        left,right = 0,n-1
        top , bottom = 0,n-1
        num = 1
        direction = 0
        while left <= right and top <= bottom:
            if direction == 0:
                for i in range(left , right +1):
                    matrix[top][i] = num
                    num +=1
                top +=1
            elif direction == 1:
                for i in range(top, bottom +1):
                    matrix[i][right] = num
                    num +=1
                right -=1
            elif direction == 2:
                for i in range(right,left -1,-1):
                    matrix[bottom][i] = num
                    num +=1
                bottom -=1
            else:
                for i in range(bottom,top-1,-1):
                    matrix[i][left] = num
                    num +=1
                left +=1
            direction = (direction + 1)%4
        return matrix

        