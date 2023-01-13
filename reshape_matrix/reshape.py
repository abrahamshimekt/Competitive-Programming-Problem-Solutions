class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        n = len(mat)
        m = len(mat[0])
        if r*c != n*m:
            return mat
        else:
            one_D = []
            for row in range(n):
                for col in range(m):
                    one_D.append(mat[row][col])

            reshaped = []
            curr_position = 0
            for row_ in range(r):
                curr_row = []
                for col_ in range(c):
                    curr_row.append(one_D[curr_position])
                    curr_position +=1
                reshaped.append(curr_row)
            return reshaped