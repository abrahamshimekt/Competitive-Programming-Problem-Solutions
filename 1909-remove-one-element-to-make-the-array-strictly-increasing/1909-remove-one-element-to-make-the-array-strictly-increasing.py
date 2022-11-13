class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        n = len(nums)
        def isIncreasing(arr):
            i =0
            while i <len(arr)-1:
                if arr[i] >= arr[i +1]:
                    return False
                i +=1
            return True 
        
        for i in range(n-1,-1,-1):
            temp = nums.pop(i)
            if isIncreasing(nums):
                return True
            nums.insert(i,temp)
        return False
                