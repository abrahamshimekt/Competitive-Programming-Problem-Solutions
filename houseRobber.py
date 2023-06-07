class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0]*(n + 2)
        for index in range(2, n + 2):
            dp[index]  = max(dp[index-2] + nums[index-2],dp[index-1])
        return dp[-1]
        
