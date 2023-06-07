class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = {}
        def maxSum(row,move):

            if row >= n:
                return 0
            if (row,move) not in dp:
                minPathSum = min(maxSum(row + 1,move) + triangle[row][move],maxSum(row+1,move+1) + triangle[row][move])
                dp[(row,move)] = minPathSum
            return dp[(row,move)]
        return maxSum(0,0)
