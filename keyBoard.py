class Solution:
    def minSteps(self, n: int) -> int:
        dp = [0]*(n+1)
        for i in range(2,n+1):
            for j in range(i-1,0,-1):
                if not i%j:
                    dp[i] = dp[j] + (i//j)
                    break
        return dp[n]

        
            
                

