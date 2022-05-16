class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i , j = 0,1
        while i < len(nums)-1 and j < len(nums):
            if nums[j] == nums[i]:
                j +=1
            elif nums[j] > nums[i]:
                nums[i +1] , nums[j] =  nums[j] , nums[i +1]
                i +=1
                j +=1
        return i + 1
                
       
        