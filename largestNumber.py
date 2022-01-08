class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        if nums == [0]* len(nums):
            return "0"
        for k in range(len(nums)):
            nums[k] = str(nums[k])
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if int(nums[i] + nums[j]) < int(nums[j] + nums[i]):
                    nums[i],nums[j] = nums[j],nums[i]
        return "".join(nums)