class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        memo = [-1] * n
        
        def lis_length(i):
            
            if memo[i] != -1:
                return memo[i]
            
            max_length = 1
            for j in range(i+1, n):
                if nums[i] < nums[j]:
                    max_length = max(max_length, 1 + lis_length(j))
            
            memo[i] = max_length
            return max_length
        
        max_length = 0
        for i in range(n):
            max_length = max(max_length, lis_length(i))
        
        return max_length