class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        n = len(nums)
        minArray = [0]*n
        minArray[0] = nums[0]
        maxArray = [0]*n
        maxArray[n-1] = nums[n-1]
        for index in range(1,n):
            minArray[index] = min(minArray[index-1],nums[index])
        for index in range(n-2,-1,-1):
             maxArray[index] =  max(maxArray[index+1],nums[index])
       
        for index in range(1,n-1):
            if minArray[index] < nums[index] < maxArray[index]:
                return True
        return False

            
        
        
