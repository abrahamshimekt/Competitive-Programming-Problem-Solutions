class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        i = 0
        maxSum = 0
        while i < len(nums):
            maxSum += nums[i]
            i +=2
        return maxSum
            