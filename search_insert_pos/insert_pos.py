class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = -1
        right = len(nums)
        while right -left > 1:
            mid = left + (right-left)//2
            if nums[mid] >= target:
                right = mid
            else:
                left = mid
        return right