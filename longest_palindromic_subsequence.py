# top down approach
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = {}
        def findLongestSub(i,j):
            if i>=n or j < 0:
                return 0
            if (i,j) in dp:
                return dp[(i,j)]
            if s[i] == s[j]:
                dp[(i,j)] = 1 + findLongestSub(i+1,j-1)
            else:
                dp[(i,j)] = max(findLongestSub(i+1,j),findLongestSub(i,j-1))
            return dp[(i,j)]
        return findLongestSub(0,n-1)
# bottom up approach

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        t = s[::-1]
        
        dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
    

        for i in range(1,n+1):
            for j in range(1,n+1):
                if s[i-1] == t[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])
        
        return dp[n][n]
        
        
