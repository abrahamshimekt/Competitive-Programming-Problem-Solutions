class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        min_prefix_sum = 0
        max_sum = float("-inf")
        prefix_sum = [nums[0]]
        for i in range(1, len(nums)):
            prefix_sum.append(prefix_sum[i - 1] + nums[i])
        for i in range(len(nums)):
            max_sum = max(max_sum, prefix_sum[i] - min_prefix_sum)
            min_prefix_sum = min(min_prefix_sum, prefix_sum[i])
        return max_sum
                