class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i,j = 0,1
        while j < len(nums):
            if nums[i] != 0:
                i +=1
                j +=1
            elif nums[j] == 0:
                j +=1
            else:
                nums[i],nums[j] = nums[j],nums[i]
                i +=1
                j +=1
            
        