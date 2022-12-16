class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        MT = []
        row = []
        for i in range(len(matrix[0])):
            for j in range(len(matrix)):
                row.append(matrix[j][i])
            MT.append(row)
            row = []
        return MT