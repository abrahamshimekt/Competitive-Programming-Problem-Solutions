class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        """[1,4,0,2,0,0] 
        """
        n = len(nums)
        i,j=0,1
        while j < n:
            if nums[i] == nums[j]:
                nums[i] = nums[i]*2
                nums[j] = 0
            i +=1
            j +=1
        for num in nums:
            if num == 0:
                nums.remove(num)
                nums.append(0)
        return nums
        
            
        
                