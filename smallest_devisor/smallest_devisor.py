class Solution:
    def isSmallestDivisor(self,divisor,nums,threshold):
        curr_sum = 0
        for num in nums:
            curr_sum += ceil(num/divisor)
        return curr_sum <= threshold

    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        
        left = 0
        right = max(nums) +1
        while right - left > 1:
            mid = left + (right-left)//2

            #check if the middle number is whether smallest devisor or not
            if self.isSmallestDivisor(mid,nums,threshold):
                right = mid
            else:
                left = mid

        return right