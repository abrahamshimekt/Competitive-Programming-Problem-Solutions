class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target not in nums:
            return [-1, -1]
        i = j = 0
        while i < len(nums) and j < len(nums):
            if nums[j] < target:
                i += 1
                j += 1
            elif nums[j] > target:
                return [i, j - 1]
            else:
                j += 1
                if j == len(nums):
                    return [i, j - 1]