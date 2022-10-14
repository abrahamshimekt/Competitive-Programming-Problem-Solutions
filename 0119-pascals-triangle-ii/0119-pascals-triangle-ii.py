class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        output = [[1]]
        for i in range(rowIndex):
            temp = [0] + output[-1] + [0]
            row = []
            for j in range(len(output[-1]) + 1):
                row.append(temp[j] + temp[j +1])
            output.append(row)
        return output[-1]
        