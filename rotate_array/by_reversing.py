class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
       
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        left = 0
        right = length -1
        k = k%length
        # reverse the whole array
        while left < right:
            nums[left],nums[right] = nums[right],nums[left]
            left +=1
            right -=1
        # reverse the first k elements 
        right_k = k-1
        left_k = 0
        while left_k < right_k:
            nums[left_k],nums[right_k] = nums[right_k],nums[left_k]
            left_k +=1
            right_k -=1

        right_after_k = length -1
        left_after_k = k
        # reverse the remaining elements
        while left_after_k < right_after_k:
            nums[left_after_k],nums[right_after_k] = nums[right_after_k],nums[left_after_k]
            left_after_k +=1
            right_after_k -=1

        

        



        



        
        
       
            
        