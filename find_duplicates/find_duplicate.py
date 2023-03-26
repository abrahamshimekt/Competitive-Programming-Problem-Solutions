class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        for index in range(len(nums)):
            while nums[index] > 0 and nums[nums[index]-1]> 0:
                if nums[index]-1 == index:
                    nums[index] = -1*nums[index]
                else:
                    nums[nums[index]-1] , nums[index] = -1*nums[index],nums[nums[index]-1]
        duplicates = []
        for indxx in range(len(nums)):
            if nums[indxx] > 0:
                duplicates.append(nums[indxx])
        return duplicates
            
        