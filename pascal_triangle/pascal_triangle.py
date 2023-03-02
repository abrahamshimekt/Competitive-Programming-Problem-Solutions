class Solution:
    @lru_cache
    def pascal(self,row,col):
        if row == col:
            return 1
        elif col == 1:
            return 1
        return self.pascal(row-1,col-1) + self.pascal(row-1,col)
    def getRow(self, rowIndex: int) -> List[int]:
        pascal_row = []
        for index in range(1,rowIndex+2):
            pascal_row.append(self.pascal(rowIndex+1,index))
        return pascal_row
        
        