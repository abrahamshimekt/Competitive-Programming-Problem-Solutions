class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target not in nums:
            return [-1,-1]
        start = bisect_left(nums,target)
        end = bisect_right(nums,target)
        return [start,end-1]