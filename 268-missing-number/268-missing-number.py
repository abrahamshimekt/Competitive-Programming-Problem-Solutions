class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums_range = []
        for i in range(len(nums) + 1):
            nums_range.append(i)
        for item in nums_range:
            if item not in nums:
                return item
            
        