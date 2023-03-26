class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.append(-1)
        for index in range(len(nums)):
           while nums[index] > -1 and nums[index] != index:
               nums[nums[index]],nums[index] = nums[index],nums[nums[index]]
       
        for index in range(len(nums)):
            if nums[index] < 0:
                return index


        