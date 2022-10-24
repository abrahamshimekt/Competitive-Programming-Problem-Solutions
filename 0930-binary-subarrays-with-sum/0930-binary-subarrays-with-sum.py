class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefix_sum = {0:1}
        total = 0
        i = 0
        res = 0
        while i < len(nums):
            total +=nums[i]
            if total - goal in prefix_sum:
                res += prefix_sum[total - goal]
            if total in prefix_sum:
                prefix_sum[total] += 1
            else:
                prefix_sum[total] =1 
            i +=1
        return res
                
        