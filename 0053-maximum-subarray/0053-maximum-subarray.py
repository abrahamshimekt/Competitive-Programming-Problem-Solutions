class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum_found = float("-inf")
        max_curr_sum = 0
        i = 0
        while i < len(nums):
            max_curr_sum += nums[i]
            if max_sum_found < max_curr_sum:
                max_sum_found = max_curr_sum
            if max_curr_sum < 0:
                max_curr_sum = 0
            i +=1
        return max_sum_found
                