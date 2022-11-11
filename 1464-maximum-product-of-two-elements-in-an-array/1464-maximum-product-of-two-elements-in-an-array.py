class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort()
        x = nums[-1]-1
        y = nums[-2]-1
        return x*y