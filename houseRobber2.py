class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 3:
            return max(nums)
    
        def maxLine(line):
            n = len(line)

            dp = [0]*n
            dp[0] = line[0]
            dp[1] = max(line[0],line[1])
            for index in range(2,n):
                dp[index] = max(dp[index-1] , dp[index-2] + line[index])
            return dp[-1]
        return max(maxLine(nums[:-1]),maxLine(nums[1:]))
        
    
        
