class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        freq = Counter(nums)
        for num in freq:
            if freq[num] >1:
                return True
        return False