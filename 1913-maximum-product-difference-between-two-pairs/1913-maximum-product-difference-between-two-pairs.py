class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort()
        a = nums[-1]
        b = nums[-2]
        c = nums[0]
        d = nums[1]
        return (a*b)-(c*d)
                