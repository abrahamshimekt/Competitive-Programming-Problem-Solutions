class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        dic_nums = {}
        for num in nums:
            dic_nums[num] =1
        for i in range(len(nums)+1):
            if i not in dic_nums:
                return i
        