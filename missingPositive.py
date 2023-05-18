class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        N = len(nums)
        index = 0
        while index < N :
            if (nums[index] > 0 and nums[index] <= N) and (nums[nums[index]-1] != nums[index]):
              nums[nums[index]-1],nums[index] =nums[index],nums[nums[index]-1]
            else:
                index +=1
        for index in range(N):
            if nums[index] != index + 1:
                return index + 1
        return N  + 1
        
        
