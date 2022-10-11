class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first, second = inf,inf
        for num in nums:
            if num < first:
                first = num
            elif num < second and num != first:
                second = num
            if num > first and num > second:
                return True
        return False