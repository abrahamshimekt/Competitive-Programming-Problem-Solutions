class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        pr1 = nums[-1]*nums[-2]*nums[-3]
        pr2 = nums[-1]*nums[0]*nums[1]
        return max(pr1,pr2)