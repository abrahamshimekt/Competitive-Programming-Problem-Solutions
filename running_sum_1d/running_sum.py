class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for index in range(1,len(nums)):
            nums[index] = nums[index-1] + nums[index]
        return nums