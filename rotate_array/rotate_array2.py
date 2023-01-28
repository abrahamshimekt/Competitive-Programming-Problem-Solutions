class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
       
        Do not return anything, modify nums in-place instead.
        """
        last_k = []
        length = len(nums)
        k = k%length 

        for index in range(length-k,length):
            last_k.append( nums[index])

        left = length -k-1
        right = length -1
        
        while left > -1:
            nums[right] = nums[left]
            right -=1
            left -=1

        for index_ in range(k):
            nums[index_] = last_k[index_]




        



        
        
       
            
        