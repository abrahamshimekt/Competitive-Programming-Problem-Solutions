class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        numsCount = Counter(nums)
        while original in numsCount:
            original *= 2
        return original