class Solution:
    def findMax(self,grid,left,top):
        max_element = 0
        for row in range(left,left+3):
            for col in range(top,top+3):
                max_element = max(max_element,grid[row][col])
        return max_element
        

    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        max_local = []
        n = len(grid)
        m = len(grid[0])
        for left in range(n-2):
            curr_row = []
            for right in range(m-2):
               curr_row.append(self.findMax(grid,left,right))
            max_local.append(curr_row)
        return max_local