def missingNumber(self, nums: List[int]) -> int:

       n = len(nums)

       # check if a number between 0 
       # and the length of the nums array is not in nums

       for i in range(n+1):
            if i not in nums:
                return i
