class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:

        n = len(mat)
        m = len(mat[0])

        if r*c != n*m:
            return mat

        else:

            reshaped = []
            index = 0
            for row in range(r):
                curr_row = []
                k = c
                while index <= r*c :
                    if k > 0:
                        curr_row.append(mat[index//m][index%m])
                        k -=1
                        index +=1
                    else:
                        reshaped.append(curr_row)
                        break
    
            return reshaped