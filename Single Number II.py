class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        single = 0
        duplicated = 0
        for num in nums:
            single =(single ^ num) & ~ duplicated
            duplicated = (duplicated ^ num) & ~ single
        return single
        
