class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        """[4,3,10,9,8] =[3,4,8,9,10] = 36"""
        nums.sort()
        output = []
        n = len(nums)
        total = sum(nums)
        maxSum = 0
        for i in range(n-1,-1,-1):
            maxSum += nums[i]
            if maxSum <= total-maxSum:
                output.append(nums[i])
            else:
                output.append(nums[i])
                break
        return output
                
            