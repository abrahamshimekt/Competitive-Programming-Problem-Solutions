class Solution:
    def fib(self, n: int) -> int:
        dp ={}
        def helper(n):
            if n==0 or n==1:
                return n
            if n in dp:
                return dp[n]
            x = helper(n-1) + helper(n-2)
            dp[n] =x
            return x
        return helper(n)