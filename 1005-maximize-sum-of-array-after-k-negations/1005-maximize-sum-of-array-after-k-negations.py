class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort()
        i = 0
        while i < len(nums) and i < k and nums[i] < 0:
            nums[i] = -1*nums[i]
            i +=1
        return sum(nums) - (k-i)%2*min(nums)*2
                