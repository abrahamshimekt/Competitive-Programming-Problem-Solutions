class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for index in range(len(nums)):
            while nums[index] > 0 and nums[nums[index]-1] >0:
                if nums[index]-1 == index:
                    nums[index] = -1*nums[index]
                else:
                    nums[nums[index]-1],nums[index] = -1*nums[index],nums[nums[index]-1]
        
        disappeared  = []
        for index in range(len(nums)):
            if nums[index] > 0:
                disappeared.append(index+1)
        return disappeared
        


        