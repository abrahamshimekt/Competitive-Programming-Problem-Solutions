class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        new_arr = []
        for i in range(len(nums)-1):
            new_arr.append((nums[i] + nums[i + 1])%10)
        return self.triangularSum(new_arr)