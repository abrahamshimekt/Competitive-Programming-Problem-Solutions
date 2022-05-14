class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        if nums == [0]* len(nums):
            return "0"
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if int(str(nums[i]) + str(nums[j])) < int(str(nums[j]) + str(nums[i])):
                    nums[i],nums[j] = nums[j],nums[i]
        return "".join([str(x) for x in nums])
        