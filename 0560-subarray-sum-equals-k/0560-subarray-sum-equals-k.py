class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = {0:1}
        count = 0
        i = 0
        running_sum = 0
        while i < len(nums):
            running_sum += nums[i]
            if running_sum - k in prefix_sum:
                count += prefix_sum[running_sum - k]
            if running_sum in prefix_sum:
                prefix_sum[running_sum] +=1
            else:
                prefix_sum[running_sum] = 1
            i +=1
        return count
                
                