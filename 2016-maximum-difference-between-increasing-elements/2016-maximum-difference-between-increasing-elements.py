class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        i,j = 0,1
        max_dif = 0
        while i < len(nums) and j < len(nums):
            if nums[i] < nums[j]:
                max_dif = max(max_dif,nums[j]-nums[i])
                j +=1
            else:
                i = j
                j +=1
        if max_dif == 0:
            return -1
        return max_dif